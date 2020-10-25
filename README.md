# TestSpark
This package is an example of how to deploy 
a python application on a spark cluster

# Installation
0 - Install spark 2.3.4 
```
brew install eddies/spark-tap/apache-spark@2.3.4
```

1 - Append the following to.bashrc:
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
PYTHONPATH=~/PycharmProjects/TestSpark:$PYTHONPATH 
export PYTHONPATH
```

2 - Install the python environment:
```
conda env create -f test_spark/environment.yml
```
3 - Create the configuration files: follow 
```
docs/setup_config_files.md
```

# Usage
##To deploy the application locally
```
sh test_spark/cicd/local_submit_app.sh
```

##To deploy the application on cluster
1 - create the cluster
```
python test_spark/script/create_infrastructure.py test_spark/config/
```
2 - copy the application installer inside the cluster
```
sh test_spark/cicd/cluster_deploy_and_enter.sh
```
3 - from inside the cluster, setup the machine and deploy the application
```
sh test_spark/cicd/cluster_setup.sh
source ~/.bashrc
conda activate test_spark 
sh test_spark/cicd/cluster_submit_app.sh
```

3 - to check the application status, open with chrome
```
localhost:8157
```
in case of problems, read these instructions: 
```
docs/setup_spark_ui.md
```

4 - to kill all running applications
```
sh test_spark/cicd/cluster_kill_apps.sh
```

# Important:
When the application is completed,  
exit the cluster and destroy the infrastructure:
```
python test_spark/script/delete_infrastructure.py test_spark/config/
```

#TODO:
- centralise $MODULE_NAME at the beginning of each script
- make the environment deployment faster (currently done zipping the environment)