# Logging with AWS CloudTrail for S3 Vectors

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

Amazon S3 Vectors is integrated with AWS CloudTrail, a service that provides a record of actions that are
taken by a user, role, or an AWS service. CloudTrail captures all API calls for S3 Vectors as
events. Using the information that's collected by CloudTrail, you can determine the request that
was made to S3 Vectors, the IP address from which the request was made, when it was made, and
additional details. When a supported event activity occurs in S3 Vectors, that activity is
recorded in a CloudTrail event. You can use CloudTrail trail to log management events
and data events for S3 Vectors.

To learn more about CloudTrail, see the [CloudTrail User
Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## S3 Vectors information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity
occurs in S3 Vectors, that activity is recorded in a CloudTrail event along with other AWS
service events in Event history. You can view, search, and download recent events in
your AWS account. For more information, see [Viewing Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
S3 Vectors, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all
AWS Regions. The trail logs events from all Regions in the AWS partition and
delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can
configure other AWS services to further analyze and act upon the event data collected
in CloudTrail logs. For more information, see [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md"), [Configuring Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting-notifications-top-level.md "../../../awscloudtrail/latest/userguide/getting-notifications-top-level.md"), [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md"), and [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md") in the _CloudTrail
User Guide_.

All S3 Vectors API actions are logged by CloudTrail and are documented in the [Amazon S3 Vectors](../API/API_Operations_Amazon_S3_Vectors.md "../API/API_Operations_Amazon_S3_Vectors.md") API Reference. For example, calls to the
[CreateVectorBucket](../API/API_S3VectorBuckets_CreateVectorBucket.md "../API/API_S3VectorBuckets_CreateVectorBucket.md"), [CreateIndex](../API/API_S3VectorBuckets_CreateIndex.md "../API/API_S3VectorBuckets_CreateIndex.md"), and
[QueryVectors](../API/API_S3VectorBuckets_QueryVectors.md "../API/API_S3VectorBuckets_QueryVectors.md") actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or IAM user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md") in the _CloudTrail User
Guide_.

## CloudTrail management events for

S3 Vectors

Management events provide information about management operations that are performed
on resources in your AWS account. These are also known as control plane operations. By
default, CloudTrail logs management events.

For S3 Vectors, CloudTrail logs the following management events:

- [CreateVectorBucket](../API/API_S3VectorBuckets_CreateVectorBucket.md "../API/API_S3VectorBuckets_CreateVectorBucket.md")
- [DeleteVectorBucket](../API/API_S3VectorBuckets_DeleteVectorBucket.md "../API/API_S3VectorBuckets_DeleteVectorBucket.md")
- [GetVectorBucket](../API/API_S3VectorBuckets_GetVectorBucket.md "../API/API_S3VectorBuckets_GetVectorBucket.md")
- [ListVectorBuckets](../API/API_S3VectorBuckets_ListVectorBuckets.md "../API/API_S3VectorBuckets_ListVectorBuckets.md")
- [PutVectorBucketPolicy](../API/API_S3VectorBuckets_PutVectorBucketPolicy.md "../API/API_S3VectorBuckets_PutVectorBucketPolicy.md")
- [GetVectorBucketPolicy](../API/API_S3VectorBuckets_GetVectorBucketPolicy.md "../API/API_S3VectorBuckets_GetVectorBucketPolicy.md")
- [DeleteVectorBucketPolicy](../API/API_S3VectorBuckets_DeleteVectorBucketPolicy.md "../API/API_S3VectorBuckets_DeleteVectorBucketPolicy.md")
- [CreateIndex](../API/API_S3VectorBuckets_CreateIndex.md "../API/API_S3VectorBuckets_CreateIndex.md")
- [DeleteIndex](../API/API_S3VectorBuckets_DeleteIndex.md "../API/API_S3VectorBuckets_DeleteIndex.md")
- [GetIndex](../API/API_S3VectorBuckets_GetIndex.md "../API/API_S3VectorBuckets_GetIndex.md")
- [ListIndexes](../API/API_S3VectorBuckets_ListIndexes.md "../API/API_S3VectorBuckets_ListIndexes.md")

The `eventSource` for S3 Vectors management events and data events is
`s3vectors.amazonaws.com`.

For more information about management events, see [Logging management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md") in the _CloudTrail User
Guide_.

## CloudTrail data events for

S3 Vectors

Data events provide information about the resource operations performed on or in a
resource. These are also known as data plane operations. By default, CloudTrail doesn't log
data events. However, you can configure trails to log data events for S3 Vectors
resources.

When you configure your trail to log data events, you can specify the S3 Vectors
resource type. S3 Vectors supports the following resource types for data events:

- `AWS::S3Vectors::VectorBucket` - Logs data events for all
  vector indexes in the specified vector buckets
- `AWS::S3Vectors::Index` - Logs data events for specific
  vector indexes

For S3 Vectors, CloudTrail logs the following data events:

Vector data operations:

- [PutVectors](../API/API_S3VectorBuckets_PutVectors.md "../API/API_S3VectorBuckets_PutVectors.md") - Logs when vectors are added to a
  vector index
- [GetVectors](../API/API_S3VectorBuckets_GetVectors.md "../API/API_S3VectorBuckets_GetVectors.md") - Logs when vectors are retrieved from a
  vector index
- [DeleteVectors](../API/API_S3VectorBuckets_DeleteVectors.md "../API/API_S3VectorBuckets_DeleteVectors.md") - Logs when vectors are deleted from a
  vector index
- [ListVectors](../API/API_S3VectorBuckets_ListVectors.md "../API/API_S3VectorBuckets_ListVectors.md") - Logs when vectors in a vector index are
  listed
- [QueryVectors](../API/API_S3VectorBuckets_QueryVectors.md "../API/API_S3VectorBuckets_QueryVectors.md") - Logs when similarity queries are performed on a
  vector index

The `eventSource` for S3 Vectors data events is
`s3vectors.amazonaws.com`.

## Enabling data event logging

for S3 Vectors

You can enable data event logging for S3 Vectors resources when you create or update
a CloudTrail trail. You can specify logging for all vector buckets and vector indexes in
your account, or you can specify individual vector buckets or vector indexes. For
detailed steps about creating a trail, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the _CloudTrail User Guide_.

To enable data event logging for all S3 Vectors resources:

- When creating or updating a trail, choose **Data
  events**.
- For **Resource type**, choose
  `AWS::S3Vectors::VectorBucket`.
- For **Resource ARN**, enter
  `arn:aws:s3vectors:_:_:bucket/*` to log events for all
  vector buckets, or specify individual vector bucket ARNs (for example,
  `arn:aws:s3vectors:`us-east-1`:`123456789012`:bucket/`amzn-s3-demo-vector-bucket``).

To enable data event logging for specific vector indexes:

- When creating or updating a trail, choose **Data
  events**.
- For **Resource type**, choose
  `AWS::S3Vectors::Index`.
- For **Resource ARN**, enter the ARN of the
  specific vector index, such as:
  `arn:aws:s3vectors:`us-east-1`:`123456789012`:bucket/`amzn-s3-demo-vector-bucket`/index/`my-index``.

For more information about data events, see [Logging data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") in the _CloudTrail User Guide_.

###### Topics

- [CloudTrail log file example for S3 Vectors](s3-vectors-cloudtrail-log-example.md "s3-vectors-cloudtrail-log-example.md")
