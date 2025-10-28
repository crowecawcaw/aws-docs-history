# Access point compatibility

You can use access points to access data stored on an FSx for OpenZFS volume using the following subset of Amazon S3 API object operations related to data access.
All the operations listed below can accept either access point ARNs or access point aliases.

The following table is a partial list of Amazon S3 operations and if they are compatible with access points.
The table shows which operations are supported by access points using an FSx for OpenZFS volume as a data source.

| S3 operation                               | Access point attached to an FSx for OpenZFS volume             |
| ------------------------------------------ | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AbortMultipartUpload`                     | Supported                                                      |
| `CompleteMultipartUpload`                  | Supported                                                      |
| `CopyObject` (same-Region copies only)     | Supported, if source and destination are the same access point |
| `CreateMultipartUpload`                    | Supported                                                      |
| `DeleteObject`                             | Supported                                                      |
| `DeleteObjects`                            | Supported                                                      |
| `DeleteObjectTagging`                      | Supported                                                      |
| `GetBucketAcl`                             | Not supported                                                  |
| `GetBucketCors`                            | Not supported                                                  |
| `GetBucketLocation`                        | Supported                                                      |
| `GetBucketNotificationConfiguration`       | Not supported                                                  |
| `GetBucketPolicy`                          | Not supported                                                  |
| `GetObject`                                | Supported                                                      |
| `GetObjectAcl`                             | Not supported                                                  |
| `GetObjectAttributes`                      | Supported                                                      |
| `GetObjectLegalHold`                       | Not supported                                                  |
| `GetObjectRetention`                       | Not supported                                                  |
| `GetObjectTagging`                         | Supported                                                      |
| `HeadBucket`                               | Supported                                                      |
| `HeadObject`                               | Supported                                                      |
| `ListMultipartUploads`                     | Supported                                                      |
| `ListObjects`                              | Supported                                                      |
| `ListObjectsV2`                            | Supported                                                      |
| `ListObjectVersions`                       | Not supported                                                  |
| `ListParts`                                | Supported                                                      |
| `Presign`                                  | Not supported                                                  |
| `PutObject`                                | Supported                                                      |
| `PutObjectAcl`                             | Not supported                                                  |
| `PutObjectLegalHold`                       | Not supported                                                  |
| `PutObjectRetention`                       | Not supported                                                  |
| `PutObjectTagging`                         | Supported                                                      |
| `RestoreObject`                            | Not supported                                                  |
| `UploadPart`                               | Supported                                                      |
| `UploadPartCopy` (same-Region copies only) | Supported, if source and destination are the same access point | Limitations to using Amazon S3 operations are the following: <br>• Maximum object size is 5 GB <br>• `FSX_OPENZFS` is the only supported storage class <br>• [SSE_FSX](s3-ap-manage-access-fsx.md#data-encryption "s3-ap-manage-access-fsx.md#data-encryption") is the only supported server-side encryption mode For examples of using access points to perform data access operations on file data, see [Using access points](access-points-usage-examples.md "access-points-usage-examples.md"). |
