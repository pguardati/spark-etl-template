MODULE_NAME="spark_etl_template"
DIR_PACKAGING="archive"

# --- outside the cluster
echo "\Creating archive folder"
mkdir $DIR_PACKAGING

echo "\nCreating zip archive of python module and environment.."
conda env export --no-builds --from-history | grep -v "^prefix: "> $MODULE_NAME/environment.yml
conda-pack -o $DIR_PACKAGING/environment.zip -n $MODULE_NAME --format zip
zip -r $DIR_PACKAGING/$MODULE_NAME.zip $MODULE_NAME

echo "\nCreate log folder"
mkdir log/
