MODULE_NAME="spark_etl_template"

# get host from config file
host=$(grep -i 'host' $MODULE_NAME/config/dl.cfg | sed -E 's/host = (.*)/\1/')

# push the code into the cluster
rsync -e "ssh -i ~/.aws/spark-cluster.pem" -av ./$MODULE_NAME hadoop@"$host":~/.

# enter in the cluster, forwarding spark history server port 18080 to local port 8157
ssh -i ~/.aws/spark-cluster.pem -L 8157:localhost:18080 hadoop@"$host"

