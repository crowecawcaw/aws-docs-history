

# Access point compatibility
<a name="access-points-object-api-support"></a>

You can use access points to access data stored on an FSx for OpenZFS volume using the following subset of Amazon S3 API object operations related to data access. All the operations listed below can accept either access point ARNs or access point aliases.

The following table is a partial list of Amazon S3 operations and if they are compatible with access points. The table shows which operations are supported by access points using an FSx for OpenZFS volume as a data source.


| S3 operation | Access point attached to an FSx for OpenZFS volume | 
| --- | --- | 
| `[AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)` | Supported | 
| `[CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)` | Supported | 
| `[CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)` (same-Region copies only) | Supported, if source and destination are the same access point. The `x-amz-object-annotation-directive` header is not supported. | 
| `[CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)` | Supported | 
| `[DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)` | Supported | 
| `[DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html)` | Supported | 
| `[DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html)` | Supported | 
| `[DeleteObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectAnnotation.html)` | Not supported | 
| `[GetBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html)` | Not supported | 
| `[GetBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html)` | Not supported | 
| `[GetBucketLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html)` | Supported | 
| `[GetBucketNotificationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html)` | Not supported | 
| `[GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html)` | Not supported | 
| `[GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)` | Supported | 
| `[GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html)` | Not supported | 
| `[GetObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAnnotation.html)` | Not supported | 
| `[GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)` | Supported | 
| `[GetObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLegalHold.html)` | Not supported | 
| `[GetObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectRetention.html)` | Not supported | 
| `[GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html)` | Supported | 
| `[HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html)` | Supported | 
| `[HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html)` | Supported | 
| `[ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html)` | Supported | 
| `[ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html)` | Supported | 
| `[ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)` | Supported | 
| `[ListObjectVersions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html)` | Not supported | 
| `[ListObjectAnnotations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectAnnotations.html)` | Not supported | 
| `[ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)` | Supported | 
| `[Presign](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html)` | Not supported | 
| `[PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)` | Supported | 
| `[PutObjectAnnotation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAnnotation.html)` | Not supported | 
| `[PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html)` | Not supported | 
| `[PutObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLegalHold.html)` | Not supported | 
| `[PutObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectRetention.html)` | Not supported | 
| `[PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)` | Supported | 
| `[RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html)` | Not supported | 
| `[UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)` | Supported | 
| `[UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html)` (same-Region copies only) | Supported, if source and destination are the same access point | 

Limitations to using Amazon S3 operations are the following:
+ Maximum object size is 50 GB
+ `FSX_OPENZFS` is the only supported storage class
+ [SSE\_FSX](s3-ap-manage-access-fsx.md#data-encryption) is the only supported server-side encryption mode
+ The following Amazon S3 features are not supported: Object Annotations

For examples of using access points to perform data access operations on file data, see [Using access points](access-points-usage-examples.md).