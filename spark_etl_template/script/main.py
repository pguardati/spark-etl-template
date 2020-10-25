from pyspark.sql import SparkSession

from spark_etl_template.src.library import test_fun

spark = SparkSession.builder.appName("spark_application_template").getOrCreate()
log4jLogger = spark.sparkContext._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger(__name__)
logger.setLevel(log4jLogger.Level.INFO)
logger.info("Logger Initialised..")


def main():
    df = test_fun(spark, logger)
    logger.info("Closing app..")


if __name__ == "__main__":
    main()
