def test_fun(spark, logger):
    logger.info("Creating a dataframe..")
    return spark.createDataFrame([('Alice', 1), ('Me', 2)])
