import os
import sys
import configparser
import argparse

from spark_etl_template.src.infrastructure import logger, delete_bucket, terminate_emr


def parse_args(args):
    parser = argparse.ArgumentParser(description="Delete output Bucket and Emr cluster")
    parser.add_argument("dir_credentials", help="path of the aws configuration file")
    parser.add_argument("--skip_s3", help="do not delete s3 bucket for output storage", action="store_true")
    parser.add_argument("--skip_emr", help="do not delete emr cluster", action="store_true")
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
    CLUSTER_ID = config.get("CLUSTER", "ID")

    if args.skip_s3:
        logger.info("Skipping s3 bucket deletion..")
    else:
        delete_bucket(
            KEY,
            SECRET,
            BUCKET_NAME
        )

    if args.skip_emr:
        logger.info("Skipping emr cluster deletion..")
    else:
        _ = terminate_emr(
            KEY,
            SECRET,
            LOCATION,
            CLUSTER_ID
        )


if __name__ == "__main__":
    main()
