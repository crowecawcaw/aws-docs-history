

# Logging with AWS CloudTrail for S3 Vectors
<a name="s3-vectors-logging"></a>

Amazon S3 Vectors is integrated with AWS CloudTrail, a service that provides a record of actions that are taken by a user, role, or an AWS service. CloudTrail captures all API calls for S3 Vectors as events. Using the information that's collected by CloudTrail, you can determine the request that was made to S3 Vectors, the IP address from which the request was made, when it was made, and additional details. When a supported event activity occurs in S3 Vectors, that activity is recorded in a CloudTrail event. You can use CloudTrail trail to log management events and data events for S3 Vectors.

To learn more about CloudTrail, see the [CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## S3 Vectors information in CloudTrail
<a name="s3-vectors-logging-information"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in S3 Vectors, that activity is recorded in a CloudTrail event along with other AWS service events in Event history. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for S3 Vectors, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html), [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting-notifications-top-level.html), [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html), and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html) in the *CloudTrail User Guide*.

All S3 Vectors API actions are logged by CloudTrail and are documented in the [Amazon S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Vectors.html) API Reference. For example, calls to the [CreateVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateVectorBucket.html), [CreateIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateIndex.html), and [QueryVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryVectors.html) actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or IAM user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html) in the *CloudTrail User Guide*.

## CloudTrail management events for S3 Vectors
<a name="s3-vectors-logging-management-events"></a>

Management events provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

For S3 Vectors, CloudTrail logs the following management events:
+ [CreateVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateVectorBucket.html)
+ [DeleteVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectorBucket.html)
+ [GetVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectorBucket.html)
+ [ListVectorBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectorBuckets.html)
+ [PutVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectorBucketPolicy.html)
+ [GetVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectorBucketPolicy.html)
+ [DeleteVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectorBucketPolicy.html)
+ [CreateIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateIndex.html)
+ [DeleteIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteIndex.html)
+ [GetIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetIndex.html)
+ [ListIndexes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListIndexes.html)

The `eventSource` for S3 Vectors management events and data events is `s3vectors.amazonaws.com`.

For more information about management events, see [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) in the *CloudTrail User Guide*.

## CloudTrail data events for S3 Vectors
<a name="s3-vectors-logging-data-events"></a>

Data events provide information about the resource operations performed on or in a resource. These are also known as data plane operations. By default, CloudTrail doesn't log data events. However, you can configure trails to log data events for S3 Vectors resources.

When you configure your trail to log data events, you can specify the S3 Vectors resource type. S3 Vectors supports the following resource types for data events:
+ `AWS::S3Vectors::VectorBucket` - Logs data events for all vector indexes in the specified vector buckets
+ `AWS::S3Vectors::Index` - Logs data events for specific vector indexes

For S3 Vectors, CloudTrail logs the following data events:

Vector data operations:
+ [PutVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectors.html) - Logs when vectors are added to a vector index
+ [GetVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectors.html) - Logs when vectors are retrieved from a vector index
+ [DeleteVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectors.html) - Logs when vectors are deleted from a vector index
+ [ListVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectors.html) - Logs when vectors in a vector index are listed
+ [QueryVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryVectors.html) - Logs when similarity queries are performed on a vector index

The `eventSource` for S3 Vectors data events is `s3vectors.amazonaws.com`.

## Enabling data event logging for S3 Vectors
<a name="s3-vectors-logging-enabling-data-events"></a>

You can enable data event logging for S3 Vectors resources when you create or update a CloudTrail trail. You can specify logging for all vector buckets and vector indexes in your account, or you can specify individual vector buckets or vector indexes. For detailed steps about creating a trail, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *CloudTrail User Guide*.

To enable data event logging for all S3 Vectors resources:
+ When creating or updating a trail, choose **Data events**.
+ For **Resource type**, choose `AWS::S3Vectors::VectorBucket`.
+ For **Resource ARN**, enter `arn:aws:s3vectors:_:_:bucket/*` to log events for all vector buckets, or specify individual vector bucket ARNs (for example, `arn:aws:s3vectors:{{us-east-1}}:{{123456789012}}:bucket/{{amzn-s3-demo-vector-bucket}}`).

To enable data event logging for specific vector indexes:
+ When creating or updating a trail, choose **Data events**.
+ For **Resource type**, choose `AWS::S3Vectors::Index`.
+ For **Resource ARN**, enter the ARN of the specific vector index, such as: `arn:aws:s3vectors:{{us-east-1}}:{{123456789012}}:bucket/{{amzn-s3-demo-vector-bucket}}/index/{{my-index}}`.

For more information about data events, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *CloudTrail User Guide*.

**Topics**
+ [S3 Vectors information in CloudTrail](#s3-vectors-logging-information)
+ [CloudTrail management events for S3 Vectors](#s3-vectors-logging-management-events)
+ [CloudTrail data events for S3 Vectors](#s3-vectors-logging-data-events)
+ [Enabling data event logging for S3 Vectors](#s3-vectors-logging-enabling-data-events)
+ [CloudTrail log file example for S3 Vectors](s3-vectors-cloudtrail-log-example.md)