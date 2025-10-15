# Document History

The following table describes the important changes in each release of the *Amazon Simple Storage Service API Reference* up to March 27, 2019. For changes after March 27, 2019, see the consolidated [Document History](https://docs.aws.amazon.com/AmazonS3/latest/dev/WhatsNew.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/WhatsNew.html") in the *Amazon Simple Storage Service User Guide*.


* **API version:** 2006-03-01
* **Latest documentation update:** March 27, 2019


| Change | Description | Release Date |
| --- | --- | --- |
| New archive storage class  | Amazon S3 now offers a new archive storage class, DEEP\_ARCHIVE, for storing rarely accessed objects.
 For more information, see [Storage Classes](../userguide/storage-class-intro.md "../userguide/storage-class-intro.md")
 in the *Amazon Simple Storage Service User Guide*.  | March 27, 2019 |
| Support for Parquet-formatted Amazon S3 inventory files | Amazon S3 now supports the [Apache Parquet
 (Parquet)](https://parquet.apache.org/ "https://parquet.apache.org/") format in addition to the [Apache optimized row columnar (ORC)](https://orc.apache.org/ "https://orc.apache.org/")
 and comma-separated values (CSV) file formats for inventory output files. For
 more information, see [Amazon S3
 Inventory](../userguide/storage-inventory.md "../userguide/storage-inventory.md") in the *Amazon Simple Storage Service User Guide*. 
The following APIs were updated accordingly:

* [GetBucketInventoryConfiguration](API_GetBucketInventoryConfiguration.md "API_GetBucketInventoryConfiguration.md")
* [PutBucketInventoryConfiguration](API_PutBucketInventoryConfiguration.md "API_PutBucketInventoryConfiguration.md")
 | December 04, 2018 |
| PUT directly to the GLACIER storage class | The Amazon S3 PUT and related operations now support specifying GLACIER 
 as the storage class when creating objects.
 Previously, you had to transition to the GLACIER storage class from 
 another Amazon S3 storage class. For more information about the GLACIER storage class, 
 see [Storage Classes](../userguide/storage-class-intro.md "../userguide/storage-class-intro.md")
 in the *Amazon Simple Storage Service User Guide*. 
The following APIs were updated accordingly:

* [PutObject](API_PutObject.md "API_PutObject.md")
* [POST Object](RESTObjectPOST.md "RESTObjectPOST.md")
* [CopyObject](API_CopyObject.md "API_CopyObject.md")
* [CreateMultipartUpload](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md")
 | November 26, 2018 |
| Object Lock | Amazon S3 now supports locking objects using a Write Once Read Many (WORM) model. You can
 lock objects for a definite period of time using a retention period or
 indefinitely using a legal hold. For more information about Amazon S3 Object
 Lock, see [Locking Objects](../userguide/object-lock.md "../userguide/object-lock.md")
 in the *Amazon Simple Storage Service User Guide*.The following APIs were
 updated for S3 Object Lock:

* [PutObject](API_PutObject.md "API_PutObject.md")
* [GetObject](API_GetObject.md "API_GetObject.md")
* [HeadObject](API_HeadObject.md "API_HeadObject.md")
* [CreateBucket](API_CreateBucket.md "API_CreateBucket.md")
* [HeadBucket](API_HeadBucket.md "API_HeadBucket.md")
 | November 26, 2018 |
| New storage class | Amazon S3 now offers a new storage class named INTELLIGENT\_TIERING that is for storing data
 that has changing or unknown access patterns. For more information, see
 [Storage
 Classes](../userguide/storage-class-intro.md "../userguide/storage-class-intro.md") in the *Amazon Simple Storage Service User Guide*. 
The following APIs were updated accordingly:

* [PutObject](API_PutObject.md "API_PutObject.md")
* [POST Object](RESTObjectPOST.md "RESTObjectPOST.md")
* [CopyObject](API_CopyObject.md "API_CopyObject.md")
* [CreateMultipartUpload](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md")
 | November 26, 2018 |
| Block Public Access | Amazon S3 now includes the ability to block public access to buckets and objects on a
 per-bucket or account-wide basis. For more information, see [Using
 Amazon S3 Block Public Access](../userguide/access-control-block-public-access.md "../userguide/access-control-block-public-access.md")  in the
 *Amazon Simple Storage Service User Guide*. | November 15, 2018 |
| Filtering enhancements in cross-region replication (CRR) rules | In a CRR rule configuration, you can specify an object filter to choose a subset of
 objects to apply the rule to. Previously, you could filter only on an
 object key prefix. In this release, you can filter on an object key
 prefix, one or more object tags, or both. For more information, see
 [Replication
 Configuration Overview](../userguide/replication-add-config.md "../userguide/replication-add-config.md") in the
 *Amazon Simple Storage Service User Guide*.
The following APIs are updated accordingly:

* [PutBucketReplication](API_PutBucketReplication.md "API_PutBucketReplication.md")
* [GetBucketReplication](API_GetBucketReplication.md "API_GetBucketReplication.md")
* [DeleteBucketReplication](API_DeleteBucketReplication.md "API_DeleteBucketReplication.md")
 | September 19, 2018 |
| New storage class  | Amazon S3 now offers a new storage class, ONEZONE\_IA (IA, for infrequent
 access) for storing objects. For more information, see [Storage Classes](../userguide/storage-class-intro.md "../userguide/storage-class-intro.md")
 in the *Amazon Simple Storage Service User Guide*.  | April 4, 2018 |
| Amazon S3 Select | Amazon S3 Select is now generally available. This feature retrieves object
 content based on an SQL expression. For more information, see  [Selecting Content from
 Objects](../userguide/selecting-content-from-objects.md "../userguide/selecting-content-from-objects.md") in the *Amazon Simple Storage Service User Guide*.
The following API has been updated:

* [SelectObjectContent](API_SelectObjectContent.md "API_SelectObjectContent.md")
 | April 4, 2018 |
| Asia Pacific (Osaka-Local) Region | Amazon S3 is now available in the Asia Pacific (Osaka-Local) Region. 
 For more information about Amazon S3 Regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the
 *AWS General Reference*.
ImportantYou can use the Asia Pacific (Osaka-Local) Region only in conjunction with the 
 Asia Pacific (Tokyo) Region. To request access to Asia Pacific (Osaka-Local) Region, 
 contact your sales representative. | February 12, 2018 |
| Europe (Paris) Region | Amazon S3 is now available in the Europe (Paris) Region. 
 For more information about Amazon S3 regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the
 *AWS General Reference*. | December 18, 2017 |
| China (Ningxia) Region | Amazon S3 is now available in the China (Ningxia) Region. 
 For more information about Amazon S3 regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the
 *AWS General Reference*. | December 11, 2017 |
| Querying archives with SQL | Amazon S3 now supports querying Amazon Glacier data archives with SQL. For more information, see  [Querying Archived
 Objects](../userguide/querying-glacier-archives.md "../userguide/querying-glacier-archives.md") in the *Amazon Simple Storage Service User Guide*. 
The following API changed:

* [RestoreObject](API_RestoreObject.md "API_RestoreObject.md")
 | November 29, 2017 |
| SELECT Object Content (Preview) | Amazon S3 now supports the SELECT Object Content functionality as part of a Preview program.
 This feature retrieves object content based on an SQL expression.
The following API has been added:

* [SelectObjectContent](API_SelectObjectContent.md "API_SelectObjectContent.md")
 | November 29, 2017 |
| Support for ORC-formatted Amazon S3 inventory files | Amazon S3 now supports the [Apache optimized row columnar (ORC)](https://orc.apache.org/ "https://orc.apache.org/") 
 format in addition to comma-separated values (CSV) file format for inventory 
 output files. For more information, see [Amazon S3 Inventory](../userguide/storage-inventory.md "../userguide/storage-inventory.md") in
 the *Amazon Simple Storage Service User Guide*.
The following APIs are updated accordingly:

* [GetBucketInventoryConfiguration](API_GetBucketInventoryConfiguration.md "API_GetBucketInventoryConfiguration.md")
* [PutBucketInventoryConfiguration](API_PutBucketInventoryConfiguration.md "API_PutBucketInventoryConfiguration.md")
 | November 17, 2017 |
| Default encryption for S3 buckets | Amazon S3 default encryption provides a way to set the default encryption behavior for an S3
 bucket. You can set default encryption on a bucket so that all objects
 are encrypted when they are stored in the bucket. The objects are
 encrypted using server-side encryption with either Amazon S3-managed keys
 (SSE-S3) or AWS KMS-managed keys (SSE-KMS). For more information, see
 [Amazon S3 Default
 Encryption for S3 Buckets](../userguide/bucket-encryption.md "../userguide/bucket-encryption.md") in the
 *Amazon Simple Storage Service User Guide*.
The following APIs are updated accordingly:

* [DeleteBucketEncryption](API_DeleteBucketEncryption.md "API_DeleteBucketEncryption.md")
* [GetBucketEncryption](API_GetBucketEncryption.md "API_GetBucketEncryption.md")
* [PutBucketEncryption](API_PutBucketEncryption.md "API_PutBucketEncryption.md")
 | November 06, 2017 |
| Encryption status in Amazon S3 inventory | Amazon S3 now supports including encryption status in Amazon S3 inventory so you can see how your
 objects are encrypted at rest for compliance auditing or other purposes.
 You can also configure to encrypt Amazon S3 inventory with server-side
 encryption (SSE) or SSE-KMS so that all inventory files are encrypted
 accordingly. For more information, see [Amazon S3 Inventory](../userguide/storage-inventory.md "../userguide/storage-inventory.md") in
 the *Amazon Simple Storage Service User Guide*. 
The following APIs are updated accordingly:

* [GetBucketInventoryConfiguration](API_GetBucketInventoryConfiguration.md "API_GetBucketInventoryConfiguration.md")
* [PutBucketInventoryConfiguration](API_PutBucketInventoryConfiguration.md "API_PutBucketInventoryConfiguration.md")
 | November 06, 2017 |
| Cross-region replication (CRR) enhancements | Cross-region replication (CRR) now supports the following:

* In a cross-account scenario, you can add a CRR configuration to change replica
 ownership to the AWS account that owns the destination bucket.
 For more information, see [CRR: Change Replica
 Owner](../userguide/replication-change-owner.md "../userguide/replication-change-owner.md") in the *Amazon Simple Storage Service User Guide*.
* By default, Amazon S3 does not replicate objects in your source bucket that are created
 using server-side encryption using AWS KMS-managed keys. In your
 CRR configuration, you can now direct Amazon S3 to replicate these
 objects. For more information, see [CRR: Replicating Objects Created with SEE Using AWS
 KMS-Managed Encryption Keys](../userguide/replication-config-for-kms-objects.md "../userguide/replication-config-for-kms-objects.md") in the
 *Amazon Simple Storage Service User Guide*.

The following APIs are updated accordingly:

* [GetBucketReplication](API_GetBucketReplication.md "API_GetBucketReplication.md")
* [PutBucketReplication](API_PutBucketReplication.md "API_PutBucketReplication.md")
 | November 06, 2017 |
| Europe (London) Region | Amazon S3 is now available in the Europe (London) Region. 
 For more information about Amazon S3 regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the
 *AWS General Reference*. | December 13, 2016 |
| Canada (Central) Region | Amazon S3 is now available in the Canada (Central) Region. 
 For more information about Amazon S3 regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the
 *AWS General Reference*. | December 8, 2016 |
| Object tagging support | Amazon S3 now supports object tagging. The following new API operations support object tagging:

* [PutObjectTagging](API_PutObjectTagging.md "API_PutObjectTagging.md")
* [GetObjectTagging](API_GetObjectTagging.md "API_GetObjectTagging.md")
* [DeleteObjectTagging](API_DeleteObjectTagging.md "API_DeleteObjectTagging.md")

In addition, other API operations are updated to support object tagging. For more information, see
 [Object Tagging](../userguide/object-tagging.md "../userguide/object-tagging.md")
 in the *Amazon Simple Storage Service User Guide*.  | November 29, 2016 |
| S3 lifecycle now supports object tag based filter | Amazon S3 now supports tag-based filtering in lifecycle configuration. You can now specify a
 lifecycle rule, in which you can specify a key prefix, one or more
 object tags, or a combination of both, to select a subset of objects to
 which the lifecycle rule applies. For more information, see [Object Lifecycle
 Management](../userguide/object-lifecycle-mgmt.md "../userguide/object-lifecycle-mgmt.md")in the *Amazon Simple Storage Service User Guide*.
Amazon S3 now supports Expedited and Bulk data retrievals in addition to Standard retrievals
 when restoring objects archived to Amazon Glacier.  | November 29, 2016 |
| CloudWatch request metrics for buckets  | Amazon S3 now supports CloudWatch metrics for requests made on buckets. The following new API operations support configuring request metrics:

* [DeleteBucketMetricsConfiguration](API_DeleteBucketMetricsConfiguration.md "API_DeleteBucketMetricsConfiguration.md")
* [GetBucketMetricsConfiguration](API_GetBucketMetricsConfiguration.md "API_GetBucketMetricsConfiguration.md")
* [PutBucketMetricsConfiguration](API_PutBucketMetricsConfiguration.md "API_PutBucketMetricsConfiguration.md")
* [ListBucketMetricsConfigurations](API_ListBucketMetricsConfigurations.md "API_ListBucketMetricsConfigurations.md")

For more information, see
 [Monitoring Metrics with Amazon CloudWatch](../userguide/cloudwatch-monitoring.md "../userguide/cloudwatch-monitoring.md")
 in the *Amazon Simple Storage Service User Guide*.  | November 29, 2016 |
| Amazon S3 Inventory | Amazon S3 now supports storage inventory. Amazon S3 inventory provides a flat-file output of
 your objects and their corresponding metadata on a daily or weekly basis
 for an S3 bucket or a shared prefix (that is, objects that have names that begin
 with a common string).
The following new API operations are for storage inventory:

* [DeleteBucketInventoryConfiguration](API_DeleteBucketInventoryConfiguration.md "API_DeleteBucketInventoryConfiguration.md")
* [GetBucketInventoryConfiguration](API_GetBucketInventoryConfiguration.md "API_GetBucketInventoryConfiguration.md")
* [PutBucketInventoryConfiguration](API_PutBucketInventoryConfiguration.md "API_PutBucketInventoryConfiguration.md")
* [ListBucketInventoryConfigurations](API_ListBucketInventoryConfigurations.md "API_ListBucketInventoryConfigurations.md")

For more information, see
 [Amazon S3 Storage Inventory](../userguide/storage-inventory.md "../userguide/storage-inventory.md")
 in the *Amazon Simple Storage Service User Guide*.  | November 29, 2016 |
| Amazon S3 Analytics – Storage Class Analysis | The new Amazon S3 analytics – storage class analysis feature observes data access patterns to
 help you determine when to transition less frequently accessed STANDARD
 storage to the STANDARD\_IA (IA, for infrequent access) storage class. After
 storage class analysis observes the infrequent access patterns of a filtered
 set of data over a period of time, you can use the analysis results to help
 you improve your lifecycle configurations. This feature also includes a detailed
 daily analysis of your storage usage at the specified bucket, prefix, or tag
 level that you can export to a S3 bucket.The following new API
 operations are for storage class analysis:
* [DeleteBucketAnalyticsConfiguration](API_DeleteBucketAnalyticsConfiguration.md "API_DeleteBucketAnalyticsConfiguration.md")
* [GetBucketAnalyticsConfiguration](API_GetBucketAnalyticsConfiguration.md "API_GetBucketAnalyticsConfiguration.md")
* [PutBucketAnalyticsConfiguration](API_PutBucketAnalyticsConfiguration.md "API_PutBucketAnalyticsConfiguration.md")
* [ListBucketAnalyticsConfigurations](API_ListBucketAnalyticsConfigurations.md "API_ListBucketAnalyticsConfigurations.md")
For more information, see [Amazon S3 Analytics –
 Storage Class Analysis](../userguide/analytics-storage-class.md "../userguide/analytics-storage-class.md") in the
 *Amazon Simple Storage Service User Guide*.  | November 29, 2016 |
| Added Amazon Glacier retrieval options to [RestoreObject](API_RestoreObject.md "API_RestoreObject.md") | Amazon S3 now supports Expedited and Bulk data retrievals in addition to Standard retrievals
 when restoring objects archived to Amazon Glacier. For more information, see
 [Restoring Archived
 Objects](../userguide/restoring-objects.md "../userguide/restoring-objects.md") in the *Amazon Simple Storage Service User Guide*. | November 21, 2016 |
| US East (Ohio) Region | Amazon S3 is now available in the US East (Ohio) Region. 
 For more information about Amazon S3 regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the
 *AWS General Reference*. | October 17, 2016 |
| Asia Pacific (Mumbai) region | Amazon S3 is now available in the Asia Pacific (Mumbai) region. 
 For more information about Amazon S3 regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the
 *AWS General Reference*. | June 27, 2016 |
| GET Bucket (List Objects) API revised | The GET Bucket (List Objects) API has been revised. We recommend that you use the new version, GET Bucket (List Objects) version 2.
 For more information, see [ListObjectsV2](API_ListObjectsV2.md "API_ListObjectsV2.md"). | May 4, 2016 |
| Amazon S3 Transfer Acceleration | Amazon S3 Transfer Acceleration enables fast, easy, and secure transfers
 of files over long distances between your client and an S3 bucket. 
 Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations. 
 For more information, see 
 [Transfer Acceleration](../userguide/transfer-acceleration.md "../userguide/transfer-acceleration.md") in the
 *Amazon Simple Storage Service User Guide*.
 The following new API operations support Transfer Acceleration: 
 [GetBucketAccelerateConfiguration](API_GetBucketAccelerateConfiguration.md "API_GetBucketAccelerateConfiguration.md") and
 [PutBucketAccelerateConfiguration](API_PutBucketAccelerateConfiguration.md "API_PutBucketAccelerateConfiguration.md"). 
  | April 19, 2016 |
| Lifecycle support to remove expired object delete marker  | Lifecycle configuration expiration action now allows you to direct Amazon S3 to remove
 expired object delete markers in versioned bucket. For more information,
 see [Elements
 to Describe Lifecycle Actions](../userguide/intro-lifecycle-rules.md#intro-lifecycle-rules-actions "../userguide/intro-lifecycle-rules.md#intro-lifecycle-rules-actions") in the
 *Amazon Simple Storage Service User Guide*.

 | March 16, 2016 |
| Bucket lifecycle configuration now supports the action to cancel incomplete multipart uploads  | Bucket lifecycle configuration now supports the
 `AbortIncompleteMultipartUpload` action that you can use
 to direct Amazon S3 to cancel multipart uploads that don't complete
 within a specified number of days after being initiated. When a multipart
 upload becomes eligible for an abort operation, Amazon S3 deletes any uploaded parts 
 and cancels the multipart upload.
 The following API operations have been updated to support the new
 action:


* [PutBucketLifecycleConfiguration](API_PutBucketLifecycleConfiguration.md "API_PutBucketLifecycleConfiguration.md") – The XML
 configuration now allows you to specify the
 `AbortIncompleteMultipartUpload` action in a
 lifecycle configuration rule.
* [ListParts](API_ListParts.md "API_ListParts.md") and [CreateMultipartUpload](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md") – Both of these API operations now
 return two additional response headers
 (`x-amz-abort-date`, and
 `x-amz-abort-rule-id`) if the bucket has a
 lifecycle rule that specifies the
 `AbortIncompleteMultipartUpload` action.
 These headers in the response indicate when the initiated
 multipart upload will become eligible for an abort operation
 and which lifecycle rule is applicable.

For conceptual information, see the following topics in the
 *Amazon Simple Storage Service User Guide*:


* [Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle configuration](../userguide/mpuoverview.md#mpu-abort-incomplete-mpu-lifecycle-config "../userguide/mpuoverview.md#mpu-abort-incomplete-mpu-lifecycle-config")
* [Elements to Describe Lifecycle Actions](../userguide/intro-lifecycle-rules.md#intro-lifecycle-rules-actions "../userguide/intro-lifecycle-rules.md#intro-lifecycle-rules-actions")
 | March 16, 2016 |
| Amazon S3 Signature Version 4 now supports unsigned payloads | Amazon S3 Signature Version 4 now supports unsigned payloads when
 authenticating requests using the `Authorization` header. Because you don't
 sign the payload, it does not provide the same security that comes with payload
 signing, but it provides similar performance characteristics as signature
 version 2. For more information, see [Signature Calculations for the Authorization Header:
 Transferring Payload in a Single Chunk (AWS Signature Version 4)](sig-v4-header-based-auth.md "sig-v4-header-based-auth.md"). | January 15, 2016 |
| Asia Pacific (Seoul) region | Amazon S3 is now available in the Asia Pacific (Seoul) region. 
 For more information about Amazon S3 regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the
 *AWS General Reference*. | January 6, 2016 |
| Renamed the US Standard region  | Changed the region name string from US Standard to US East (N. Virginia). This is
 only a region name update, there is no change in the functionality. | December 11, 2015 |
| New storage class  | Amazon S3 now offers a new storage class, STANDARD\_IA (IA, for infrequent access) for storing
 objects. This storage class is optimized for long-lived and less
 frequently accessed data. For more information, see [Storage Classes](../userguide/storage-class-intro.md "../userguide/storage-class-intro.md") in the *Amazon Simple Storage Service User Guide*. 
Lifecycle configuration feature updates now allow you to transition objects to the
 STANDARD\_IA storage class. For more information, see [Object Lifecycle Management](../userguide/object-lifecycle-mgmt.md "../userguide/object-lifecycle-mgmt.md") in the *Amazon Simple Storage Service User Guide*.
Previously, the cross-region replication feature used the storage class 
 of the source object for object replicas. Now, when you configure cross-region 
 replication you can specify a storage class for the object replica created in the 
 destination bucket. For more information, see [Cross-Region Replication](../userguide/replication.md "../userguide/replication.md") in the *Amazon Simple Storage Service User Guide*. | September 16, 2015 |
| Event notifications | Amazon S3 event notifications have been updated to add notifications when objects are deleted 
 and to add filtering on object names with prefix and suffix matching.
 For the relevant API operations, see [PutBucketNotificationConfiguration](API_PutBucketNotificationConfiguration.md "API_PutBucketNotificationConfiguration.md"), and
 [GetBucketNotificationConfiguration](API_GetBucketNotificationConfiguration.md "API_GetBucketNotificationConfiguration.md").
 For more information,
 see [Configuring Amazon S3 Event Notifications](../userguide/NotificationHowTo.md "../userguide/NotificationHowTo.md")
 in the *Amazon Simple Storage Service User Guide*.  | July 28, 2015 |
| Cross-region replication | Amazon S3 now supports cross-region replication. Cross-region replication is the automatic,
 asynchronous copying of objects across buckets in different AWS Regions.
 For the relevant API operations, see [PutBucketReplication](API_PutBucketReplication.md "API_PutBucketReplication.md"), 
 [GetBucketReplication](API_GetBucketReplication.md "API_GetBucketReplication.md") and 
 [DeleteBucketReplication](API_DeleteBucketReplication.md "API_DeleteBucketReplication.md"). For more information,
 see [Enabling Cross-Region Replication](../userguide/replication.md "../userguide/replication.md") in the *Amazon Simple Storage Service User Guide*.  | March 24, 2015 |
| Event notifications | Amazon S3 now supports new event types and destinations in a bucket notification
 configuration. Prior to this release, Amazon S3 supported only the
 `s3:ReducedRedundancyLostObject`
 event type and an Amazon SNS topic as the destination. For more
 information about the new event types, go to [Setting Up Notification of
 Bucket Events](../userguide/NotificationHowTo.md "../userguide/NotificationHowTo.md") in the *Amazon Simple Storage Service User Guide*. For the relevant API operations, see [PutBucketNotificationConfiguration](API_PutBucketNotificationConfiguration.md "API_PutBucketNotificationConfiguration.md") and
 [GetBucketNotificationConfiguration](API_GetBucketNotificationConfiguration.md "API_GetBucketNotificationConfiguration.md"). | November 13, 2014 |
| Server-side encryption with AWS Key Management Service (KMS) | Amazon S3 now supports server-side encryption using AWS Key Management Service (KMS). With server-side encryption with KMS, you 
 manage the envelope key through KMS, and Amazon S3 calls KMS to access the envelope key within the permissions you set. 
 
For more information about server-side encryption with KMS, see [Protecting Data Using Server-Side Encryption with AWS Key Management Service](../userguide/UsingKMSEncryption.md "../userguide/UsingKMSEncryption.md") in the *Amazon Simple Storage Service User Guide*.
The following Amazon S3 REST API operations support headers related to KMS. 

* [PutObject](API_PutObject.md "API_PutObject.md")
* [CopyObject](API_CopyObject.md "API_CopyObject.md")
* [POST Object](RESTObjectPOST.md "RESTObjectPOST.md")
* [CreateMultipartUpload](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md")
* [UploadPart](API_UploadPart.md "API_UploadPart.md")
 | November 12, 2014 |
| Europe (Frankfurt) Region | Amazon S3 is now available in the Europe (Frankfurt) Region region. | October 23, 2014 |
| Server-side encryption with customer-provided encryption keys | Amazon S3 now supports server-side encryption using customer-provided encryption keys (SSE-C).
 Server-side encryption enables you to request Amazon S3 to encrypt your data
 at rest. When using SSE-C, Amazon S3 encrypts your objects with the custom encryption keys that you provide. 
 Since Amazon S3 performs the encryption for you, you get the benefits of using your own encryption 
 keys without the cost of writing or executing your own encryption code.
 
For more information about SSE-C, go to [Server-Side Encryption (Using Customer-Provided Encryption Keys)](../userguide/ServerSideEncryptionCustomerKeys.md "../userguide/ServerSideEncryptionCustomerKeys.md") 
 in the *Amazon Simple Storage Service User Guide*.
The following Amazon S3 REST API operations support headers related to SSE-C. 

* [GetObject](API_GetObject.md "API_GetObject.md")
* [HeadObject](API_HeadObject.md "API_HeadObject.md")
* [PutObject](API_PutObject.md "API_PutObject.md")
* [CopyObject](API_CopyObject.md "API_CopyObject.md")
* [POST Object](RESTObjectPOST.md "RESTObjectPOST.md")
* [CreateMultipartUpload](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md")
* [UploadPart](API_UploadPart.md "API_UploadPart.md")
* [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md")
 | June 12, 2014 |
| Lifecycle support for versioning | Prior to this release lifecycle configuration was supported only on nonversioned
 buckets. Now you can configure lifecycle on both the nonversioned and
 versioning-enabled buckets. 
For more information, go to [Object Lifecycle Management](../userguide/object-lifecycle-mgmt.md "../userguide/object-lifecycle-mgmt.md") in the *Amazon Simple Storage Service User Guide*. 
The related API operations, see [PutBucketLifecycleConfiguration](API_PutBucketLifecycleConfiguration.md "API_PutBucketLifecycleConfiguration.md"), 
 [GetBucketLifecycleConfiguration](API_GetBucketLifecycleConfiguration.md "API_GetBucketLifecycleConfiguration.md"), 
 and [DeleteBucketLifecycle](API_DeleteBucketLifecycle.md "API_DeleteBucketLifecycle.md").  | May 20, 2014 |
| Amazon S3 now supports Signature Version 4 | Amazon S3 now supports Signature Version 4 (SigV4) in all regions, the latest specification
 for how to sign and authenticate AWS requests. 
For more information, see [Authenticating Requests (AWS Signature Version
 4)](sig-v4-authenticating-requests.md "sig-v4-authenticating-requests.md"). | January 30, 2014 |
| Amazon S3 list actions now support `encoding-type` request parameter | The following Amazon S3 list actions now support `encoding-type` optional
 request parameter.
[ListObjects](API_ListObjects.md "API_ListObjects.md")
[ListObjectVersions](API_ListObjectVersions.md "API_ListObjectVersions.md")
[ListMultipartUploads](API_ListMultipartUploads.md "API_ListMultipartUploads.md")
[ListParts](API_ListParts.md "API_ListParts.md")
An object key can contain any Unicode character; however, the XML 1.0 parser cannot parse some
 characters, such as characters with an ASCII value from 0 to 10. For
 characters that are not supported in XML 1.0, you can add this parameter
 to request that Amazon S3 encode the keys in the response.  | November 1, 2013 |
| SOAP Support Over HTTP Deprecated | SOAP support over HTTP is deprecated, but it is still available over HTTPS. 
 New Amazon S3 features will not be supported for SOAP. We recommend that you use 
 either the REST API or the AWS SDKs. | September 19, 2013 |
| Root domain support for website hosting | Amazon S3 now supports hosting static websites at the root domain. Visitors to
 your website can access your site from their
 browser without specifying "www" in the web address (e.g.,
 "example.com"). Many customers already host static websites on Amazon S3
 that are accessible from a "www" subdomain (e.g., "www.example.com").
 Previously, to support root domain access, you needed to run your own
 web server to proxy root domain requests from browsers to your website
 on Amazon S3. Running a web server to proxy requests introduces additional
 costs, operational burden, and another potential point of failure. Now,
 you can take advantage of the high availability and durability of Amazon S3 for both
 "www" and root domain addresses.
For an example walkthrough, go to [Example: Setting Up a Static Website Using a Custom Domain](../userguide/website-hosting-custom-domain-walkthrough.md "../userguide/website-hosting-custom-domain-walkthrough.md") in the *Amazon Simple Storage Service User Guide*.
 For conceptual information, go to [Hosting Static Websites on
 Amazon S3](../userguide/WebsiteHosting.md "../userguide/WebsiteHosting.md") in the *Amazon Simple Storage Service User Guide*.  | December 27, 2012 |
| Support for Archiving Data to Amazon Glacier | Amazon S3 now supports a storage option that enables you to utilize Amazon Glacier's low-cost
 storage service for data archival. To archive objects, you define
 archival rules identifying objects and a timeline when you want Amazon S3 to
 archive these objects to Amazon Glacier. You can easily set the rules on a bucket
 using the Amazon S3 console or programmatically using the Amazon S3 API or AWS
 SDKs.To support data archival rules, Amazon S3 lifecycle
 management API has been updated. For more information, see [PutBucketLifecycleConfiguration](API_PutBucketLifecycleConfiguration.md "API_PutBucketLifecycleConfiguration.md"). 
After you archive objects, you must first restore a copy before you can access the data.
 Amazon S3 offers a new API for you to initiate a restore. For more
 information, see [RestoreObject](API_RestoreObject.md "API_RestoreObject.md").For conceptual information, go to [Object
 Lifecycle Management](../userguide/object-lifecycle-mgmt.md "../userguide/object-lifecycle-mgmt.md") in the
 *Amazon Simple Storage Service User Guide*. | November 13, 2012 |
| Support for Website Page Redirects | For a bucket that is configured as a website, Amazon S3 now supports redirecting a request for
 an object to another object in the same bucket or to an external URL.
 You can configure redirect by adding the
 `x-amz-website-redirect-location` metadata to the object. 
The object upload API operations [PutObject](API_PutObject.md "API_PutObject.md"), [CreateMultipartUpload](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md"), 
 and [POST Object](RESTObjectPOST.md "RESTObjectPOST.md") allow you
 to configure the `x-amz-website-redirect-location` object
 metadata.
For conceptual information, go to [How
 to Configure Website Page Redirects](../userguide/how-to-page-redirect.md "../userguide/how-to-page-redirect.md") in the
 *Amazon Simple Storage Service User Guide*. |  October 4, 2012  |
| Cross-Origin Resource Sharing (CORS) support | Amazon S3 now supports Cross-Origin Resource Sharing (CORS). CORS defines a way in which
 client web applications that are loaded in one domain can interact with or
 access resources in a different domain. With CORS support in Amazon S3, you
 can build rich client-side web applications on top of Amazon S3 and
 selectively allow cross-domain access to your Amazon S3 resources. For more
 information, see [Enabling Cross-Origin Resource Sharing](../userguide/cors.md "../userguide/cors.md") in the *Amazon Simple Storage Service User Guide*. | August 31, 2012 |
| Cost Allocation Tagging support  | Amazon S3 now supports cost allocation tagging, which allows you to label S3 buckets so you can more easily track
 their cost against projects or other criteria.
 For more information, see [Cost Allocation Tagging](../userguide/BucketBilling.md#CostAllocTagging "../userguide/BucketBilling.md#CostAllocTagging") in the 
 *Amazon Simple Storage Service User Guide*. | August 21, 2012 |
| Object Expiration support  | You can use Object Expiration to schedule automatic removal of data after a configured
 time period. You set object expiration by adding lifecycle configuration to
 a bucket. For more information, see [Transitioning Objects: General Considerations](../userguide/object-lifecycle-mgmt.md#lifecycle-transition-general-considerations "../userguide/object-lifecycle-mgmt.md#lifecycle-transition-general-considerations") 
 in the *Amazon Simple Storage Service User Guide*. | December 27, 2011 |
| New Region supported | Amazon S3 now supports the South America (São Paulo) region. For more
 information, see [Buckets and Regions](../userguide/UsingBucket.md#access-bucket-intro "../userguide/UsingBucket.md#access-bucket-intro") in the *Amazon Simple Storage Service User Guide*. | December 14, 2011 |
| Multi-Object Delete | Amazon S3 now supports Multi-Object Delete API that enables you to
 delete multiple objects in a single request. With this feature, you can
 remove large numbers of objects from Amazon S3 more quickly than using
 multiple individual DELETE requests. 
For more information about the API see, see [DeleteObjects](API_DeleteObjects.md "API_DeleteObjects.md").
For conceptual information about the delete operation, see 
 [Deleting Objects](../userguide/DeletingObjects.md "../userguide/DeletingObjects.md") in the *Amazon Simple Storage Service User Guide*. | December 7, 2011 |
| New region supported | Amazon S3 now supports the US West (Oregon) region. For more
 information, see [Buckets and
 Regions](../userguide/UsingBucket.md#access-bucket-intro "../userguide/UsingBucket.md#access-bucket-intro") in the *Amazon Simple Storage Service User Guide*. | November 8, 2011 |
| Server-side encryption support | Amazon S3 now supports server-side encryption. It enables you to request Amazon S3 to
 encrypt your data at rest, that is, encrypt your object data when Amazon
 S3 writes your data to disks in its data centers. To request server-side
 encryption, you must add the `x-amz-server-side-encryption`
 header to your request. To learn more about data encryption, go to
 [Using Data Encryption](../userguide/UsingEncryption.md "../userguide/UsingEncryption.md") in the *Amazon Simple Storage Service User Guide*. | October 17, 2011 |
| Multipart Upload API extended to enable copying objects up to 5 TB | Prior to this release, Amazon S3 API supported copying objects (see [CopyObject](API_CopyObject.md "API_CopyObject.md")) of up to
 5 GB in size. To enable copying objects larger than 5 GB, Amazon S3
 extends the multipart upload API with a new operation, `Upload Part
 (Copy)`. You can use this multipart upload operation to copy
 objects up to 5 TB in size. For conceptual information about multipart
 upload, go to [Uploading Objects Using Multipart Upload](../userguide/uploadobjusingmpu.md "../userguide/uploadobjusingmpu.md") in the *Amazon Simple Storage Service User Guide*. To learn more
 about the new API, see [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md").
 
  | June 21, 2011 |
| SOAP API calls over HTTP disabled | To increase security, SOAP API calls over HTTP are disabled. Authenticated and anonymous
 SOAP requests must be sent to Amazon S3 using SSL. | June 6, 2011 |
| Support for hosting static websites in Amazon S3 | Amazon S3 introduces enhanced support for hosting static websites. This includes support
 for index documents and custom error documents. When using these
 features, requests to the root of your bucket or a subfolder (e.g.,
 `http://mywebsite.com/subfolder`) returns your index
 document instead of the list of objects in your bucket. If an error is
 encountered, Amazon S3 returns your custom error message instead of an
 Amazon S3 error message. For API information to configure your bucket as
 a website, see the following sections:

* [PutBucketWebsite](API_PutBucketWebsite.md "API_PutBucketWebsite.md")
* [GetBucketWebsite](API_GetBucketWebsite.md "API_GetBucketWebsite.md")
* [DeleteBucketWebsite](API_DeleteBucketWebsite.md "API_DeleteBucketWebsite.md")

For conceptual overview, go to [Hosting Websites on Amazon S3](../userguide/WebsiteHosting.md "../userguide/WebsiteHosting.md") in the *Amazon Simple Storage Service User Guide*.  | February 17, 2011 |
| Response Header API Support | The GET Object REST API now allows you to change the response headers of the REST GET
 Object request for each request. That is, you can alter object metadata
 in the response, without altering the object itself. For more
 information, see [GetObject](API_GetObject.md "API_GetObject.md"). | January 14, 2011 |
| Large Object Support | Amazon S3 has increased the maximum size of an object you can store in an S3 bucket from
 5 GB to 5 TB. If you are using the REST API you can upload objects of up
 to 5 GB size in a single PUT operation. For larger objects, you must use
 the Multipart Upload REST API to upload objects in parts. For conceptual
 information, go to [Uploading Objects Using Multipart Upload](../userguide/uploadobjusingmpu.md "../userguide/uploadobjusingmpu.md") in the *Amazon Simple Storage Service User Guide*. For multipart
 upload API information, see [CreateMultipartUpload](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md"), [UploadPart](API_UploadPart.md "API_UploadPart.md"),
 [CompleteMultipartUpload](API_CompleteMultipartUpload.md "API_CompleteMultipartUpload.md"),
 [ListParts](API_ListParts.md "API_ListParts.md"), and 
 [ListMultipartUploads](API_ListMultipartUploads.md "API_ListMultipartUploads.md")
 | December 9, 2010 |
| Multipart upload | Multipart upload enables faster, more flexible uploads into Amazon S3. It allows you to
 upload a single object as a set of parts. For conceptual information,
 go to [Uploading Objects Using Multipart Upload](../userguide/uploadobjusingmpu.md "../userguide/uploadobjusingmpu.md") in the *Amazon Simple Storage Service User Guide*. For multipart
 upload API information, see [CreateMultipartUpload](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md"), [UploadPart](API_UploadPart.md "API_UploadPart.md"),
 [CompleteMultipartUpload](API_CompleteMultipartUpload.md "API_CompleteMultipartUpload.md"),
 [ListParts](API_ListParts.md "API_ListParts.md"), and [ListMultipartUploads](API_ListMultipartUploads.md "API_ListMultipartUploads.md")
 | November 10, 2010 |
| Notifications | The Amazon S3 notifications feature enables you to configure a bucket so
 that Amazon S3 publishes a message to an Amazon Simple Notification Service
 (SNS) topic when Amazon S3 detects a key event on a bucket. For more
 information, see [GET Bucket
 notification](API_GetBucketNotificationConfiguration.md "API_GetBucketNotificationConfiguration.md") and [PUT
 Bucket notification](API_GetBucketNotificationConfiguration.md "API_GetBucketNotificationConfiguration.md"). | July 14, 2010 |
| Bucket policies | Bucket policies is an access management system you use to set access
 permissions on buckets, objects, and sets of objects. This functionality
 supplements and in many cases replaces access control lists. | July 6, 2010 |
| Reduced Redundancy | Amazon S3 now enables you to reduce your storage costs by storing objects
 in Amazon S3 with reduced redundancy. For more information, see [PUT Object](API_PutObject.md "API_PutObject.md"). | May 12, 2010 |
| New region supported | Amazon S3 now supports the Asia Pacific (Singapore) region and therefore
 new location constraints. For more information, see [GET Bucket location](API_GetBucketLocation.md "API_GetBucketLocation.md") and [PUT Bucket](API_CreateBucket.md "API_CreateBucket.md"). | April 28, 2010 |
| Object Versioning | This release introduces object Versioning. All objects now have a key and
 a version. If you enable versioning for a bucket, Amazon S3 gives all
 objects added to a bucket a unique version ID. This feature enables you to
 recover from unintended overwrites and deletions. For more information, see
 [GET Object](API_GetObject.md "API_GetObject.md"), [DELETE Object](API_DeleteObject.md "API_DeleteObject.md"), [PUT Object](API_PutObject.md "API_PutObject.md"), [PUT Object Copy](API_CopyObject.md "API_CopyObject.md"), or [POST Object](RESTObjectPOST.md "RESTObjectPOST.md"). The SOAP API does not
 support versioned objects. | February 8, 2010 |
| New region supported | Amazon S3 now supports the US-West (Northern California) region. The new
 endpoint is `s3-us-west-1.amazonaws.com`. For more
 information, see [How to Select a Region for Your Buckets](../userguide/UsingBucket.md#access-bucket-intro "../userguide/UsingBucket.md#access-bucket-intro") in the *Amazon Simple Storage Service User Guide*. | December 2, 2009 |
| C# Library Support  | AWS now provides Amazon S3 C# libraries, sample code, tutorials, and
 other resources for software developers who prefer to build applications
 using language-specific API operations instead of REST or SOAP. These libraries
 provide basic functions (not included in the REST or SOAP APIs), such as
 request authentication, request retries, and error handling so that it's
 easier to get started. | November 11, 2009 |
| Technical documents reorganized | The API reference has been split out of the *Amazon S3
 Developer Guide*. Now, on the documentation landing 
 page, [Amazon 
 Simple Storage Service Documentation](https://aws.amazon.com/documentation/s3/ "https://aws.amazon.com/documentation/s3/"), you can select the 
 document you want to view. When viewing the documents
 online, the links in one document will take you, when appropriate, to one of
 the other guides. | September 16, 2009 |
