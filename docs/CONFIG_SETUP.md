# Configuration file templates
This is a description of the configuration files that
should be put in test_spark/config to run the scripts

##dl.cfg
configuration to setup emr cluster and a s3 bucket to store the results
```
[AWS]
aws_access_key_id = your-acces-key
aws_secret_access_key = your-secret-key

[COMMON]
location = us-west-2

[OUTPUT_BUCKET]
name = name-output-s3

[CLUSTER]
name_cluster = spark-cluster-emr
instance_type = m4.xlarge
name_security_group = sg-292b4502
name_ec2_key = spark-cluster
instance_count = 3
```

# spark-env.sh
This file is sourced when running various Spark programs.  
Copy it as spark-env.sh and edit that to configure Spark.
```
# Options read in YARN client/cluster mode
SPARK_LOG_DIR="log/nodes"

# Options for the daemons used in the standalone deploy mode
SPARK_MASTER_HOST=localhost
SPARK_MASTER_PORT=7077
SPARK_MASTER_WEBUI_PORT=8080

SPARK_WORKER_INSTANCES=1
SPARK_WORKER_CORES=2
SPARK_WORKER_MEMORY=1g
```

# spark-defaults.conf 
Default system properties included when running spark-submit.
```
spark.ui.port=4040

spark.eventLog.enabled=true
spark.eventLog.dir=log/events
spark.history.fs.logDirector=log/events

spark.executorEnv.PYSPARK_PYTHON=./environment/bin/python
spark.appMasterEnv.PYSPARK_PYTHON=./environment/bin/python
spark.yarn.appMasterEnv.PYSPARK_PYTHON=./environment/bin/python
spark.yarn.executorEnv.PYSPARK_PYTHON=./environment/bin/python

spark.serializer=org.apache.spark.serializer.KryoSerializer
spark.executor.extraJavaOptions=-XX:+PrintGCDetails -Dkey=value -Dnumbers="one two three"

```

# driver_log4j.properties
Logger configuration
```
log4j.rootCategory=INFO,FILE
log4j.appender.console=org.apache.log4j.ConsoleAppender
log4j.appender.console.target=System.err
log4j.appender.console.layout=org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern=%d{yy/MM/dd HH:mm:ss} %p %c{1}: %m%n

log4j.appender.FILE=org.apache.log4j.RollingFileAppender
log4j.appender.FILE.File=log/events/app_console.log
log4j.appender.FILE.ImmediateFlush=true
log4j.appender.FILE.Threshold=debug
#log4j.appender.FILE.Append=true
log4j.appender.FILE.Append=false
log4j.appender.FILE.MaxFileSize=500MB
log4j.appender.FILE.MaxBackupIndex=10
log4j.appender.FILE.layout=org.apache.log4j.PatternLayout
log4j.appender.FILE.layout.ConversionPattern=%d{yy/MM/dd HH:mm:ss} %p %c{1}: %m%n

#Settings to quiet third party logs that are too verbose
log4j.logger.org.eclipse.jetty=WARN
log4j.logger.org.eclipse.jetty.util.component.AbstractLifeCycle=ERROR
log4j.logger.org.apache.spark.repl.SparkIMain$exprTyper=INFO
log4j.logger.org.apache.spark.repl.SparkILoop$SparkILoopInterpreter=INFO
```
