echo "\nkilling master and slave.."
/usr/local/Cellar/apache-spark/3.0.1/libexec/sbin/stop-master.sh
/usr/local/Cellar/apache-spark/3.0.1/libexec/sbin/stop-slave.sh
echo "no master, no slave:"
jps

# configuration using flags - should be done with spark-env.sh
/usr/local/Cellar/apache-spark/3.0.1/libexec/sbin/start-master.sh --host localhost --webui-port 8080
/usr/local/Cellar/apache-spark/3.0.1/libexec/sbin/start-slave.sh spark://localhost:7077 --cores 2 --memory 1g
echo "\nmaster and slave are on:"
jps

# configuration using flags - should be done with spark-default.conf
echo "submitting spark app"
/usr/local/bin/spark-submit \
--master spark://localhost:7077 \
--deploy-mode client \
--driver-java-options "-Dlog4j.configuration=file:../conf/driver_log4j.properties" \
--conf spark.ui.port=4040 \
--conf spark.eventLog.enabled=True \
--conf spark.eventLog.dir=../log \
--conf spark.history.fs.logDirector=../log \
./main.py > ../log/log-console1.txt
