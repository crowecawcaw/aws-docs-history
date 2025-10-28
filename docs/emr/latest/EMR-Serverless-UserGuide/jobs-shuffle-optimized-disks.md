# Using shuffle-optimized disks

With Amazon EMR releases 7.1.0 and higher, use shuffle-optimized disks when you run Apache Spark or Hive jobs to improve performance for I/O-intensive workloads.
Compared to standard disks, shuffle-optimized disks provide higher IOPS (I/O operations per second) for faster
data movement and reduced latency during shuffle operations. Shuffle-optimized disks let you attach disk sizes of up to 2 TB per worker,
so configure the appropriate capacity for your workload requirements.

## Key benefits

Shuffle-optimized disks provide the following benefits.

- **High IOPS performance** – shuffle-optimized disks provide
  higher IOPS than standard disks, leading to more efficient and rapid data shuffling during Spark
  and Hive jobs and other shuffle-intensive workloads.
- **Larger disk size** – Shuffle-optimized disks support disk sizes from 20GB to 2TB per worker, so choose the
  appropriate capacity based on your workloads.

## Getting started

See the following steps to use shuffle-optimized disks in your workflows.

Spark

1. Create an EMR Serverless release 7.1.0 application with the following command.

```
aws emr-serverless create-application \
  --type "SPARK" \
  --name my-application-name \
  --release-label emr-7.1.0 \
  --region `<AWS_REGION>`
```

2. Configure your Spark job to include the parameters `spark.emr-serverless.driver.disk.type` and/or `spark.emr-serverless.executor.disk.type` to run with shuffle-optimized disks. You can use
   either one or both parameters, depending on your use case.

```
aws emr-serverless start-job-run \
    --application-id `application-id` \
    --execution-role-arn `job-role-arn` \
    --job-driver '{
        "sparkSubmit": {
            "entryPoint": "/usr/lib/spark/examples/jars/spark-examples.jar",
            "entryPointArguments": ["1"],
            "sparkSubmitParameters": "--class org.apache.spark.examples.SparkPi
            --conf spark.executor.cores=4
            --conf spark.executor.memory=20g
            --conf spark.driver.cores=4
            --conf spark.driver.memory=8g
            --conf spark.executor.instances=1
            --conf spark.emr-serverless.executor.disk.type=shuffle_optimized"
        }
    }'
```

For more information, refer to [Spark job properties](jobs-spark.md#spark-defaults "jobs-spark.md#spark-defaults").

Hive

1. Create an EMR Serverless release 7.1.0 application with the following command.

```
aws emr-serverless create-application \
  --type "HIVE" \
  --name my-application-name \
  --release-label emr-7.1.0 \
  --region `<AWS_REGION>`
```

2. Configure your Hive job to include the parameters `hive.driver.disk.type` and/or `hive.tez.disk.type` to run with shuffle-optimized disks. You can use
   either one or both parameters, depending on your use case.

```
aws emr-serverless start-job-run \
    --application-id `application-id` \
    --execution-role-arn `job-role-arn` \
    --job-driver '{
        "hive": {
            "query": "s3://`<DOC-EXAMPLE-BUCKET>`/emr-serverless-hive/query/hive-query.ql",
            "parameters": "--hiveconf hive.log.explain.output=false"
        }
    }' \
    --configuration-overrides '{
        "applicationConfiguration": [{
            "classification": "hive-site",
            "properties": {
                "hive.exec.scratchdir": "s3://`<DOC-EXAMPLE-BUCKET>`/emr-serverless-hive/hive/scratch",
                "hive.metastore.warehouse.dir": "s3://`<DOC-EXAMPLE-BUCKET>`/emr-serverless-hive/hive/warehouse",
                "hive.driver.cores": "2",
                "hive.driver.memory": "4g",
                "hive.tez.container.size": "4096",
                "hive.tez.cpu.vcores": "1",
                "hive.driver.disk.type": "shuffle_optimized",
                "hive.tez.disk.type": "shuffle_optimized"
            }
        }]
    }'
```

For more information, [Hive job properties](jobs-hive.md#hive-defaults "jobs-hive.md#hive-defaults").

**Configuring an application with pre-initialized capacity**

See the following examples to create applications
based on Amazon EMR release 7.1.0. These applications have the following properties:

- 5 pre-initialized Spark drivers, each with 2 vCPU, 4 GB of memory, and 50 GB of shuffle-optimized disk.
- 50 pre-initialized executors, each with 4 vCPU, 8 GB of memory, and 500 GB of shuffle-optimized disk.

When this application runs Spark jobs, it first consumes the pre-initialized workers and then scales the
on-demand workers up to the maximum capacity of 400 vCPU and 1024 GB of memory.
Optionally, you can omit capacity for either `DRIVER` or `EXECUTOR`.

Spark

```
aws emr-serverless create-application \
  --type "SPARK" \
  --name `<my-application-name>` \
  --release-label emr-7.1.0 \
  --initial-capacity '{
    "DRIVER": {
        "workerCount": 5,
        "workerConfiguration": {
            "cpu": "2vCPU",
            "memory": "4GB",
            "disk": "50GB",
            "diskType": "SHUFFLE_OPTIMIZED"
        }
    },
    "EXECUTOR": {
        "workerCount": 50,
        "workerConfiguration": {
            "cpu": "4vCPU",
            "memory": "8GB",
            "disk": "500GB",
            "diskType": "SHUFFLE_OPTIMIZED"
        }
    }
  }' \
  --maximum-capacity '{
    "cpu": "400vCPU",
    "memory": "1024GB"
  }'
```

Hive

```
aws emr-serverless create-application \
  --type "HIVE" \
  --name `<my-application-name>` \
  --release-label emr-7.1.0 \
  --initial-capacity '{
    "DRIVER": {
        "workerCount": 5,
        "workerConfiguration": {
            "cpu": "2vCPU",
            "memory": "4GB",
            "disk": "50GB",
            "diskType": "SHUFFLE_OPTIMIZED"
        }
    },
    "EXECUTOR": {
        "workerCount": 50,
        "workerConfiguration": {
            "cpu": "4vCPU",
            "memory": "8GB",
            "disk": "500GB",
            "diskType": "SHUFFLE_OPTIMIZED"
        }
    }
  }' \
  --maximum-capacity '{
    "cpu": "400vCPU",
    "memory": "1024GB"
  }'
```
