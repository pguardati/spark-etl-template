# --- outside the cluster
echo "\Creating archive folder"
DIR_PACKAGING="archive"
mkdir $DIR_PACKAGING

echo "\nCreating zip archive of python module.."
zip -r $DIR_PACKAGING/test_spark.zip test_spark
conda-pack -o $DIR_PACKAGING/environment.zip -n test_spark --format zip

echo "\nCreate log folder"
mkdir log/
