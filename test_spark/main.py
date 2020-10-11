import os
import logging
from pyspark.sql import SparkSession

from test_spark.main_utils import test_fun

spark = SparkSession.builder.appName("hello").getOrCreate()
log4jLogger = spark.sparkContext._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger(__name__)
logger.setLevel(log4jLogger.Level.INFO)
logger.info("Logger Initialised..")


def main():
    df = test_fun(spark, logger)
    logger.info("Closing app..")
    # while(1):
    #     pass


if __name__ == "__main__":
    main()

# create history
# log 1
# log multiple local clusters
# check how to print local env
