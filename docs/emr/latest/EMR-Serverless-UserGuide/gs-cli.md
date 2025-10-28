# Getting started from the AWS CLI

Get started with EMR Serverless from the AWS CLI with commands to create an application, run jobs, check job run output, and delete your resources.

## Step 1: Create an EMR Serverless application

Use the [`emr-serverless
 create-application`](../../../emr-serverless/latest/APIReference/API_CreateApplication.md "../../../emr-serverless/latest/APIReference/API_CreateApplication.md") command to create your first EMR Serverless
application. You need to specify the application type and the the Amazon EMR release label
associated with the application version you want to use. The name of the application is
optional.

Spark
To create a Spark application, run the following command.

```
aws emr-serverless create-application \
    --release-label emr-6.6.0 \
    --type "SPARK" \
    --name my-application
```

Hive
To create a Hive application, run the following command.

```
aws emr-serverless create-application \
    --release-label emr-6.6.0 \
    --type "HIVE" \
    --name my-application
```

Note the application ID returned in the output. You'll use the ID to start the
application and during job submission, referred to after this as the
`application-id`.

Before you move on to [Step 2: Submit a job run to your EMR Serverless
application](#gs-job-run-cli "#gs-job-run-cli"),
make sure that your application has reached the `CREATED` state with the [`get-application`](../../../emr-serverless/latest/APIReference/API_GetApplication.md "../../../emr-serverless/latest/APIReference/API_GetApplication.md") API.

```
aws emr-serverless get-application \
    --application-id `application-id`
```

EMR Serverless creates workers to accommodate your requested jobs. By default, these
are created on demand, but you can also specify a pre-initialized capacity by setting the
`initialCapacity` parameter when you create the application. You can also limit
the total maximum capacity that an application can use with the `maximumCapacity`
parameter. To learn more about these options, see [Configuring an application when working with EMR Serverless](application-capacity.md "application-capacity.md").

## Step 2: Submit a job run to your EMR Serverless

application

Now your EMR Serverless application is ready to run jobs.

Spark
In this step, we use a PySpark script to compute the number of occurrences of
unique words across multiple text files. A public, read-only S3 bucket stores both the
script and the dataset. The application sends the output file and the log data from
the Spark runtime to `/output` and `/logs` directories in the S3
bucket that you created.

###### To run a Spark job

1. Use the following command to copy the sample script we will run into your new
   bucket.

```
aws s3 cp s3://us-east-1.elasticmapreduce/emr-containers/samples/wordcount/scripts/wordcount.py s3://`amzn-s3-demo-bucket`/scripts/
```

2. In the following command, substitute
   `application-id` with your application
   ID. Substitute `job-role-arn` with the
   runtime role ARN you created in [Create a job runtime role](getting-started.md#gs-runtime-role "getting-started.md#gs-runtime-role"). Substitute
   `job-run-name` with the name you want to
   call your job run. Replace all
   `amzn-s3-demo-bucket` strings with the Amazon S3
   bucket that you created, and add `/output` to the path. This creates a
   new folder in your bucket where EMR Serverless can copy the output files of your
   application.

```
aws emr-serverless start-job-run \
    --application-id `application-id` \
    --execution-role-arn `job-role-arn` \
    --name `job-run-name` \
    --job-driver '{
        "sparkSubmit": {
          "entryPoint": "s3://`amzn-s3-demo-bucket`/scripts/wordcount.py",
          "entryPointArguments": ["s3://`amzn-s3-demo-bucket`/emr-serverless-spark/output"],
          "sparkSubmitParameters": "--conf spark.executor.cores=1 --conf spark.executor.memory=4g --conf spark.driver.cores=1 --conf spark.driver.memory=4g --conf spark.executor.instances=1"
        }
    }'
```

3. Note the job run ID returned in the output . Replace
   `job-run-id` with this ID in the
   following steps.

Hive
In this tutorial, we create a table, insert a few records, and run a count
aggregation query. To run the Hive job, first create a file that contains all Hive
queries to run as part of single job, upload the file to S3, and specify this S3 path
when you start the Hive job.

###### To run a Hive job

1. Create a file called `hive-query.ql` that contains all the queries
   that you want to run in your Hive job.

```
create database if not exists emrserverless;
use emrserverless;
create table if not exists test_table(id int);
drop table if exists Values__Tmp__Table__1;
insert into test_table values (1),(2),(2),(3),(3),(3);
select id, count(id) from test_table group by id order by id desc;
```

2. Upload `hive-query.ql` to your S3 bucket with the following
   command.

```
aws s3 cp hive-query.ql s3://`amzn-s3-demo-bucket`/emr-serverless-hive/query/hive-query.ql
```

3. In the following command, substitute
   `application-id` with your own
   application ID. Substitute `job-role-arn`
   with the runtime role ARN you created in [Create a job runtime role](getting-started.md#gs-runtime-role "getting-started.md#gs-runtime-role"). Replace all
   `amzn-s3-demo-bucket` strings with the
   Amazon S3 bucket that you created, and add `/output` and `/logs`
   to the path. This creates new folders in your bucket, where EMR Serverless can
   copy the output and log files of your application.

```
aws emr-serverless start-job-run \
    --application-id `application-id` \
    --execution-role-arn `job-role-arn` \
    --job-driver '{
        "hive": {
          "query": "s3://`amzn-s3-demo-bucket`/emr-serverless-hive/query/hive-query.ql",
          "parameters": "--hiveconf hive.log.explain.output=false"
        }
    }' \
    --configuration-overrides '{
      "applicationConfiguration": [{
        "classification": "hive-site",
          "properties": {
            "hive.exec.scratchdir": "s3://`amzn-s3-demo-bucket`/emr-serverless-hive/hive/scratch",
            "hive.metastore.warehouse.dir": "s3://`amzn-s3-demo-bucket`/emr-serverless-hive/hive/warehouse",
            "hive.driver.cores": "2",
            "hive.driver.memory": "4g",
            "hive.tez.container.size": "4096",
            "hive.tez.cpu.vcores": "1"
            }
        }],
        "monitoringConfiguration": {
          "s3MonitoringConfiguration": {
            "logUri": "s3://`amzn-s3-demo-bucket`/emr-serverless-hive/logs"
           }
        }
    }'
```

4. Note the job run ID returned in the output. Replace
   `job-run-id` with this ID in the
   following steps.

## Step 3: Review your job run's output

The job run should typically take 3-5 minutes to complete.

Spark
You can check for the state of your Spark job with the following command.

```
aws emr-serverless get-job-run \
    --application-id `application-id` \
    --job-run-id `job-run-id`
```

With your log destination set to
`s3://`amzn-s3-demo-bucket`/emr-serverless-spark/logs`,
you can find the logs for this specific job run under
`s3://`amzn-s3-demo-bucket`/emr-serverless-spark/logs/applications/`application-id`/jobs/`job-run-id``.

For Spark applications, EMR Serverless pushes event logs every 30 seconds to the
`sparklogs` folder in your S3 log destination. When your job completes,
Spark runtime logs for the driver and executors upload to folders named appropriately
by the worker type, such as `driver` or `executor`. The output
of the PySpark job uploads to
`s3://`amzn-s3-demo-bucket`/output/`.

Hive
You can check for the state of your Hive job with the following command.

```
aws emr-serverless get-job-run \
    --application-id `application-id` \
    --job-run-id `job-run-id`
```

With your log destination set to
`s3://`amzn-s3-demo-bucket`/emr-serverless-hive/logs`,
you can find the logs for this specific job run under
`s3://`amzn-s3-demo-bucket`/emr-serverless-hive/logs/applications/`application-id`/jobs/`job-run-id``.

For Hive applications, EMR Serverless continuously uploads the Hive driver to the
`HIVE_DRIVER` folder, and Tez tasks logs to the `TEZ_TASK`
folder, of your S3 log destination. After the job run reaches the
`SUCCEEDED` state, the output of your Hive query becomes available in the
Amazon S3 location that you specified in the `monitoringConfiguration` field of
`configurationOverrides`.

## Step 4: Clean up

When you’re done working with this tutorial, consider deleting the resources that you
created. We recommend that you release resources that you don't intend to use again.

### Delete your application

To delete an application, use the following command.

```
aws emr-serverless delete-application \
    --application-id `application-id`
```

### Delete your S3 log bucket

To delete your S3 logging and output bucket, use the following command. Replace
`amzn-s3-demo-bucket` with the actual name of the
S3 bucket created in [Prepare storage for EMR Serverless](getting-started.md#gs-prepare-storage "getting-started.md#gs-prepare-storage")..

```
aws s3 rm s3://`amzn-s3-demo-bucket` --recursive
aws s3api delete-bucket --bucket `amzn-s3-demo-bucket`
```

### Delete your job runtime role

To delete the runtime role, detach the policy from the role. You can then delete both
the role and the policy.

```
aws iam detach-role-policy \
    --role-name EMRServerlessS3RuntimeRole \
    --policy-arn `policy-arn`
```

To delete the role, use the following command.

```
aws iam delete-role \
    --role-name EMRServerlessS3RuntimeRole
```

To delete the policy that was attached to the role, use the following command.

```
aws iam delete-policy \
    --policy-arn `policy-arn`
```

For more examples of running Spark and Hive jobs, see [Using Spark configurations when you run EMR Serverless jobs](jobs-spark.md "jobs-spark.md") and [Using Hive configurations when you run EMR Serverless jobs](jobs-hive.md "jobs-hive.md").
