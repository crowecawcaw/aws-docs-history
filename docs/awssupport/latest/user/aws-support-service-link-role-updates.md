

# Permission changes for AWSSupportServiceRolePolicy
<a name="aws-support-service-link-role-updates"></a>

Most permissions added to `AWSSupportServiceRolePolicy` allow AWS Support to call an API operation with the same name. However, some API operations require permissions that have a different name. 

The following table only lists the API operations that require permissions with a different name. This table describes these differences beginning on February 17, 2022. 



- **Added permissions on February 17, 2022**
  - **API operation name:** `s3.GetBucketAnalyticsConfiguration`<br />`s3.ListBucketAnalyticsConfiguration` / **Required policy permission:** `s3:GetAnalyticsConfiguration`
  - **API operation name:** `s3.GetBucketNotificationConfiguration` / **Required policy permission:** `s3:GetBucketNotification`
  - **API operation name:** `s3.GetBucketEncryption` / **Required policy permission:** `s3:GetEncryptionConfiguration`
  - **API operation name:** `s3.GetBucketIntelligentTieringConfiguration`<br />`s3.ListBucketIntelligentTieringConfiguration` / **Required policy permission:** `s3:GetIntelligentTieringConfiguration`
  - **API operation name:** `s3.GetBucketInventoryConfiguration`<br />`s3.ListBucketInventoryConfiguration` / **Required policy permission:** `s3:GetInventoryConfiguration`
  - **API operation name:** `s3.GetBucketLifecycleConfiguration` / **Required policy permission:** `s3:GetLifecycleConfiguration`
  - **API operation name:** `s3.GetBucketMetricsConfiguration`<br />`s3.ListBucketMetricsConfiguration` / **Required policy permission:** `s3:GetMetricsConfiguration`
  - **API operation name:** `s3.GetBucketReplication` / **Required policy permission:** `s3:GetReplicationConfiguration`
  - **API operation name:** `s3.HeadBucket`<br />`s3.ListObjects` / **Required policy permission:** `s3:ListBucket`
  - **API operation name:** `s3.ListBuckets` / **Required policy permission:** `s3:ListAllMyBuckets`
  - **API operation name:** `s3.ListMultipartUploads` / **Required policy permission:** `s3:ListBucketMultipartUploads`
  - **API operation name:** `s3.ListObjectVersions` / **Required policy permission:** `s3:ListBucketVersions`
  - **API operation name:** `s3.ListParts` / **Required policy permission:** `s3:ListMultipartUploadParts`

- **Added permissions on July 15, 2025**
  - **API operation name:** `cloudcontrolapi:GetResource` / **Required policy permission:** `cloudformation:GetResource`
  - **API operation name:** `cloudcontrolapi:ListResources` / **Required policy permission:** `cloudformation:ListResources`

