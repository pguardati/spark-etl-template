echo "\nkilling master and slave.."
/usr/local/Cellar/apache-spark/3.0.1/libexec/sbin/stop-master.sh
/usr/local/Cellar/apache-spark/3.0.1/libexec/sbin/stop-slave.sh
echo "no master, no slave:"
jps

echo "\nCopying env. variables and spinning master and slaves:"
cp ../conf/spark-env.sh /usr/local/Cellar/apache-spark/3.0.1/libexec/conf/spark-env.sh
/usr/local/Cellar/apache-spark/3.0.1/libexec/sbin/start-master.sh
/usr/local/Cellar/apache-spark/3.0.1/libexec/sbin/start-slave.sh spark://localhost:7077
jps

echo "\nSubmitting file using configuration file"
/usr/local/bin/spark-submit \
--deploy-mode client \
--driver-java-options "-Dlog4j.configuration=file:../conf/driver_log4j.properties" \
--properties-file ../conf/spark-defaults.conf \
--py-files ./main_utils.py \
./main.py > ../log/driver_console.txt
