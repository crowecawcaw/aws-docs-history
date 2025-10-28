# Streaming data to tables with Amazon Data Firehose

Amazon Data Firehose is a fully managed service for delivering real-time [streaming data](https://aws.amazon.com/streaming-data/ "https://aws.amazon.com/streaming-data/") to destinations such as Amazon S3, Amazon Redshift, Amazon OpenSearch Service,
Splunk, Apache Iceberg tables, and custom HTTP endpoints or HTTP endpoints
owned by supported third-party service providers. With Amazon Data Firehose, you don't need to write applications or
manage resources. You configure your data producers to send data to Firehose, and it automatically delivers
the data to the destination that you specified. You can also configure Firehose to transform your data before
delivering it. To learn more about Amazon Data Firehose, see [What is Amazon Data Firehose?](../../../firehose/latest/dev/what-is-this-service.md "../../../firehose/latest/dev/what-is-this-service.md")

Complete these steps to set up Firehose streaming to tables in S3 table buckets:

1. [Integrate your table buckets with AWS
   analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").
2. Configure Firehose to deliver data into your S3 tables. To do so, you [create an AWS Identity and Access Management (IAM)
   service role that allows Firehose to access your tables](#firehose-role-s3tables "#firehose-role-s3tables").
3. Grant the Firehose service role explicit permissions to your table or table's namespace. For more information, see [Grant Lake Formation permissions on your table resources](grant-permissions-tables.md "grant-permissions-tables.md").
4. [Create a Firehose stream that routes data to your table.](#firehose-stream-tables "#firehose-stream-tables")

## Creating a role for Firehose to use S3 tables as a

destination

Firehose needs an IAM [service role](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") with specific
permissions to access AWS Glue tables and write data to S3 tables. You need this provide this IAM role
when you create a Firehose stream.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose
   **Policies**
3. Choose **Create a policy**, and choose **JSON** in policy editor.
4. Add the following inline policy that grants permissions to all databases and tables in
   your data catalog. If you want, you can give permissions only to specific tables and databases. To
   use this policy, replace the `user input placeholders` with
   your own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "S3TableAccessViaGlueFederation",
 "Effect": "Allow",
 "Action": [
 "glue:GetTable",
 "glue:GetDatabase",
 "glue:UpdateTable"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog/s3tablescatalog/*",
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog/s3tablescatalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/*",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/*/*"
 ]
 },
 {
 "Sid": "S3DeliveryErrorBucketPermission",
 "Effect": "Allow",
 "Action": [
 "s3:AbortMultipartUpload",
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`error delivery bucket`",
 "arn:aws:s3:::`error delivery bucket`/*"
 ]
 },
 {
 "Sid": "RequiredWhenUsingKinesisDataStreamsAsSource",
 "Effect": "Allow",
 "Action": [
 "kinesis:DescribeStream",
 "kinesis:GetShardIterator",
 "kinesis:GetRecords",
 "kinesis:ListShards"
 ],
 "Resource": "arn:aws:kinesis:`us-east-1`:`111122223333`:stream/`stream-name`"
 },
 {
 "Sid": "RequiredWhenDoingMetadataReadsANDDataAndMetadataWriteViaLakeformation",
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess"
 ],
 "Resource": "*"
 },
 {
 "Sid": "RequiredWhenUsingKMSEncryptionForS3ErrorBucketDelivery",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`KMS-key-id`"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.`us-east-1`.amazonaws.com"
 },
 "StringLike": {
 "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::`error delivery bucket`/prefix*"
 }
 }
 },
 {
 "Sid": "LoggingInCloudWatch",
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:`log-group-name`:log-stream:`log-stream-name`"
 ]
 },
 {
 "Sid": "RequiredWhenAttachingLambdaToFirehose",
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction",
 "lambda:GetFunctionConfiguration"
 ],
 "Resource": [
 "arn:aws:lambda:`us-east-1`:`111122223333`:function:`function-name`:`function-version`"
 ]
 }
 ]
}`

```

This policy has a statements that allow access to Kinesis Data Streams, invoking Lambda
functions and access to AWS KMS keys. If you don't use any of these resources,
you can remove the respective statements.

If error logging is enabled, Firehose also sends data delivery errors to your
CloudWatch log group and streams. For this, you must configure log group and log stream
names. For log group and log stream names, see [Monitor
Amazon Data Firehose Using CloudWatch Logs](../../../firehose/latest/dev/controlling-access.md#using-iam-iceberg "../../../firehose/latest/dev/controlling-access.md#using-iam-iceberg"). 5. After you create the policy, create an IAM role with **AWS
service** as the **Trusted entity type**. 6. For **Service or use case**, choose
**Kinesis**. For **Use case** choose
**Kinesis Firehose**. 7. Choose **Next**, and then select the policy you created
earlier. 8. Give your role a name. Review your role details, and choose **Create
role**. The role will have the following trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Principal": {
 "Service": [
 "firehose.amazonaws.com"
 ]
 }
 }
 ]
}`

```

## Creating a Firehose stream to S3 tables

The following procedure shows how to create a Firehose stream to deliver data to S3 tables
using the console. The following prerequisites are required to set up a Firehose stream to
S3 tables.

###### Prerequisites

- [Integrate your table buckets with
  AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").
  - [Create a namespace](s3-tables-namespace-create.md "s3-tables-namespace-create.md").
  - [Create a table](s3-tables-create.md "s3-tables-create.md").

- Create the [Role for Firehose to access
  S3 Tables](#firehose-role-s3tables "#firehose-role-s3tables").
- [Grant Lake Formation permissions](grant-permissions-tables.md "grant-permissions-tables.md") to the Firehose service role you created to access tables.

To provide routing information to Firehose when you configure a stream, you use your
namespace as the database name and the name of a table in that namespace. You can use these values in the Unique key section of a Firehose
stream configuration to route data to a single table. You can also use this values to
route to a table using JSON Query expressions. For more information, see [Route incoming
records to a single Iceberg table](../../../firehose/latest/dev/apache-iceberg-format-input-record.md "../../../firehose/latest/dev/apache-iceberg-format-input-record.md").

###### To set up a Firehose stream to S3 tables (Console)

1. Open the Firehose console at
   [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/ "https://console.aws.amazon.com/firehose/").
2. Choose **Create Firehose stream**.
3. For **Source**, choose one of the following sources:
   - Amazon Kinesis Data Streams
   - Amazon MSK
   - Direct PUT

4. For **Destination**, choose **Apache Iceberg
   Tables**.
5. Enter a **Firehose stream name**.
6. Configure your **Source settings**.
7. For **Destination settings**, choose **Current account** to stream to tables in your account or **Cross-account** for tables in another account.
   - For tables in the **Current account**, select your S3 Tables catalog from the **Catalog** dropdown.
   - For tables in a **Cross-account**, enter the **Catalog ARN** of the catalog you want to stream to in another account.

8. Configure database and table names using **Unique Key configuration**,
   JSONQuery expressions, or in a Lambda function. For more information, refer to [Route
   incoming records to a single Iceberg table](../../../firehose/latest/dev/apache-iceberg-format-input-record.md "../../../firehose/latest/dev/apache-iceberg-format-input-record.md") and [Route incoming
   records to different Iceberg tables](../../../firehose/latest/dev/apache-iceberg-format-input-record-different.md "../../../firehose/latest/dev/apache-iceberg-format-input-record-different.md") in the _Amazon Data Firehose Developer
   Guide_.
9. Under **Backup settings**, specify a **S3 backup
   bucket**.
10. For **Existing IAM roles** under **Advanced
    settings**, select the IAM role you created for Firehose.
11. Choose **Create Firehose stream**.

For more information about the other settings that you can configure for a stream, see [Set up the Firehose
stream](../../../firehose/latest/dev/apache-iceberg-stream.md "../../../firehose/latest/dev/apache-iceberg-stream.md") in the _Amazon Data Firehose Developer Guide_.
