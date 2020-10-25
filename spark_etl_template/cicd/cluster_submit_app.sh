MODULE_NAME="spark_etl_template"

echo "\nImporting spark environment configuration.."
source /usr/lib/spark/conf/spark-env.sh
echo "Spark home: $SPARK_HOME"

echo "\nPackaging application.."
sh $MODULE_NAME/cicd/package_app.sh

echo "\nSubmitting app.."
$SPARK_HOME/bin/spark-submit \
--deploy-mode cluster \
--master yarn \
--conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=./environment/bin/python \
--conf spark.yarn.executorEnv.PYSPARK_PYTHON=./environment/bin/python \
--archives archive/environment.zip#environment \
--py-files archive/$MODULE_NAME.zip \
$MODULE_NAME/script/main.py


