def test_fun(spark, logger):
    logger.info("Creating a dataframe..")
    df_spark = spark.createDataFrame([('Alice', 1), ('Me', 2)])
    return df_spark
