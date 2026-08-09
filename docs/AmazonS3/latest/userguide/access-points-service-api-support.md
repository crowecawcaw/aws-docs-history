# Access point compatibility

You can use access points to access objects using the following subset of Amazon S3 APIs. All the
operations listed below can accept either access point ARNs or access point aliases.

For examples of using access points to perform operations on objects, see [Using Amazon S3 access points for general purpose buckets](using-access-points.md "using-access-points.md").

## Access points compatibility with S3 operations

The following table is a partial list of Amazon S3 operations and if they are compatible with access points.
All operations below are supported by access points using an S3 bucket as its data source, while only
some operations are supported by access points using an FSx for ONTAP or FSx for OpenZFS volume or an S3
recovery point in AWS Backup as a data source.

For more information see, access point compatibility in the [_FSx for ONTAP User Guide_](../../../fsx/latest/ONTAPGuide/access-points-for-fsxn-object-api-support.md "../../../fsx/latest/ONTAPGuide/access-points-for-fsxn-object-api-support.md") or the [_FSx for OpenZFS User Guide_](../../../fsx/latest/OpenZFSGuide/access-points-object-api-support.md "../../../fsx/latest/OpenZFSGuide/access-points-object-api-support.md").

| S3 operation                               | Access point attached to an S3 bucket | Access point attached to an FSx for OpenZFS volume             | Access point attached to an Amazon S3 recovery point in AWS Backup |
| ------------------------------------------ | ------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------ |
| `AbortMultipartUpload`                     | Supported                             | Supported                                                      | Not supported                                                      |
| `CompleteMultipartUpload`                  | Supported                             | Supported                                                      | Not supported                                                      |
| `CopyObject`<br>(same-Region copies only)  | Supported                             | Supported, if source and destination are the same access point | Not supported                                                      |
| `CreateMultipartUpload`                    | Supported                             | Supported                                                      | Not supported                                                      |
| `DeleteObject`                             | Supported                             | Supported                                                      | Not supported                                                      |
| `DeleteObjects`                            | Supported                             | Supported                                                      | Not supported                                                      |
| `DeleteObjectTagging`                      | Supported                             | Supported                                                      | Not supported                                                      |
| `GetBucketAcl`                             | Supported                             | Not supported                                                  | Not supported                                                      |
| `GetBucketCors`                            | Supported                             | Not supported                                                  | Not supported                                                      |
| `GetBucketLocation`                        | Supported                             | Supported                                                      | Supported                                                          |
| `GetBucketNotificationConfiguration`       | Supported                             | Not supported                                                  | Not supported                                                      |
| `GetBucketPolicy`                          | Supported                             | Not supported                                                  | Not supported                                                      |
| `GetObject`                                | Supported                             | Supported                                                      | Supported                                                          |
| `GetObjectAcl`                             | Supported                             | Not supported                                                  | Not supported                                                      |
| `GetObjectAttributes`                      | Supported                             | Supported                                                      | Supported                                                          |
| `GetObjectLegalHold`                       | Supported                             | Not supported                                                  | Not supported                                                      |
| `GetObjectRetention`                       | Supported                             | Not supported                                                  | Not supported                                                      |
| `GetObjectTagging`                         | Supported                             | Supported                                                      | Supported                                                          |
| `HeadBucket`                               | Supported                             | Supported                                                      | Not supported                                                      |
| `HeadObject`                               | Supported                             | Supported                                                      | Supported                                                          |
| `ListMultipartUploads`                     | Supported                             | Supported                                                      | Not supported                                                      |
| `ListObjects`                              | Supported                             | Supported                                                      | Supported                                                          |
| `ListObjectsV2`                            | Supported                             | Supported                                                      | Supported                                                          |
| `ListObjectVersions`                       | Supported                             | Not supported                                                  | Supported                                                          |
| `ListParts`                                | Supported                             | Supported                                                      | Not supported                                                      |
| `Presign`                                  | Supported                             | Supported                                                      | Not supported                                                      |
| `PutObject`                                | Supported                             | Supported                                                      | Not supported                                                      |
| `PutObjectAcl`                             | Supported                             | Not supported                                                  | Not supported                                                      |
| `PutObjectLegalHold`                       | Supported                             | Not supported                                                  | Not supported                                                      |
| `PutObjectRetention`                       | Supported                             | Not supported                                                  | Not supported                                                      |
| `PutObjectTagging`                         | Supported                             | Supported                                                      | Not supported                                                      |
| `RestoreObject`                            | Supported                             | Not supported                                                  | Not supported                                                      |
| `UploadPart`                               | Supported                             | Supported                                                      | Not supported                                                      |
| `UploadPartCopy` (same-Region copies only) | Supported                             | Supported, if source and destination are the same access point | Not supported                                                      |
