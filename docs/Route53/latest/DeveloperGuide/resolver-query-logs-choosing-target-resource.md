# AWS resources that you

can send VPC Resolver query logs to

###### Note

If you expect to log queries for workloads with high queries per second (QPS), you
should use Amazon S3 to ensure your query logs are not throttled when written to your
destination. If you use Amazon CloudWatch, you can increase your requests per second limit
for the `PutLogEvents` operation. To learn more about increasing your
CloudWatch limits, see [CloudWatch Logs
quotas](../../../AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.md "../../../AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.md") in the _Amazon CloudWatch User Guide_.

You can send VPC Resolver query logs to the following AWS resources:

**Amazon CloudWatch Logs (Amazon CloudWatch Logs) log group**

You can analyze logs with Logs Insights and create metrics and
alarms.

For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").

**Amazon S3 (S3) bucket**

An S3 bucket is economical for long-term log archiving. Latency is
typically higher.

All S3 server-side encryption options are supported. For more information,
see [Protecting
data with server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the _Amazon S3 User
Guide_.

If you choose Server-Side Encryption with AWS KMS Keys (SSE-KMS), you must
update the key policy for your customer managed key so that the log delivery
account can write to your Amazon S3 bucket. For more information about the
required key policy for use with SSE-KMS, see [Amazon S3 bucket server-side encryption](../../../AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.md#AWS-logs-SSE-KMS-S3-V2 "../../../AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.md#AWS-logs-SSE-KMS-S3-V2") in the
_Amazon CloudWatch User Guide_.

If the S3 bucket is in an account that you own, the required permissions
are automatically added to your bucket policy. If you want to send logs to
an S3 bucket in an account that you don't own, the owner of the S3 bucket
must add permissions for your account in their bucket policy. For
example:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "CrossAccountAccess",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`your_bucket_name`/AWSLogs/`your_caller_account`/*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::`your_bucket_name`"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "`iam_user_arn_or_account_number_for_root`"
 },
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::`your_bucket_name`"
 }
 ]
}`

```

###### Note

If you want to store logs in a central S3 bucket for your
organization, we recommend that you set up your query logging
configuration from a centralized account (with the necessary permissions
to write to a central bucket) and use [RAM](query-logging-configurations-managing-sharing.md "query-logging-configurations-managing-sharing.md")
to share the configuration across accounts.

For more information, see the [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md").

**Firehose delivery stream**

You can stream logs in real time to Amazon OpenSearch Service, Amazon Redshift, or other
applications.

For more information, see the [Amazon Data Firehose Developer Guide](../../../firehose/latest/dev.md "../../../firehose/latest/dev.md").

For information about the pricing for Resolver query logging, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

CloudWatch Vended Logs charges apply when using VPC Resolver logs, even when logs are published
directly to Amazon S3. For more information, see [_Logs pricing_ at Amazon
CloudWatch pricing](https://aws.amazon.com//cloudwatch/pricing/#Vended_Logs "https://aws.amazon.com//cloudwatch/pricing/#Vended_Logs").
