# Controlling access with Amazon Data Firehose

The following sections cover how to control access to and from your Amazon Data Firehose resources. The
information they cover includes how to grant your application access so it can send data to
your Firehose stream. They also describe how you can grant Amazon Data Firehose access to your
Amazon Simple Storage Service (Amazon S3) bucket, Amazon Redshift cluster, or Amazon OpenSearch Service cluster, as well as the
access permissions you need if you use Datadog, Dynatrace, LogicMonitor, MongoDB, New Relic,
Splunk, or Sumo Logic as your destination. Finally, you'll find in this topic guidance on
how to configure Amazon Data Firehose so it can deliver data to a destination that belongs to a different
AWS account. The technology for managing all these forms of access is AWS Identity and Access Management (IAM).
For more information about IAM, see [What
is IAM?](../../../IAM/latest/UserGuide/IAM_Introduction.md "../../../IAM/latest/UserGuide/IAM_Introduction.md").

###### Contents

- [Grant access to your Firehose resources](#access-to-firehose "#access-to-firehose")
- [Grant Firehose access to your private Amazon MSK cluster](#access-to-msk "#access-to-msk")
- [Allow Firehose to assume an IAM role](#firehose-assume-role "#firehose-assume-role")
- [Grant Firehose access to AWS Glue for data format
  conversion](#using-iam-glue "#using-iam-glue")
- [Grant Firehose access to an Amazon S3 destination](#using-iam-s3 "#using-iam-s3")
- [Grant Firehose access to Amazon S3 Tables](#using-s3-tables "#using-s3-tables")
- [Grant Firehose access to an Apache Iceberg Tables
  destination](#using-iam-iceberg "#using-iam-iceberg")
- [Grant Firehose access to an Amazon Redshift destination](#using-iam-rs "#using-iam-rs")
- [Grant Firehose access to a public OpenSearch Service destination](#using-iam-es "#using-iam-es")
- [Grant Firehose access to an OpenSearch Service destination in a
  VPC](#using-iam-es-vpc "#using-iam-es-vpc")
- [Grant Firehose access to a public OpenSearch
  Serverless destination](#using-iam-serverless "#using-iam-serverless")
- [Grant Firehose access to an OpenSearch
  Serverless destination in a VPC](#using-iam-serverless-vpc "#using-iam-serverless-vpc")
- [Grant Firehose access to a Splunk destination](#using-iam-splunk "#using-iam-splunk")
- [Accessing Splunk in VPC](#using-iam-splunk-vpc "#using-iam-splunk-vpc")
- [Ingest VPC flow logs into Splunk using Amazon Data Firehose](#vpc-splunk-tutorial "#vpc-splunk-tutorial")
- [Accessing Snowflake or HTTP end
  point](#using-snowflake-http-endpoint "#using-snowflake-http-endpoint")
- [Grant Firehose access to a Snowflake
  destination](#using-iam-snowflake "#using-iam-snowflake")
- [Accessing Snowflake in VPC](#using-iam-snowflake-vpc "#using-iam-snowflake-vpc")
- [Grant Firehose access to an HTTP endpoint
  destination](#using-iam-http "#using-iam-http")
- [Cross-account delivery from Amazon MSK](#cross-account-delivery-msk "#cross-account-delivery-msk")
- [Cross-account delivery to an Amazon S3
  destination](#cross-account-delivery-s3 "#cross-account-delivery-s3")
- [Cross-account delivery to an OpenSearch Service
  destination](#cross-account-delivery-es "#cross-account-delivery-es")
- [Using tags to control access](#tag-based-access-control "#tag-based-access-control")

## Grant access to your Firehose resources

To give your application access to your Firehose stream, use a policy similar to
this example. You can adjust the individual API operations to which you grant access by
modifying the `Action` section, or grant access to all operations with
`"firehose:*"`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "firehose:DeleteDeliveryStream",
 "firehose:PutRecord",
 "firehose:PutRecordBatch",
 "firehose:UpdateDestination"
 ],
 "Resource": [
 "`arn:aws:`firehose:`us-east-1`:`123456789012`:deliverystream/`delivery-stream-name`"
 ]
 }
 ]
}`

```

## Grant Firehose access to your private Amazon MSK cluster

If the source of your Firehose stream is a private Amazon MSK cluster, then use a policy similar
to this example.

You must add a policy like this to the cluster's resource-based policy to grant Firehose
service principal the permission to invoke the Amazon MSK `CreateVpcConnection`
API operation.

## Allow Firehose to assume an IAM role

This section describes the permissions and policies that grant Amazon Data Firehose
access to ingest, process, and deliver data from source to destination.

###### Note

If you use the console to create a Firehose stream and choose the option to create
a new role, AWS attaches the required trust policy to the role. If you want Amazon Data Firehose
to use an existing IAM role or if you create a role on your own, attach the
following trust policies to that role so that Amazon Data Firehose can assume it. Edit the policies
to replace `account-id` with your AWS account ID. For
information about how to modify the trust relationship of a role, see [Modifying a Role](../../../IAM/latest/UserGuide/id_roles_manage_modify.md "../../../IAM/latest/UserGuide/id_roles_manage_modify.md").

Amazon Data Firehose uses an IAM role for all the permissions that the Firehose stream needs to
process and deliver data. Make sure that the following trust policies are attached to
that role so that Amazon Data Firehose can assume it.

If you choose Amazon MSK as the source for your Firehose stream, you must specify
another IAM role that grants Amazon Data Firehose permissions to ingest source data
from the specified Amazon MSK cluster. Make sure that the following trust policies
are attached to that role so that Amazon Data Firehose can assume it.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Principal": {
 "Service": [
 "firehose.amazonaws.com"
 ]
 },
 "Effect": "Allow",
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Make sure that this role that grants Amazon Data Firehose permissions to ingest source data
from the specified Amazon MSK cluster grants the following permissions:

## Grant Firehose access to AWS Glue for data format

conversion

If your Firehose stream performs data-format conversion, Amazon Data Firehose references table
definitions stored in AWS Glue. To give Amazon Data Firehose the necessary access to AWS Glue, add the
following statement to your policy. For information on how to find the ARN of the table,
see [Specifying AWS Glue Resource ARNs](../../../glue/latest/dg/glue-specifying-resource-arns.md "../../../glue/latest/dg/glue-specifying-resource-arns.md").

```
{
    "Sid": "",
    "Effect": "Allow",
    "Action": [
        "glue:GetTable",
        "glue:GetTableVersion",
        "glue:GetTableVersions"
    ],
    "Resource": [
        "arn:aws:glue:us-east-1:123456789012:catalog",
        "arn:aws:glue:us-east-1:123456789012:database/b",
        "arn:aws:glue:us-east-1:123456789012:table/b/easd"
    ]
},
{
      actions: ['glue:GetSchemaVersion'],
      grantee: options.role,
      resourceArns: ['*'],
}
```

The recommended policy for getting schemas from schema registry has no resource restrictions. For more information, see [IAM examples for deserializers](../../../glue/latest/dg/schema-registry-gs.md#schema-registry-gs1b "../../../glue/latest/dg/schema-registry-gs.md#schema-registry-gs1b") in the AWS Glue Developer Guide.

## Grant Firehose access to an Amazon S3 destination

When you're using an Amazon S3 destination, Amazon Data Firehose delivers data to your S3 bucket and can
optionally use an AWS KMS key that you own for data encryption. If error logging is
enabled, Amazon Data Firehose also sends data delivery errors to your CloudWatch log group and streams. You
are required to have an IAM role when creating a Firehose stream. Amazon Data Firehose assumes that
IAM role and gains access to the specified bucket, key, and CloudWatch log group and
streams.

Use the following access policy to enable Amazon Data Firehose to access your S3 bucket and AWS KMS
key. If you don't own the S3 bucket, add `s3:PutObjectAcl` to the list of
Amazon S3 actions. This grants the bucket owner full access to the objects delivered by
Amazon Data Firehose.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
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
 "`arn:aws:`s3:::`amzn-s3-demo-bucket`",
 "`arn:aws:`s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesis:DescribeStream",
 "kinesis:GetShardIterator",
 "kinesis:GetRecords",
 "kinesis:ListShards"
 ],
 "Resource": "`arn:aws:`kinesis:`us-east-1`:`123456789012`:stream/`stream-name`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "`arn:aws:`kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.`us-east-1`.amazonaws.com"
 },
 "StringLike": {
 "kms:EncryptionContext:aws:s3:arn": "`arn:aws:`s3:::`amzn-s3-demo-bucket/prefix`*"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents"
 ],
 "Resource": [
 "`arn:aws:`logs:`us-east-1`:`123456789012`:log-group:`log-group-name`:log-stream:`log-stream-name`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction",
 "lambda:GetFunctionConfiguration"
 ],
 "Resource": [
 "`arn:aws:`lambda:`us-east-1`:`123456789012`:function:`function-name`:`function-version`"
 ]
 }
 ]
}`

```

The policy above also has a statement that allows access to Amazon Kinesis Data Streams. If you don't
use Kinesis Data Streams as your data source, you can remove that statement. If you use Amazon MSK as
your source, then you can substitute that statement with the following:

```
{
   "Sid":"",
   "Effect":"Allow",
   "Action":[
      "kafka:GetBootstrapBrokers",
      "kafka:DescribeCluster",
      "kafka:DescribeClusterV2",
      "kafka-cluster:Connect"
   ],
   "Resource":"`arn:aws:`kafka:{{mskClusterRegion}}:{{mskClusterAccount}}:cluster/{{mskClusterName}}/{{clusterUUID}}"
},
{
   "Sid":"",
   "Effect":"Allow",
   "Action":[
      "kafka-cluster:DescribeTopic",
      "kafka-cluster:DescribeTopicDynamicConfiguration",
      "kafka-cluster:ReadData"
   ],
   "Resource":"`arn:aws:`kafka:{{mskClusterRegion}}:{{mskClusterAccount}}:topic/{{mskClusterName}}/{{clusterUUID}}/{{mskTopicName}}"
},
{
   "Sid":"",
   "Effect":"Allow",
   "Action":[
      "kafka-cluster:DescribeGroup"
   ],
   "Resource":"`arn:aws:`kafka:{{mskClusterRegion}}:{{mskClusterAccount}}:group/{{mskClusterName}}/{{clusterUUID}}/*"
}
```

For more information about allowing other AWS services to access your AWS
resources, see [Creating a
Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

To learn how to grant Amazon Data Firehose access to an Amazon S3 destination in another account, see
[Cross-account delivery to an Amazon S3
destination](#cross-account-delivery-s3 "#cross-account-delivery-s3").

## Grant Firehose access to Amazon S3 Tables

You must have an IAM role before you create a Firehose stream. Use the following steps
to create a policy and an IAM role. Firehose assumes this IAM role and performs the
required actions.

Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

Create a policy and choose **JSON** in the policy editor. Add the
following inline policy that grants Amazon S3 permissions such as read/write permissions,
permissions to update the table in the data catalog, and others.

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
 "`arn:aws:`glue:`us-east-1`:`123456789012`:catalog/s3tablescatalog/*",
 "`arn:aws:`glue:`us-east-1`:`123456789012`:catalog/s3tablescatalog",
 "`arn:aws:`glue:`us-east-1`:`123456789012`:catalog",
 "`arn:aws:`glue:`us-east-1`:`123456789012`:database/*",
 "`arn:aws:`glue:`us-east-1`:`123456789012`:table/*/*"
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
 "`arn:aws:`s3:::<error delivery bucket>",
 "`arn:aws:`s3:::<error delivery bucket>/*"
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
 "Resource": "`arn:aws:`kinesis:`us-east-1`:`123456789012`:stream/<stream-name>"
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
 "`arn:aws:`kms:`us-east-1`:`123456789012`:key/<KMS-key-id>"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.`us-east-1`.amazonaws.com"
 },
 "StringLike": {
 "kms:EncryptionContext:aws:s3:arn": "`arn:aws:`s3:::<error delivery bucket>/prefix*"
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
 "`arn:aws:`logs:`us-east-1`:`123456789012`:log-group:log-group-name>:log-stream:<log-stream-name>"
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
 "`arn:aws:`lambda:`us-east-1`:`123456789012`:function:<function-name>:<function-version>"
 ]
 }
 ]
}`

```

The policy has statements that allows access to Amazon Kinesis Data Streams, invoking Lambda functions,
and access to AWS KMS keys. If you don't use any of these resources, you can remove the
respective statements. If error logging is enabled, Amazon Data Firehose also sends data delivery
errors to your CloudWatch log group and streams. You must configure log group and log stream
names to use this option. For log group and log stream names, see [Monitor Amazon Data Firehose Using
CloudWatch Logs](monitoring-with-cloudwatch-logs.md "monitoring-with-cloudwatch-logs.md").

In the inline policies, replace `<error delivery bucket>` with your Amazon S3
bucket name, `aws-account-id` and Region with a valid AWS account number
and Region of the resource.

After you create the policy, open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") and create
an IAM role with **AWS service** as the **Trusted entity
type**.

For **Service or use case**, choose **Kinesis**. For
**Use case** , choose **Kinesis Firehose**.

On the next page, choose the policy created in the previous step to attach to this
role. On the review page, you will find trust policy already attached to this role
giving permissions to the Firehose service to assume this role. When you create the role,
Amazon Data Firehose can assume it to perform required operations on AWS Glue and S3 buckets. Add the
Firehose service principal to the trust policy of the role that is created. For more
information, see [Allow Firehose to assume an IAM role](#firehose-assume-role "#firehose-assume-role").

## Grant Firehose access to an Apache Iceberg Tables

destination

You must have an IAM role before you create a Firehose stream and Apache Iceberg Tables
using AWS Glue. Use the following steps to create a policy and an IAM role. Firehose assumes
this IAM role and performs the required actions.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Create a policy and choose **JSON** in policy editor.
3. Add the following inline policy that grants Amazon S3 permissions like the
   read/write permissions, permissions to update the table in the data catalog etc.

This policy has a statement that allows access to Amazon Kinesis Data Streams, invoking Lambda
functions, and access to KMS keys. If you don't use any of these resources,
you can remove the respective statements.

If error logging is enabled, Firehose also sends data delivery errors to your
CloudWatch log group and streams. For this you must configure log group and log stream
names. For log group and log stream names, see [Monitor Amazon Data Firehose Using
CloudWatch Logs](monitoring-with-cloudwatch-logs.md "monitoring-with-cloudwatch-logs.md"). 4. In the inline policies, replace `amzn-s3-demo-bucket`
with your Amazon S3 bucket name, aws-account-id and Region with a valid AWS account
number and Region of the resources.

###### Note

This role gives permission to all databases and tables in your data
catalog. If you want, you can give permissions only to specific tables and
databases. 5. After you create the policy, open the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") and create an
IAM role with **AWS service** as the **Trusted entity
type**. 6. For **Service or use case**, choose
**Kinesis**. For **Use case** choose
**Kinesis Firehose**. 7. On the next page, choose the policy created in the previous step to attach to
this role. On the review page, you will find trust policy already attached to
this role giving permissions to Firehose service to assume this role. When you
create the role, Amazon Data Firehose can assume it to perform required operations on AWS Glue
and S3 buckets.

## Grant Firehose access to an Amazon Redshift destination

Refer to the following when you are granting access to Amazon Data Firehose when using an Amazon Redshift
destination.

###### Topics

- [IAM role and access policy](#using-iam-rs-policy "#using-iam-rs-policy")
- [VPC access to an Amazon Redshift provisioned cluster or
  Amazon Redshift Serverless workgroup](#using-iam-rs-vpc "#using-iam-rs-vpc")

### IAM role and access policy

When you're using an Amazon Redshift destination, Amazon Data Firehose delivers data to your S3 bucket
as an intermediate location. It can optionally use an AWS KMS key you own for data
encryption. Amazon Data Firehose then loads the data from the S3 bucket to your Amazon Redshift
provisioned cluster or Amazon Redshift Serverless workgroup. If error logging is enabled, Amazon Data Firehose
also sends data delivery errors to your CloudWatch log group and streams. Amazon Data Firehose uses the
specified Amazon Redshift user name and password to access your provisioned cluster or Amazon Redshift
Serverless workgroup, and uses an IAM role to access the specified bucket, key,
CloudWatch log group, and streams. You are required to have an IAM role when creating a
Firehose stream.

Use the following access policy to enable Amazon Data Firehose to access your S3 bucket and AWS KMS
key. If you don't own the S3 bucket, add `s3:PutObjectAcl` to the list of
Amazon S3 actions, which grants the bucket owner full access to the objects delivered by
Amazon Data Firehose. This policy also has a statement that allows access to Amazon Kinesis Data Streams. If you
don't use Kinesis Data Streams as your data source, you can remove that statement.

JSON

```
`{
"Version":"2012-10-17",
 "Statement":
 [
 {
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
 "`arn:aws:`s3:::`amzn-s3-demo-bucket`",
 "`arn:aws:`s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "`arn:aws:`kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.`us-east-1`.amazonaws.com"
 },
 "StringLike": {
 "kms:EncryptionContext:aws:s3:arn": "`arn:aws:`s3:::`amzn-s3-demo-bucket/prefix`*"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesis:DescribeStream",
 "kinesis:GetShardIterator",
 "kinesis:GetRecords",
 "kinesis:ListShards"
 ],
 "Resource": "`arn:aws:`kinesis:`us-east-1`:`123456789012`:stream/`stream-name`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents"
 ],
 "Resource": [
 "`arn:aws:`logs:`us-east-1`:`123456789012`:log-group:`log-group-name`:log-stream:`log-stream-name`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction",
 "lambda:GetFunctionConfiguration"
 ],
 "Resource": [
 "`arn:aws:`lambda:`us-east-1`:`123456789012`:function:`function-name`:`function-version`"
 ]
 }
 ]
}`

```

For more information about allowing other AWS services to access your AWS
resources, see [Creating
a Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

### VPC access to an Amazon Redshift provisioned cluster or

Amazon Redshift Serverless workgroup

If your Amazon Redshift provisioned cluster or Amazon Redshift Serverless workgroup is in a virtual private
cloud (VPC), it must be publicly accessible with a public IP address. Also, grant
Amazon Data Firehose access to your Amazon Redshift provisioned cluster or Amazon Redshift Serverless workgroup by
unblocking the Amazon Data Firehose IP addresses. Amazon Data Firehose currently uses one CIDR block for
each available Region.

| Region                    | CIDR blocks         |
| ------------------------- | ------------------- |
| US East (Ohio)            | `13.58.135.96/27`   |
| US East (N. Virginia)     | `52.70.63.192/27`   |
| US West (N. California)   | `13.57.135.192/27`  |
| US West (Oregon)          | `52.89.255.224/27`  |
| AWS GovCloud (US-East)    | `18.253.138.96/27`  |
| AWS GovCloud (US-West)    | `52.61.204.160/27`  |
| Canada (Central)          | `35.183.92.128/27`  |
| Canada West (Calgary)     | `40.176.98.192/27`  |
| Asia Pacific (Hong Kong)  | `18.162.221.32/27`  |
| Asia Pacific (Mumbai)     | `13.232.67.32/27`   |
| Asia Pacific (Hyderabad)  | `18.60.192.128/27`  |
| Asia Pacific (Seoul)      | `13.209.1.64/27`    |
| Asia Pacific (Singapore)  | `13.228.64.192/27`  |
| Asia Pacific (Sydney)     | `13.210.67.224/27`  |
| Asia Pacific (Jakarta)    | `108.136.221.64/27` |
| Asia Pacific (Tokyo)      | `13.113.196.224/27` |
| Asia Pacific (Osaka)      | `13.208.177.192/27` |
| Asia Pacific (Thailand)   | `43.208.112.96/27`  |
| Asia Pacific (Taipei)     | `43.212.53.160/27`  |
| China (Beijing)           | `52.81.151.32/27`   |
| China (Ningxia)           | `161.189.23.64/27`  |
| Europe (Zurich)           | `16.62.183.32/27`   |
| Europe (Frankfurt)        | `35.158.127.160/27` |
| Europe (Ireland)          | `52.19.239.192/27`  |
| Europe (London)           | `18.130.1.96/27`    |
| Europe (Paris)            | `35.180.1.96/27`    |
| Europe (Stockholm)        | `13.53.63.224/27`   |
| Europe (Spain)            | `18.100.71.96/27`   |
| Middle East (Bahrain)     | `15.185.91.0/27`    |
| Mexico (Central)          | `78.12.207.32/27`   |
| South America (São Paulo) | `18.228.1.128/27`   |
| Europe (Milan)            | `15.161.135.128/27` |
| Africa (Cape Town)        | `13.244.121.224/27` |
| Middle East (UAE)         | `3.28.159.32/27`    |
| Israel (Tel Aviv)         | `51.16.102.0/27`    |
| Asia Pacific (Melbourne)  | `16.50.161.128/27`  |
| Asia Pacific (Malaysia)   | `43.216.58.0/27`    |

For more information about how to unblock IP addresses, see the step [Authorize Access to the
Cluster](../../../redshift/latest/gsg/rs-gsg-authorize-cluster-access.md "../../../redshift/latest/gsg/rs-gsg-authorize-cluster-access.md") in the _Amazon Redshift Getting Started Guide_ guide.

## Grant Firehose access to a public OpenSearch Service destination

When you're using an OpenSearch Service destination, Amazon Data Firehose delivers data to your
OpenSearch Service cluster, and concurrently backs up failed or all documents to your S3
bucket. If error logging is enabled, Amazon Data Firehose also sends data delivery errors to your CloudWatch
log group and streams. Amazon Data Firehose uses an IAM role to access the specified OpenSearch
Service domain, S3 bucket, AWS KMS key, and CloudWatch log group and streams. You are required
to have an IAM role when creating a Firehose stream.

Use the following access policy to enable Amazon Data Firehose to access your S3 bucket, OpenSearch
Service domain, and AWS KMS key. If you do not own the S3 bucket, add
`s3:PutObjectAcl` to the list of Amazon S3 actions, which grants the bucket
owner full access to the objects delivered by Amazon Data Firehose. This policy also has a statement
that allows access to Amazon Kinesis Data Streams. If you don't use Kinesis Data Streams as your data source, you can
remove that statement.

For more information about allowing other AWS services to access your AWS
resources, see [Creating a
Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

To learn how to grant Amazon Data Firehose access to an OpenSearch Service cluster in another
account, see [Cross-account delivery to an OpenSearch Service
destination](#cross-account-delivery-es "#cross-account-delivery-es").

## Grant Firehose access to an OpenSearch Service destination in a

VPC

If your OpenSearch Service domain is in a VPC, make sure you give Amazon Data Firehose the
permissions that are described in the previous section. In addition, you need to give
Amazon Data Firehose the following permissions to enable it to access your OpenSearch Service domain's
VPC.

- `ec2:DescribeVpcs`
- `ec2:DescribeVpcAttribute`
- `ec2:DescribeSubnets`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeNetworkInterfaces`
- `ec2:CreateNetworkInterface`
- `ec2:CreateNetworkInterfacePermission`
- `ec2:DeleteNetworkInterface`

###### Important

Do not revoke these permissions after you create the Firehose stream. If you revoke these
permissions, your Firehose stream will be degraded or stop delivering data to your
OpenSearch service domain whenever the service attempts to query or update
ENIs.

###### Important

When you specify subnets for delivering data to the destination in a private VPC, make sure you have enough number
of free IP addresses in chosen subnets. If there is no available free IP address in a specified subnet, Firehose cannot create or
add ENIs for the data delivery in the private VPC, and the delivery will be degraded or fail.

When you create or update your Firehose stream, you specify a security group for Firehose to
use when it sends data to your OpenSearch Service domain. You can use the same security
group that the OpenSearch Service domain uses or a different one. If you specify a
different security group, ensure that it allows outbound HTTPS traffic to the OpenSearch
Service domain's security group. Also ensure that the OpenSearch Service domain's
security group allows HTTPS traffic from the security group you specified when you
configured your Firehose stream. If you use the same security group for both your Firehose stream
and the OpenSearch Service domain, make sure the security group inbound rule allows
HTTPS traffic. For more information about security group rules, see [Security group rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules") in the Amazon VPC documentation.

## Grant Firehose access to a public OpenSearch

Serverless destination

When you're using an OpenSearch Serverless destination, Amazon Data Firehose delivers data to your
OpenSearch Serverless collection, and concurrently backs up failed or all documents to
your S3 bucket. If error logging is enabled, Amazon Data Firehose also sends data delivery errors to
your CloudWatch log group and streams. Amazon Data Firehose uses an IAM role to access the specified
OpenSearch Serverless collection, S3 bucket, AWS KMS key, and CloudWatch log group and streams.
You are required to have an IAM role when creating a Firehose stream.

Use the following access policy to enable Amazon Data Firehose to access your S3 bucket, OpenSearch
Serverless domain, and AWS KMS key. If you do not own the S3 bucket, add
`s3:PutObjectAcl` to the list of Amazon S3 actions, which grants the bucket
owner full access to the objects delivered by Amazon Data Firehose. This policy also has a statement
that allows access to Amazon Kinesis Data Streams. If you don't use Kinesis Data Streams as your data source, you can
remove that statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
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
 "`arn:aws:`s3:::`amzn-s3-demo-bucket`",
 "`arn:aws:`s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "`arn:aws:`kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.`us-east-1`.amazonaws.com"
 },
 "StringLike": {
 "kms:EncryptionContext:aws:s3:arn": "`arn:aws:`s3:::`amzn-s3-demo-bucket/prefix`*"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesis:DescribeStream",
 "kinesis:GetShardIterator",
 "kinesis:GetRecords",
 "kinesis:ListShards"
 ],
 "Resource": "`arn:aws:`kinesis:`us-east-1`:`123456789012`:stream/`stream-name`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents"
 ],
 "Resource": [
 "`arn:aws:`logs:`us-east-1`:`123456789012`:log-group:`log-group-name`:log-stream:`log-stream-name`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction",
 "lambda:GetFunctionConfiguration"
 ],
 "Resource": [
 "`arn:aws:`lambda:`us-east-1`:`123456789012`:function:`function-name`:`function-version`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "aoss:APIAccessAll",
 "Resource": "`arn:aws:`aoss:`us-east-1`:`123456789012`:collection/`collection-id`"
 }
 ]
}`

```

In addition to the policy above, you must also configure Amazon Data Firehose to have
the following minimum permissions assigned in a data access policy:

```

[
   {
      "Rules":[
         {
            "ResourceType":"index",
            "Resource":[
               "index/target-collection/target-index"
            ],
            "Permission":[
               "aoss:WriteDocument",
               "aoss:UpdateIndex",
               "aoss:CreateIndex"
            ]
         }
      ],
      "Principal":[
         "`arn:aws:`sts::`123456789012`:assumed-role/`firehose-delivery-role-name`/*"
      ]
   }
]
```

For more information about allowing other AWS services to access your AWS
resources, see [Creating a
Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

## Grant Firehose access to an OpenSearch

Serverless destination in a VPC

If your OpenSearch Serverless collection is in a VPC, make sure you give Amazon Data Firehose the
permissions that are described in the previous section. In addition, you need to give
Amazon Data Firehose the following permissions to enable it to access your OpenSearch Serverless
collection's VPC.

- `ec2:DescribeVpcs`
- `ec2:DescribeVpcAttribute`
- `ec2:DescribeSubnets`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeNetworkInterfaces`
- `ec2:CreateNetworkInterface`
- `ec2:CreateNetworkInterfacePermission`
- `ec2:DeleteNetworkInterface`

###### Important

Do not revoke these permissions after you create the Firehose stream. If you revoke these
permissions, your Firehose stream will be degraded or stop delivering data to your
OpenSearch service domain whenever the service attempts to query or update
ENIs.

###### Important

When you specify subnets for delivering data to the destination in a private VPC, make sure you have enough number
of free IP addresses in chosen subnets. If there is no available free IP address in a specified subnet, Firehose cannot create or
add ENIs for the data delivery in the private VPC, and the delivery will be degraded or fail.

When you create or update your Firehose stream, you specify a security group for Firehose to
use when it sends data to your OpenSearch Serverless collection. You can use the same
security group that the OpenSearch Serverless collection uses or a different one. If you
specify a different security group, ensure that it allows outbound HTTPS traffic to the
OpenSearch Serverless collection's security group. Also ensure that the OpenSearch
Serverless collection's security group allows HTTPS traffic from the security group you
specified when you configured your Firehose stream. If you use the same security group for
both your Firehose stream and the OpenSearch Serverless collection, make sure the security
group inbound rule allows HTTPS traffic. For more information about security group
rules, see [Security group rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules") in the Amazon VPC documentation.

## Grant Firehose access to a Splunk destination

When you're using a Splunk destination, Amazon Data Firehose delivers data to your Splunk HTTP Event
Collector (HEC) endpoint. It also backs up that data to the Amazon S3 bucket that you
specify, and you can optionally use an AWS KMS key that you own for Amazon S3 server-side

encryption. If error logging is enabled, Firehose sends data delivery errors to your CloudWatch
log streams. You can also use AWS Lambda for data transformation.

If you use an AWS load balancer, make sure that it is a Classic Load Balancer or an Application Load Balancer. Also, enable duration-based sticky sessions with
cookie expiration disabled for Classic Load Balancer and expiration is set to the maximum (7 days) for Application Load Balancer. For information about how to do this, see Duration-Based Session Stickiness
for [Classic Load Balancer](../../../elasticloadbalancing/latest/classic/elb-sticky-sessions.md#enable-sticky-sessions-duration "../../../elasticloadbalancing/latest/classic/elb-sticky-sessions.md#enable-sticky-sessions-duration") or
an [Application Load Balancer](../../../elasticloadbalancing/latest/application/sticky-sessions.md "../../../elasticloadbalancing/latest/application/sticky-sessions.md").

You must have an IAM role when you create a Firehose stream. Firehose assumes that IAM
role and gains access to the specified bucket, key, and CloudWatch log group and
streams.

Use the following access policy to enable Amazon Data Firehose to access your S3 bucket. If you don't
own the S3 bucket, add `s3:PutObjectAcl` to the list of Amazon S3 actions, which
grants the bucket owner full access to the objects delivered by Amazon Data Firehose. This policy also
grants Amazon Data Firehose access to CloudWatch for error logging and to AWS Lambda for data transformation.
The policy also has a statement that allows access to Amazon Kinesis Data Streams. If you don't use Kinesis Data Streams
as your data source, you can remove that statement. Amazon Data Firehose doesn't use IAM to access
Splunk. For accessing Splunk, it uses your HEC token.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
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
 "`arn:aws:`s3:::`amzn-s3-demo-bucket`",
 "`arn:aws:`s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "`arn:aws:`kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.`us-east-1`.amazonaws.com"
 },
 "StringLike": {
 "kms:EncryptionContext:aws:s3:arn": "`arn:aws:`s3:::`amzn-s3-demo-bucket/prefix`*"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesis:DescribeStream",
 "kinesis:GetShardIterator",
 "kinesis:GetRecords",
 "kinesis:ListShards"
 ],
 "Resource": "`arn:aws:`kinesis:`us-east-1`:`123456789012`:stream/`stream-name`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents"
 ],
 "Resource": [
 "`arn:aws:`logs:`us-east-1`:`123456789012`:log-group:`log-group-name`:log-stream:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction",
 "lambda:GetFunctionConfiguration"
 ],
 "Resource": [
 "`arn:aws:`lambda:`us-east-1`:`123456789012`:function:`function-name`:`function-version`"
 ]
 }
 ]
}`

```

For more information about allowing other AWS services to access your AWS
resources, see [Creating a
Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

## Accessing Splunk in VPC

If your Splunk platform is in a VPC, it must be publicly accessible with a public IP
address. Also, grant Amazon Data Firehose access to your Splunk platform by unblocking the Amazon Data Firehose IP
addresses. Amazon Data Firehose currently uses the following CIDR blocks.

| Region                    | CIDR blocks                                                 |
| ------------------------- | ----------------------------------------------------------- |
| US East (Ohio)            | `18.216.68.160/27, 18.216.170.64/27,<br>18.216.170.96/27`\  |
| US East (N. Virginia)     | `34.238.188.128/26, 34.238.188.192/26,<br>34.238.195.0/26`  |
| US West (N. California)   | `13.57.180.0/26`                                            |
| US West (Oregon)          | `34.216.24.32/27, 34.216.24.192/27,<br>34.216.24.224/27`    |
| AWS GovCloud (US-East)    | `18.253.138.192/26`                                         |
| AWS GovCloud (US-West)    | `52.61.204.192/26`                                          |
| Asia Pacific (Hong Kong)  | `18.162.221.64/26`                                          |
| Asia Pacific (Mumbai)     | `13.232.67.64/26`                                           |
| Asia Pacific (Seoul)      | `13.209.71.0/26`                                            |
| Asia Pacific (Singapore)  | `13.229.187.128/26`                                         |
| Asia Pacific (Sydney)     | `13.211.12.0/26`                                            |
| Asia Pacific (Thailand)   | `43.208.112.128/26`                                         |
| Asia Pacific (Tokyo)      | `13.230.21.0/27, 13.230.21.32/27`                           |
| Canada (Central)          | `35.183.92.64/26`                                           |
| Canada West (Calgary)     | `40.176.98.128/26`                                          |
| Europe (Frankfurt)        | `18.194.95.192/27, 18.194.95.224/27,<br>18.195.48.0/27`     |
| Europe (Ireland)          | `34.241.197.32/27, 34.241.197.64/27,<br>34.241.197.96/27`   |
| Europe (London)           | `18.130.91.0/26`                                            |
| Europe (Paris)            | `35.180.112.0/26`                                           |
| Europe (Spain)            | `18.100.194.0/26`                                           |
| Europe (Stockholm)        | `13.53.191.0/26`                                            |
| Middle East (Bahrain)     | `15.185.91.64/26`                                           |
| Mexico (Central)          | `78.12.207.64/26`                                           |
| South America (São Paulo) | `18.228.1.192/26`                                           |
| Europe (Milan)            | `15.161.135.192/26`                                         |
| Africa (Cape Town)        | `13.244.165.128/26`                                         |
| Asia Pacific (Osaka)      | `13.208.217.0/26`                                           |
| China (Beijing)           | `52.81.151.64/26`                                           |
| China (Ningxia)           | `161.189.23.128/26`                                         |
| Asia Pacific (Jakarta)    | `108.136.221.128/26`                                        |
| Middle East (UAE)         | `3.28.159.64/26`                                            |
| Israel (Tel Aviv)         | `51.16.102.64/26`                                           |
| Europe (Zurich)           | `16.62.183.64/26`                                           |
| Asia Pacific (Hyderabad)  | `18.60.192.192/26`                                          |
| Asia Pacific (Melbourne)  | `16.50.161.192/26`                                          |
| Asia Pacific (Malaysia)   | `43.216.44.192/26`                                          |

## Ingest VPC flow logs into Splunk using Amazon Data Firehose

To learn more about how to create a VPC flow log subscription, publish to Firehose, and send
the VPC flow logs to a supported destination see [Ingest VPC flow logs into Splunk using Amazon Data Firehose](https://www.splunk.com/en_us/blog/partners/streamline-your-amazon-vpc-flow-logs-ingestion-to-splunk.html "https://www.splunk.com/en_us/blog/partners/streamline-your-amazon-vpc-flow-logs-ingestion-to-splunk.html").

## Accessing Snowflake or HTTP end

point

There is no subset of [AWS IP address ranges](../../../vpc/latest/userguide/aws-ip-ranges.md "../../../vpc/latest/userguide/aws-ip-ranges.md")
specific to Amazon Data Firehose when the destination is HTTP end point or Snowflake public
clusters.

To add Firehose to an allow list for public Snowflake clusters or to your public HTTP or
HTTPS endpoints, add all the current [AWS IP address ranges](../../../vpc/latest/userguide/aws-ip-ranges.md "../../../vpc/latest/userguide/aws-ip-ranges.md") to
your ingress rules.

###### Note

Notifications aren't always sourced from IP addresses in the same AWS Region as
their associated topic. You must include the AWS IP address range for all
Regions.

## Grant Firehose access to a Snowflake

destination

When you're using Snowflake as a destination, Firehose delivers data to a Snowflake account using your Snowflake account URL. It also backs up
error data to the Amazon Simple Storage Service bucket that you specify, and you can optionally use an AWS Key Management Service key that you own for Amazon S3 server-side encryption.
If error logging is enabled, Firehose sends data delivery errors to your CloudWatch Logs streams.

You must have an IAM role before you create a Firehose stream. Firehose assumes that IAM role
and gains access to the specified bucket, key, and CloudWatch Logs group and streams. Use the
following access policy to enable Firehose to access your S3 bucket. If you don't own the
S3 bucket, add `s3:PutObjectAcl` to the list of Amazon Simple Storage Service actions, which
grants the bucket owner full access to the objects delivered by Firehose. This policy also
grants Firehose access to CloudWatch for error logging. The policy also has a statement that
allows access to Amazon Kinesis Data Streams. If you don't use Kinesis Data Streams as your data source, you can remove
that statement. Firehose doesn't use IAM to access Snowflake. For accessing Snowflake, it
uses your Snowflake account Url and PrivateLink Vpce Id in the case of a private
cluster.

JSON

```
`{
"Version":"2012-10-17",
 "Statement":
 [
 {
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
 "`arn:aws:`s3:::`amzn-s3-demo-bucket`",
 "`arn:aws:`s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
"Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "`arn:aws:`kms:`us-east-1`:`123456789012`:key/key-id"
 ],
 "Condition": {
"StringEquals": {
"kms:ViaService": "s3.`us-east-1`.amazonaws.com"
 },
 "StringLike": {
"kms:EncryptionContext:aws:s3:arn": "`arn:aws:`s3:::`amzn-s3-demo-bucket`/prefix*"
 }
 }
 },
 {
"Effect": "Allow",
 "Action": [
 "kinesis:DescribeStream",
 "kinesis:GetShardIterator",
 "kinesis:GetRecords",
 "kinesis:ListShards"
 ],
 "Resource": "`arn:aws:`kinesis:`us-east-1`:`123456789012`:stream/stream-name"
 },
 {
"Effect": "Allow",
 "Action": [
 "logs:PutLogEvents"
 ],
 "Resource": [
 "`arn:aws:`logs:`us-east-1`:`123456789012`:log-group:log-group-name:log-stream:*"
 ]
 }
 ]
}`

```

For more information about allowing other AWS services to access your AWS resources, see [Creating a Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md")
in the _IAM User Guide_.

## Accessing Snowflake in VPC

If your Snowflake cluster is private link enabled, Firehose will use one of the following
VPC endpoints at time of private link creation to deliver data to your private cluster
without going through public internet. For this, create Snowflake network rules to allow
ingress from the following `AwsVpceIds` for the AWS Region your cluster is
in. For more information, see [Creating
network rule](https://docs.snowflake.com/en/sql-reference/sql/create-network-rule "https://docs.snowflake.com/en/sql-reference/sql/create-network-rule") in _Snowflake User Guide_.

| VPC Endpoint Ids to use based on Regions your cluster is in | AWS Region                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `VPCE IDs` |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| US East (Ohio)                                              | vpce-0d96cafcd96a50aeb<br>vpce-0cec34343d48f537b                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| US East (N. Virginia)                                       | vpce-0b4d7e8478e141ba8<br>vpce-0b75cd681fb507352<br>vpce-01c03e63820ec00d8<br>vpce-0c2cfc51dc2882422<br>vpce-06ca862f019e4e056<br>vpce-020cda0cfa63f8d1c<br>vpce-0b80504a1a783cd70<br>vpce-0289b9ff0b5259a96<br>vpce-0d7add8628bd69a12<br>vpce-02bfb5966cc59b2af<br>vpce-09e707674af878bf2<br>vpce-049b52e96cc1a2165<br>vpce-0bb6c7b7a8a86cdbb<br>vpce-03b22d599f51e80f3<br>vpce-01d60dc60fc106fe1<br>vpce-0186d20a4b24ecbef<br>vpce-0533906401a36e416<br>vpce-05111fb13d396710e<br>vpce-0694613f4fbd6f514<br>vpce-09b21cb25fe4cc4f4<br>vpce-06029c3550e4d2399<br>vpce-00961862a21b033da<br>vpce-01620b9ae33273587<br>vpce-078cf4ec226880ac9<br>vpce-0d711bf076ce56381<br>vpce-066b7e13cbfca6f6e<br>vpce-0674541252d9ccc26<br>vpce-03540b88dedb4b000<br>vpce-0b1828e79ad394b95<br>vpce-0dc0e6f001fb1a60d<br>vpce-0d8f82e71a244098a<br>vpce-00e374d9e3f1af5ce<br>vpce-0c1e3d6631ddb442f |
| US West (Oregon)                                            | vpce-0f60f72da4cd1e4e7<br>vpce-0c60d21eb8b1669fd<br>vpce-01c4e3e29afdafbef<br>vpce-0cc6bf2a88da139de<br>vpce-0797e08e169e50662<br>vpce-033cbe480381b5c0e<br>vpce-00debbdd8f9eb10a5<br>vpce-08ec2f386c809e889<br>vpce-0856d14310857b545                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Europe (Frankfurt)                                          | vpce-068dbb7d71c9460fb<br>vpce-0a7a7f095942d4ec9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Europe (Ireland)                                            | vpce-06857e59c005a6276<br>vpce-04390f4f8778b75f2<br>vpce-011fd2b1f0aa172fd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Asia Pacific (Tokyo)                                        | vpce-06369e5258144e68a<br>vpce-0f2363cdb8926fbe8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Asia Pacific (Singapore)                                    | vpce-049cd46cce7a12d52<br>vpce-0e8965a1a4bdb8941                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Asia Pacific (Seoul)                                        | vpce-0aa444d9001e1faa1<br>vpce-04a49d4dcfd02b884                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Asia Pacific (Sydney)                                       | vpce-048a60a182c52be63<br>vpce-03c19949787fd1859                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Asia Pacific (Mumbai)                                       | vpce-0d68cb822f6f0db68<br>vpce-0517d32692ffcbde2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Europe (London)                                             | vpce-0fd1874a0ba3b9374<br>vpce-08091b1a85e206029                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| South America (Sao Paulo)                                   | vpce-065169b8144e4f12e<br>vpce-0493699f0e5762d63                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Canada (Central)                                            | vpce-07e6ed81689d5271f<br>vpce-0f53239730541394c                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Europe (Paris)                                              | vpce-09419680077e6488a<br>vpce-0ea81ba2c08140c14                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Asia Pacific (Osaka)                                        | vpce-0a9f003e6a7e38c05<br>vpce-02886510b897b1c5a                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Europe (Stockholm)                                          | vpce-0d96410833219025a<br>vpce-060a32f9a75ba969f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Asia Pacific (Jakarta)                                      | vpce-00add4b9a25e5c649<br>vpce-004ae2de34338a856                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Grant Firehose access to an HTTP endpoint

destination

You can use Amazon Data Firehose to deliver data to any HTTP endpoint destination. Amazon Data Firehose also backs
up that data to the Amazon S3 bucket that you specify, and you can optionally use an AWS KMS
key that you own for Amazon S3 server-side encryption. If error logging is enabled, Amazon Data Firehose
sends data delivery errors to your CloudWatch log streams. You can also use AWS Lambda for data
transformation.

You are required to have an IAM role when creating a Firehose stream. Amazon Data Firehose assumes
that IAM role and gains access to the specified bucket, key, and CloudWatch log group and
streams.

Use the following access policy to enable Amazon Data Firehose to access the S3 bucket that you
specified for data backup. If you don't own the S3 bucket, add
`s3:PutObjectAcl` to the list of Amazon S3 actions, which grants the bucket
owner full access to the objects delivered by Amazon Data Firehose. This policy also grants Amazon Data Firehose
access to CloudWatch for error logging and to AWS Lambda for data transformation. The policy
also has a statement that allows access to Amazon Kinesis Data Streams. If you don't use Kinesis Data Streams as your
data source, you can remove that statement.

###### Important

Amazon Data Firehose doesn't use IAM to access HTTP endpoint destinations owned by supported
third-party service providers, including Datadog, Dynatrace, LogicMonitor, MongoDB,
New Relic, Splunk, or Sumo Logic. For accessing a specified HTTP endpoint
destination owned by a supported third-party service provider, contact that service
provider to obtain the API key or the access key that is required to enable data
delivery to that service from Amazon Data Firehose.

For more information about allowing other AWS services to access your AWS
resources, see [Creating a
Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

###### Important

Currently Amazon Data Firehose does NOT support data delivery to HTTP endpoints in a VPC.

## Cross-account delivery from Amazon MSK

When you're creating a Firehose stream from your Firehose account (for example, Account B) and
your source is an MSK cluster in another AWS account (Account A), you must have the
following configurations in place.

**Account A:**

1. In the Amazon MSK console, choose the provisioned cluster and then choose **Properties**.
2. Under **Network settings**, choose **Edit** and turn on **Multi-VPC connectivity**.
3. Under **Security settings** choose **Edit cluster policy**.
   1. If the cluster does not already have a policy configured, check **Include Firehose service principal** and **Enable Firehose cross-account S3 delivery**. The AWS Management Console will
      automatically generate a policy with the appropriate permissions.
   2. If the cluster already has a policy configured, add the following permissions to the existing policy:

   ```
   {
         "Effect": "Allow",
         "Principal": {
           "AWS": "`arn:aws:`iam::`us-east-1`:role/mskaasTestDeliveryRole"
         },
         "Action": [
           "kafka:GetBootstrapBrokers",
           "kafka:DescribeCluster",
           "kafka:DescribeClusterV2",
           "kafka-cluster:Connect"
         ],
         "Resource": "`arn:aws:`kafka:`us-east-1`:`123456789012`:cluster/DO-NOT-TOUCH-mskaas-provisioned-privateLink/xxxxxxxxx-2f3a-462a-ba09-xxxxxxxxxx-20"  // ARN of the cluster
       },
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "`arn:aws:`:iam::`us-east-1`:role/mskaasTestDeliveryRole"
         },
         "Action": [
           "kafka-cluster:DescribeTopic",
           "kafka-cluster:DescribeTopicDynamicConfiguration",
           "kafka-cluster:ReadData"
         ],
         "Resource": "`arn:aws:`kafka:`us-east-1`:`arn`:topic/DO-NOT-TOUCH-mskaas-provisioned-privateLink/xxxxxxxxx-2f3a-462a-ba09-xxxxxxxxxx-20/*"//topic of the cluster
       },
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "`arn:aws:`iam::`us-east-1`:role/mskaasTestDeliveryRole"
         },
         "Action": "kafka-cluster:DescribeGroup",
         "Resource": "`arn:aws:`kafka:`us-east-1`:`arn`:group/DO-NOT-TOUCH-mskaas-provisioned-privateLink/xxxxxxxxx-2f3a-462a-ba09-xxxxxxxxxx-20/*" //topic of the cluster
       },
    }

   ```

4. Under **AWS principal**, enter the principal ID from Account B.
5. Under **Topic**, specify the Apache Kafka topic from which you want your
   Firehose stream to ingest data. Once the Firehose stream is created, you cannot update
   this topic.
6. Choose **Save changes**

**Account B:**

1. In the Firehose console, choose **Create Firehose stream** using Account B.
2. Under **Source**, choose **Amazon Managed Streaming for Apache Kafka**.
3. Under **Source settings**, for the **Amazon Managed Streaming for Apache Kafka cluster**, enter the ARN of the Amazon MSK cluster in Account A.
4. Under **Topic**, specify the Apache Kafka topic from which you want your
   Firehose stream to ingest data. Once the Firehose stream is created, you cannot update
   this topic.
5. In **Delivery stream name** specify the name for your Firehose stream.

In Account B when you're creating your Firehose stream, you must have an IAM role (created by
default when using the AWS Management Console) that grants the Firehose stream 'read' access to the
cross-account Amazon MSK cluster for the configured topic.

The following is what gets configured by the AWS Management Console:

```
{
    "Sid": "",
    "Effect": "Allow",
    "Action": [
        "kafka:GetBootstrapBrokers",
        "kafka:DescribeCluster",
        "kafka:DescribeClusterV2",
        "kafka-cluster:Connect"
        ],
    "Resource": "`arn:aws:`kafka:`us-east-1`:`arn:aws:`:cluster/DO-NOT-TOUCH-mskaas-provisioned-privateLink/xxxxxxxxx-2f3a-462a-ba09-xxxxxxxxxx-20/*" //topic of the cluster
    },
    {
    "Sid": "",
    "Effect": "Allow",
    "Action": [
        "kafka-cluster:DescribeTopic",
        "kafka-cluster:DescribeTopicDynamicConfiguration",
        "kafka-cluster:ReadData"
    ],
    "Resource": "`arn:aws:`kafka:`us-east-1`:`arn:aws:`:topic/DO-NOT-TOUCH-mskaas-provisioned-privateLink/xxxxxxxxx-2f3a-462a-ba09-xxxxxxxxxx-20/mskaas_test_topic" //topic of the cluster
    },
    {
    "Sid": "",
    "Effect": "Allow",
    "Action": [
        "kafka-cluster:DescribeGroup"
    ],
    "Resource": "`arn:aws:`kafka:`us-east-1`:`arn:aws:`:group/DO-NOT-TOUCH-mskaas-provisioned-privateLink/xxxxxxxxx-2f3a-462a-ba09-xxxxxxxxxx-20/*" //topic of the cluster
    },
 }

```

Next, you can complete the optional step of configuring record transformation and
record format conversion. For more information, see [(Optional) Configure record transformation and format
conversion](create-transform.md "create-transform.md").

## Cross-account delivery to an Amazon S3

destination

You can use the AWS CLI or the Amazon Data Firehose APIs to create a Firehose stream in one AWS
account with an Amazon S3 destination in a different account. The following procedure shows
an example of configuring a Firehose stream owned by account A to deliver data to
an Amazon S3 bucket owned by account B.

1. Create an IAM role under account A using steps described in [Grant Firehose Access to an Amazon S3 Destination](controlling-access.md#using-iam-s3 "controlling-access.md#using-iam-s3").

###### Note

The Amazon S3 bucket specified in the access policy is owned by account B in
this case. Make sure you add `s3:PutObjectAcl` to the list of
Amazon S3 actions in the access policy, which grants account B full access to the
objects delivered by Amazon Data Firehose. This permission is required for cross
account delivery. Amazon Data Firehose sets the "x-amz-acl" header on the request to
"bucket-owner-full-control". 2. To allow access from the IAM role previously created, create an S3 bucket
policy under account B. The following code is an example of the bucket policy.
For more information, see [Using
Bucket Policies and User Policies](../../../AmazonS3/latest/userguide/using-iam-policies.md "../../../AmazonS3/latest/userguide/using-iam-policies.md").

JSON

```
`{

 "Version":"2012-10-17",
 "Id": "PolicyID",
 "Statement": [
 {
 "Sid": "StmtID",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`arn:aws:`iam::`123456789012`:role/`iam-role-name`"
 },
 "Action": [
 "s3:AbortMultipartUpload",
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": [
 "`arn:aws:`s3:::`amzn-s3-demo-bucket`",
 "`arn:aws:`s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

3. Create a Firehose stream under account A using the IAM role that you
   created in step 1.

## Cross-account delivery to an OpenSearch Service

destination

You can use the AWS CLI or the Amazon Data Firehose APIs to create a Firehose stream in one AWS
account with an OpenSearch Service destination in a different account. The following procedure shows
an example of how you can create a Firehose stream under account A and configure it to
deliver data to an OpenSearch Service destination owned by account B.

1. Create an IAM role under account A using the steps described in [Grant Firehose access to a public OpenSearch Service destination](#using-iam-es "#using-iam-es").
2. To allow access from the IAM role that you created in the previous step,
   create an OpenSearch Service policy under account B. The following JSON is an
   example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "`arn:aws:`iam::`123456789012`:role/firehose_delivery_role "
 },
 "Action": "es:ESHttpGet",
 "Resource": [
 "`arn:aws:`es:`us-east-1`:`123456789012`:domain/cross-account-cluster/_all/_settings",
 "`arn:aws:`es:`us-east-1`:`123456789012`:domain/cross-account-cluster/_cluster/stats",
 "`arn:aws:`es:`us-east-1`:`123456789012`:domain/cross-account-cluster/roletest*/_mapping/roletest",
 "`arn:aws:`es:`us-east-1`:`123456789012`:domain/cross-account-cluster/_nodes",
 "`arn:aws:`es:`us-east-1`:`123456789012`:domain/cross-account-cluster/_nodes/stats",
 "`arn:aws:`es:`us-east-1`:`123456789012`:domain/cross-account-cluster/_nodes/*/stats",
 "`arn:aws:`es:`us-east-1`:`123456789012`:domain/cross-account-cluster/_stats",
 "`arn:aws:`es:`us-east-1`:`123456789012`:domain/cross-account-cluster/roletest*/_stats",
 "`arn:aws:`es:`us-east-1`:`123456789012`:domain/cross-account-cluster/"
 ]
 }
 ]
}`

```

3. Create a Firehose stream under account A using the IAM role that you
   created in step 1. When you create the Firehose stream, use the AWS CLI or the
   Amazon Data Firehose APIs and specify the `ClusterEndpoint` field instead of
   `DomainARN` for OpenSearch Service.

###### Note

To create a Firehose stream in one AWS account with an OpenSearch Service
destination in a different account, you must use the AWS CLI or the Amazon Data Firehose APIs. You
can't use the AWS Management Console to create this kind of cross-account configuration.

## Using tags to control access

You can use the optional `Condition` element (or `Condition`
_block_) in an IAM policy to fine-tune access to Amazon Data Firehose operations
based on tag keys and values. The following subsections describe how to do this for the
different Amazon Data Firehose operations. For more on the use of the `Condition` element
and the operators that you can use within it, see [IAM JSON Policy Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md").

### CreateDeliveryStream

For the `CreateDeliveryStream` operation, use the
`aws:RequestTag` condition key. In the following example,
`MyKey` and `MyValue` represent the key and corresponding
value for a tag. For more information, see [Understand tag basics](firehose-tagging-basics.md "firehose-tagging-basics.md")

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "firehose:CreateDeliveryStream",
 "firehose:TagDeliveryStream"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/MyKey": "MyValue"
 }
 }
 }]
}`

```

### TagDeliveryStream

For the `TagDeliveryStream` operation, use the `aws:TagKeys`
condition key. In the following example, `MyKey` is an example tag
key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "firehose:TagDeliveryStream",
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "MyKey"
 }
 }
 }
 ]
}`

```

### UntagDeliveryStream

For the `UntagDeliveryStream` operation, use the
`aws:TagKeys` condition key. In the following example,
`MyKey` is an example tag key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "firehose:UntagDeliveryStream",
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "MyKey"
 }
 }
 }
 ]
}`

```

### ListDeliveryStreams

You can't use tag-based access control with
`ListDeliveryStreams`.

### Other operations

For all Firehose operations other than `CreateDeliveryStream`,
`TagDeliveryStream`, `UntagDeliveryStream`, and
`ListDeliveryStreams`, use the `aws:RequestTag` condition
key. In the following example, `MyKey` and `MyValue` represent
the key and corresponding value for a tag.

`ListDeliveryStreams`, use the `firehose:ResourceTag`
condition key to control access based on the tags on that Firehose stream.

In the following example, `MyKey` and `MyValue` represent
the key and corresponding value for a tag. The policy would only apply to Data
Firehose streams having a tag named `MyKey` with a value of
`MyValue`. For more information about controlling access based on
resource tags, see [Controlling access to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources") in the
_IAM User Guide_.
