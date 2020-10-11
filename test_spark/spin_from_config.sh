echo "\nKilling master and slave.."
/usr/local/Cellar/apache-spark/3.0.1/libexec/sbin/stop-master.sh
/usr/local/Cellar/apache-spark/3.0.1/libexec/sbin/stop-slave.sh
jps

echo "Reset logs folder"
mkdir log/events
mkdir log/nodes

echo "\nCopying env. variables and spinning master and slaves:"
cp conf/spark-env.sh /usr/local/Cellar/apache-spark/3.0.1/libexec/conf/spark-env.sh
/usr/local/Cellar/apache-spark/3.0.1/libexec/sbin/start-master.sh
/usr/local/Cellar/apache-spark/3.0.1/libexec/sbin/start-slave.sh spark://localhost:7077
jps

echo "\nCreating zip archive.."
zip -r test_spark.zip test_spark

echo "\nSubmitting file using configuration file"
/usr/local/bin/spark-submit \
--driver-java-options "-Dlog4j.configuration=file:conf/driver_log4j.properties" \
--properties-file conf/spark-defaults.conf \
--deploy-mode client \
--py-files test_spark.zip \
test_spark/main.py > log/events/app_response.txt
