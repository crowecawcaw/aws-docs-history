# Access point compatibility

You can use access points to access objects using the following subset of Amazon S3 APIs. All the
operations listed below can accept either access point ARNs or access point aliases.

For examples of using access points to perform operations on objects, see [Using Amazon S3 access points for general purpose buckets](using-access-points.md "using-access-points.md").

## Access points compatibility with S3

operations

The following table is a partial list of Amazon S3 operations and if they are compatible with access points.
All operations below are supported by access points using an S3 bucket as its data source, while only
some operations are supported by access points using an FSx for OpenZFS volume as a data
source.

For more information see,
[Access point compatibility](../../../fsx/latest/OpenZFSGuide/access-points-object-api-support.md "../../../fsx/latest/OpenZFSGuide/access-points-object-api-support.md") in the
_FSx for OpenZFS User Guide_.

| S3 operation                               | Access point attached to an S3 bucket | Access point attached to an FSx for OpenZFS volume             |
| ------------------------------------------ | ------------------------------------- | -------------------------------------------------------------- |
| `AbortMultipartUpload`                     | Supported                             | Supported                                                      |
| `CompleteMultipartUpload`                  | Supported                             | Supported                                                      |
| `CopyObject`<br>(same-Region copies only)  | Supported                             | Supported, if source and destination are the same access point |
| `CreateMultipartUpload`                    | Supported                             | Supported                                                      |
| `DeleteObject`                             | Supported                             | Supported                                                      |
| `DeleteObjects`                            | Supported                             | Supported                                                      |
| `DeleteObjectTagging`                      | Supported                             | Supported                                                      |
| `GetBucketAcl`                             | Supported                             | Not supported                                                  |
| `GetBucketCors`                            | Supported                             | Not supported                                                  |
| `GetBucketLocation`                        | Supported                             | Supported                                                      |
| `GetBucketNotificationConfiguration`       | Supported                             | Not supported                                                  |
| `GetBucketPolicy`                          | Supported                             | Not supported                                                  |
| `GetObject`                                | Supported                             | Supported                                                      |
| `GetObjectAcl`                             | Supported                             | Not supported                                                  |
| `GetObjectAttributes`                      | Supported                             | Supported                                                      |
| `GetObjectLegalHold`                       | Supported                             | Not supported                                                  |
| `GetObjectRetention`                       | Supported                             | Not supported                                                  |
| `GetObjectTagging`                         | Supported                             | Supported                                                      |
| `HeadBucket`                               | Supported                             | Supported                                                      |
| `HeadObject`                               | Supported                             | Supported                                                      |
| `ListMultipartUploads`                     | Supported                             | Supported                                                      |
| `ListObjects`                              | Supported                             | Supported                                                      |
| `ListObjectsV2`                            | Supported                             | Supported                                                      |
| `ListObjectVersions`                       | Supported                             | Not supported                                                  |
| `ListParts`                                | Supported                             | Supported                                                      |
| `Presign`                                  | Supported                             | Supported                                                      |
| `PutObject`                                | Supported                             | Supported                                                      |
| `PutObjectAcl`                             | Supported                             | Not supported                                                  |
| `PutObjectLegalHold`                       | Supported                             | Not supported                                                  |
| `PutObjectRetention`                       | Supported                             | Not supported                                                  |
| `PutObjectTagging`                         | Supported                             | Supported                                                      |
| `RestoreObject`                            | Supported                             | Not supported                                                  |
| `UploadPart`                               | Supported                             | Supported                                                      |
| `UploadPartCopy` (same-Region copies only) | Supported                             | Supported, if source and destination are the same access point |
