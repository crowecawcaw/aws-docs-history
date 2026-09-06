

# Access point compatibility
<a name="access-points-service-api-support"></a>

You can use access points to access objects using the following subset of Amazon S3 APIs. All the operations listed below can accept either access point ARNs or access point aliases.

For examples of using access points to perform operations on objects, see [Using Amazon S3 access points for general purpose buckets](using-access-points.md).

## Access points compatibility with S3 operations
<a name="access-points-operations-support"></a>

The following table is a partial list of Amazon S3 operations and if they are compatible with access points. All operations below are supported by access points using an S3 bucket as its data source, while only some operations are supported by access points using an FSx for ONTAP or FSx for OpenZFS volume or an S3 recovery point in AWS Backup as a data source.

For more information see, access point compatibility in the [*FSx for ONTAP User Guide*](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/access-points-for-fsxn-object-api-support.html) or the [*FSx for OpenZFS User Guide*](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-object-api-support.html).


| S3 operation | Access point attached to an S3 bucket | Access point attached to an FSx for OpenZFS volume | Access point attached to an Amazon S3 recovery point in AWS Backup | 
| --- | --- | --- | --- | 
| `[AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)` | Supported | Supported | Not supported | 
| `[CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)` | Supported | Supported | Not supported | 
| `[CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)` (same-Region copies only) | Supported | Supported, if source and destination are the same access point | Not supported | 
| `[CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)` | Supported | Supported | Not supported | 
| `[DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)` | Supported | Supported | Not supported | 
| `[DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html)` | Supported | Supported | Not supported | 
| `[DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)` | Supported | Supported | Not supported | 
| `[GetBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html)` | Supported | Not supported | Not supported | 
| `[GetBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html)` | Supported | Not supported | Not supported | 
| `[GetBucketLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html)` | Supported | Supported | Supported | 
| `[GetBucketNotificationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html)` | Supported | Not supported | Not supported | 
| `[GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html)` | Supported | Not supported | Not supported | 
| `[GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)` | Supported | Supported | Supported | 
| `[GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html)` | Supported | Not supported | Not supported | 
| `[GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)` | Supported | Supported | Supported | 
| `[GetObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLegalHold.html)` | Supported | Not supported | Not supported | 
| `[GetObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectRetention.html)` | Supported | Not supported | Not supported | 
| `[GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html)` | Supported | Supported | Supported | 
| `[HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html)` | Supported | Supported | Not supported | 
| `[HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html)` | Supported | Supported | Supported | 
| `[ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html)` | Supported | Supported | Not supported | 
| `[ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html)` | Supported | Supported | Supported | 
| `[ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)` | Supported | Supported | Supported | 
| `[ListObjectVersions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html)` | Supported | Not supported | Supported | 
| `[ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)` | Supported | Supported | Not supported | 
| `[Presign](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html)` | Supported | Supported | Not supported | 
| `[PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)` | Supported | Supported | Not supported | 
| `[PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html)` | Supported | Not supported | Not supported | 
| `[PutObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLegalHold.html)` | Supported | Not supported | Not supported | 
| `[PutObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectRetention.html)` | Supported | Not supported | Not supported | 
| `[PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)` | Supported | Supported | Not supported | 
| `[RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html)` | Supported | Not supported | Not supported | 
| `[UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)` | Supported | Supported | Not supported | 
| `[UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html)` (same-Region copies only) | Supported | Supported, if source and destination are the same access point | Not supported | 