import boto3
import json
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def delete_all_objects(s3_resource, bucket_name):
    """Delete all objects from a s3 bucket"""
    all_elems = []
    bucket = s3_resource.Bucket(bucket_name)
    for obj_version in bucket.object_versions.all():
        all_elems.append({'Key': obj_version.object_key,
                          'VersionId': obj_version.id})
    if list(all_elems):
        bucket.delete_objects(Delete={'Objects': all_elems})
    else:
        print("Bucket is empty")


def create_bucket(
        key,
        secret,
        bucket_name,
        location
):
    """Create Public S3 Bucket
    """
    # create bucket
    s3_resource = boto3.client(
        's3',
        aws_access_key_id=key,
        aws_secret_access_key=secret
    )
    s3_bucket = s3_resource.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': location})

    # set public access to bucket
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': ['s3:GetObject'],
            'Resource': 'arn:aws:s3:::{}/*'.format(bucket_name)
        }]
    }
    s3_resource.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(bucket_policy))
    logger.info("Created new public bucket: {}".format(bucket_name))


def delete_bucket(
        key,
        secret,
        bucket_name
):
    """Delete a s3 bucket with all the data contained in it.
    """
    s3_resource = boto3.resource(
        's3',
        aws_access_key_id=key,
        aws_secret_access_key=secret
    )
    delete_all_objects(s3_resource, bucket_name)
    s3_resource.Bucket(bucket_name).delete()
    logger.info("Deleted bucket: {}".format(bucket_name))


def create_emr(
        key,
        secret,
        location,
        name_cluster,
        instance_type,
        instance_count,
        name_ec2_key,
        name_security_group
):
    """Create emr instance in aws
    """
    logger.info("Spinning new EMR Cluster..")
    emr_client = boto3.client(
        'emr',
        region_name=location,
        aws_access_key_id=key,
        aws_secret_access_key=secret
    )
    cluster_descriptor = emr_client.run_job_flow(
        Name=name_cluster,
        ReleaseLabel='emr-5.28.0',
        Applications=[{'Name': 'Spark'}],
        Instances={
            'MasterInstanceType': instance_type,
            'SlaveInstanceType': instance_type,
            'InstanceCount': int(instance_count),
            'KeepJobFlowAliveWhenNoSteps': True,
            'TerminationProtected': False,
            'Ec2KeyName': name_ec2_key,
            'EmrManagedSlaveSecurityGroup': name_security_group,
            'EmrManagedMasterSecurityGroup': name_security_group,
        },
        Steps=[],
        VisibleToAllUsers=True,
        JobFlowRole='EMR_EC2_DefaultRole',
        ServiceRole='EMR_DefaultRole',
    )
    cluster_id = cluster_descriptor["JobFlowId"]

    logger.info("Waiting the server to generate cluster dns...")
    while "MasterPublicDnsName" not in emr_client.describe_cluster(ClusterId=cluster_id)["Cluster"]:
        time.sleep(1)
    cluster_dns = emr_client.describe_cluster(ClusterId=cluster_id)["Cluster"]["MasterPublicDnsName"]
    logger.info("Created new cluster: \nid: {}, \ndns: {}".format(cluster_id, cluster_dns))
    return cluster_id, cluster_dns


def terminate_emr(
        key,
        secret,
        location,
        cluster_id
):
    """Delete emr instance
    """
    logger.info("Terminating EMR Cluster with id {}..".format(cluster_id))
    emr_client = boto3.client(
        'emr',
        region_name=location,
        aws_access_key_id=key,
        aws_secret_access_key=secret
    )
    response = emr_client.terminate_job_flows(JobFlowIds=[cluster_id])
    return response
