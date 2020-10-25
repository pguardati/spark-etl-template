import os
import sys
import configparser
import argparse

from test_spark.src.infrastructure import create_emr, create_bucket, logger


def parse_args(args):
    parser = argparse.ArgumentParser(description="Create bucket to store processed data and spin an Emr cluster")
    parser.add_argument("dir_credentials", help="path of the aws configuration file")
    parser.add_argument("--skip_s3", help="do not create s3 bucket for output storage", action="store_true")
    parser.add_argument("--skip_emr", help="do not create emr cluster", action="store_true")
    return parser.parse_args(args)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    args = parse_args(args)

    logger.info("Reading Configuration..")
    config = configparser.ConfigParser()
    config_file = os.path.join(args.dir_credentials, "dl.cfg")
    config.read(config_file)
    KEY = config.get("AWS", "AWS_ACCESS_KEY_ID")
    SECRET = config.get("AWS", "AWS_SECRET_ACCESS_KEY")
    LOCATION = config.get("COMMON", "LOCATION")
    BUCKET_NAME = config.get("OUTPUT_BUCKET", "NAME")
    NAME_CLUSTER = config.get("CLUSTER", "NAME_CLUSTER")
    INSTANCE_TYPE = config.get("CLUSTER", "INSTANCE_TYPE")
    NAME_SECURITY_GROUP = config.get("CLUSTER", "NAME_SECURITY_GROUP")
    NAME_EC2_KEY = config.get("CLUSTER", "NAME_EC2_KEY")
    INSTANCE_COUNT = config.get("CLUSTER", "INSTANCE_COUNT")

    if args.skip_s3:
        logger.info("Skipping s3 bucket creation..")
    else:
        create_bucket(
            KEY,
            SECRET,
            BUCKET_NAME,
            LOCATION
        )
    if args.skip_emr:
        logger.info("Skipping emr cluster creation..")
    else:
        cluster_id, cluster_dns = create_emr(
            KEY,
            SECRET,
            LOCATION,
            NAME_CLUSTER,
            INSTANCE_TYPE,
            INSTANCE_COUNT,
            NAME_EC2_KEY,
            NAME_SECURITY_GROUP
        )
        logger.info("Updating configuration file {}..".format(config_file))
        config.set('CLUSTER', 'HOST', cluster_dns)
        config.set('CLUSTER', 'ID', cluster_id)
        with open(config_file, 'w') as f:
            config.write(f)


if __name__ == "__main__":
    main()
