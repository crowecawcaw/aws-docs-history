# Logging Amazon S3 API calls using AWS CloudTrail

[AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") is
a service that provides a record of actions taken by a user, role, or an AWS service.
CloudTrail captures all API calls for Amazon S3 as events. The calls captured include
calls from the Amazon S3 console and code calls to the Amazon S3 API operations.
Using the information collected by CloudTrail, you can determine the request that was made to
Amazon S3, the IP address from which the request was made, when it was made, and
additional details.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root user or user credentials.
- Whether the request was made on behalf of an IAM Identity Center user.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.
  CloudTrail is active in your AWS account when you create the account and you automatically
  have access to the CloudTrail **Event history**. The CloudTrail **Event
  history** provides a viewable, searchable, downloadable, and immutable
  record of the past 90 days of recorded management events in an AWS Region. For more
  information, see [Working with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the
  _AWS CloudTrail User Guide_. There are no CloudTrail charges for viewing the
  **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or
a [CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") event data store.

**CloudTrail trails**

A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") and [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the _AWS CloudTrail User Guide_.

You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

**CloudTrail Lake event data stores**

_CloudTrail Lake_ lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/") format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into _event data stores_, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors"). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") in the _AWS CloudTrail User Guide_.

CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

You can store your log files in your bucket for as long as you want, but you can also
define Amazon S3 Lifecycle rules to archive or delete log files automatically. By default,
your log files are encrypted by using Amazon S3 server-side encryption (SSE).

## Using CloudTrail logs with Amazon S3 server

access logs and CloudWatch Logs

AWS CloudTrail logs provide a record of actions taken by a user, role, or an AWS
service in Amazon S3, while Amazon S3 server access logs provide detailed records for the
requests that are made to an S3 bucket. For more information about how the different
logs work, and their properties, performance, and costs, see [Logging options for Amazon S3](logging-with-S3.md "logging-with-S3.md").

You can use AWS CloudTrail logs together with server access logs for Amazon S3. CloudTrail logs
provide you with detailed API tracking for Amazon S3 bucket-level and object-level
operations. Server access logs for Amazon S3 provide you with visibility into
object-level operations on your data in Amazon S3. For more information about server
access logs, see [Logging requests with server access logging](ServerLogs.md "ServerLogs.md").

You can also use CloudTrail logs together with Amazon CloudWatch for Amazon S3. CloudTrail integration with
CloudWatch Logs delivers S3 bucket-level API activity captured by CloudTrail to a CloudWatch log stream in
the CloudWatch log group that you specify. You can create CloudWatch alarms for monitoring
specific API activity and receive email notifications when the specific API activity
occurs. For more information about CloudWatch alarms for monitoring specific API activity,
see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md"). For more information
about using CloudWatch with Amazon S3, see [Monitoring metrics with Amazon CloudWatch](cloudwatch-monitoring.md "cloudwatch-monitoring.md").

###### Note

S3 does not support delivery of CloudTrail logs to the requester or the bucket owner
for VPC endpoint requests when the VPC endpoint policy denies them.

## CloudTrail tracking with Amazon S3 SOAP API calls

CloudTrail tracks Amazon S3 SOAP API calls. Amazon S3 SOAP support over HTTP is deprecated, but it
is still available over HTTPS. For more information about Amazon S3 SOAP support, see
[Appendix:
SOAP API](../API/APISoap.md "../API/APISoap.md") in the _Amazon S3 API Reference_.

###### Important

Newer Amazon S3 features are not supported for SOAP. We recommend that you use
either the REST API or the AWS SDKs.

The following table shows Amazon S3 SOAP actions tracked by CloudTrail logging.

| SOAP API name                                                                                                           | API event name used in CloudTrail log |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ListAllMyBuckets](../API/SOAPListAllMyBuckets.md "../API/SOAPListAllMyBuckets.md")                                     | `ListBuckets`                         |
| [CreateBucket](../API/SOAPCreateBucket.md "../API/SOAPCreateBucket.md")                                                 | `CreateBucket`                        |
| [DeleteBucket](../API/SOAPDeleteBucket.md "../API/SOAPDeleteBucket.md")                                                 | `DeleteBucket`                        |
| [GetBucketAccessControlPolicy](../API/SOAPGetBucketAccessControlPolicy.md "../API/SOAPGetBucketAccessControlPolicy.md") | `GetBucketAcl`                        |
| [SetBucketAccessControlPolicy](../API/SOAPSetBucketAccessControlPolicy.md "../API/SOAPSetBucketAccessControlPolicy.md") | `PutBucketAcl`                        |
| [GetBucketLoggingStatus](../API/SOAPGetBucketLoggingStatus.md "../API/SOAPGetBucketLoggingStatus.md")                   | `GetBucketLogging`                    |
| [SetBucketLoggingStatus](../API/SOAPSetBucketLoggingStatus.md "../API/SOAPSetBucketLoggingStatus.md")                   | `PutBucketLogging`                    | For more information about CloudTrail and Amazon S3, see the following topics: ###### Topics <br>• [Amazon S3 CloudTrail events](cloudtrail-logging-s3-info.md "cloudtrail-logging-s3-info.md") <br>• [CloudTrail log file entries for Amazon S3 and S3 on Outposts](cloudtrail-logging-understanding-s3-entries.md "cloudtrail-logging-understanding-s3-entries.md") <br>• [Enabling CloudTrail event logging for S3 buckets and objects](enable-cloudtrail-logging-for-s3.md "enable-cloudtrail-logging-for-s3.md") <br>• [Identifying Amazon S3 requests using CloudTrail](cloudtrail-request-identification.md "cloudtrail-request-identification.md") |
