# Troubleshooting errors Spark errors

If you encounter errors in AWS Glue, use the following information to help you find the source of the
problems and fix them.

###### Note

The AWS Glue GitHub repository contains additional troubleshooting guidance in [AWS Glue
Frequently Asked Questions](https://github.com/aws-samples/aws-glue-samples/blob/master/FAQ_and_How_to.md "https://github.com/aws-samples/aws-glue-samples/blob/master/FAQ_and_How_to.md").

###### Topics

- [Error: Resource unavailable](#error-resource-unavailable "#error-resource-unavailable")
- [Error: Could not find S3 endpoint or NAT gateway for
  subnetId in VPC](#error-s3-subnet-vpc-NAT-configuration "#error-s3-subnet-vpc-NAT-configuration")
- [Error: Inbound rule in security group required](#error-inbound-self-reference-rule "#error-inbound-self-reference-rule")
- [Error: Outbound rule in security group required](#error-outbound-self-reference-rule "#error-outbound-self-reference-rule")
- [Error: Job run failed because the role passed should be given
  assume role permissions for the AWS Glue service](#error-assume-role-user-policy "#error-assume-role-user-policy")
- [Error: DescribeVpcEndpoints action is unauthorized. unable
  to validate VPC ID vpc-id](#error-DescribeVpcEndpoints-permission "#error-DescribeVpcEndpoints-permission")
- [Error: DescribeRouteTables action is unauthorized. unable
  to validate subnet id: Subnet-id in VPC id: vpc-id](#error-DescribeRouteTables-permission "#error-DescribeRouteTables-permission")
- [Error: Failed to call ec2:DescribeSubnets](#error-DescribeSubnets-permission "#error-DescribeSubnets-permission")
- [Error: Failed to call ec2:DescribeSecurityGroups](#error-DescribeSecurityGroups-permission "#error-DescribeSecurityGroups-permission")
- [Error: Could not find subnet for AZ](#error-az-not-available "#error-az-not-available")
- [Error: Job run exception when writing to a JDBC target](#error-job-run-jdbc-target "#error-job-run-jdbc-target")
- [Error: Amazon S3: The operation is not valid for the object's storage class](#error-s3-operation-not-valid "#error-s3-operation-not-valid")
- [Error: Amazon S3 timeout](#error-s3-timeout "#error-s3-timeout")
- [Error: Amazon S3 access denied](#error-s3-access-denied "#error-s3-access-denied")
- [Error: Amazon S3 access key ID does not exist](#error-s3-accesskeyid-not-found "#error-s3-accesskeyid-not-found")
- [Error: Job run fails when accessing Amazon S3 with an
  s3a:// URI](#error-s3a-uri-directory-listing "#error-s3a-uri-directory-listing")
- [Error: Amazon S3 service token expired](#error-s3-service-token-expired "#error-s3-service-token-expired")
- [Error: No private DNS for network interface found](#error-no-private-DNS "#error-no-private-DNS")
- [Error: Development endpoint provisioning failed](#error-development-endpoint-failed "#error-development-endpoint-failed")
- [Error: Notebook server CREATE_FAILED](#error-notebook-server-ec2-instance-profile "#error-notebook-server-ec2-instance-profile")
- [Error: Local notebook fails to start](#error-local-notebook-fails-to-start "#error-local-notebook-fails-to-start")
- [Error: Running crawler failed](#error-running-crawler-failed "#error-running-crawler-failed")
- [Error: Partitions were not updated](#error-update-from-job-partitions "#error-update-from-job-partitions")
- [Error: Job bookmark update failed due to version mismatch](#error-job-bookmarks-limitation "#error-job-bookmarks-limitation")
- [Error: A job is reprocessing data when job bookmarks are
  enabled](#error-job-bookmarks-reprocess-data "#error-job-bookmarks-reprocess-data")
- [Error: Failover behavior between VPCs in AWS Glue](#vpc-failover-behavior-error-10 "#vpc-failover-behavior-error-10")

## Error: Resource unavailable

If AWS Glue returns a resource unavailable message, you can view error messages or logs to help
you learn more about the issue. The following tasks describe general methods for troubleshooting.

- For any connections and development endpoints that you use, check that your cluster has not run out of
  elastic network interfaces.

## Error: Could not find S3 endpoint or NAT gateway for

subnetId in VPC

Check the subnet ID and VPC ID in the message to help you diagnose the issue.

- Check that you have an Amazon S3 VPC endpoint set up, which is required with AWS Glue. In addition,
  check your NAT gateway if that's part of your configuration. For more information, see [Amazon VPC endpoints for Amazon S3](vpc-endpoints-s3.md "vpc-endpoints-s3.md").

## Error: Inbound rule in security group required

At least one security group must open all ingress ports. To limit traffic, the source security group in your
inbound rule can be restricted to the same security group.

- For any connections that you use, check your security group for an inbound rule that is self-referencing.
  For more information, see [Setting up network access to data stores](start-connecting.md "start-connecting.md").
- When you are using a development endpoint, check your security group for an inbound rule that is
  self-referencing. For more information, see [Setting up network access to data stores](start-connecting.md "start-connecting.md").

## Error: Outbound rule in security group required

At least one security group must open all egress ports. To limit traffic, the source security group in your
outbound rule can be restricted to the same security group.

- For any connections that you use, check your security group for an outbound rule that is self-referencing.
  For more information, see [Setting up network access to data stores](start-connecting.md "start-connecting.md").
- When you are using a development endpoint, check your security group for an outbound rule that is
  self-referencing. For more information, see [Setting up network access to data stores](start-connecting.md "start-connecting.md").

## Error: Job run failed because the role passed should be given

assume role permissions for the AWS Glue service

The user who defines a job must have permission for `iam:PassRole` for
AWS Glue.

- When a user creates an AWS Glue job, confirm that the user's role contains a policy that
  contains `iam:PassRole` for AWS Glue. For more information, see [Step 3: Attach a policy to users or groups that access AWS Glue](attach-policy-iam-user.md "attach-policy-iam-user.md").

## Error: DescribeVpcEndpoints action is unauthorized. unable

to validate VPC ID vpc-id

- Check the policy passed to AWS Glue for the `ec2:DescribeVpcEndpoints`
  permission.

## Error: DescribeRouteTables action is unauthorized. unable

to validate subnet id: Subnet-id in VPC id: vpc-id

- Check the policy passed to AWS Glue for the `ec2:DescribeRouteTables`
  permission.

## Error: Failed to call ec2:DescribeSubnets

- Check the policy passed to AWS Glue for the `ec2:DescribeSubnets`
  permission.

## Error: Failed to call ec2:DescribeSecurityGroups

- Check the policy passed to AWS Glue for the `ec2:DescribeSecurityGroups`
  permission.

## Error: Could not find subnet for AZ

- The Availability Zone might not be available to AWS Glue. Create and use a new subnet in a
  different Availability Zone from the one specified in the message.

## Error: Job run exception when writing to a JDBC target

When you are running a job that writes to a JDBC target, the job might encounter errors in the following
scenarios:

- If your job writes to a Microsoft SQL Server table, and the table has columns defined as type
  `Boolean`, then the table must be predefined in the SQL Server database. When you define the job on
  the AWS Glue console using a SQL Server target with the option **Create tables in your
  data target**, don't map any source columns to a target column with data type `Boolean`.
  You might encounter an error when the job runs.

You can avoid the error by doing the following:

    + Choose an existing table with the **Boolean** column.
    + Edit the `ApplyMapping` transform and map the **Boolean** column in the
     source to a number or string in the target.
    + Edit the `ApplyMapping` transform to remove the **Boolean** column from
     the source.

- If your job writes to an Oracle table, you might need to adjust the length of names of Oracle objects. In
  some versions of Oracle, the maximum identifier length is limited to 30 bytes or 128 bytes. This limit affects
  the table names and column names of Oracle target data stores.

You can avoid the error by doing the following:

    + Name Oracle target tables within the limit for your version.
    + The default column names are generated from the field names in the data. To handle the case when the
     column names are longer than the limit, use `ApplyMapping` or `RenameField`
     transforms to change the name of the column to be within the limit.

## Error: Amazon S3: The operation is not valid for the object's storage class

If AWS Glue returns this error, your AWS Glue job may have been reading data from tables that have partitions across Amazon S3 storage class tiers.

- By using storage class exclusions, you can ensure that your AWS Glue jobs will work on tables that have partitions across these storage class tiers. Without exclusions, jobs that read data from these tiers fail with the following error: `AmazonS3Exception: The operation is not valid for the object's storage class`.

For more information, see [Excluding Amazon S3 storage classes](aws-glue-programming-etl-storage-classes.md "aws-glue-programming-etl-storage-classes.md").

## Error: Amazon S3 timeout

If AWS Glue returns a connect timed out error, it might be because it is trying to access an Amazon S3
bucket in another AWS Region.

- An Amazon S3 VPC endpoint can only route traffic to buckets within an AWS Region. If you need to connect to
  buckets in other Regions, a possible workaround is to use a NAT gateway. For more information, see [NAT Gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md").

## Error: Amazon S3 access denied

If AWS Glue returns an access denied error to an Amazon S3 bucket or object, it might be because the
IAM role provided does not have a policy with permission to your data store.

- An ETL job must have access to an Amazon S3 data store used as a source or target. A crawler must have access
  to an Amazon S3 data store that it crawls. For more information, see [Step 2: Create an IAM role for AWS Glue](create-an-iam-role.md "create-an-iam-role.md").

## Error: Amazon S3 access key ID does not exist

If AWS Glue returns an access key ID does not exist error when running a job, it might be because
of one of the following reasons:

- An ETL job uses an IAM role to access data stores, confirm that the IAM role for your job was not
  deleted before the job started.
- An IAM role contains permissions to access your data stores, confirm that any attached Amazon S3 policy
  containing `s3:ListBucket` is correct.

## Error: Job run fails when accessing Amazon S3 with an

`s3a://` URI

If a job run returns an error like _Failed to parse XML document with handler class_ , it
might be because of a failure trying to list hundreds of files using an `s3a://` URI. Access your data
store using an `s3://` URI instead. The following exception trace highlights the errors to look
for:

```

**1. com.amazonaws.SdkClientException: Failed to parse XML document with handler class com.amazonaws.services.s3.model.transform.XmlResponsesSaxParser$ListBucketHandler**
2.	at com.amazonaws.services.s3.model.transform.XmlResponsesSaxParser.parseXmlInputStream(XmlResponsesSaxParser.java:161)
3.	at com.amazonaws.services.s3.model.transform.XmlResponsesSaxParser.parseListBucketObjectsResponse(XmlResponsesSaxParser.java:317)
4.	at com.amazonaws.services.s3.model.transform.Unmarshallers$ListObjectsUnmarshaller.unmarshall(Unmarshallers.java:70)
5.	at com.amazonaws.services.s3.model.transform.Unmarshallers$ListObjectsUnmarshaller.unmarshall(Unmarshallers.java:59)
6.	at com.amazonaws.services.s3.internal.S3XmlResponseHandler.handle(S3XmlResponseHandler.java:62)
7.	at com.amazonaws.services.s3.internal.S3XmlResponseHandler.handle(S3XmlResponseHandler.java:31)
8.	at com.amazonaws.http.response.AwsResponseHandlerAdapter.handle(AwsResponseHandlerAdapter.java:70)
9.	at com.amazonaws.http.AmazonHttpClient$RequestExecutor.handleResponse(AmazonHttpClient.java:1554)
10.	at com.amazonaws.http.AmazonHttpClient$RequestExecutor.executeOneRequest(AmazonHttpClient.java:1272)
11.	at com.amazonaws.http.AmazonHttpClient$RequestExecutor.executeHelper(AmazonHttpClient.java:1056)
12.	at com.amazonaws.http.AmazonHttpClient$RequestExecutor.doExecute(AmazonHttpClient.java:743)
13.	at com.amazonaws.http.AmazonHttpClient$RequestExecutor.executeWithTimer(AmazonHttpClient.java:717)
14.	at com.amazonaws.http.AmazonHttpClient$RequestExecutor.execute(AmazonHttpClient.java:699)
15.	at com.amazonaws.http.AmazonHttpClient$RequestExecutor.access$500(AmazonHttpClient.java:667)
16.	at com.amazonaws.http.AmazonHttpClient$RequestExecutionBuilderImpl.execute(AmazonHttpClient.java:649)
17.	at com.amazonaws.http.AmazonHttpClient.execute(AmazonHttpClient.java:513)
18.	at com.amazonaws.services.s3.AmazonS3Client.invoke(AmazonS3Client.java:4325)
19.	at com.amazonaws.services.s3.AmazonS3Client.invoke(AmazonS3Client.java:4272)
20.	at com.amazonaws.services.s3.AmazonS3Client.invoke(AmazonS3Client.java:4266)
21.	at com.amazonaws.services.s3.AmazonS3Client.listObjects(AmazonS3Client.java:834)
**22. at org.apache.hadoop.fs.s3a.S3AFileSystem.getFileStatus(S3AFileSystem.java:971)**
**23. at org.apache.hadoop.fs.s3a.S3AFileSystem.deleteUnnecessaryFakeDirectories(S3AFileSystem.java:1155)**
24.	at org.apache.hadoop.fs.s3a.S3AFileSystem.finishedWrite(S3AFileSystem.java:1144)
**25. at org.apache.hadoop.fs.s3a.S3AOutputStream.close(S3AOutputStream.java:142)**
26.	at org.apache.hadoop.fs.FSDataOutputStream$PositionCache.close(FSDataOutputStream.java:74)
27.	at org.apache.hadoop.fs.FSDataOutputStream.close(FSDataOutputStream.java:108)
28.	at org.apache.parquet.hadoop.ParquetFileWriter.end(ParquetFileWriter.java:467)
29.	at org.apache.parquet.hadoop.InternalParquetRecordWriter.close(InternalParquetRecordWriter.java:117)
30.	at org.apache.parquet.hadoop.ParquetRecordWriter.close(ParquetRecordWriter.java:112)
31.	at org.apache.spark.sql.execution.datasources.parquet.ParquetOutputWriter.close(ParquetOutputWriter.scala:44)
32.	at org.apache.spark.sql.execution.datasources.FileFormatWriter$SingleDirectoryWriteTask.releaseResources(FileFormatWriter.scala:252)
33.	at org.apache.spark.sql.execution.datasources.FileFormatWriter$$anonfun$org$apache$spark$sql$execution$datasources$FileFormatWriter$$executeTask$3.apply(FileFormatWriter.scala:191)
34.	at org.apache.spark.sql.execution.datasources.FileFormatWriter$$anonfun$org$apache$spark$sql$execution$datasources$FileFormatWriter$$executeTask$3.apply(FileFormatWriter.scala:188)
35.	at org.apache.spark.util.Utils$.tryWithSafeFinallyAndFailureCallbacks(Utils.scala:1341)
36.	at org.apache.spark.sql.execution.datasources.FileFormatWriter$.org$apache$spark$sql$execution$datasources$FileFormatWriter$$executeTask(FileFormatWriter.scala:193)
37.	at org.apache.spark.sql.execution.datasources.FileFormatWriter$$anonfun$write$1$$anonfun$3.apply(FileFormatWriter.scala:129)
38.	at org.apache.spark.sql.execution.datasources.FileFormatWriter$$anonfun$write$1$$anonfun$3.apply(FileFormatWriter.scala:128)
39.	at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:87)
40.	at org.apache.spark.scheduler.Task.run(Task.scala:99)
41.	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:282)
42.	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
43.	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
44.	at java.lang.Thread.run(Thread.java:748)

```

## Error: Amazon S3 service token expired

When moving data to and from Amazon Redshift, temporary Amazon S3 credentials, which expire after 1 hour, are used. If you
have a long running job, it might fail. For information about how to set up your long running jobs to move data to
and from Amazon Redshift, see [aws-glue-programming-etl-connect-redshift-home](aws-glue-programming-etl-connect-redshift-home.md "aws-glue-programming-etl-connect-redshift-home.md").

## Error: No private DNS for network interface found

If a job fails or a development endpoint fails to provision, it might be because of a problem in the network
setup.

- If you are using the Amazon provided DNS, the value of `enableDnsHostnames` must be set to
  true. For more information, see [DNS](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md") .

## Error: Development endpoint provisioning failed

If AWS Glue fails to successfully provision a development endpoint, it might be because of a
problem in the network setup.

- When you define a development endpoint, the VPC, subnet, and security groups are validated to confirm that
  they meet certain requirements.
- If you provided the optional SSH public key, check that it is a valid SSH public key.
- Check in the VPC console that your VPC uses a valid **DHCP option set**. For more
  information, see [DHCP option
  sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md").
- If the cluster remains in the PROVISIONING state, contact
  AWS Support.

## Error: Notebook server CREATE_FAILED

If AWS Glue fails to create the notebook server for a development endpoint, it might be because of
one of the following problems:

- AWS Glue passes an IAM role to Amazon EC2 when it is setting up the notebook server. The IAM
  role must have a trust relationship to Amazon EC2.
- The IAM role must have an instance profile of the same name. When you create the role for Amazon EC2 with the
  IAM console, the instance profile with the same name is automatically created. Check for an error in the log
  regarding the instance profile name `iamInstanceProfile.name` that is not valid. For more
  information, see
  [Using Instance Profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md") .
- Check that your role has permission to access `aws-glue*` buckets in the policy that you pass
  to create the notebook server.

## Error: Local notebook fails to start

If your local notebook fails to start and reports errors that a directory or folder cannot be found, it might
be because of one of the following problems:

- If you are running on Microsoft Windows, make sure that the `JAVA_HOME` environment variable
  points to the correct Java directory. It's possible to update Java without updating this variable, and if it
  points to a folder that no longer exists, Jupyter notebooks fail to start.

## Error: Running crawler failed

If AWS Glue fails to successfully run a crawler to catalog your data, it might be because of one
of the following reasons. First check if an error is listed in the AWS Glue console crawlers list.
Check if there is an exclamation icon next to the crawler name and hover over the icon to see any associated
messages.

- Check the logs for the crawler run in CloudWatch Logs under `/aws-glue/crawlers`.

## Error: Partitions were not updated

In case your partitions were not updated in the Data Catalog when you ran an ETL job, these log statements from the
`DataSink` class in the CloudWatch logs may be helpful:

- "`Attempting to fast-forward updates to the Catalog - nameSpace:`"  —  Shows
  which database, table, and catalogId are attempted to be modified by this job. If this statement is not here,
  check if `enableUpdateCatalog` is set to true and properly passed as a `getSink()`
  parameter or in `additional_options`.
- "`Schema change policy behavior:`"  —  Shows which schema `updateBehavior` value you passed in.
- "`Schemas qualify (schema compare):`"  —  Will be true or false.
- "`Schemas qualify (case-insensitive compare):`"  —  Will be true or
  false.
- If both are false and your `updateBehavior` is not set to `UPDATE_IN_DATABASE`,
  then your DynamicFrame schema needs to be identical or contain a subset of the columns seen in the Data Catalog
  table schema.

For more information on updating partitions, see [Updating the schema, and adding new partitions in the Data Catalog using
AWS Glue ETL jobs](update-from-job.md "update-from-job.md").

## Error: Job bookmark update failed due to version mismatch

You may be trying to parametize AWS Glue jobs to apply the same transformation/logic on different
datasets in Amazon S3. You want to track processed files on the locations provided. When you run the same job on the
same source bucket and write to the same/different destination concurrently (concurrency >1) the job fails with
this error:

```
py4j.protocol.Py4JJavaError: An error occurred while callingz:com.amazonaws.services.glue.util.Job.commit.:com.amazonaws.services.gluejobexecutor.model.VersionMismatchException: Continuation update failed due to version mismatch. Expected version 2 but found version 3
```

Solution: set concurrency to 1 or don't run the job concurrently.

Currently AWS Glue bookmarks don't support concurrent job runs and commits will fail.

## Error: A job is reprocessing data when job bookmarks are

enabled

There might be cases when you have enabled AWS Glue job bookmarks, but your ETL job is
reprocessing data that was already processed in an earlier run. Check for these common causes of this error:

###### Max Concurrency

Setting the maximum number of concurrent runs for the job greater than the default value of 1 can interfere with job bookmarks. This can occur when job bookmarks check the last modified time of objects to verify which objects need to be reprocessed. For more information, see the discussion
of max concurrency in [Configuring job properties for Spark jobs in AWS Glue](add-job.md "add-job.md").

###### Missing Job Object

Ensure that your job run script ends with the following commit:

```
job.commit()
```

When you include this object, AWS Glue records the timestamp and path of the job run. If you run
the job again with the same path, AWS Glue processes only the new files. If you don't include this
object and job bookmarks are enabled, the job reprocesses the already processed files along with the new files and
creates redundancy in the job's target data store.

###### Missing Transformation Context Parameter

Transformation context is an optional parameter in the `GlueContext` class, but job bookmarks
don't work if you don't include it. To resolve this error, add the transformation context parameter when you
[create the DynamicFrame](aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_catalog "aws-glue-api-crawler-pyspark-extensions-glue-context.md#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_catalog"), as shown following:

```
sample_dynF=create_dynamic_frame_from_catalog(database, table_name,transformation_ctx="sample_dynF")
```

###### Input Source

If you are using a relational database (a JDBC connection) for the input source, job bookmarks work only if
the table's primary keys are in sequential order. Job bookmarks work for new rows, but not for updated rows.
That is because job bookmarks look for the primary keys, which already exist. This does not apply if your input
source is Amazon Simple Storage Service (Amazon S3).

###### Last Modified Time

For Amazon S3 input sources, job bookmarks check the last modified time of the objects, rather than the file
names, to verify which objects need to be reprocessed. If your input source data has been modified since your
last job run, the files are reprocessed when you run the job again.

## Error: Failover behavior between VPCs in AWS Glue

The following process is used for failover for jobs in AWS Glue 5.1 and previous versions.

Summary: an AWS Glue connection is selected at the time a job run is submitted. If the job run encounters some
issues, (lack of IP addresses, connectivity to source, routing problem), the job run will fail. If retries are
configured, AWS Glue will retry with the same connection.

1.  For each run attempt, AWS Glue will check the connections health in the order listed in the job configuration, given until it finds one it can use. In the case of an Availability Zone (AZ) failure, the connections from that AZ will fail the check and will be skipped.
2.  AWS Glue validates the connection with the following:

        * checks for valid Amazon VPC id and subnet.
        * checks that a NAT gateway or Amazon VPC endpoint exists.
        * checks that the subnet has more than 0 allocated IP addresses.
        * checks that the AZ is healthy.

    AWS Glue cannot verify connectivity at the time of job run submission.

3.  For jobs using Amazon VPC, all drivers and executors will be created in the same AZ with the
    connection selected at the time of job run submission.
4.  If retries are configured, AWS Glue will retry with the same connection. This is because
    we cannot guarantee problems with this connection are long-running. If an AZ fails, existing job
    runs (depending on the stage of the job run) in that AZ can fail. A retry should detect an AZ
    failure and choose another AZ for the new run.
