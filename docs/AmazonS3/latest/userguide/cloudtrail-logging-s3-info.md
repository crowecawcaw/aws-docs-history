# Amazon S3 CloudTrail events

###### Important

Amazon S3 now applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for every bucket in Amazon S3. Starting January 5, 2023, all new object uploads to Amazon S3 are automatically encrypted at no additional cost and with no impact on performance. The automatic encryption status for S3 bucket default encryption configuration and for new object uploads is available in CloudTrail logs, S3 Inventory, S3 Storage Lens, the Amazon S3 console, and as an additional Amazon S3 API response header in the AWS CLI and AWS SDKs. For more information, see [Default encryption FAQ](default-encryption-faq.md "default-encryption-faq.md").

This section provides information about the events that S3 logs to CloudTrail.

## Amazon S3 data events in

CloudTrail

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") provide information about the resource operations
performed on or in a resource (for example, reading or writing to an Amazon S3
object). These are also
known as data plane operations. Data events are often high-volume activities. By
default, CloudTrail doesn’t log data events. The CloudTrail **Event
history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail
pricing, see [AWS CloudTrail
Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

You can log data events for the Amazon S3 resource types by using the CloudTrail
console, AWS CLI, or CloudTrail API operations. For more information about how to log
data events, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") and [Logging data events with the AWS Command Line Interface](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI") in the
_AWS CloudTrail User Guide_.

The following table lists the Amazon S3 resource types for which you can
log data events. The **Data event type (console)**
column shows the value to choose from the **Data event type**
list on the CloudTrail console. The **resources.type
value** column shows the `resources.type` value, which
you would specify when configuring advanced event selectors using the AWS CLI or
CloudTrail APIs. The **Data APIs logged to CloudTrail** column
shows the API calls logged to CloudTrail for the resource type.

| Data event type (console) | resources.type value               | Data APIs logged to CloudTrail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **S3**                    | `AWS::S3::Object`                  | • [AbortMultipartUpload](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")<br>• [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")<br>• [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")<br>• [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")<br>• [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md")<br>• [DeleteObjectTagging](../API/API_DeleteObjectTagging.md "../API/API_DeleteObjectTagging.md")<br>• [DeleteObjects](../API/API_DeleteObjects.md "../API/API_DeleteObjects.md")<br>• [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")<br>• [GetObjectAcl](../API/API_GetObjectAcl.md "../API/API_GetObjectAcl.md")<br>• [GetObjectAttributes](../API/API_GetObjectAttributes.md "../API/API_GetObjectAttributes.md")<br>• [GetObjectLegalHold](../API/API_GetObjectLegalHold.md "../API/API_GetObjectLegalHold.md")<br>• [GetObjectRetention](../API/API_GetObjectRetention.md "../API/API_GetObjectRetention.md")<br>• [GetObjectTagging](../API/API_GetObjectTagging.md "../API/API_GetObjectTagging.md")<br>• [GetObjectTorrent](../API/API_GetObjectTorrent.md "../API/API_GetObjectTorrent.md")<br>• [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")<br>• [HeadBucket](../API/API_HeadBucket.md "../API/API_HeadBucket.md")<br>• [ListObjectVersions](../API/API_ListObjectVersions.md "../API/API_ListObjectVersions.md")<br>• [ListObjects](../API/API_ListObjects.md "../API/API_ListObjects.md")<br>• [ListParts](../API/API_ListParts.md "../API/API_ListParts.md")<br>• [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")<br>• [PutObjectAcl](../API/API_PutObjectAcl.md "../API/API_PutObjectAcl.md")<br>• [PutObjectLegalHold](../API/API_PutObjectLegalHold.md "../API/API_PutObjectLegalHold.md")<br>• [PutObjectRetention](../API/API_PutObjectRetention.md "../API/API_PutObjectRetention.md")<br>• [PutObjectTagging](../API/API_PutObjectTagging.md "../API/API_PutObjectTagging.md")<br>• [RestoreObject](../API/API_RestoreObject.md "../API/API_RestoreObject.md")<br>• [SelectObjectContent](../API/API_SelectObjectContent.md "../API/API_SelectObjectContent.md")<br>• [UpdateObjectEncryption](../API/API_UpdateObjectEncryption.md "../API/API_UpdateObjectEncryption.md")<br>• [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")<br>• [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md") |
| **S3 Express One Zone**   | `AWS::S3Express::Object`           | • [AbortMultipartUpload](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")<br>• [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")<br>• [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md")<br>• [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")<br>• [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")<br>• [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md")<br>• [DeleteObjects](../API/API_DeleteObjects.md "../API/API_DeleteObjects.md")<br>• [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")<br>• [GetObjectAttributes](../API/API_GetObjectAttributes.md "../API/API_GetObjectAttributes.md")<br>• [HeadBucket](../API/API_HeadBucket.md "../API/API_HeadBucket.md")<br>• [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")<br>• [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md")<br>• [ListParts](../API/API_ListParts.md "../API/API_ListParts.md")<br>• [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")<br>• [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")<br>• [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **S3 Access Point**       | `AWS::S3::Access Point`            | • [AbortMultipartUpload](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")<br>• [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")<br>• [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") (same-region<br>copies only)<br>• [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")<br>• [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md")<br>• [DeleteObjectTagging](../API/API_DeleteObjectTagging.md "../API/API_DeleteObjectTagging.md")<br>• [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")<br>• [GetObjectAcl](../API/API_GetObjectAcl.md "../API/API_GetObjectAcl.md")<br>• [GetObjectAttributes](../API/API_GetObjectAttributes.md "../API/API_GetObjectAttributes.md")<br>• [GetObjectLegalHold](../API/API_GetObjectLegalHold.md "../API/API_GetObjectLegalHold.md")<br>• [GetObjectRetention](../API/API_GetObjectRetention.md "../API/API_GetObjectRetention.md")<br>• [GetObjectTagging](../API/API_GetObjectTagging.md "../API/API_GetObjectTagging.md")<br>• [HeadBucket](../API/API_HeadBucket.md "../API/API_HeadBucket.md")<br>• [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")<br>• [ListObjects](../API/API_ListObjects.md "../API/API_ListObjects.md")<br>• [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md")<br>• [ListObjectVersions](../API/API_ListObjectVersions.md "../API/API_ListObjectVersions.md")<br>• [ListParts](../API/API_ListParts.md "../API/API_ListParts.md")<br>• [Presign](../API/sigv4-query-string-auth.md "../API/sigv4-query-string-auth.md")<br>• [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")<br>• [PutObjectLegalHold](../API/API_PutObjectLegalHold.md "../API/API_PutObjectLegalHold.md")<br>• [PutObjectRetention](../API/API_PutObjectRetention.md "../API/API_PutObjectRetention.md")<br>• [PutObjectAcl](../API/API_PutObjectAcl.md "../API/API_PutObjectAcl.md")<br>• [PutObjectTagging](../API/API_PutObjectTagging.md "../API/API_PutObjectTagging.md")<br>• [RestoreObject](../API/API_RestoreObject.md "../API/API_RestoreObject.md")<br>• [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")<br>• [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")<br>(same-region copies only)                                                                                                                                                       |
| **S3 Object Lambda**      | `AWS::S3ObjectLambda::AccessPoint` | • [AbortMultipartUpload](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")<br>• [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")<br>• [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") (same-region<br>copies only)<br>• [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")<br>• [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md")<br>• [DeleteObjectTagging](../API/API_DeleteObjectTagging.md "../API/API_DeleteObjectTagging.md")<br>• [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")<br>• [GetObjectAcl](../API/API_GetObjectAcl.md "../API/API_GetObjectAcl.md")<br>• [GetObjectLegalHold](../API/API_GetObjectLegalHold.md "../API/API_GetObjectLegalHold.md")<br>• [GetObjectRetention](../API/API_GetObjectRetention.md "../API/API_GetObjectRetention.md")<br>• [GetObjectTagging](../API/API_GetObjectTagging.md "../API/API_GetObjectTagging.md")<br>• [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")<br>• [ListObjects](../API/API_ListObjects.md "../API/API_ListObjects.md")<br>• [ListObjectVersions](../API/API_ListObjectVersions.md "../API/API_ListObjectVersions.md")<br>• [ListParts](../API/API_ListParts.md "../API/API_ListParts.md")<br>• [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")<br>• [PutObjectLegalHold](../API/API_PutObjectLegalHold.md "../API/API_PutObjectLegalHold.md")<br>• [PutObjectRetention](../API/API_PutObjectRetention.md "../API/API_PutObjectRetention.md")<br>• [PutObjectAcl](../API/API_PutObjectAcl.md "../API/API_PutObjectAcl.md")<br>• [PutObjectTagging](../API/API_PutObjectTagging.md "../API/API_PutObjectTagging.md")<br>• [RestoreObject](../API/API_RestoreObject.md "../API/API_RestoreObject.md")<br>• [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")<br>• [WriteGetObjectResponse](../API/API_WriteGetObjectResponse.md "../API/API_WriteGetObjectResponse.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **S3 Outposts**           | `AWS::S3Outposts::Object`          | • [AbortMultipartUpload](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")<br>• [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")<br>• [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") (same-region<br>copies only)<br>• [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")<br>• [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md")<br>• [DeleteObjectTagging](../API/API_DeleteObjectTagging.md "../API/API_DeleteObjectTagging.md")<br>• [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")<br>• [GetObjectTagging](../API/API_GetObjectTagging.md "../API/API_GetObjectTagging.md")<br>• [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")<br>• [ListObjects](../API/API_ListObjects.md "../API/API_ListObjects.md")<br>• [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md")<br>• [ListParts](../API/API_ListParts.md "../API/API_ListParts.md")<br>• [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")<br>• [PutObjectTagging](../API/API_PutObjectTagging.md "../API/API_PutObjectTagging.md")<br>• [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")<br>• [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

You can configure advanced event selectors to filter on the
`eventName`, `readOnly`, and
`resources.ARN` fields to log only those events that are
important to you. For more information about these fields, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") in the
_AWS CloudTrail API Reference_.

## Amazon S3 management events

in CloudTrail

Amazon S3 logs all control plane operations as management events. For more
information about S3 API operations, see the [Amazon S3 API
Reference](../API/API_Operations.md "../API/API_Operations.md").

## How CloudTrail captures requests made

to Amazon S3

By default, CloudTrail logs S3 bucket-level API calls that were made in the last 90
days, but not log requests made to objects. Bucket-level calls include events
such as `CreateBucket`, `DeleteBucket`,
`PutBucketLifecycle`, `PutBucketPolicy`, and so on.
You can see bucket-level events on the CloudTrail console. However, you can't view
data events (Amazon S3 object-level calls) there—you must parse or query CloudTrail
logs for them.

If you are logging data activity with AWS CloudTrail, the event record for an Amazon S3 `DeleteObjects` data event includes both the `DeleteObjects` event and a `DeleteObject` event for each object deleted as part of that operation. You can exclude the additional visibility about deleted objects from the event record. For more information, see [AWS CLI examples for filtering data events](../../../awscloudtrail/latest/userguide/filtering-data-events.md#filtering-data-events-deleteobjects "../../../awscloudtrail/latest/userguide/filtering-data-events.md#filtering-data-events-deleteobjects") in the _AWS CloudTrail User Guide._

## Amazon S3 account-level actions

tracked by CloudTrail logging

CloudTrail logs account-level actions. Amazon S3 records are written together with other
AWS service records in a log file. CloudTrail determines when to create and write to
a new file based on a time period and file size.

The tables in this section list the Amazon S3 account-level actions that are
supported for logging by CloudTrail.

Amazon S3 account-level API actions tracked by CloudTrail logging appear as the following
event names. The CloudTrail event names differ from the API action name. For example,
DeletePublicAccessBlock is DeleteAccountPublicAccessBlock.

- [DeleteAccountPublicAccessBlock](../API/API_control_DeletePublicAccessBlock.md "../API/API_control_DeletePublicAccessBlock.md")
- [GetAccountPublicAccessBlock](../API/API_control_GetPublicAccessBlock.md "../API/API_control_GetPublicAccessBlock.md")
- [PutAccountPublicAccessBlock](../API/API_control_PutPublicAccessBlock.md "../API/API_control_PutPublicAccessBlock.md")

## Amazon S3 bucket-level actions

that are tracked by CloudTrail logging

By default, CloudTrail logs bucket-level actions for general purpose buckets. Amazon S3
records are written together with other AWS service records in a log file.
CloudTrail determines when to create and write to a new file based on a time period
and file size.

This section lists the Amazon S3 bucket-level actions that are supported for
logging by CloudTrail.

Amazon S3 bucket-level API actions tracked by CloudTrail logging appear as the following
event names. In some cases, the CloudTrail event name differs from the API action
name. For example, `PutBucketLifecycleConfiguration` is
`PutBucketLifecycle`.

- [CreateBucket](../API/API_CreateBucket.md "../API/API_CreateBucket.md")
- [CreateBucketMetadataConfiguration](../API/API_CreateBucketMetadataConfiguration.md "../API/API_CreateBucketMetadataConfiguration.md") (V2 API operation)
- [CreateBucketMetadataTableConfiguration](../API/API_CreateBucketMetadataTableConfiguration.md "../API/API_CreateBucketMetadataTableConfiguration.md") (V1 API operation)
- [DeleteBucket](../API/API_DeleteBucket.md "../API/API_DeleteBucket.md")
- [DeleteBucketAnalyticsConfiguration](../API/API_DeleteBucketAnalyticsConfiguration.md "../API/API_DeleteBucketAnalyticsConfiguration.md")
- [DeleteBucketCors](../API/API_DeleteBucketCors.md "../API/API_DeleteBucketCors.md")
- [DeleteBucketEncryption](../API/API_DeleteBucketEncryption.md "../API/API_DeleteBucketEncryption.md")
- [DeleteBucketIntelligentTieringConfiguration](../API/API_DeleteBucketIntelligentTieringConfiguration.md "../API/API_DeleteBucketIntelligentTieringConfiguration.md")
- [DeleteBucketInventoryConfiguration](../API/API_DeleteBucketInventoryConfiguration.md "../API/API_DeleteBucketInventoryConfiguration.md")
- [DeleteBucketLifecycle](../API/API_DeleteBucketLifecycle.md "../API/API_DeleteBucketLifecycle.md")
- [DeleteBucketMetadataConfiguration](../API/API_DeleteBucketMetadataConfiguration.md "../API/API_DeleteBucketMetadataConfiguration.md") (V2 API operation)
- [DeleteBucketMetadataTableConfiguration](../API/API_DeleteBucketMetadataTableConfiguration.md "../API/API_DeleteBucketMetadataTableConfiguration.md") (V1 API operation)
- [DeleteBucketMetricsConfiguration](../API/API_DeleteBucketMetricsConfiguration.md "../API/API_DeleteBucketMetricsConfiguration.md")
- [DeleteBucketOwnershipControls](../API/API_DeleteBucketOwnershipControls.md "../API/API_DeleteBucketOwnershipControls.md")
- [DeleteBucketPolicy](../API/API_DeleteBucketPolicy.md "../API/API_DeleteBucketPolicy.md")
- [DeleteBucketPublicAccessBlock](../API/API_DeletePublicAccessBlock.md "../API/API_DeletePublicAccessBlock.md")
- [DeleteBucketReplication](../API/API_DeleteBucketReplication.md "../API/API_DeleteBucketReplication.md")
- [DeleteBucketTagging](../API/API_DeleteBucketTagging.md "../API/API_DeleteBucketTagging.md")
- [GetAccelerateConfiguration](../API/API_GetBucketAccelerateConfiguration.md "../API/API_GetBucketAccelerateConfiguration.md")
- [GetBucketAcl](../API/API_GetBucketAcl.md "../API/API_GetBucketAcl.md")
- [GetBucketAnalyticsConfiguration](../API/API_GetBucketAnalyticsConfiguration.md "../API/API_GetBucketAnalyticsConfiguration.md")
- [GetBucketCors](../API/API_GetBucketCors.md "../API/API_GetBucketCors.md")
- [GetBucketEncryption](../API/API_GetBucketEncryption.md "../API/API_GetBucketEncryption.md")
- [GetBucketIntelligentTieringConfiguration](../API/API_GetBucketIntelligentTieringConfiguration.md "../API/API_GetBucketIntelligentTieringConfiguration.md")
- [GetBucketInventoryConfiguration](../API/API_GetBucketInventoryConfiguration.md "../API/API_GetBucketInventoryConfiguration.md")
- [GetBucketLifecycle](../API/API_GetBucketLifecycle.md "../API/API_GetBucketLifecycle.md")
- [GetBucketLocation](../API/API_GetBucketLocation.md "../API/API_GetBucketLocation.md")
- [GetBucketLogging](../API/API_GetBucketLogging.md "../API/API_GetBucketLogging.md")
- [GetBucketMetadataConfiguration](../API/API_GetBucketMetadataConfiguration.md "../API/API_GetBucketMetadataConfiguration.md") (V2 API operation)
- [GetBucketMetadataTableConfiguration](../API/API_GetBucketMetadataTableConfiguration.md "../API/API_GetBucketMetadataTableConfiguration.md") (V1 API operation)
- [GetBucketMetricsConfiguration](../API/API_GetBucketMetricsConfiguration.md "../API/API_GetBucketMetricsConfiguration.md")
- [GetBucketNotification](../API/API_GetBucketNotification.md "../API/API_GetBucketNotification.md")
- [GetBucketObjectLockConfiguration](../API/API_GetObjectLockConfiguration.md "../API/API_GetObjectLockConfiguration.md")
- [GetBucketOwnershipControls](../API/API_GetBucketOwnershipControls.md "../API/API_GetBucketOwnershipControls.md")
- [GetBucketPolicy](../API/API_GetBucketPolicy.md "../API/API_GetBucketPolicy.md")
- [GetBucketPolicyStatus](../API/API_GetBucketPolicyStatus.md "../API/API_GetBucketPolicyStatus.md")
- [GetBucketPublicAccessBlock](../API/API_GetPublicAccessBlock.md "../API/API_GetPublicAccessBlock.md")
- [GetBucketReplication](../API/API_GetBucketReplication.md "../API/API_GetBucketReplication.md")
- [GetBucketRequestPayment](../API/API_GetBucketRequestPayment.md "../API/API_GetBucketRequestPayment.md")
- [GetBucketTagging](../API/API_GetBucketTagging.md "../API/API_GetBucketTagging.md")
- [GetBucketVersioning](../API/API_GetBucketVersioning.md "../API/API_GetBucketVersioning.md")
- [GetBucketWebsite](../API/API_GetBucketWebsite.md "../API/API_GetBucketWebsite.md")
- [HeadBucket](../API/API_HeadBucket.md "../API/API_HeadBucket.md")
- [ListBuckets](../API/API_ListBuckets.md "../API/API_ListBuckets.md")
- [PutAccelerateConfiguration](../API/API_PutBucketAccelerateConfiguration.md "../API/API_PutBucketAccelerateConfiguration.md")
- [PutBucketAcl](../API/API_PutBucketAcl.md "../API/API_PutBucketAcl.md")
- [PutBucketAnalyticsConfiguration](../API/API_PutBucketAnalyticsConfiguration.md "../API/API_PutBucketAnalyticsConfiguration.md")
- [PutBucketCors](../API/API_PutBucketCors.md "../API/API_PutBucketCors.md")
- [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md")
- [PutBucketIntelligentTieringConfiguration](../API/API_PutBucketIntelligentTieringConfiguration.md "../API/API_PutBucketIntelligentTieringConfiguration.md")
- [PutBucketInventoryConfiguration](../API/API_PutBucketInventoryConfiguration.md "../API/API_PutBucketInventoryConfiguration.md")
- [PutBucketLifecycle](../API/API_PutBucketLifecycle.md "../API/API_PutBucketLifecycle.md")
- [PutBucketLogging](../API/API_PutBucketLogging.md "../API/API_PutBucketLogging.md")
- [PutBucketMetricsConfiguration](../API/API_PutBucketMetricsConfiguration.md "../API/API_PutBucketMetricsConfiguration.md")
- [PutBucketNotification](../API/API_PutBucketNotification.md "../API/API_PutBucketNotification.md")
- [PutBucketObjectLockConfiguration](../API/API_PutObjectLockConfiguration.md "../API/API_PutObjectLockConfiguration.md")
- [PutBucketOwnershipControls](../API/API_PutBucketOwnershipControls.md "../API/API_PutBucketOwnershipControls.md")
- [PutBucketPolicy](../API/API_PutBucketPolicy.md "../API/API_PutBucketPolicy.md")
- [PutBucketPublicAccessBlock](../API/API_PutPublicAccessBlock.md "../API/API_PutPublicAccessBlock.md")
- [PutBucketReplication](../API/API_PutBucketReplication.md "../API/API_PutBucketReplication.md")
- [PutBucketRequestPayment](../API/API_PutBucketRequestPayment.md "../API/API_PutBucketRequestPayment.md")
- [PutBucketTagging](../API/API_PutBucketTagging.md "../API/API_PutBucketTagging.md")
- [PutBucketVersioning](../API/API_PutBucketVersioning.md "../API/API_PutBucketVersioning.md")
- [PutBucketWebsite](../API/API_PutBucketWebsite.md "../API/API_PutBucketWebsite.md")
- [UpdateBucketMetadataJournalTableConfiguration](../API/API_UpdateBucketMetadataJournalTableConfiguratione.md "../API/API_UpdateBucketMetadataJournalTableConfiguratione.md")
- [UpdateBucketMetadataInventoryTableConfiguration](../API/API_UpdateBucketMetadataInventoryTableConfiguration.md "../API/API_UpdateBucketMetadataInventoryTableConfiguration.md")

In addition to these API operations, you can also use the [OPTIONS
object](../API/RESTOPTIONSobject.md "../API/RESTOPTIONSobject.md") object-level action. This action is treated like a
bucket-level action in CloudTrail logging because the action checks the CORS
configuration of a bucket.

###### Note

The HeadBucket API is supported as an Amazon S3 data event in CloudTrail.

## Amazon S3 Express One Zone

bucket-level (Regional API endpoint) actions tracked by CloudTrail logging

By default, CloudTrail logs bucket-level actions for directory buckets as management
events. The `eventsource` for CloudTrail management events for S3 Express One Zone
is `s3express.amazonaws.com`.

These following Regional endpoint API operations are logged to CloudTrail.

- [CreateBucket](../API/API_CreateBucket.md "../API/API_CreateBucket.md")
- [DeleteBucket](../API/API_DeleteBucket.md "../API/API_DeleteBucket.md")
- [DeleteBucketPolicy](../API/API_DeleteBucketPolicy.md "../API/API_DeleteBucketPolicy.md")
- [GetBucketPolicy](../API/API_GetBucketPolicy.md "../API/API_GetBucketPolicy.md")
- [PutBucketPolicy](../API/API_PutBucketPolicy.md "../API/API_PutBucketPolicy.md")
- [ListDirectoryBuckets](../API/API_ListDirectoryBuckets.md "../API/API_ListDirectoryBuckets.md")
- [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md")
- [GetBucketEncryption](../API/API_GetBucketEncryption.md "../API/API_GetBucketEncryption.md")
- [DeleteBucketEncryption](../API/API_DeleteBucketEncryption.md "../API/API_DeleteBucketEncryption.md")

For more information, see [Logging with AWS CloudTrail for S3 Express One Zone](s3-express-one-zone-logging.md "s3-express-one-zone-logging.md")

## Amazon S3 object-level actions

in cross-account scenarios

The following are special use cases involving the object-level API calls in
cross-account scenarios and how CloudTrail logs are reported. CloudTrail delivers logs to
the requester (the account that made the API call), except in some access denied
cases where log entries are redacted or omitted. When setting up cross-account
access, consider the examples in this section.

###### Note

The examples assume that CloudTrail logs are appropriately configured.

### Example 1: CloudTrail delivers

logs to the bucket owner

CloudTrail delivers logs to the bucket owner even if the bucket owner does not
have permissions for the same object API operation. Consider the following
cross-account scenario:

- Account A owns the bucket.
- Account B (the requester) tries to access an object in that
  bucket.
- Account C owns the object. Account C might or might not be the
  same account as Account A.

###### Note

CloudTrail always delivers object-level API logs to the requester (Account
B). In addition, CloudTrail also delivers the same logs to the bucket owner
(Account A) even when the bucket owner does not own the object (Account
C) or have permissions for those same API operations on that
object.

### Example 2: CloudTrail does not

proliferate email addresses that are used in setting object ACLs

Consider the following cross-account scenario:

- Account A owns the bucket.
- Account B (the requester) sends a request to set an object ACL
  grant by using an email address. For more information about ACLs,
  see [Access control list (ACL) overview](acl-overview.md "acl-overview.md").

The requester gets the logs along with the email information. However, the
bucket owner—if they are eligible to receive logs, as in example
1—gets the CloudTrail log reporting the event. However, the bucket owner
doesn't get the ACL configuration information, specifically the grantee
email address and the grant. The only information that the log tells the
bucket owner is that an ACL API call was made by Account B.
