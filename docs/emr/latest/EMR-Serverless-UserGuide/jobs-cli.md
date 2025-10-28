# Running jobs from the AWS CLI

You can create, describe, and delete individual jobs on the AWS CLI. You can also list all
of your jobs to access them at a glance.

To submit a new job, use `start-job-run`. Provide the ID of the application
that you want to run, along with job-specific properties. For Spark examples, refer to [Using Spark configurations when you run EMR Serverless jobs](jobs-spark.md "jobs-spark.md"). For Hive examples, refer to [Using Hive configurations when you run EMR Serverless jobs](jobs-hive.md "jobs-hive.md"). This command returns your
`application-id`, ARN, and new `job-id`.

Each job run has a set timeout duration. If the job run exceeds this duration,
EMR Serverless will automatically cancel it. The default timeout is 12 hours. When you start
your job run, configure this timeout setting to a value that meets your job
requirements. Configure the value with the `executionTimeoutMinutes`
property.

```
aws emr-serverless start-job-run \
  --application-id `application-id` \
  --execution-role-arn `job-role-arn` \
  --execution-timeout-minutes 15 \
  --job-driver '{
    "hive": {
        "query": "s3://`amzn-s3-demo-bucket`/scripts/create_table.sql",
        "parameters": "--hiveconf hive.exec.scratchdir=s3://`amzn-s3-demo-bucket`/hive/scratch --hiveconf hive.metastore.warehouse.dir=s3://`amzn-s3-demo-bucket`/hive/warehouse"
    }
   }' \
  --configuration-overrides '{
    "applicationConfiguration": [{
        "classification": "hive-site",
        "properties": {
            "hive.client.cores": "2",
            "hive.client.memory": "4GIB"
        }
    }]
}'
```

To describe a job, use `get-job-run`. This command returns job-specific
configurations and the set capacity for your new job.

```
aws emr-serverless get-job-run \
--job-run-id `job-id` \
--application-id `application-id`
```

To list your jobs, use `list-job-runs`. This command returns an abbreviated set
of properties that includes job type, state, and other high-level attributes. If you don't
want to access all of your jobs, specify the maximum number of jobs you want to access, up
to 50. The following example specifies that you want to access your two last job runs.

```
aws emr-serverless list-job-runs \
--max-results 2 \
--application-id `application-id`
```

To cancel a job, use `cancel-job-run`. Provide the `application-id`
and the `job-id` of the job that you want to cancel.

```
aws emr-serverless cancel-job-run \
--job-run-id `job-id` \
--application-id `application-id`
```

For more information on how to run jobs from the AWS CLI, refer to the [EMR Serverless
API Reference](../../../emr-serverless/latest/APIReference/Welcome.md "../../../emr-serverless/latest/APIReference/Welcome.md").
