# Step 2: Configure the AWS Glue job that exports the

Amazon Keyspaces table

In the second step of the tutorial you use the script
`setup-export.sh` available on
[Github](https://github.com/aws-samples/amazon-keyspaces-examples/blob/main/scala/datastax-v4/aws-glue/export-to-s3/setup-export.sh "https://github.com/aws-samples/amazon-keyspaces-examples/blob/main/scala/datastax-v4/aws-glue/export-to-s3/setup-export.sh")
to create and configure the AWS Glue job that connects to Amazon Keyspaces using
the SigV4 plugin and then exports the specified table to your Amazon S3 bucket created in the
previous step. Using the script allows you to export data from Amazon Keyspaces without setting up
an Apache Spark cluster.

###### Create an AWS Glue job to export an Amazon Keyspaces table to an Amazon S3 bucket.

- In this step, you run the `setup-export.sh` shell script located in the `export-to-s3/` directory
  to use CloudFormation to create and configure the AWS Glue export job. The
  script takes the following parameters.

```
PARENT_STACK_NAME, EXPORT_STACK_NAME, KEYSPACE_NAME, TABLE_NAME, S3_URI, FORMAT
```

    + `PARENT_STACK_NAME` – The name of the CloudFormation stack created in the previous step.
    + `EXPORT_STACK_NAME` – The name of the CloudFormation stack that creates the AWS Glue export job.
    + `KEYSPACE_NAME` and `TABLE_NAME` – The fully qualified name of the keyspace and table
     to be exported. For this tutorial, we use `catalog.book_awards`, but you can replace this with your own fully
     qualified table name.
    + `S3URI` – The optional URI of the Amazon S3 bucket. The default is the Amazon S3 bucket from the parent stack.
    + `FORMAT` – The optional data format. The default value is `parquet`. For this tutorial,
     to make data load and transformation easier, we use the default.

You can use the following command as an example.

```
setup-export.sh `cfn-setup` `cfn-glue` `catalog` `book_awards`
```

To confirm that the job has been created, you can use the following statement.

```
aws glue list-jobs
```

The output of the statement should look similar to this.

```
`{
 "JobNames": [
 "AmazonKeyspacesExportToS3-cfn-setup-cfn-glue"
 ]
}`
```

To see the details of the job, you can use the following command.

```
aws glue get-job --job-name `AmazonKeyspacesExportToS3-cfn-setup-cfn-glue`
```

The output of the command shows all the details of the job. This includes the
default arguments that you can override when running the job.

```
`{
 "Job": {
 "Name": "AmazonKeyspacesExportToS3-cfn-setup-cfn-glue",
 "JobMode": "SCRIPT",
 "JobRunQueuingEnabled": false,
 "Description": "export to s3",
 "Role": "iam-export-role",
 "CreatedOn": "2025-01-30T15:53:30.765000+00:00",
 "LastModifiedOn": "2025-01-30T15:53:30.765000+00:00",
 "ExecutionProperty": {
 "MaxConcurrentRuns": 1
 },
 "Command": {
 "Name": "glueetl",
 "ScriptLocation": "s3://s3-keyspaces/scripts/cfn-setup-cfn-glue-export.scala",
 "PythonVersion": "3"
 },
 "DefaultArguments": {
 "--write-shuffle-spills-to-s3": "true",
 "--S3_URI": "s3://s3-keyspaces",
 "--TempDir": "s3://s3-keyspaces/shuffle-space/export-sample/",
 "--extra-jars": "s3://s3-keyspaces/jars/spark-cassandra-connector-assembly_2.12-3.1.0.jar,s3://s3-keyspaces/jars/aws-sigv4-auth-cassandra-java-driver-plugin-4.0.9-shaded.jar,s3://s3-keyspaces/jars/spark-extension_2.12-2.8.0-3.4.jar,s3://s3-keyspaces/jars/amazon-keyspaces-helpers-1.0-SNAPSHOT.jar",
 "--class": "GlueApp",
 "--user-jars-first": "true",
 "--enable-metrics": "true",
 "--enable-spark-ui": "true",
 "--KEYSPACE_NAME": "catalog",
 "--spark-event-logs-path": "s3://s3-keyspaces/spark-logs/",
 "--enable-continuous-cloudwatch-log": "true",
 "--write-shuffle-files-to-s3": "true",
 "--FORMAT": "parquet",
 "--TABLE_NAME": "book_awards",
 "--job-language": "scala",
 "--extra-files": "s3://s3-keyspaces/conf/keyspaces-application.conf",
 "--DRIVER_CONF": "keyspaces-application.conf"
 },
 "MaxRetries": 0,
 "AllocatedCapacity": 4,
 "Timeout": 2880,
 "MaxCapacity": 4.0,
 "WorkerType": "G.2X",
 "NumberOfWorkers": 2,
 "GlueVersion": "3.0"
 }
}`
```

If the CloudFormation stack process fails, you can review the errors for the failed stack in the CloudFormation console. You can review the details of the
export job in the AWS Glue console by choosing **ETL jobs** on the left-side menu.

After you have confirmed the details of the AWS Glue export job, proceed to [Step 3: Run the AWS Glue job to export the Amazon Keyspaces table to the Amazon S3 bucket from the
AWS CLI](S3-tutorial-step3.md "S3-tutorial-step3.md") to run the job to
export the data from your Amazon Keyspaces table.
