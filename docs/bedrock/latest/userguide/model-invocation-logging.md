# Monitor model invocation using CloudWatch Logs and Amazon S3

You can use model invocation logging to collect invocation logs,
model input data, and model output data for all invocations in your AWS account used
in Amazon Bedrock in a Region.

With invocation logging, you can collect the full request data, response data, and
metadata associated with all calls performed in your account in a Region. Logging can be configured
to provide the destination resources where the log data will be published. Supported
destinations include Amazon CloudWatch Logs and Amazon Simple Storage Service (Amazon S3). Only destinations from the same account
and Region are supported.

Model invocation logging is disabled by default. After model invocation logging is enabled, logs are stored until the logging configuration is deleted.

The following operations can log model invocations.

- [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md")
- [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md")
- [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md")
- [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")
  When [using the Converse API](conversation-inference-call.md "conversation-inference-call.md"), any image or document data that you pass is logged in Amazon S3
  (if you have [enabled](#model-invocation-logging-console "#model-invocation-logging-console") delivery and
  image logging in Amazon S3).

Before you can enable invocation logging, you need to set up an Amazon S3 or CloudWatch Logs destination.
You can enable invocation logging through either the console or the API.

###### Topics

- [Set up an Amazon S3 destination](#setup-s3-destination "#setup-s3-destination")
- [Set up an CloudWatch Logs destination](#setup-cloudwatch-logs-destination "#setup-cloudwatch-logs-destination")
- [Model invocation logging using the console](#model-invocation-logging-console "#model-invocation-logging-console")
- [Model invocation logging using the API](#using-apis-logging "#using-apis-logging")

## Set up an Amazon S3 destination

###### Note

When using Amazon S3 as a logging destination, the bucket needs to be created
in the same AWS Region as the one where you're creating the model invocation
logging configuration.

You can set up an S3 destination for logging in Amazon Bedrock with these steps:

1. Create an S3 bucket where the logs will be delivered.
2. Add a bucket policy to it like the one below (Replace values for
   `accountId`, `region`,
   `bucketName`, and optionally
   `prefix`):

###### Note

A bucket policy is automatically attached to the bucket on your behalf when you configure
logging with the permissions `S3:GetBucketPolicy` and `S3:PutBucketPolicy`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonBedrockLogsWrite",
 "Effect": "Allow",
 "Principal": {
 "Service": "bedrock.amazonaws.com"
 },
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucketName`/`prefix`/AWSLogs/`123456789012`/BedrockModelInvocationLogs/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:bedrock:`us-east-1`:`123456789012`:*"
 }
 }
 }
 ]
}`

```

3. (Optional) If configuring SSE-KMS on the bucket, add the below policy on the KMS key:

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "bedrock.amazonaws.com"
    },
    "Action": "kms:GenerateDataKey",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`accountId`"
        },
        "ArnLike": {
           "aws:SourceArn": "arn:aws:bedrock:`region`:`accountId`:*"
        }
    }
}
```

For more information on S3 SSE-KMS configurations, see [Specifying KMS Encryption](../../../AmazonS3/latest/userguide/specifying-kms-encryption.md "../../../AmazonS3/latest/userguide/specifying-kms-encryption.md").

###### Note

The bucket ACL must be disabled in order for the bucket policy to take effect.
For more information, see [Disabling ACLs for all new buckets and enforcing Object Ownership](../../../AmazonS3/latest/userguide/ensure-object-ownership.md "../../../AmazonS3/latest/userguide/ensure-object-ownership.md").

## Set up an CloudWatch Logs destination

You can set up a Amazon CloudWatch Logs destination for logging in Amazon Bedrock with the following steps:

1. Create a CloudWatch log group where the logs will be published.
2. Create an IAM role with the following permissions for CloudWatch Logs.

**Trusted entity**:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "bedrock.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:bedrock:`us-east-1`:`123456789012`:*"
 }
 }
 }
 ]
}`

```

**Role policy**:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:`us-east-1`:`123456789012`:log-group:`logGroupName`:log-stream:aws/bedrock/modelinvocations"
 }
 ]
}`

```

For more information on setting up SSE for CloudWatch Logs,
see [Encrypt log data in CloudWatch Logs using AWS Key Management Service](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md").

## Model invocation logging using the console

To enable model invocation logging, drag the slider button next to the **Logging**
toggle switch in the **Settings** page.
Additional configuration settings for logging will appear on the panel.

Choose which data requests and responses you want to publish to the logs. You can choose any
combination of the following output options:

- Text
- Image
- Embedding

Choose where to
publish the logs:

- Amazon S3 only
- CloudWatch Logs only
- Both Amazon S3 and CloudWatch Logs

Amazon S3 and CloudWatch Logs destinations are supported for invocation logs, and small
input and output data. For large input and output data or binary image outputs, only
Amazon S3 is supported. The following details summarize how the data will be represented
in the target location.

- **S3 destination** — Gzipped JSON files, each
  containing a batch of invocation log records, are delivered to the specified S3
  bucket. Similar to a CloudWatch Logs event, each record will contain
  the invocation metadata, and input and output JSON bodies of up to 100 KB in size.
  Binary data or JSON bodies
  larger than 100 KB will be uploaded as individual objects in the specified Amazon S3
  bucket under the data prefix. The data can be queried using Amazon S3 Select and Amazon Athena, and
  can be catalogued for ETL using AWS Glue. The data can be loaded into OpenSearch service,
  or be processed by any Amazon EventBridge targets.
- **CloudWatch Logs destination** — JSON invocation log
  events are delivered to a specified log group in CloudWatch Logs.
  The log event contains the invocation metadata, and input and output JSON bodies of up to 100 KB in
  size. If an Amazon S3 location for large data delivery is provided, binary data or JSON bodies larger
  than 100 KB will be uploaded to the Amazon S3 bucket under the data prefix instead.
  data can be queried using CloudWatch Logs Insights, and can be further streamed to various services in
  real-time using CloudWatch Logs.

## Model invocation logging using the API

Model invocation logging can be configured using the following APIs:

- [PutModelInvocationLoggingConfiguration](../APIReference/API_PutModelInvocationLoggingConfiguration.md "../APIReference/API_PutModelInvocationLoggingConfiguration.md")
- [GetModelInvocationLoggingConfiguration](../APIReference/API_GetModelInvocationLoggingConfiguration.md "../APIReference/API_GetModelInvocationLoggingConfiguration.md")
- [DeleteModelInvocationLoggingConfiguration](../APIReference/API_DeleteModelInvocationLoggingConfiguration.md "../APIReference/API_DeleteModelInvocationLoggingConfiguration.md")
