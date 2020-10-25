# spark-etl-template
This package is an example of how to deploy 
a python application on a spark cluster

# Installation
0 - Install spark 2.3.4 
```
brew install eddies/spark-tap/apache-spark@2.3.4
```

1 - Append the following to `~/.bashrc`:
```
export SPARK_HOME=/usr/local/Cellar/apache-spark@2.3.4/2.3.4/libexec
# allow to call scripts by name
export PATH=$SPARK_HOME/bin:$PATH
export PATH=$SPARK_HOME/python:$PATH
export PATH
# include spark python modules
PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH
# include current repository in python path
PYTHONPATH=~/PycharmProjects/spark-etl-template:$PYTHONPATH 
export PYTHONPATH
```

2 - Install the python environment:
```
conda env create -f spark_etl_template/environment.yml
```
3 - Create the configuration files: follow 
```
docs/setup_config_files.md
```

# Usage
## To deploy the application locally
```
sh spark_etl_template/cicd/local_submit_app.sh
```

## To deploy the application on cluster
1 - Create the cluster
```
python spark_etl_template/script/create_infrastructure.py spark_etl_template/config/
```
2 - Copy the application installer inside the cluster
```
sh spark_etl_template/cicd/cluster_deploy_and_enter.sh
```
3 - From inside the cluster,  
setup the machine and deploy the application
```
sh spark_etl_template/cicd/cluster_setup.sh
source ~/.bashrc
conda activate spark_etl_template 
sh spark_etl_template/cicd/cluster_submit_app.sh
```

4 - To check the application status,  
open the following address with chrome
```
localhost:8157
```
in case of problems, read `docs/setup_spark_ui.md`

5 - To kill all running applications
```
sh spark_etl_template/cicd/cluster_kill_apps.sh
```

# Important:
When the application is completed,  
closet the ssh connection with the cluster  
and destroy the infrastructure, running:
```
python spark_etl_template/script/delete_infrastructure.py spark_etl_template/config/
```

# TODO:
- centralise $MODULE_NAME at the beginning of each script
- make the environment deployment faster (currently done zipping the environment)