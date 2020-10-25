MODULE_NAME="test_spark"

echo "\nImporting spark environment configuration.."
echo "Spark home: $SPARK_HOME"
cp ../config/spark-env-local.sh $SPARK_HOME/conf/spark-env.sh

echo "\nPackaging application.."
sh $MODULE_NAME/cicd/package_app.sh

echo "\nKilling master and slave.."
$SPARK_HOME/sbin/stop-master.sh
$SPARK_HOME/sbin/stop-slave.sh

echo "\nSpinning master and slaves:"
$SPARK_HOME/sbin/start-master.sh
$SPARK_HOME/sbin/start-slave.sh spark://localhost:7077

echo "\nSubmitting app.."
$SPARK_HOME/bin/spark-submit \
--deploy-mode client \
--master spark://localhost:7077 \
--driver-java-options "-Dlog4j.configuration=file:test_spark/config/driver_log4j.properties" \
--properties-file test_spark/config/spark-defaults.conf \
--py-files archive/test_spark.zip \
--archives archive/environment.zip#environment \
test_spark/script/main.py

echo "\nApplication Completed"
