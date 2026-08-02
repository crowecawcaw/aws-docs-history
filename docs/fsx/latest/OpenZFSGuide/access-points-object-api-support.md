# Access point compatibility

You can use access points to access data stored on an FSx for OpenZFS volume using the following subset of Amazon S3 API object operations related to data access.
All the operations listed below can accept either access point ARNs or access point aliases.

The following table is a partial list of Amazon S3 operations and if they are compatible with access points.
The table shows which operations are supported by access points using an FSx for OpenZFS volume as a data source.

| S3 operation                               | Access point attached to an FSx for OpenZFS volume                                                                               |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `AbortMultipartUpload`                     | Supported                                                                                                                        |
| `CompleteMultipartUpload`                  | Supported                                                                                                                        |
| `CopyObject`<br>(same-Region copies only)  | Supported, if source and destination are the same access point. The `x-amz-object-annotation-directive` header is not supported. |
| `CreateMultipartUpload`                    | Supported                                                                                                                        |
| `DeleteObject`                             | Supported                                                                                                                        |
| `DeleteObjects`                            | Supported                                                                                                                        |
| `DeleteObjectTagging`                      | Supported                                                                                                                        |
| `DeleteObjectAnnotation`                   | Not supported                                                                                                                    |
| `GetBucketAcl`                             | Not supported                                                                                                                    |
| `GetBucketCors`                            | Not supported                                                                                                                    |
| `GetBucketLocation`                        | Supported                                                                                                                        |
| `GetBucketNotificationConfiguration`       | Not supported                                                                                                                    |
| `GetBucketPolicy`                          | Not supported                                                                                                                    |
| `GetObject`                                | Supported                                                                                                                        |
| `GetObjectAcl`                             | Not supported                                                                                                                    |
| `GetObjectAnnotation`                      | Not supported                                                                                                                    |
| `GetObjectAttributes`                      | Supported                                                                                                                        |
| `GetObjectLegalHold`                       | Not supported                                                                                                                    |
| `GetObjectRetention`                       | Not supported                                                                                                                    |
| `GetObjectTagging`                         | Supported                                                                                                                        |
| `HeadBucket`                               | Supported                                                                                                                        |
| `HeadObject`                               | Supported                                                                                                                        |
| `ListMultipartUploads`                     | Supported                                                                                                                        |
| `ListObjects`                              | Supported                                                                                                                        |
| `ListObjectsV2`                            | Supported                                                                                                                        |
| `ListObjectVersions`                       | Not supported                                                                                                                    |
| `ListObjectAnnotations`                    | Not supported                                                                                                                    |
| `ListParts`                                | Supported                                                                                                                        |
| `Presign`                                  | Not supported                                                                                                                    |
| `PutObject`                                | Supported                                                                                                                        |
| `PutObjectAnnotation`                      | Not supported                                                                                                                    |
| `PutObjectAcl`                             | Not supported                                                                                                                    |
| `PutObjectLegalHold`                       | Not supported                                                                                                                    |
| `PutObjectRetention`                       | Not supported                                                                                                                    |
| `PutObjectTagging`                         | Supported                                                                                                                        |
| `RestoreObject`                            | Not supported                                                                                                                    |
| `UploadPart`                               | Supported                                                                                                                        |
| `UploadPartCopy` (same-Region copies only) | Supported, if source and destination are the same access point                                                                   |

Limitations to using Amazon S3 operations are the following:

- Maximum object size is 50 GB
- `FSX_OPENZFS` is the only supported storage class
- [SSE\_FSX](s3-ap-manage-access-fsx.md#data-encryption "s3-ap-manage-access-fsx.md#data-encryption") is the only supported server-side encryption mode
- The following Amazon S3 features are not supported: Object Annotations
  For examples of using access points to perform data access operations on file data, see
  [Using access points](access-points-usage-examples.md "access-points-usage-examples.md").
