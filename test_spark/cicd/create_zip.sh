# --- outside the cluster
echo "\nCreating zip archive of python module.."
zip -r test_spark.zip test_spark
conda-pack -n test_spark -o environment.tar.gz

echo "\nReset logs folder"
mkdir log/events
mkdir log/nodes
