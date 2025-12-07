# Using serverless storage for Amazon EMR Serverless

With Amazon EMR releases 7.12 and higher, use serverless storage when you run Apache Spark jobs to eliminate local disk provisioning and reduce data processing costs, and prevent job failures from disk capacity constraints. Serverless storage automatically handles shuffle, disk spill, and disk caching operations for your jobs without requiring capacity configuration and stores intermediate data at no cost. Amazon EMR Serverless stores intermediate data in a fully managed serverless storage that scales automatically based on workload demands and enables Spark to release compute workers immediately when idle, reducing compute costs.

## Key benefits

Serverless storage for EMR Serverless provides the following benefits.

- **Zero-configuration storage** –
  Serverless storage eliminates the need to configure local disk type and size for
  each application or job. EMR Serverless automatically manages intermediate data
  operations without capacity planning.
- **Prevents job failures through automatic
  scaling** – Storage capacity scales automatically based on
  workload demand, preventing job failures from insufficient disk capacity.
- **Reduced data processing costs** –
  Serverless storage reduces processing costs through two mechanisms. First,
  intermediate data storage is provided at no cost—you pay only for compute and
  memory resources. Second, decoupled storage with Spark’s dynamic resource
  allocation enables Spark to release workers immediately when idle rather than
  retaining them to preserve intermediate data on local disks. This enables faster
  scale-out and scale-in per Spark stage, reducing compute costs for jobs where
  later stages need fewer workers than initial stages.
- **Encrypted storage with job-level isolation**
  – All intermediate data is encrypted in transit and at rest with strict
  job-level isolation.
- **Fine-grained access control support** –
  Serverless storage supports fine-grained access control through AWS Lake
  Formation integration.

## Getting started

See the following steps to use serverless storage for EMR Serverless in your Spark
workflows.

1. **Create an EMR Serverless application**

Create an EMR Serverless release 7.12 (or later) application with serverless
storage enabled by setting the spark property
`spark.aws.serverlessStorage.enabled` to **true** in the spark-defaults classification.

```
aws emr-serverless create-application \
  --type "SPARK" \
  --name `my-application` \
  --release-label emr-7.12.0 \
  --runtime-configuration '[{
      "classification": "spark-defaults",
        "properties": {
          "spark.aws.serverlessStorage.enabled": "true"
        }
    }]' \
  --region `<AWS_REGION>`
```

2. **Start a Spark job**

Start a job run on your application. Serverless storage for EMR Serverless
automatically handles intermediate data operation such as shuffle for your job.

```
aws emr-serverless start-job-run \
  --application-id `<application-id>` \
  --execution-role-arn `<job-role-arn>` \
  --job-driver '{
    "sparkSubmit": {
      "entryPoint": "s3://`<bucket>`/script.py",
      "sparkSubmitParameters": "--conf spark.executor.cores=4
        --conf spark.executor.memory=20g
        --conf spark.driver.cores=4
        --conf spark.driver.memory=8g
        --conf spark.executor.instances=10"
    }
  }'
```

You can also enable serverless storage for EMR Serverless at the job level
even when it is not enabled at the application level. This will launch worker
nodes enabled with serverless storage to process your jobs. You can also disable
serverless storage for a specific job by setting the same Spark property
`spark.aws.serverlessStorage.enabled` to **false**.

```
# Turn on serverless storage for EMR serverless for a specific job
aws emr-serverless start-job-run \
    --application-id `<application-id>` \
    --execution-role-arn `<job-role-arn>` \
    --job-driver '{
"sparkSubmit": {
"entryPoint": "/usr/lib/spark/examples/jars/`spark-examples`.jar",
            "entryPointArguments": ["1"],
            "sparkSubmitParameters": "--class org.apache.spark.examples.SparkPi
            --conf spark.aws.serverlessStorage.enabled": "true"
        }
    }'
```

###### Note

To continue using traditional local disk provisioning, omit the
`spark.aws.serverlessStorage.enabled` configuration or set it
to **false**.

## Considerations and limitations

- **Release version** – Serverless
  storage is supported on Amazon EMR release 7.12 and later.
- **Data volume limits** – Each job can read and write up to a total of
  200 GB of intermediate data per job run. Jobs exceeding this limit
  will fail with an error message indicating that serverless storage
  limit was reached.
- **Job execution timeout** – Serverless storage supports jobs with
  execution timeouts up to 24 hours. Jobs configured for longer
  execution timeouts will fail with an error message.
- **Pre-initialized capacity** –
  Pre-initialized capacity workers do not support serverless storage. When you
  configure pre-initialized capacity, it will only be utilized by jobs that
  explicitly disable serverless storage at the job level. Jobs with serverless
  storage enabled will always provision new workers on demand and will not use any
  pre-initialized capacity, regardless of the configuration in application
  level.
- **Workload types** – Serverless storage is not supported for streaming
  and interactive jobs.
- **Worker configuration** – Serverless storage is not supported for
  workers with 1 or 2 vCPUs.

## Supported AWS Regions

EMR Serverless support serverless storage in the following regions:

- US East (N. Virginia)
- US West (Oregon)
- Europe (Ireland)
