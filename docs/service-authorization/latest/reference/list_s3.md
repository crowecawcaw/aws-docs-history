

# Actions, resources, and condition keys for Amazon S3
<a name="list_s3"></a>

Amazon S3 (service prefix: `s3`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonS3/latest/API/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-overview.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/s3/s3.json) for this service.

**Topics**
+ [API operations defined by Amazon S3](#list_s3-operations)
+ [Actions defined by Amazon S3](#list_s3-actions-as-permissions)
+ [Permission-only actions for Amazon S3](#list_s3-permission-only-actions)
+ [Resource types defined by Amazon S3](#list_s3-resources-for-iam-policies)
+ [Condition keys for Amazon S3](#list_s3-policy-keys)

## API operations defined by Amazon S3
<a name="list_s3-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_s3-actions-as-permissions).




- **   AbortMultipartUpload  **
  - **SDK client:** s3
  - **IAM action:**  [s3:AbortMultipartUpload](#list_s3-action-AbortMultipartUpload)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3-object-lambda:AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CompleteMultipartUpload  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutObject](#list_s3-action-PutObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3-object-lambda:PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CopyObject  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObject](#list_s3-action-GetObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:GetObjectVersion](#list_s3-action-GetObjectVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:PutObject](#list_s3-action-PutObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutObjectAcl](#list_s3-action-PutObjectAcl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3:PutObjectLegalHold](#list_s3-action-PutObjectLegalHold)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutObjectRetention](#list_s3-action-PutObjectRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutObjectTagging](#list_s3-action-PutObjectTagging)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [s3-object-lambda:PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateBucket  **
  - **SDK client:** s3
  - **IAM action:**  [s3:CreateBucket](#list_s3-action-CreateBucket)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutBucketAcl](#list_s3-action-PutBucketAcl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3:PutBucketObjectLockConfiguration](#list_s3-action-PutBucketObjectLockConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutBucketOwnershipControls](#list_s3-action-PutBucketOwnershipControls)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3:PutBucketVersioning](#list_s3-action-PutBucketVersioning)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateBucketMetadataConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:CreateBucketMetadataTableConfiguration](#list_s3-action-CreateBucketMetadataTableConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:CreateNamespace](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateNamespace.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:CreateTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateTable.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:CreateTableBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateTableBucket.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:GetTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTable.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3tables:PutTableEncryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.html#s3-tables-actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:PutTablePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTablePolicy.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   CreateBucketMetadataTableConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:CreateBucketMetadataTableConfiguration](#list_s3-action-CreateBucketMetadataTableConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:CreateNamespace](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateNamespace.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:CreateTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateTable.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:GetTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTable.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3tables:PutTablePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTablePolicy.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   CreateMultipartUpload  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutObject](#list_s3-action-PutObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutObjectAcl](#list_s3-action-PutObjectAcl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3:PutObjectLegalHold](#list_s3-action-PutObjectLegalHold)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutObjectRetention](#list_s3-action-PutObjectRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutObjectTagging](#list_s3-action-PutObjectTagging)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [s3-object-lambda:PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteBucket  **
  - **SDK client:** s3
  - **IAM action:**  [s3:DeleteBucket](#list_s3-action-DeleteBucket) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketAnalyticsConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutAnalyticsConfiguration](#list_s3-action-PutAnalyticsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketCors  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketCORS](#list_s3-action-PutBucketCORS) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketEncryption  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutEncryptionConfiguration](#list_s3-action-PutEncryptionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketIntelligentTieringConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutIntelligentTieringConfiguration](#list_s3-action-PutIntelligentTieringConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketInventoryConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutInventoryConfiguration](#list_s3-action-PutInventoryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketLifecycle  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutLifecycleConfiguration](#list_s3-action-PutLifecycleConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketMetadataConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:DeleteBucketMetadataTableConfiguration](#list_s3-action-DeleteBucketMetadataTableConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketMetadataTableConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:DeleteBucketMetadataTableConfiguration](#list_s3-action-DeleteBucketMetadataTableConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketMetricsConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutMetricsConfiguration](#list_s3-action-PutMetricsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketOwnershipControls  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketOwnershipControls](#list_s3-action-PutBucketOwnershipControls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteBucketPolicy  **
  - **SDK client:** s3
  - **IAM action:**  [s3:DeleteBucketPolicy](#list_s3-action-DeleteBucketPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteBucketReplication  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutReplicationConfiguration](#list_s3-action-PutReplicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketTagging  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketTagging](#list_s3-action-PutBucketTagging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteBucketWebsite  **
  - **SDK client:** s3
  - **IAM action:**  [s3:DeleteBucketWebsite](#list_s3-action-DeleteBucketWebsite) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteObject  **
  - **SDK client:** s3
  - **IAM action:**  [s3:BypassGovernanceRetention](#list_s3-action-BypassGovernanceRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3:DeleteObject](#list_s3-action-DeleteObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:DeleteObjectVersion](#list_s3-action-DeleteObjectVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3-object-lambda:DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteObjectTagging  **
  - **SDK client:** s3
  - **IAM action:**  [s3:DeleteObjectTagging](#list_s3-action-DeleteObjectTagging)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [s3:DeleteObjectVersionTagging](#list_s3-action-DeleteObjectVersionTagging)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [s3-object-lambda:DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteObjects  **
  - **SDK client:** s3
  - **IAM action:**  [s3:BypassGovernanceRetention](#list_s3-action-BypassGovernanceRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3:DeleteObject](#list_s3-action-DeleteObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:DeleteObjectVersion](#list_s3-action-DeleteObjectVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeletePublicAccessBlock  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketPublicAccessBlock](#list_s3-action-PutBucketPublicAccessBlock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   GetBucketAccelerateConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetAccelerateConfiguration](#list_s3-action-GetAccelerateConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketAcl  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketAcl](#list_s3-action-GetBucketAcl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketAnalyticsConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetAnalyticsConfiguration](#list_s3-action-GetAnalyticsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketCors  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketCORS](#list_s3-action-GetBucketCORS) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketEncryption  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetEncryptionConfiguration](#list_s3-action-GetEncryptionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketIntelligentTieringConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetIntelligentTieringConfiguration](#list_s3-action-GetIntelligentTieringConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketInventoryConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetInventoryConfiguration](#list_s3-action-GetInventoryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketLifecycle  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetLifecycleConfiguration](#list_s3-action-GetLifecycleConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketLifecycleConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetLifecycleConfiguration](#list_s3-action-GetLifecycleConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3express:GetLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetBucketLocation  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketLocation](#list_s3-action-GetBucketLocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketLogging  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketLogging](#list_s3-action-GetBucketLogging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketMetadataConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketMetadataTableConfiguration](#list_s3-action-GetBucketMetadataTableConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketMetadataTableConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketMetadataTableConfiguration](#list_s3-action-GetBucketMetadataTableConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketMetricsConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetMetricsConfiguration](#list_s3-action-GetMetricsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketNotification  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketNotification](#list_s3-action-GetBucketNotification) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketNotificationConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketNotification](#list_s3-action-GetBucketNotification) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketOwnershipControls  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketOwnershipControls](#list_s3-action-GetBucketOwnershipControls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketPolicy  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketPolicy](#list_s3-action-GetBucketPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketPolicyStatus  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketPolicyStatus](#list_s3-action-GetBucketPolicyStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketReplication  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetReplicationConfiguration](#list_s3-action-GetReplicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketRequestPayment  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketRequestPayment](#list_s3-action-GetBucketRequestPayment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketTagging  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketTagging](#list_s3-action-GetBucketTagging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketVersioning  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketVersioning](#list_s3-action-GetBucketVersioning) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketWebsite  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketWebsite](#list_s3-action-GetBucketWebsite) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetObject  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObject](#list_s3-action-GetObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:GetObjectLegalHold](#list_s3-action-GetObjectLegalHold)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:GetObjectRetention](#list_s3-action-GetObjectRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:GetObjectTagging](#list_s3-action-GetObjectTagging)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:GetObjectVersion](#list_s3-action-GetObjectVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3-object-lambda:GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetObjectAcl  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObjectAcl](#list_s3-action-GetObjectAcl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:GetObjectVersionAcl](#list_s3-action-GetObjectVersionAcl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3-object-lambda:GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetObjectAttributes  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObject](#list_s3-action-GetObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:GetObjectVersion](#list_s3-action-GetObjectVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetObjectLegalHold  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObjectLegalHold](#list_s3-action-GetObjectLegalHold)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3-object-lambda:GetObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLegalHold.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetObjectLockConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketObjectLockConfiguration](#list_s3-action-GetBucketObjectLockConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetObjectRetention  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObjectRetention](#list_s3-action-GetObjectRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3-object-lambda:GetObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectRetention.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetObjectTagging  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObjectTagging](#list_s3-action-GetObjectTagging)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:GetObjectVersionTagging](#list_s3-action-GetObjectVersionTagging)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3-object-lambda:GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetObjectTorrent  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObject](#list_s3-action-GetObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPublicAccessBlock  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetBucketPublicAccessBlock](#list_s3-action-GetBucketPublicAccessBlock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   HeadBucket  **
  - **SDK client:** s3
  - **IAM action:**  [s3:ListBucket](#list_s3-action-ListBucket) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   HeadObject  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObject](#list_s3-action-GetObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:GetObjectLegalHold](#list_s3-action-GetObjectLegalHold)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:GetObjectRetention](#list_s3-action-GetObjectRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3-object-lambda:GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListBucketAnalyticsConfigurations  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetAnalyticsConfiguration](#list_s3-action-GetAnalyticsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBucketIntelligentTieringConfigurations  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetIntelligentTieringConfiguration](#list_s3-action-GetIntelligentTieringConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBucketInventoryConfigurations  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetInventoryConfiguration](#list_s3-action-GetInventoryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBucketMetricsConfigurations  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetMetricsConfiguration](#list_s3-action-GetMetricsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBuckets  **
  - **SDK client:** s3
  - **IAM action:**  [s3:ListAllMyBuckets](#list_s3-action-ListAllMyBuckets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMultipartUploads  **
  - **SDK client:** s3
  - **IAM action:**  [s3:ListBucketMultipartUploads](#list_s3-action-ListBucketMultipartUploads)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [s3-object-lambda:ListBucketMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListObjectVersions  **
  - **SDK client:** s3
  - **IAM action:**  [s3:ListBucketVersions](#list_s3-action-ListBucketVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListObjects  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObjectAcl](#list_s3-action-GetObjectAcl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:ListBucket](#list_s3-action-ListBucket)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [s3-object-lambda:ListBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListObjectsV2  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObjectAcl](#list_s3-action-GetObjectAcl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:ListBucket](#list_s3-action-ListBucket)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [s3-object-lambda:ListBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListParts  **
  - **SDK client:** s3
  - **IAM action:**  [s3:ListMultipartUploadParts](#list_s3-action-ListMultipartUploadParts)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [s3-object-lambda:ListMultipartUploadParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   PutBucketAccelerateConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutAccelerateConfiguration](#list_s3-action-PutAccelerateConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBucketAcl  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketAcl](#list_s3-action-PutBucketAcl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutBucketAnalyticsConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutAnalyticsConfiguration](#list_s3-action-PutAnalyticsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBucketCors  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketCORS](#list_s3-action-PutBucketCORS) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBucketEncryption  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutEncryptionConfiguration](#list_s3-action-PutEncryptionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBucketIntelligentTieringConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutIntelligentTieringConfiguration](#list_s3-action-PutIntelligentTieringConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBucketInventoryConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutInventoryConfiguration](#list_s3-action-PutInventoryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBucketLifecycle  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutLifecycleConfiguration](#list_s3-action-PutLifecycleConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBucketLifecycleConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutLifecycleConfiguration](#list_s3-action-PutLifecycleConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3express:PutLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutBucketLogging  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketLogging](#list_s3-action-PutBucketLogging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBucketMetricsConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutMetricsConfiguration](#list_s3-action-PutMetricsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBucketNotificationConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketNotification](#list_s3-action-PutBucketNotification) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBucketOwnershipControls  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketOwnershipControls](#list_s3-action-PutBucketOwnershipControls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutBucketPolicy  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketPolicy](#list_s3-action-PutBucketPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutBucketReplication  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutReplicationConfiguration](#list_s3-action-PutReplicationConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** s3.amazonaws.com / **Access level:** Write

- **   PutBucketRequestPayment  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketRequestPayment](#list_s3-action-PutBucketRequestPayment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBucketTagging  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketTagging](#list_s3-action-PutBucketTagging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   PutBucketVersioning  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketVersioning](#list_s3-action-PutBucketVersioning) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBucketWebsite  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketWebsite](#list_s3-action-PutBucketWebsite) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutObject  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutObject](#list_s3-action-PutObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutObjectAcl](#list_s3-action-PutObjectAcl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3:PutObjectLegalHold](#list_s3-action-PutObjectLegalHold)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutObjectRetention](#list_s3-action-PutObjectRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutObjectTagging](#list_s3-action-PutObjectTagging)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [s3-object-lambda:PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutObjectAcl  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutObjectAcl](#list_s3-action-PutObjectAcl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3:PutObjectVersionAcl](#list_s3-action-PutObjectVersionAcl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3-object-lambda:PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   PutObjectLegalHold  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutObjectLegalHold](#list_s3-action-PutObjectLegalHold)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3-object-lambda:PutObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLegalHold.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutObjectLockConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketObjectLockConfiguration](#list_s3-action-PutBucketObjectLockConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutObjectRetention  **
  - **SDK client:** s3
  - **IAM action:**  [s3:BypassGovernanceRetention](#list_s3-action-BypassGovernanceRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3:PutObjectRetention](#list_s3-action-PutObjectRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3-object-lambda:PutObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectRetention.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutObjectTagging  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutObjectTagging](#list_s3-action-PutObjectTagging)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [s3:PutObjectVersionTagging](#list_s3-action-PutObjectVersionTagging)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [s3-object-lambda:PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutPublicAccessBlock  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutBucketPublicAccessBlock](#list_s3-action-PutBucketPublicAccessBlock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RestoreObject  **
  - **SDK client:** s3
  - **IAM action:**  [s3:RestoreObject](#list_s3-action-RestoreObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3-object-lambda:RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   SelectObjectContent  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObject](#list_s3-action-GetObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UpdateBucketMetadataInventoryTableConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:UpdateBucketMetadataInventoryTableConfiguration](#list_s3-action-UpdateBucketMetadataInventoryTableConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:CreateNamespace](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateNamespace.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:CreateTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateTable.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:CreateTableBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateTableBucket.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:GetTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTable.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3tables:PutTableEncryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.html#s3-tables-actions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:PutTablePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTablePolicy.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   UpdateBucketMetadataJournalTableConfiguration  **
  - **SDK client:** s3
  - **IAM action:**  [s3:UpdateBucketMetadataJournalTableConfiguration](#list_s3-action-UpdateBucketMetadataJournalTableConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UploadPart  **
  - **SDK client:** s3
  - **IAM action:**  [s3:PutObject](#list_s3-action-PutObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3-object-lambda:PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UploadPartCopy  **
  - **SDK client:** s3
  - **IAM action:**  [s3:GetObject](#list_s3-action-GetObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:GetObjectVersion](#list_s3-action-GetObjectVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3:PutObject](#list_s3-action-PutObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AssociateAccessGrantsIdentityCenter  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:AssociateAccessGrantsIdentityCenter](#list_s3-action-AssociateAccessGrantsIdentityCenter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [sso:CreateApplication](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplication.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:PutApplicationAuthenticationMethod](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationAuthenticationMethod.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:PutApplicationGrant](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationGrant.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateAccessGrant  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:CreateAccessGrant](#list_s3-action-CreateAccessGrant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [identitystore:DescribeUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:DescribeApplication](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeApplication.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:DescribeInstance](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeInstance.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateAccessGrantsInstance  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:CreateAccessGrantsInstance](#list_s3-action-CreateAccessGrantsInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [sso:CreateApplication](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplication.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:DescribeInstance](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeInstance.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:PutApplicationAuthenticationMethod](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationAuthenticationMethod.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:PutApplicationGrant](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationGrant.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateAccessGrantsLocation  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:CreateAccessGrantsLocation](#list_s3-action-CreateAccessGrantsLocation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateAccessPoint  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:CreateAccessPoint](#list_s3-action-CreateAccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAccessPointForObjectLambda  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:CreateAccessPointForObjectLambda](#list_s3-action-CreateAccessPointForObjectLambda) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBucket  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:CreateBucket](#list_s3-action-CreateBucket)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutBucketAcl](#list_s3-action-PutBucketAcl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3:PutBucketObjectLockConfiguration](#list_s3-action-PutBucketObjectLockConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:PutBucketOwnershipControls](#list_s3-action-PutBucketOwnershipControls)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3:PutBucketVersioning](#list_s3-action-PutBucketVersioning)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateJob  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:CreateJob](#list_s3-action-CreateJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMultiRegionAccessPoint  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:CreateMultiRegionAccessPoint](#list_s3-action-CreateMultiRegionAccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateStorageLensGroup  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:CreateStorageLensGroup](#list_s3-action-CreateStorageLensGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3:TagResource](#list_s3-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAccessGrant  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteAccessGrant](#list_s3-action-DeleteAccessGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteAccessGrantsInstance  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteAccessGrantsInstance](#list_s3-action-DeleteAccessGrantsInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteAccessGrantsInstanceResourcePolicy  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteAccessGrantsInstanceResourcePolicy](#list_s3-action-DeleteAccessGrantsInstanceResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteAccessGrantsLocation  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteAccessGrantsLocation](#list_s3-action-DeleteAccessGrantsLocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteAccessPoint  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteAccessPoint](#list_s3-action-DeleteAccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccessPointForObjectLambda  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteAccessPointForObjectLambda](#list_s3-action-DeleteAccessPointForObjectLambda) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccessPointPolicy  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteAccessPointPolicy](#list_s3-action-DeleteAccessPointPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteAccessPointPolicyForObjectLambda  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteAccessPointPolicyForObjectLambda](#list_s3-action-DeleteAccessPointPolicyForObjectLambda) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteBucket  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteBucket](#list_s3-action-DeleteBucket) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketPolicy  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteBucketPolicy](#list_s3-action-DeleteBucketPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteBucketReplication  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutReplicationConfiguration](#list_s3-action-PutReplicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBucketTagging  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutBucketTagging](#list_s3-action-PutBucketTagging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteJobTagging  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteJobTagging](#list_s3-action-DeleteJobTagging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteMultiRegionAccessPoint  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteMultiRegionAccessPoint](#list_s3-action-DeleteMultiRegionAccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePublicAccessBlock  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutBucketPublicAccessBlock](#list_s3-action-PutBucketPublicAccessBlock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteStorageLensConfiguration  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteStorageLensConfiguration](#list_s3-action-DeleteStorageLensConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStorageLensConfigurationTagging  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteStorageLensConfigurationTagging](#list_s3-action-DeleteStorageLensConfigurationTagging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteStorageLensGroup  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DeleteStorageLensGroup](#list_s3-action-DeleteStorageLensGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeJob  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DescribeJob](#list_s3-action-DescribeJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMultiRegionAccessPointOperation  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DescribeMultiRegionAccessPointOperation](#list_s3-action-DescribeMultiRegionAccessPointOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DissociateAccessGrantsIdentityCenter  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:DissociateAccessGrantsIdentityCenter](#list_s3-action-DissociateAccessGrantsIdentityCenter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [sso:DeleteApplication](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplication.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   GetAccessGrant  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetAccessGrant](#list_s3-action-GetAccessGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessGrantsInstance  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetAccessGrantsInstance](#list_s3-action-GetAccessGrantsInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessGrantsInstanceForPrefix  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetAccessGrantsInstanceForPrefix](#list_s3-action-GetAccessGrantsInstanceForPrefix) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessGrantsInstanceResourcePolicy  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetAccessGrantsInstanceResourcePolicy](#list_s3-action-GetAccessGrantsInstanceResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessGrantsLocation  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetAccessGrantsLocation](#list_s3-action-GetAccessGrantsLocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessPoint  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetAccessPoint](#list_s3-action-GetAccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessPointConfigurationForObjectLambda  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetAccessPointConfigurationForObjectLambda](#list_s3-action-GetAccessPointConfigurationForObjectLambda) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessPointForObjectLambda  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetAccessPointForObjectLambda](#list_s3-action-GetAccessPointForObjectLambda) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessPointPolicy  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetAccessPointPolicy](#list_s3-action-GetAccessPointPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessPointPolicyForObjectLambda  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetAccessPointPolicyForObjectLambda](#list_s3-action-GetAccessPointPolicyForObjectLambda) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessPointPolicyStatus  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetAccessPointPolicyStatus](#list_s3-action-GetAccessPointPolicyStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessPointPolicyStatusForObjectLambda  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetAccessPointPolicyStatusForObjectLambda](#list_s3-action-GetAccessPointPolicyStatusForObjectLambda) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketLifecycleConfiguration  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetLifecycleConfiguration](#list_s3-action-GetLifecycleConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [s3express:GetLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetBucketPolicy  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetBucketPolicy](#list_s3-action-GetBucketPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketReplication  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetReplicationConfiguration](#list_s3-action-GetReplicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketTagging  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetBucketTagging](#list_s3-action-GetBucketTagging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketVersioning  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetBucketVersioning](#list_s3-action-GetBucketVersioning) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataAccess  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetDataAccess](#list_s3-action-GetDataAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJobTagging  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetJobTagging](#list_s3-action-GetJobTagging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMultiRegionAccessPoint  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetMultiRegionAccessPoint](#list_s3-action-GetMultiRegionAccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMultiRegionAccessPointPolicy  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetMultiRegionAccessPointPolicy](#list_s3-action-GetMultiRegionAccessPointPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMultiRegionAccessPointPolicyStatus  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetMultiRegionAccessPointPolicyStatus](#list_s3-action-GetMultiRegionAccessPointPolicyStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMultiRegionAccessPointRoutes  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetMultiRegionAccessPointRoutes](#list_s3-action-GetMultiRegionAccessPointRoutes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPublicAccessBlock  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetBucketPublicAccessBlock](#list_s3-action-GetBucketPublicAccessBlock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStorageLensConfiguration  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetStorageLensConfiguration](#list_s3-action-GetStorageLensConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStorageLensConfigurationTagging  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetStorageLensConfigurationTagging](#list_s3-action-GetStorageLensConfigurationTagging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStorageLensGroup  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:GetStorageLensGroup](#list_s3-action-GetStorageLensGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccessGrants  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:ListAccessGrants](#list_s3-action-ListAccessGrants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccessGrantsInstances  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:ListAccessGrantsInstances](#list_s3-action-ListAccessGrantsInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccessGrantsLocations  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:ListAccessGrantsLocations](#list_s3-action-ListAccessGrantsLocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccessPoints  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:ListAccessPoints](#list_s3-action-ListAccessPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccessPointsForObjectLambda  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:ListAccessPointsForObjectLambda](#list_s3-action-ListAccessPointsForObjectLambda) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCallerAccessGrants  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:ListCallerAccessGrants](#list_s3-action-ListCallerAccessGrants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobs  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:ListJobs](#list_s3-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMultiRegionAccessPoints  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:ListMultiRegionAccessPoints](#list_s3-action-ListMultiRegionAccessPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStorageLensConfigurations  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:ListStorageLensConfigurations](#list_s3-action-ListStorageLensConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStorageLensGroups  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:ListStorageLensGroups](#list_s3-action-ListStorageLensGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:ListTagsForResource](#list_s3-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAccessGrantsInstanceResourcePolicy  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutAccessGrantsInstanceResourcePolicy](#list_s3-action-PutAccessGrantsInstanceResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutAccessPointConfigurationForObjectLambda  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutAccessPointConfigurationForObjectLambda](#list_s3-action-PutAccessPointConfigurationForObjectLambda) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAccessPointPolicy  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutAccessPointPolicy](#list_s3-action-PutAccessPointPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutAccessPointPolicyForObjectLambda  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutAccessPointPolicyForObjectLambda](#list_s3-action-PutAccessPointPolicyForObjectLambda) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutBucketLifecycleConfiguration  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutLifecycleConfiguration](#list_s3-action-PutLifecycleConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3express:PutLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutBucketPolicy  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutBucketPolicy](#list_s3-action-PutBucketPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutBucketReplication  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutReplicationConfiguration](#list_s3-action-PutReplicationConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** s3.amazonaws.com / **Access level:** Write

- **   PutBucketTagging  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutBucketTagging](#list_s3-action-PutBucketTagging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   PutBucketVersioning  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutBucketVersioning](#list_s3-action-PutBucketVersioning) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutJobTagging  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutJobTagging](#list_s3-action-PutJobTagging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   PutMultiRegionAccessPointPolicy  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutMultiRegionAccessPointPolicy](#list_s3-action-PutMultiRegionAccessPointPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutPublicAccessBlock  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutBucketPublicAccessBlock](#list_s3-action-PutBucketPublicAccessBlock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutStorageLensConfiguration  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutStorageLensConfiguration](#list_s3-action-PutStorageLensConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutStorageLensConfigurationTagging  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:PutStorageLensConfigurationTagging](#list_s3-action-PutStorageLensConfigurationTagging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   SubmitMultiRegionAccessPointRoutes  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:SubmitMultiRegionAccessPointRoutes](#list_s3-action-SubmitMultiRegionAccessPointRoutes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:TagResource](#list_s3-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:UntagResource](#list_s3-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccessGrantsLocation  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:UpdateAccessGrantsLocation](#list_s3-action-UpdateAccessGrantsLocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateJobPriority  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:UpdateJobPriority](#list_s3-action-UpdateJobPriority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateJobStatus  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:UpdateJobStatus](#list_s3-action-UpdateJobStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStorageLensGroup  **
  - **SDK client:** s3control
  - **IAM action:**  [s3:UpdateStorageLensGroup](#list_s3-action-UpdateStorageLensGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon S3
<a name="list_s3-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)  **
  - **Description:** Grants permission to abort a multipart upload
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html)  **
  - **Description:** Grants permission to configure server access logs delivery to CloudWatch
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:deliverySourceArn](#list_s3-s3_deliverySourceArn)<br />[s3:logType](#list_s3-s3_logType)<br />[s3:resourceArnBeingAuthorized](#list_s3-s3_resourceArnBeingAuthorized)
  - **Access level:** Read

- **   [AssociateAccessGrantsIdentityCenter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AssociateAccessGrantsIdentityCenter.html)  **
  - **Description:** Grants permission to associate Access Grants identity center
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [BypassGovernanceRetention](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-managing.html#object-lock-managing-bypass)  **
  - **Description:** Grants permission to allow circumvention of governance-mode object retention settings
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:RequestObjectTag/<key>](#list_s3-s3_RequestObjectTag_key)<br />[s3:RequestObjectTagKeys](#list_s3-s3_RequestObjectTagKeys)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-acl](#list_s3-s3_x-amz-acl)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-copy-source](#list_s3-s3_x-amz-copy-source)<br />[s3:x-amz-grant-full-control](#list_s3-s3_x-amz-grant-full-control)<br />[s3:x-amz-grant-read](#list_s3-s3_x-amz-grant-read)<br />[s3:x-amz-grant-read-acp](#list_s3-s3_x-amz-grant-read-acp)<br />[s3:x-amz-grant-write](#list_s3-s3_x-amz-grant-write)<br />[s3:x-amz-grant-write-acp](#list_s3-s3_x-amz-grant-write-acp)<br />[s3:x-amz-metadata-directive](#list_s3-s3_x-amz-metadata-directive)<br />[s3:x-amz-server-side-encryption](#list_s3-s3_x-amz-server-side-encryption)<br />[s3:x-amz-server-side-encryption-aws-kms-key-id](#list_s3-s3_x-amz-server-side-encryption-aws-kms-key-id)<br />[s3:x-amz-server-side-encryption-customer-algorithm](#list_s3-s3_x-amz-server-side-encryption-customer-algorithm)<br />[s3:x-amz-storage-class](#list_s3-s3_x-amz-storage-class)<br />[s3:x-amz-website-redirect-location](#list_s3-s3_x-amz-website-redirect-location)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:RequestObjectTag/<key>](#list_s3-s3_RequestObjectTag_key)<br />[s3:RequestObjectTagKeys](#list_s3-s3_RequestObjectTagKeys)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-acl](#list_s3-s3_x-amz-acl)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-copy-source](#list_s3-s3_x-amz-copy-source)<br />[s3:x-amz-grant-full-control](#list_s3-s3_x-amz-grant-full-control)<br />[s3:x-amz-grant-read](#list_s3-s3_x-amz-grant-read)<br />[s3:x-amz-grant-read-acp](#list_s3-s3_x-amz-grant-read-acp)<br />[s3:x-amz-grant-write](#list_s3-s3_x-amz-grant-write)<br />[s3:x-amz-grant-write-acp](#list_s3-s3_x-amz-grant-write-acp)<br />[s3:x-amz-metadata-directive](#list_s3-s3_x-amz-metadata-directive)<br />[s3:x-amz-server-side-encryption](#list_s3-s3_x-amz-server-side-encryption)<br />[s3:x-amz-server-side-encryption-aws-kms-key-id](#list_s3-s3_x-amz-server-side-encryption-aws-kms-key-id)<br />[s3:x-amz-server-side-encryption-customer-algorithm](#list_s3-s3_x-amz-server-side-encryption-customer-algorithm)<br />[s3:x-amz-storage-class](#list_s3-s3_x-amz-storage-class)<br />[s3:x-amz-website-redirect-location](#list_s3-s3_x-amz-website-redirect-location)
  - **Access level:** Permissions management, Write

- **   [CreateAccessGrant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrant.html)  **
  - **Description:** Grants permission to create Access Grant
  - **Resource types (\*required):** [accessgrant\*](#list_s3-resource-accessgrant)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:AccessGrantScope](#list_s3-s3_AccessGrantScope)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [CreateAccessGrantsInstance](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsInstance.html)  **
  - **Description:** Grants permission to Create Access Grants Instance
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [CreateAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsLocation.html)  **
  - **Description:** Grants permission to create Access Grants location
  - **Resource types (\*required):** [accessgrantslocation\*](#list_s3-resource-accessgrantslocation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:AccessGrantsLocationScope](#list_s3-s3_AccessGrantsLocationScope)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [CreateAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html)  **
  - **Description:** Grants permission to create a new access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3-resource-accesspoint)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:locationconstraint](#list_s3-s3_locationconstraint)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-acl](#list_s3-s3_x-amz-acl)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [CreateAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html)  **
  - **Description:** Grants permission to create an object lambda enabled accesspoint
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)  **
  - **Description:** Grants permission to create a new bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:locationconstraint](#list_s3-s3_locationconstraint)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-acl](#list_s3-s3_x-amz-acl)<br />[s3:x-amz-bucket-namespace](#list_s3-s3_x-amz-bucket-namespace)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-grant-full-control](#list_s3-s3_x-amz-grant-full-control)<br />[s3:x-amz-grant-read](#list_s3-s3_x-amz-grant-read)<br />[s3:x-amz-grant-read-acp](#list_s3-s3_x-amz-grant-read-acp)<br />[s3:x-amz-grant-write](#list_s3-s3_x-amz-grant-write)<br />[s3:x-amz-grant-write-acp](#list_s3-s3_x-amz-grant-write-acp)<br />[s3:x-amz-object-ownership](#list_s3-s3_x-amz-object-ownership)
  - **Access level:** Write

- **   [CreateBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html)  **
  - **Description:** Grants permission to create a new S3 Metadata configuration for a specified general purpose bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [CreateJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html)  **
  - **Description:** Grants permission to create a new Amazon S3 Batch Operations job
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:RequestJobOperation](#list_s3-s3_RequestJobOperation)<br />[s3:RequestJobPriority](#list_s3-s3_RequestJobPriority)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [CreateMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html)  **
  - **Description:** Grants permission to create a new Multi-Region Access Point
  - **Resource types (\*required):** [multiregionaccesspoint\*](#list_s3-resource-multiregionaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)
  - **Access level:** Write

- **   [CreateStorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateStorageLensGroup.html)  **
  - **Description:** Grants permission to create an Amazon S3 Storage Lens group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteAccessGrant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrant.html)  **
  - **Description:** Grants permission to delete Access Grant
  - **Resource types (\*required):** [accessgrant\*](#list_s3-resource-accessgrant)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:AccessGrantScope](#list_s3-s3_AccessGrantScope)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [DeleteAccessGrantsInstance](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsInstance.html)  **
  - **Description:** Grants permission to Delete Access Grants Instance
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [DeleteAccessGrantsInstanceResourcePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsInstanceResourcePolicy.html)  **
  - **Description:** Grants permission to read Access grants instance resource policy
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [DeleteAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsLocation.html)  **
  - **Description:** Grants permission to delete Access Grants location
  - **Resource types (\*required):** [accessgrantslocation\*](#list_s3-resource-accessgrantslocation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:AccessGrantsLocationScope](#list_s3-s3_AccessGrantsLocationScope)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html)  **
  - **Description:** Grants permission to delete the access point named in the URI
  - **Resource types (\*required):** [accesspoint\*](#list_s3-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html)  **
  - **Description:** Grants permission to delete the object lambda enabled access point named in the URI
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html)  **
  - **Description:** Grants permission to delete the policy on a specified access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [DeleteAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicyForObjectLambda.html)  **
  - **Description:** Grants permission to delete the policy on a specified object lambda enabled access point
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)  **
  - **Description:** Grants permission to delete the bucket named in the URI
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataConfiguration.html)  **
  - **Description:** Grants permission to delete the S3 Metadata configuration for a specified general purpose bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html)  **
  - **Description:** Grants permission to delete the policy on a specified bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [DeleteBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketWebsite.html)  **
  - **Description:** Grants permission to remove the website configuration for a bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteJobTagging.html)  **
  - **Description:** Grants permission to remove tags from an existing Amazon S3 Batch Operations job
  - **Resource types (\*required):** [job\*](#list_s3-resource-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ExistingJobOperation](#list_s3-s3_ExistingJobOperation)<br />[s3:ExistingJobPriority](#list_s3-s3_ExistingJobPriority)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [DeleteMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html)  **
  - **Description:** Grants permission to delete the Multi-Region Access Point named in the URI
  - **Resource types (\*required):** [multiregionaccesspoint\*](#list_s3-resource-multiregionaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)
  - **Access level:** Write

- **   [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)  **
  - **Description:** Grants permission to remove the null version of an object and insert a delete marker, which becomes the current version of the object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:if-match](#list_s3-s3_if-match)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:if-match](#list_s3-s3_if-match)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectAnnotation.html)  **
  - **Description:** Grants permission to delete an annotation from an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-object-if-match](#list_s3-s3_x-amz-object-if-match)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-object-if-match](#list_s3-s3_x-amz-object-if-match)
  - **Access level:** Write

- **   [DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)  **
  - **Description:** Grants permission to use the tagging subresource to remove the entire tag set from the specified object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [DeleteObjectVersion](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)  **
  - **Description:** Grants permission to remove a specific version of an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteObjectVersionAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectAnnotation.html)  **
  - **Description:** Grants permission to delete an annotation from a specific version of an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-object-if-match](#list_s3-s3_x-amz-object-if-match)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-object-if-match](#list_s3-s3_x-amz-object-if-match)
  - **Access level:** Write

- **   [DeleteObjectVersionTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)  **
  - **Description:** Grants permission to remove the entire tag set for a specific version of the object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [DeleteStorageLensConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensConfiguration.html)  **
  - **Description:** Grants permission to delete an existing Amazon S3 Storage Lens configuration
  - **Resource types (\*required):** [storagelensconfiguration\*](#list_s3-resource-storagelensconfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [DeleteStorageLensConfigurationTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensConfigurationTagging.html)  **
  - **Description:** Grants permission to remove tags from an existing Amazon S3 Storage Lens configuration
  - **Resource types (\*required):** [storagelensconfiguration\*](#list_s3-resource-storagelensconfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [DeleteStorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensGroup.html)  **
  - **Description:** Grants permission to delete an existing S3 Storage Lens group
  - **Resource types (\*required):** [storagelensgroup\*](#list_s3-resource-storagelensgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [DescribeJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html)  **
  - **Description:** Grants permission to retrieve the configuration parameters and status for a batch operations job
  - **Resource types (\*required):** [job\*](#list_s3-resource-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [DescribeMultiRegionAccessPointOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html)  **
  - **Description:** Grants permission to retrieve the configurations for a Multi-Region Access Point
  - **Resource types (\*required):** [multiregionaccesspointrequestarn\*](#list_s3-resource-multiregionaccesspointrequestarn)
  - **Condition keys:** [s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)
  - **Access level:** Read

- **   [DissociateAccessGrantsIdentityCenter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DissociateAccessGrantsIdentityCenter.html)  **
  - **Description:** Grants permission to disassociate Access Grants identity center
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [GetAccelerateConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAccelerateConfiguration.html)  **
  - **Description:** Grants permission to uses the accelerate subresource to return the Transfer Acceleration state of a bucket, which is either Enabled or Suspended
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessGrant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrant.html)  **
  - **Description:** Grants permission to read Access Grant
  - **Resource types (\*required):** [accessgrant\*](#list_s3-resource-accessgrant)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:AccessGrantScope](#list_s3-s3_AccessGrantScope)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessGrantsInstance](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstance.html)  **
  - **Description:** Grants permission to Read Access Grants Instance
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessGrantsInstanceForPrefix](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstanceForPrefix.html)  **
  - **Description:** Grants permission to Read Access Grants Instance by prefix
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessGrantsInstanceResourcePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstanceResourcePolicy.html)  **
  - **Description:** Grants permission to read Access grants instance resource policy
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsLocation.html)  **
  - **Description:** Grants permission to read Access Grants location
  - **Resource types (\*required):** [accessgrantslocation\*](#list_s3-resource-accessgrantslocation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:AccessGrantsLocationScope](#list_s3-s3_AccessGrantsLocationScope)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html)  **
  - **Description:** Grants permission to return configuration information about the specified access point
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessPointConfigurationForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointConfigurationForObjectLambda.html)  **
  - **Description:** Grants permission to retrieve the configuration of the object lambda enabled access point
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointForObjectLambda.html)  **
  - **Description:** Grants permission to create an object lambda enabled accesspoint
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html)  **
  - **Description:** Grants permission to return the access point policy associated with the specified access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyForObjectLambda.html)  **
  - **Description:** Grants permission to return the access point policy associated with the specified object lambda enabled access point
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessPointPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyStatus.html)  **
  - **Description:** Grants permission to return the policy status for a specific access point policy
  - **Resource types (\*required):** [accesspoint\*](#list_s3-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccessPointPolicyStatusForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyStatusForObjectLambda.html)  **
  - **Description:** Grants permission to return the policy status for a specific object lambda access point policy
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAccountPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetPublicAccessBlock.html)  **
  - **Description:** Grants permission to retrieve the PublicAccessBlock configuration for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:** [s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAnalyticsConfiguration.html)  **
  - **Description:** Grants permission to get an analytics configuration from an Amazon S3 bucket, identified by the analytics configuration ID
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketAbac](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAbac.html)  **
  - **Description:** Grants permission to retrieve ABAC configuration for a general purpose bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html)  **
  - **Description:** Grants permission to use the acl subresource to return the access control list (ACL) of an Amazon S3 bucket
  - **Resource types (\*required):** [accesspoint](#list_s3-resource-accesspoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketCORS](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html)  **
  - **Description:** Grants permission to return the CORS configuration information set for an Amazon S3 bucket
  - **Resource types (\*required):** [accesspoint](#list_s3-resource-accesspoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html)  **
  - **Description:** Grants permission to return the Region that an Amazon S3 bucket resides in
  - **Resource types (\*required):** [accesspoint](#list_s3-resource-accesspoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketLogging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLogging.html)  **
  - **Description:** Grants permission to return the logging status of an Amazon S3 bucket and the permissions users have to view or modify that status
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataConfiguration.html)  **
  - **Description:** Grants permission to return the S3 Metadata configuration for a specified general purpose bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketNotification](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotification.html)  **
  - **Description:** Grants permission to get the notification configuration of an Amazon S3 bucket
  - **Resource types (\*required):** [accesspoint](#list_s3-resource-accesspoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketObjectLockConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLockConfiguration.html)  **
  - **Description:** Grants permission to get the Object Lock configuration of an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)
  - **Access level:** Read

- **   [GetBucketOwnershipControls](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketOwnershipControls.html)  **
  - **Description:** Grants permission to retrieve ownership controls on a bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html)  **
  - **Description:** Grants permission to return the policy of the specified bucket
  - **Resource types (\*required):** [accesspoint](#list_s3-resource-accesspoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html)  **
  - **Description:** Grants permission to retrieve the policy status for a specific Amazon S3 bucket, which indicates whether the bucket is public
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html)  **
  - **Description:** Grants permission to retrieve the PublicAccessBlock configuration for an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketRequestPayment](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketRequestPayment.html)  **
  - **Description:** Grants permission to return the request payment configuration for an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html)  **
  - **Description:** Grants permission to return the tag set associated with an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html)  **
  - **Description:** Grants permission to return the versioning state of an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketWebsite.html)  **
  - **Description:** Grants permission to return the website configuration for an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetDataAccess](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetDataAccess.html)  **
  - **Description:** Grants permission to get Access
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetEncryptionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html)  **
  - **Description:** Grants permission to return the default encryption configuration an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketIntelligentTieringConfiguration.html)  **
  - **Description:** Grants permission to get an or list all Amazon S3 Intelligent Tiering configuration in a S3 Bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html)  **
  - **Description:** Grants permission to return an inventory configuration from an Amazon S3 bucket, identified by the inventory configuration ID
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetJobTagging.html)  **
  - **Description:** Grants permission to return the tag set of an existing Amazon S3 Batch Operations job
  - **Resource types (\*required):** [job\*](#list_s3-resource-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)  **
  - **Description:** Grants permission to return the lifecycle configuration information set on an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetricsConfiguration.html)  **
  - **Description:** Grants permission to get a metrics configuration from an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html)  **
  - **Description:** Grants permission to return configuration information about the specified Multi-Region Access Point
  - **Resource types (\*required):** [multiregionaccesspoint\*](#list_s3-resource-multiregionaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)
  - **Access level:** Read

- **   [GetMultiRegionAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicy.html)  **
  - **Description:** Grants permission to return the access point policy associated with the specified Multi-Region Access Point
  - **Resource types (\*required):** [multiregionaccesspoint\*](#list_s3-resource-multiregionaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)
  - **Access level:** Read

- **   [GetMultiRegionAccessPointPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicyStatus.html)  **
  - **Description:** Grants permission to return the policy status for a specific Multi-Region Access Point policy
  - **Resource types (\*required):** [multiregionaccesspoint\*](#list_s3-resource-multiregionaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)
  - **Access level:** Read

- **   [GetMultiRegionAccessPointRoutes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointRoutes.html)  **
  - **Description:** Grants permission to return the route configuration for a Multi-Region Access Point
  - **Resource types (\*required):** [multiregionaccesspoint\*](#list_s3-resource-multiregionaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)
  - **Access level:** Read

- **   [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)  **
  - **Description:** Grants permission to retrieve objects from Amazon S3
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html)  **
  - **Description:** Grants permission to return the access control list (ACL) of an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAnnotation.html)  **
  - **Description:** Grants permission to retrieve an annotation from an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)  **
  - **Description:** Grants permission to retrieve attributes related to a specific object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLegalHold.html)  **
  - **Description:** Grants permission to get an object's current Legal Hold status
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectRetention.html)  **
  - **Description:** Grants permission to retrieve the retention settings for an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html)  **
  - **Description:** Grants permission to return the tag set of an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectTorrent](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTorrent.html)  **
  - **Description:** Grants permission to return torrent files from an Amazon S3 bucket
  - **Resource types (\*required):** [object\*](#list_s3-resource-object)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectVersion](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)  **
  - **Description:** Grants permission to retrieve a specific version of an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectVersionAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html)  **
  - **Description:** Grants permission to return the access control list (ACL) of a specific object version
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectVersionAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAnnotation.html)  **
  - **Description:** Grants permission to retrieve an annotation from a specific version of an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectVersionAnnotationForReplication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html)  **
  - **Description:** Grants permission to get an object version annotation for replication
  - **Resource types (\*required):** [object\*](#list_s3-resource-object)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectVersionAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)  **
  - **Description:** Grants permission to retrieve attributes related to a specific version of an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectVersionForReplication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-config-for-kms-objects.html)  **
  - **Description:** Grants permission to replicate both unencrypted objects and objects encrypted with SSE-S3 or SSE-KMS
  - **Resource types (\*required):** [object\*](#list_s3-resource-object)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectVersionTagging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html)  **
  - **Description:** Grants permission to return the tag set for a specific version of the object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetObjectVersionTorrent](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTorrent.html)  **
  - **Description:** Grants permission to get Torrent files about a different version using the versionId subresource
  - **Resource types (\*required):** [object\*](#list_s3-resource-object)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetReplicationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketReplication.html)  **
  - **Description:** Grants permission to get the replication configuration information set on an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetStorageLensConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensConfiguration.html)  **
  - **Description:** Grants permission to get an Amazon S3 Storage Lens configuration
  - **Resource types (\*required):** [storagelensconfiguration\*](#list_s3-resource-storagelensconfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetStorageLensConfigurationTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensConfigurationTagging.html)  **
  - **Description:** Grants permission to get the tag set of an existing Amazon S3 Storage Lens configuration
  - **Resource types (\*required):** [storagelensconfiguration\*](#list_s3-resource-storagelensconfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetStorageLensDashboard](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_dashboard.html)  **
  - **Description:** Grants permission to get an Amazon S3 Storage Lens dashboard
  - **Resource types (\*required):** [storagelensconfiguration\*](#list_s3-resource-storagelensconfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [GetStorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensGroup.html)  **
  - **Description:** Grants permission to get an Amazon S3 Storage Lens group
  - **Resource types (\*required):** [storagelensgroup\*](#list_s3-resource-storagelensgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Read

- **   [ListAccessGrants](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrants.html)  **
  - **Description:** Grants permission to list Access Grant
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListAccessGrantsInstances](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsInstances.html)  **
  - **Description:** Grants permission to List Access Grants Instances
  - **Resource types (\*required):** 
  - **Condition keys:** [s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListAccessGrantsLocations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsLocations.html)  **
  - **Description:** Grants permission to list Access Grants locations
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html)  **
  - **Description:** Grants permission to list access points
  - **Resource types (\*required):** 
  - **Condition keys:** [s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListAccessPointsForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html)  **
  - **Description:** Grants permission to list object lambda enabled accesspoints
  - **Resource types (\*required):** 
  - **Condition keys:** [s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListAllMyBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html)  **
  - **Description:** Grants permission to list all buckets owned by the authenticated sender of the request
  - **Resource types (\*required):** 
  - **Condition keys:** [s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)  **
  - **Description:** Grants permission to list some or all of the objects in an Amazon S3 bucket (up to 1000)
  - **Resource types (\*required):** [accesspoint](#list_s3-resource-accesspoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:delimiter](#list_s3-s3_delimiter)<br />[s3:max-keys](#list_s3-s3_max-keys)<br />[s3:prefix](#list_s3-s3_prefix)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:delimiter](#list_s3-s3_delimiter)<br />[s3:max-keys](#list_s3-s3_max-keys)<br />[s3:prefix](#list_s3-s3_prefix)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListBucketMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html)  **
  - **Description:** Grants permission to list in-progress multipart uploads
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListBucketVersions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html)  **
  - **Description:** Grants permission to list metadata about all the versions of objects in an Amazon S3 bucket
  - **Resource types (\*required):** [accesspoint](#list_s3-resource-accesspoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:delimiter](#list_s3-s3_delimiter)<br />[s3:max-keys](#list_s3-s3_max-keys)<br />[s3:prefix](#list_s3-s3_prefix)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:delimiter](#list_s3-s3_delimiter)<br />[s3:max-keys](#list_s3-s3_max-keys)<br />[s3:prefix](#list_s3-s3_prefix)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListCallerAccessGrants](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListCallerAccessGrants.html)  **
  - **Description:** Grants permission to list caller's Access Grant
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListJobs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html)  **
  - **Description:** Grants permission to list current jobs and jobs that have ended recently
  - **Resource types (\*required):** 
  - **Condition keys:** [s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListMultiRegionAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html)  **
  - **Description:** Grants permission to list Multi-Region Access Points
  - **Resource types (\*required):** 
  - **Condition keys:** [s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)
  - **Access level:** List

- **   [ListMultipartUploadParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)  **
  - **Description:** Grants permission to list the parts that have been uploaded for a specific multipart upload
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListObjectAnnotations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectAnnotations.html)  **
  - **Description:** Grants permission to list annotations on an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:annotation-prefix](#list_s3-s3_annotation-prefix)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:max-annotation-results](#list_s3-s3_max-annotation-results)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:annotation-prefix](#list_s3-s3_annotation-prefix)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:max-annotation-results](#list_s3-s3_max-annotation-results)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListObjectVersionAnnotations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectAnnotations.html)  **
  - **Description:** Grants permission to list annotations on a specific version of an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:annotation-prefix](#list_s3-s3_annotation-prefix)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:max-annotation-results](#list_s3-s3_max-annotation-results)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:annotation-prefix](#list_s3-s3_annotation-prefix)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:max-annotation-results](#list_s3-s3_max-annotation-results)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListStorageLensConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensConfigurations.html)  **
  - **Description:** Grants permission to list Amazon S3 Storage Lens configurations
  - **Resource types (\*required):** 
  - **Condition keys:** [s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListStorageLensGroups](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensGroups.html)  **
  - **Description:** Grants permission to list S3 Storage Lens groups
  - **Resource types (\*required):** 
  - **Condition keys:** [s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags attached to the specified resource
  - **Resource types (\*required):** [accessgrant](#list_s3-resource-accessgrant) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [accessgrantsinstance](#list_s3-resource-accessgrantsinstance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [accessgrantslocation](#list_s3-resource-accessgrantslocation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [accesspoint](#list_s3-resource-accesspoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [storagelensgroup](#list_s3-resource-storagelensgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** List

- **   [ObjectOwnerOverrideToBucketOwner](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-change-owner.html#repl-ownership-add-role-permission)  **
  - **Description:** Grants permission to change replica ownership
  - **Resource types (\*required):** [object\*](#list_s3-resource-object)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutAccelerateConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAccelerateConfiguration.html)  **
  - **Description:** Grants permission to use the accelerate subresource to set the Transfer Acceleration state of an existing S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutAccessGrantsInstanceResourcePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessGrantsInstanceResourcePolicy.html)  **
  - **Description:** Grants permission to put Access grants instance resource policy
  - **Resource types (\*required):** [accessgrantsinstance\*](#list_s3-resource-accessgrantsinstance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutAccessPointConfigurationForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointConfigurationForObjectLambda.html)  **
  - **Description:** Grants permission to set the configuration of the object lambda enabled access point
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html)  **
  - **Description:** Grants permission to associate an access policy with a specified access point
  - **Resource types (\*required):** [accesspoint\*](#list_s3-resource-accesspoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicyForObjectLambda.html)  **
  - **Description:** Grants permission to associate an access policy with a specified object lambda enabled access point
  - **Resource types (\*required):** [objectlambdaaccesspoint\*](#list_s3-resource-objectlambdaaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutAccessPointPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html#access-control-block-public-access-examples-access-point)  **
  - **Description:** Grants permission to associate public access block configurations with a specified access point, while creating a access point
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [PutAccountPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutPublicAccessBlock.html)  **
  - **Description:** Grants permission to create or modify the PublicAccessBlock configuration for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:** [s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAnalyticsConfiguration.html)  **
  - **Description:** Grants permission to set an analytics configuration for the bucket, specified by the analytics configuration ID
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutBucketAbac](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAbac.html)  **
  - **Description:** Grants permission to set ABAC configuration for a general purpose bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html)  **
  - **Description:** Grants permission to set the permissions on an existing bucket using access control lists (ACLs)
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-acl](#list_s3-s3_x-amz-acl)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-grant-full-control](#list_s3-s3_x-amz-grant-full-control)<br />[s3:x-amz-grant-read](#list_s3-s3_x-amz-grant-read)<br />[s3:x-amz-grant-read-acp](#list_s3-s3_x-amz-grant-read-acp)<br />[s3:x-amz-grant-write](#list_s3-s3_x-amz-grant-write)<br />[s3:x-amz-grant-write-acp](#list_s3-s3_x-amz-grant-write-acp)
  - **Access level:** Permissions management, Write

- **   [PutBucketCORS](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html)  **
  - **Description:** Grants permission to set the CORS configuration for an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutBucketLogging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html)  **
  - **Description:** Grants permission to set the logging parameters for an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutBucketNotification](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotification.html)  **
  - **Description:** Grants permission to receive notifications when certain events happen in an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutBucketObjectLockConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLockConfiguration.html)  **
  - **Description:** Grants permission to put Object Lock configuration on a specific bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)
  - **Access level:** Write

- **   [PutBucketOwnershipControls](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketOwnershipControls.html)  **
  - **Description:** Grants permission to add, replace or delete ownership controls on a bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html)  **
  - **Description:** Grants permission to add or replace a bucket policy on a bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutBucketPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html)  **
  - **Description:** Grants permission to create or modify the PublicAccessBlock configuration for a specific Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [PutBucketRequestPayment](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketRequestPayment.html)  **
  - **Description:** Grants permission to set the request payment configuration of a bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html)  **
  - **Description:** Grants permission to add a set of tags to an existing Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [PutBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html)  **
  - **Description:** Grants permission to set the versioning state of an existing Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html)  **
  - **Description:** Grants permission to set the configuration of the website that is specified in the website subresource
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutEncryptionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html)  **
  - **Description:** Grants permission to set the encryption configuration for an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketIntelligentTieringConfiguration.html)  **
  - **Description:** Grants permission to create new or update or delete an existing Amazon S3 Intelligent Tiering configuration
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketInventoryConfiguration.html)  **
  - **Description:** Grants permission to add an inventory configuration to the bucket, identified by the inventory ID
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:InventoryAccessibleOptionalFields](#list_s3-s3_InventoryAccessibleOptionalFields)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutJobTagging.html)  **
  - **Description:** Grants permission to replace tags on an existing Amazon S3 Batch Operations job
  - **Resource types (\*required):** [job\*](#list_s3-resource-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ExistingJobOperation](#list_s3-s3_ExistingJobOperation)<br />[s3:ExistingJobPriority](#list_s3-s3_ExistingJobPriority)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [PutLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)  **
  - **Description:** Grants permission to create a new lifecycle configuration for the bucket or replace an existing lifecycle configuration
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketMetricsConfiguration.html)  **
  - **Description:** Grants permission to set or update a metrics configuration for the CloudWatch request metrics from an Amazon S3 bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutMultiRegionAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicy.html)  **
  - **Description:** Grants permission to associate an access policy with a specified Multi-Region Access Point
  - **Resource types (\*required):** [multiregionaccesspoint\*](#list_s3-resource-multiregionaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)
  - **Access level:** Permissions management, Write

- **   [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)  **
  - **Description:** Grants permission to add an object to a bucket
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:if-match](#list_s3-s3_if-match)<br />[s3:if-none-match](#list_s3-s3_if-none-match)<br />[s3:object-lock-legal-hold](#list_s3-s3_object-lock-legal-hold)<br />[s3:object-lock-mode](#list_s3-s3_object-lock-mode)<br />[s3:object-lock-remaining-retention-days](#list_s3-s3_object-lock-remaining-retention-days)<br />[s3:object-lock-retain-until-date](#list_s3-s3_object-lock-retain-until-date)<br />[s3:ObjectCreationOperation](#list_s3-s3_ObjectCreationOperation)<br />[s3:RequestObjectTag/<key>](#list_s3-s3_RequestObjectTag_key)<br />[s3:RequestObjectTagKeys](#list_s3-s3_RequestObjectTagKeys)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-acl](#list_s3-s3_x-amz-acl)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-copy-source](#list_s3-s3_x-amz-copy-source)<br />[s3:x-amz-grant-full-control](#list_s3-s3_x-amz-grant-full-control)<br />[s3:x-amz-grant-read](#list_s3-s3_x-amz-grant-read)<br />[s3:x-amz-grant-read-acp](#list_s3-s3_x-amz-grant-read-acp)<br />[s3:x-amz-grant-write](#list_s3-s3_x-amz-grant-write)<br />[s3:x-amz-grant-write-acp](#list_s3-s3_x-amz-grant-write-acp)<br />[s3:x-amz-metadata-directive](#list_s3-s3_x-amz-metadata-directive)<br />[s3:x-amz-object-annotation-directive](#list_s3-s3_x-amz-object-annotation-directive)<br />[s3:x-amz-server-side-encryption](#list_s3-s3_x-amz-server-side-encryption)<br />[s3:x-amz-server-side-encryption-aws-kms-key-id](#list_s3-s3_x-amz-server-side-encryption-aws-kms-key-id)<br />[s3:x-amz-server-side-encryption-customer-algorithm](#list_s3-s3_x-amz-server-side-encryption-customer-algorithm)<br />[s3:x-amz-storage-class](#list_s3-s3_x-amz-storage-class)<br />[s3:x-amz-website-redirect-location](#list_s3-s3_x-amz-website-redirect-location)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:if-match](#list_s3-s3_if-match)<br />[s3:if-none-match](#list_s3-s3_if-none-match)<br />[s3:object-lock-legal-hold](#list_s3-s3_object-lock-legal-hold)<br />[s3:object-lock-mode](#list_s3-s3_object-lock-mode)<br />[s3:object-lock-remaining-retention-days](#list_s3-s3_object-lock-remaining-retention-days)<br />[s3:object-lock-retain-until-date](#list_s3-s3_object-lock-retain-until-date)<br />[s3:ObjectCreationOperation](#list_s3-s3_ObjectCreationOperation)<br />[s3:RequestObjectTag/<key>](#list_s3-s3_RequestObjectTag_key)<br />[s3:RequestObjectTagKeys](#list_s3-s3_RequestObjectTagKeys)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-acl](#list_s3-s3_x-amz-acl)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-copy-source](#list_s3-s3_x-amz-copy-source)<br />[s3:x-amz-grant-full-control](#list_s3-s3_x-amz-grant-full-control)<br />[s3:x-amz-grant-read](#list_s3-s3_x-amz-grant-read)<br />[s3:x-amz-grant-read-acp](#list_s3-s3_x-amz-grant-read-acp)<br />[s3:x-amz-grant-write](#list_s3-s3_x-amz-grant-write)<br />[s3:x-amz-grant-write-acp](#list_s3-s3_x-amz-grant-write-acp)<br />[s3:x-amz-metadata-directive](#list_s3-s3_x-amz-metadata-directive)<br />[s3:x-amz-object-annotation-directive](#list_s3-s3_x-amz-object-annotation-directive)<br />[s3:x-amz-server-side-encryption](#list_s3-s3_x-amz-server-side-encryption)<br />[s3:x-amz-server-side-encryption-aws-kms-key-id](#list_s3-s3_x-amz-server-side-encryption-aws-kms-key-id)<br />[s3:x-amz-server-side-encryption-customer-algorithm](#list_s3-s3_x-amz-server-side-encryption-customer-algorithm)<br />[s3:x-amz-storage-class](#list_s3-s3_x-amz-storage-class)<br />[s3:x-amz-website-redirect-location](#list_s3-s3_x-amz-website-redirect-location)
  - **Access level:** Write

- **   [PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html)  **
  - **Description:** Grants permission to set the access control list (ACL) permissions for new or existing objects in an S3 bucket
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-acl](#list_s3-s3_x-amz-acl)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-grant-full-control](#list_s3-s3_x-amz-grant-full-control)<br />[s3:x-amz-grant-read](#list_s3-s3_x-amz-grant-read)<br />[s3:x-amz-grant-read-acp](#list_s3-s3_x-amz-grant-read-acp)<br />[s3:x-amz-grant-write](#list_s3-s3_x-amz-grant-write)<br />[s3:x-amz-grant-write-acp](#list_s3-s3_x-amz-grant-write-acp)<br />[s3:x-amz-storage-class](#list_s3-s3_x-amz-storage-class)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-acl](#list_s3-s3_x-amz-acl)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-grant-full-control](#list_s3-s3_x-amz-grant-full-control)<br />[s3:x-amz-grant-read](#list_s3-s3_x-amz-grant-read)<br />[s3:x-amz-grant-read-acp](#list_s3-s3_x-amz-grant-read-acp)<br />[s3:x-amz-grant-write](#list_s3-s3_x-amz-grant-write)<br />[s3:x-amz-grant-write-acp](#list_s3-s3_x-amz-grant-write-acp)<br />[s3:x-amz-storage-class](#list_s3-s3_x-amz-storage-class)
  - **Access level:** Permissions management, Write

- **   [PutObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAnnotation.html)  **
  - **Description:** Grants permission to add or replace an annotation on an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-object-if-match](#list_s3-s3_x-amz-object-if-match)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-object-if-match](#list_s3-s3_x-amz-object-if-match)
  - **Access level:** Write

- **   [PutObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLegalHold.html)  **
  - **Description:** Grants permission to apply a Legal Hold configuration to the specified object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:object-lock-legal-hold](#list_s3-s3_object-lock-legal-hold)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:object-lock-legal-hold](#list_s3-s3_object-lock-legal-hold)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectRetention.html)  **
  - **Description:** Grants permission to place an Object Retention configuration on an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:object-lock-mode](#list_s3-s3_object-lock-mode)<br />[s3:object-lock-remaining-retention-days](#list_s3-s3_object-lock-remaining-retention-days)<br />[s3:object-lock-retain-until-date](#list_s3-s3_object-lock-retain-until-date)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:object-lock-mode](#list_s3-s3_object-lock-mode)<br />[s3:object-lock-remaining-retention-days](#list_s3-s3_object-lock-remaining-retention-days)<br />[s3:object-lock-retain-until-date](#list_s3-s3_object-lock-retain-until-date)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)  **
  - **Description:** Grants permission to set the supplied tag-set to an object that already exists in a bucket
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:RequestObjectTag/<key>](#list_s3-s3_RequestObjectTag_key)<br />[s3:RequestObjectTagKeys](#list_s3-s3_RequestObjectTagKeys)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:RequestObjectTag/<key>](#list_s3-s3_RequestObjectTag_key)<br />[s3:RequestObjectTagKeys](#list_s3-s3_RequestObjectTagKeys)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [PutObjectVersionAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html)  **
  - **Description:** Grants permission to use the acl subresource to set the access control list (ACL) permissions for an object that already exists in a bucket
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-acl](#list_s3-s3_x-amz-acl)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-grant-full-control](#list_s3-s3_x-amz-grant-full-control)<br />[s3:x-amz-grant-read](#list_s3-s3_x-amz-grant-read)<br />[s3:x-amz-grant-read-acp](#list_s3-s3_x-amz-grant-read-acp)<br />[s3:x-amz-grant-write](#list_s3-s3_x-amz-grant-write)<br />[s3:x-amz-grant-write-acp](#list_s3-s3_x-amz-grant-write-acp)<br />[s3:x-amz-storage-class](#list_s3-s3_x-amz-storage-class)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessGrantsInstanceArn](#list_s3-s3_AccessGrantsInstanceArn)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-acl](#list_s3-s3_x-amz-acl)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-grant-full-control](#list_s3-s3_x-amz-grant-full-control)<br />[s3:x-amz-grant-read](#list_s3-s3_x-amz-grant-read)<br />[s3:x-amz-grant-read-acp](#list_s3-s3_x-amz-grant-read-acp)<br />[s3:x-amz-grant-write](#list_s3-s3_x-amz-grant-write)<br />[s3:x-amz-grant-write-acp](#list_s3-s3_x-amz-grant-write-acp)<br />[s3:x-amz-storage-class](#list_s3-s3_x-amz-storage-class)
  - **Access level:** Permissions management, Write

- **   [PutObjectVersionAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAnnotation.html)  **
  - **Description:** Grants permission to add or replace an annotation on a specific version of an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-object-if-match](#list_s3-s3_x-amz-object-if-match)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-object-if-match](#list_s3-s3_x-amz-object-if-match)
  - **Access level:** Write

- **   [PutObjectVersionTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)  **
  - **Description:** Grants permission to set the supplied tag-set for a specific version of an object
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:RequestObjectTag/<key>](#list_s3-s3_RequestObjectTag_key)<br />[s3:RequestObjectTagKeys](#list_s3-s3_RequestObjectTagKeys)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:RequestObjectTag/<key>](#list_s3-s3_RequestObjectTag_key)<br />[s3:RequestObjectTagKeys](#list_s3-s3_RequestObjectTagKeys)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:versionid](#list_s3-s3_versionid)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [PutReplicationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketReplication.html)  **
  - **Description:** Grants permission to create a new replication configuration or replace an existing one
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:isReplicationPauseRequest](#list_s3-s3_isReplicationPauseRequest)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutStorageLensConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutStorageLensConfiguration.html)  **
  - **Description:** Grants permission to create or update an Amazon S3 Storage Lens configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [PutStorageLensConfigurationTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutStorageLensConfigurationTagging.html)  **
  - **Description:** Grants permission to put or replace tags on an existing Amazon S3 Storage Lens configuration
  - **Resource types (\*required):** [storagelensconfiguration\*](#list_s3-resource-storagelensconfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [ReplicateDelete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html)  **
  - **Description:** Grants permission to replicate delete markers to the destination bucket
  - **Resource types (\*required):** [object\*](#list_s3-resource-object)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [ReplicateObject](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html)  **
  - **Description:** Grants permission to replicate objects and object tags to the destination bucket
  - **Resource types (\*required):** [object\*](#list_s3-resource-object)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-server-side-encryption](#list_s3-s3_x-amz-server-side-encryption)<br />[s3:x-amz-server-side-encryption-aws-kms-key-id](#list_s3-s3_x-amz-server-side-encryption-aws-kms-key-id)<br />[s3:x-amz-server-side-encryption-customer-algorithm](#list_s3-s3_x-amz-server-side-encryption-customer-algorithm)
  - **Access level:** Write

- **   [ReplicateObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html)  **
  - **Description:** Grants permission to replicate annotations to the destination bucket
  - **Resource types (\*required):** [object\*](#list_s3-resource-object)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [ReplicateTags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html)  **
  - **Description:** Grants permission to replicate object tags to the destination bucket
  - **Resource types (\*required):** [object\*](#list_s3-resource-object)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html)  **
  - **Description:** Grants permission to restore an archived copy of an object back into Amazon S3
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [SubmitMultiRegionAccessPointRoutes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SubmitMultiRegionAccessPointRoutes.html)  **
  - **Description:** Grants permission to submit a route configuration update for a Multi-Region Access Point
  - **Resource types (\*required):** [multiregionaccesspoint\*](#list_s3-resource-multiregionaccesspoint)
  - **Condition keys:** [s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html)  **
  - **Description:** Grants permission to add tags to the specified resource
  - **Resource types (\*required):** [accessgrant](#list_s3-resource-accessgrant) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [accessgrantsinstance](#list_s3-resource-accessgrantsinstance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [accessgrantslocation](#list_s3-resource-accessgrantslocation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [accesspoint](#list_s3-resource-accesspoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3-resource-bucket) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [storagelensgroup](#list_s3-resource-storagelensgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from the specified resource
  - **Resource types (\*required):** [accessgrant](#list_s3-resource-accessgrant) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [accessgrantsinstance](#list_s3-resource-accessgrantsinstance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [accessgrantslocation](#list_s3-resource-accessgrantslocation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [accesspoint](#list_s3-resource-accesspoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [bucket](#list_s3-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Resource types (\*required):** [storagelensgroup](#list_s3-resource-storagelensgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Tagging, Write

- **   [UpdateAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateAccessGrantsLocation.html)  **
  - **Description:** Grants permission to update Access Grants location
  - **Resource types (\*required):** [accessgrantslocation\*](#list_s3-resource-accessgrantslocation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:AccessGrantsLocationScope](#list_s3-s3_AccessGrantsLocationScope)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Permissions management, Write

- **   [UpdateBucketMetadataAnnotationTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataAnnotationTableConfiguration.html)  **
  - **Description:** Grants permission to update the annotation table configuration for a bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [UpdateBucketMetadataInventoryTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataInventoryTableConfiguration.html)  **
  - **Description:** Grants permission to update the inventory table configuration on an existing S3 Metadata configuration for a specified general purpose bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [UpdateBucketMetadataJournalTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataJournalTableConfiguration.html)  **
  - **Description:** Grants permission to update the journal table configuration on an existing S3 Metadata configuration for a specified general purpose bucket
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [UpdateJobPriority](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html)  **
  - **Description:** Grants permission to update the priority of an existing job
  - **Resource types (\*required):** [job\*](#list_s3-resource-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ExistingJobOperation](#list_s3-s3_ExistingJobOperation)<br />[s3:ExistingJobPriority](#list_s3-s3_ExistingJobPriority)<br />[s3:RequestJobPriority](#list_s3-s3_RequestJobPriority)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [UpdateJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html)  **
  - **Description:** Grants permission to update the status for the specified job
  - **Resource types (\*required):** [job\*](#list_s3-resource-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ExistingJobOperation](#list_s3-s3_ExistingJobOperation)<br />[s3:ExistingJobPriority](#list_s3-s3_ExistingJobPriority)<br />[s3:JobSuspendedCause](#list_s3-s3_JobSuspendedCause)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write

- **   [UpdateObjectEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateObjectEncryption.html)  **
  - **Description:** Grants permission to update the server-side encryption type of an existing object in a general purpose bucket
  - **Resource types (\*required):** [accesspointobject](#list_s3-resource-accesspointobject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-server-side-encryption](#list_s3-s3_x-amz-server-side-encryption)<br />[s3:x-amz-server-side-encryption-aws-kms-key-id](#list_s3-s3_x-amz-server-side-encryption-aws-kms-key-id)
  - **Resource types (\*required):** [object](#list_s3-resource-object) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ExistingObjectTag/<key>](#list_s3-s3_ExistingObjectTag_key)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)<br />[s3:x-amz-server-side-encryption](#list_s3-s3_x-amz-server-side-encryption)<br />[s3:x-amz-server-side-encryption-aws-kms-key-id](#list_s3-s3_x-amz-server-side-encryption-aws-kms-key-id)
  - **Access level:** Write

- **   [UpdateStorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateStorageLensGroup.html)  **
  - **Description:** Grants permission to update an existing S3 Storage Lens group
  - **Resource types (\*required):** [storagelensgroup\*](#list_s3-resource-storagelensgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write



## Permission-only actions for Amazon S3
<a name="list_s3-permission-only-actions"></a>

The following actions are defined by Amazon S3 but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [InitiateReplication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html)  **
  - **Description:** Grants permission to initiate the replication process by setting replication status of an object to pending
  - **Resource types (\*required):** [object\*](#list_s3-resource-object)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)
  - **Access level:** Write

- **   [PauseReplication](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#bucket-pause-replication)  **
  - **Description:** Grants permission to pause S3 Replication from target source buckets to destination buckets
  - **Resource types (\*required):** [bucket\*](#list_s3-resource-bucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:authType](#list_s3-s3_authType)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:destinationRegion](#list_s3-s3_destinationRegion)<br />[s3:ResourceAccount](#list_s3-s3_ResourceAccount)<br />[s3:signatureAge](#list_s3-s3_signatureAge)<br />[s3:signatureversion](#list_s3-s3_signatureversion)<br />[s3:TlsVersion](#list_s3-s3_TlsVersion)<br />[s3:x-amz-content-sha256](#list_s3-s3_x-amz-content-sha256)
  - **Access level:** Write



## Resource types defined by Amazon S3
<a name="list_s3-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [accessgrant](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-grant.html)  | arn:${Partition}:s3:${Region}:${Account}:access-grants/default/grant/${Token} | [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys) | 
|  [accessgrantsinstance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-instance.html)  | arn:${Partition}:s3:${Region}:${Account}:access-grants/default | [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys) | 
|  [accessgrantslocation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location.html)  | arn:${Partition}:s3:${Region}:${Account}:access-grants/default/location/${Token} | [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys) | 
|  [accesspoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html)  | arn:${Partition}:s3:${Region}:${Account}:accesspoint/${AccessPointName} | [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn) | 
|  [accesspointobject](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html)  | arn:${Partition}:s3:${Region}:${Account}:accesspoint/${AccessPointName}/object/${ObjectName} | [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:AccessPointNetworkOrigin](#list_s3-s3_AccessPointNetworkOrigin)<br />[s3:AccessPointTag/${TagKey}](#list_s3-s3_AccessPointTag___TagKey_)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_)<br />[s3:DataAccessPointAccount](#list_s3-s3_DataAccessPointAccount)<br />[s3:DataAccessPointArn](#list_s3-s3_DataAccessPointArn) | 
|  [bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)  | arn:${Partition}:s3:::${BucketName} | [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_) | 
|  [job](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-managing-jobs.html)  | arn:${Partition}:s3:${Region}:${Account}:job/${JobId} | [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys) | 
|  [multiregionaccesspoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequests.html)  | arn:${Partition}:s3::${Account}:accesspoint/${AccessPointAlias} |   | 
|  [multiregionaccesspointrequestarn](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequests.html)  | arn:${Partition}:s3:us-west-2:${Account}:async-request/mrap/${Operation}/${Token} |   | 
|  [object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html)  | arn:${Partition}:s3:::${BucketName}/${ObjectName} | [aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[s3:BucketTag/${TagKey}](#list_s3-s3_BucketTag___TagKey_) | 
|  [objectlambdaaccesspoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html)  | arn:${Partition}:s3-object-lambda:${Region}:${Account}:accesspoint/${AccessPointName} |   | 
|  [storagelensconfiguration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html)  | arn:${Partition}:s3:${Region}:${Account}:storage-lens/${ConfigId} | [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys) | 
|  [storagelensgroup](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_group.html)  | arn:${Partition}:s3:${Region}:${Account}:storage-lens-group/${Name} | [aws:RequestTag/${TagKey}](#list_s3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3-aws_TagKeys) | 

## Condition keys for Amazon S3
<a name="list_s3-policy-keys"></a>

Amazon S3 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [s3:AccessGrantScope](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-grant.html)  | Filters access by the grant scope of access grants grant | String | 
|   [s3:AccessGrantsInstanceArn](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-instance.html)  | Filters access by access grants instance ARN | ARN | 
|   [s3:AccessGrantsLocationScope](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location.html)  | Filters access by the location scope of access grants location | String | 
|   [s3:AccessPointNetworkOrigin](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html#access-points-policies)  | Filters access by the network origin (Internet or VPC) | String | 
|   [s3:AccessPointTag/${TagKey}](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html#tagging-and-policies)  | Filters access by existing access point tag key and value | String | 
|   [s3:BucketTag/${TagKey}](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging.html)  | Filters access by the tags associated with the bucket | String | 
|   [s3:DataAccessPointAccount](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html#access-points-policies)  | Filters access by the AWS Account ID that owns the access point | String | 
|   [s3:DataAccessPointArn](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html#access-points-policies)  | Filters access by an access point Amazon Resource Name (ARN) | ARN | 
|   [s3:ExistingJobOperation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-tags-examples.html)  | Filters access by operation to updating the job priority | String | 
|   [s3:ExistingJobPriority](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-tags-examples.html)  | Filters access by priority range to cancelling existing jobs | Numeric | 
|   [s3:ExistingObjectTag/<key>](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html#tagging-and-policies)  | Filters access by existing object tag key and value | String | 
|   [s3:InventoryAccessibleOptionalFields](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-s3-inventory-2)  | Filters access by restricting which optional metadata fields a user can add when configuring S3 Inventory reports | ArrayOfString | 
|   [s3:JobSuspendedCause](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-tags-examples.html)  | Filters access by a specific job suspended cause (for example, AWAITING\_CONFIRMATION) to cancelling suspended jobs | String | 
|   [s3:ObjectCreationOperation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes-enforce.html)  | Filters access by whether or not the operation creates an object | Bool | 
|   [s3:RequestJobOperation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-tags-examples.html)  | Filters access by operation to creating jobs | String | 
|   [s3:RequestJobPriority](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-tags-examples.html)  | Filters access by priority range to creating new jobs | Numeric | 
|   [s3:RequestObjectTag/<key>](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html#tagging-and-policies)  | Filters access by the tag keys and values to be added to objects | String | 
|   [s3:RequestObjectTagKeys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html#tagging-and-policies)  | Filters access by the tag keys to be added to objects | ArrayOfString | 
|   [s3:ResourceAccount](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#example-object-resource-account)  | Filters access by the resource owner AWS account ID | String | 
|   [s3:TlsVersion](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#example-object-tls-version)  | Filters access by the TLS version used by the client | Numeric | 
|   [s3:annotation-prefix](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#example-annotation-prefix-condition)  | Filters access by the annotation name prefix specified in the request | String | 
|   [s3:authType](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by authentication method | String | 
|   [s3:delimiter](https://docs.aws.amazon.com/AmazonS3/latest/userguide/walkthrough1.html)  | Filters access by delimiter parameter | String | 
|   [s3:deliverySourceArn](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html)  | Filters access by specific delivery source Amazon Resource Name (ARN) | ARN | 
|   [s3:destinationRegion](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)  | Filters access by a specific replication destination region for targeted buckets of the AWS FIS action aws:s3:bucket-pause-replication | String | 
|   [s3:if-match](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes-enforce.html)  | Filters access by the request's 'If-Match' conditional header | String | 
|   [s3:if-none-match](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes-enforce.html)  | Filters access by the request's 'If-None-Match' conditional header | String | 
|   [s3:isReplicationPauseRequest](https://docs.aws.amazon.com/fis/latest/userguide/security_iam_id-based-policy-examples.html#security-iam-policy-examples-s3)  | Filters access by request made via AWS FIS action aws:s3:bucket-pause-replication | Bool | 
|   [s3:locationconstraint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#condition-key-bucket-ops-1)  | Filters access by a specific Region | String | 
|   [s3:logType](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html)  | Filters access by specific log type, currently supports S3\_SERVER\_ACCESS\_LOGS | String | 
|   [s3:max-annotation-results](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#example-annotation-max-results)  | Filters access by the maximum number of annotation results requested | Numeric | 
|   [s3:max-keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#example-numeric-condition-operators)  | Filters access by maximum number of keys returned in a ListBucket request | Numeric | 
|   [s3:object-lock-legal-hold](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-legal-holds)  | Filters access by object legal hold status | String | 
|   [s3:object-lock-mode](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-retention-modes)  | Filters access by object retention mode (COMPLIANCE or GOVERNANCE) | String | 
|   [s3:object-lock-remaining-retention-days](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-managing.html#object-lock-managing-retention-limits)  | Filters access by remaining object retention days | Numeric | 
|   [s3:object-lock-retain-until-date](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-retention-periods)  | Filters access by object retain-until date | Date | 
|   [s3:prefix](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#condition-key-bucket-ops-2)  | Filters access by key name prefix | String | 
|   [s3:resourceArnBeingAuthorized](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html)  | Filters access by source bucket Amazon Resource Name (ARN) | ARN | 
|   [s3:signatureAge](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by the age in milliseconds of the request signature | Numeric | 
|   [s3:signatureversion](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by the version of AWS Signature used on the request | String | 
|   [s3:versionid](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#getobjectversion-limit-access-to-specific-version-3)  | Filters access by a specific object version | String | 
|   [s3:x-amz-acl](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions)  | Filters access by canned ACL in the request's x-amz-acl header | String | 
|   [s3:x-amz-bucket-namespace](https://docs.aws.amazon.com/AmazonS3/latest/userguide/gpbucketnamespaces.html)  | Filters access by general purpose bucket namespace type | String | 
|   [s3:x-amz-content-sha256](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html)  | Filters access by unsigned content in your bucket | String | 
|   [s3:x-amz-copy-source](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#putobject-limit-copy-source-3)  | Filters access by copy source bucket, prefix, or object in the copy object requests | String | 
|   [s3:x-amz-grant-full-control](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions)  | Filters access by x-amz-grant-full-control (full control) header | String | 
|   [s3:x-amz-grant-read](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions)  | Filters access by x-amz-grant-read (read access) header | String | 
|   [s3:x-amz-grant-read-acp](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions)  | Filters access by the x-amz-grant-read-acp (read permissions for the ACL) header | String | 
|   [s3:x-amz-grant-write](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions)  | Filters access by the x-amz-grant-write (write access) header | String | 
|   [s3:x-amz-grant-write-acp](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions)  | Filters access by the x-amz-grant-write-acp (write permissions for the ACL) header | String | 
|   [s3:x-amz-metadata-directive](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)  | Filters access by object metadata behavior (COPY or REPLACE) when objects are copied | String | 
|   [s3:x-amz-object-annotation-directive](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)  | Filters access by the annotation copy directive specified in the request | String | 
|   [s3:x-amz-object-if-match](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#example-annotation-conditional-writes)  | Filters access by the ETag of the object version specified in the request | String | 
|   [s3:x-amz-object-ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ensure-object-ownership.html#object-ownership-requiring-bucket-owner-enforced)  | Filters access by Object Ownership | String | 
|   [s3:x-amz-server-side-encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html)  | Filters access by server-side encryption | String | 
|   [s3:x-amz-server-side-encryption-aws-kms-key-id](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html#require-sse-kms)  | Filters access by AWS KMS customer managed CMK for server-side encryption | ARN | 
|   [s3:x-amz-server-side-encryption-customer-algorithm](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html)  | Filters access by customer specified algorithm for server-side encryption | String | 
|   [s3:x-amz-storage-class](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-howtoset)  | Filters access by storage class | String | 
|   [s3:x-amz-website-redirect-location](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-page-redirect.html#page-redirect-using-rest-api)  | Filters access by a specific website redirect location for buckets that are configured as static websites | String | 