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
 [Access point compatibility](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-object-api-support.html "https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-object-api-support.html") in the 
 *FSx for OpenZFS User Guide*.




| S3 operation | Access point attached to an S3 bucket | Access point attached to an FSx for OpenZFS volume |
| --- | --- | --- |
| `[AbortMultipartUpload](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")` | Supported | Supported |
| `[CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")` | Supported | Supported |
| `[CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")`
 (same-Region copies only) | Supported | Supported, if source and destination are the same access point |
| `[CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")` | Supported | Supported |
| `[DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md")` | Supported | Supported |
| `[DeleteObjects](../API/API_DeleteObjects.md "../API/API_DeleteObjects.md")` | Supported | Supported |
| `[DeleteObjectTagging](../API/API_DeleteObjectTagging.md "../API/API_DeleteObjectTagging.md")` | Supported | Supported |
| `[GetBucketAcl](../API/API_GetBucketAcl.md "../API/API_GetBucketAcl.md")` | Supported | Not supported |
| `[GetBucketCors](../API/API_GetBucketCors.md "../API/API_GetBucketCors.md")` | Supported | Not supported |
| `[GetBucketLocation](../API/API_GetBucketLocation.md "../API/API_GetBucketLocation.md")` | Supported | Supported |
| `[GetBucketNotificationConfiguration](../API/API_GetBucketNotificationConfiguration.md "../API/API_GetBucketNotificationConfiguration.md")` | Supported | Not supported |
| `[GetBucketPolicy](../API/API_GetBucketPolicy.md "../API/API_GetBucketPolicy.md")` | Supported | Not supported |
| `[GetObject](../API/API_GetObject.md "../API/API_GetObject.md")` | Supported | Supported |
| `[GetObjectAcl](../API/API_GetObjectAcl.md "../API/API_GetObjectAcl.md")` | Supported | Not supported |
| `[GetObjectAttributes](../API/API_GetObjectAttributes.md "../API/API_GetObjectAttributes.md")` | Supported | Supported |
| `[GetObjectLegalHold](../API/API_GetObjectLegalHold.md "../API/API_GetObjectLegalHold.md")` | Supported | Not supported |
| `[GetObjectRetention](../API/API_GetObjectRetention.md "../API/API_GetObjectRetention.md")` | Supported | Not supported |
| `[GetObjectTagging](../API/API_GetObjectTagging.md "../API/API_GetObjectTagging.md")` | Supported | Supported |
| `[HeadBucket](../API/API_HeadBucket.md "../API/API_HeadBucket.md")` | Supported | Supported |
| `[HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")` | Supported | Supported |
| `[ListMultipartUploads](../API/API_ListMultipartUploads.md "../API/API_ListMultipartUploads.md")` | Supported | Supported |
| `[ListObjects](../API/API_ListObjects.md "../API/API_ListObjects.md")` | Supported | Supported |
| `[ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md")` | Supported | Supported |
| `[ListObjectVersions](../API/API_ListObjectVersions.md "../API/API_ListObjectVersions.md")` | Supported | Not supported |
| `[ListParts](../API/API_ListParts.md "../API/API_ListParts.md")` | Supported | Supported |
| `[Presign](../API/sigv4-query-string-auth.md "../API/sigv4-query-string-auth.md")` | Supported | Supported |
| `[PutObject](../API/API_PutObject.md "../API/API_PutObject.md")` | Supported | Supported |
| `[PutObjectAcl](../API/API_PutObjectAcl.md "../API/API_PutObjectAcl.md")` | Supported | Not supported |
| `[PutObjectLegalHold](../API/API_PutObjectLegalHold.md "../API/API_PutObjectLegalHold.md")` | Supported | Not supported |
| `[PutObjectRetention](../API/API_PutObjectRetention.md "../API/API_PutObjectRetention.md")` | Supported | Not supported |
| `[PutObjectTagging](../API/API_PutObjectTagging.md "../API/API_PutObjectTagging.md")` | Supported | Supported |
| `[RestoreObject](../API/API_RestoreObject.md "../API/API_RestoreObject.md")` | Supported | Not supported |
| `[UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")` | Supported | Supported |
| `[UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")` (same-Region copies only) | Supported | Supported, if source and destination are the same access point |
