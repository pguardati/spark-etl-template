# ---  inside the cluster
echo "\nImport spark environment configuration"
export SPARK_HOME=/usr/local/Cellar/apache-spark/3.0.1/libexec/
cp conf/spark-env.sh $SPARK_HOME/conf/spark-env.sh

echo "\nKilling master and slave.."
$SPARK_HOME/sbin/stop-master.sh
$SPARK_HOME/sbin/stop-slave.sh
jps

echo "Reset logs folder"
mkdir log/events
mkdir log/nodes

echo "\nCopying env. variables and spinning master and slaves:"
$SPARK_HOME/sbin/start-master.sh
$SPARK_HOME/sbin/start-slave.sh spark://localhost:7077
jps

echo "\nSubmitting file using configuration file"
$SPARK_HOME/bin/spark-submit \
--driver-java-options "-Dlog4j.configuration=file:conf/driver_log4j.properties" \
--properties-file conf/spark-defaults.conf \
--deploy-mode client \
--py-files test_spark.zip \
--archives environment.tar.gz#environment \
test_spark/script/main.py > log/events/app_response.txt

