#!/usr/bin/env bash

# This file is sourced when running various Spark programs.
# Copy it as spark-env.sh and edit that to configure Spark for your site.

# Options read in YARN client/cluster mode
SPARK_CONF_DIR="conf"
SPARK_LOG_DIR="log/nodes"

# Options for the daemons used in the standalone deploy mode
SPARK_MASTER_HOST=localhost
SPARK_MASTER_PORT=7077
SPARK_MASTER_WEBUI_PORT=8080
SPARK_WORKER_INSTANCES=1
SPARK_WORKER_CORES=2
SPARK_WORKER_MEMORY=1g
