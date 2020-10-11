import pandas as pd


def test_fun(spark, logger):
    logger.info("Creating a dataframes..")
    df_pandas = pd.DataFrame([[1, 2], [3, 4]])
    df_spark = spark.createDataFrame([('Alice', 1), ('Me', 2)])
    return df_spark
