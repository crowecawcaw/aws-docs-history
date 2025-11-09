# Permission changes for

AWSSupportServiceRolePolicy

Most permissions added to `AWSSupportServiceRolePolicy` allow AWS Support to
call an API operation with the same name. However, some API operations require
permissions that have a different name.

The following table only lists the API operations that require permissions with a
different name. This table describes these differences beginning on February 17, 2022.

| Date                                                                                            | API operation name                                                            | Required policy permission     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------ |
| Added permissions on February 17, 2022                                                          | `s3.GetBucketAnalyticsConfiguration`<br>`s3.ListBucketAnalyticsConfiguration` | `s3:GetAnalyticsConfiguration` |
| `s3.GetBucketNotificationConfiguration`                                                         | `s3:GetBucketNotification`                                                    |
| `s3.GetBucketEncryption`                                                                        | `s3:GetEncryptionConfiguration`                                               |
| `s3.GetBucketIntelligentTieringConfiguration`<br>`s3.ListBucketIntelligentTieringConfiguration` | `s3:GetIntelligentTieringConfiguration`                                       |
| `s3.GetBucketInventoryConfiguration`<br>`s3.ListBucketInventoryConfiguration`                   | `s3:GetInventoryConfiguration`                                                |
| `s3.GetBucketLifecycleConfiguration`                                                            | `s3:GetLifecycleConfiguration`                                                |
| `s3.GetBucketMetricsConfiguration`<br>`s3.ListBucketMetricsConfiguration`                       | `s3:GetMetricsConfiguration`                                                  |
| `s3.GetBucketReplication`                                                                       | `s3:GetReplicationConfiguration`                                              |
| `s3.HeadBucket`<br>`s3.ListObjects`                                                             | `s3:ListBucket`                                                               |
| `s3.ListBuckets`                                                                                | `s3:ListAllMyBuckets`                                                         |
| `s3.ListMultipartUploads`                                                                       | `s3:ListBucketMultipartUploads`                                               |
| `s3.ListObjectVersions`                                                                         | `s3:ListBucketVersions`                                                       |
| `s3.ListParts`                                                                                  | `s3:ListMultipartUploadParts`                                                 |
| Added permissions on July 15, 2025                                                              | `cloudcontrolapi:GetResource`                                                 | `cloudformation:GetResource`   |
| `cloudcontrolapi:ListResources`                                                                 | `cloudformation:ListResources`                                                |
