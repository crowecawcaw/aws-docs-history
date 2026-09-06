

# Access point compatibility
<a name="access-points-for-fsxn-object-api-support"></a>

You can use access points to access data stored on an FSx for ONTAP volume using the following Amazon S3 APIs for data acccess. All the operations listed below can accept either access point ARNs or access point aliases.

The following table is a partial list of Amazon S3 operations and if they are compatible with access points. The table shows which operations are supported by access points using an FSx for ONTAP volume as a data source.


| S3 operation | Access point attached to an FSx for ONTAP volume | 
| --- | --- | 
| `[AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)` | Supported | 
| `[CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)` | Supported | 
| `[CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)` (same-Region copies only) | Supported, if source and destination are within the same access point. The `x-amz-object-annotation-directive` header is not supported. | 
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
| `[UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html)` (same-Region copies only) | Supported, if source and destination are within the same access point | 

Limitations to using Amazon S3 operations are the following:
+ Maximum object size is 50 GiB for uploads, but you can download objects larger than that
+ `FSX_ONTAP` is the only supported storage class
+ SSE-FSX is the only supported server-side encryption mode
+ The following Amazon S3 features are not supported: access control lists (ACLs) other than `bucket-owner-full-control`, Object Annotations, Requester Pays, Object Versioning, Object Lock, Object Lifecycle, Static Website Hosting (e.g., website redirection), multi-factor authentication (MFA), and conditional writes

For examples of using access points to perform data access operations on file data, see [Using access points](access-points-for-fsxn-usage-examples.md).

**Object ETag**  
The entity tag is a hash of the object. The ETag reflects changes only to the contents of an object, not its metadata. The ETag is not an MD5 digest of the object data.

**Object Checksums**  
You can use checksum values to verify the integrity of the data that you upload. When you upload data and specify a checksum algorithm, the AWS SDK uses your chosen checksum algorithm to compute a checksum value before data transmission. Amazon S3 then independently calculates a checksum of your data and validates it against the provided checksum value. Objects are accepted only after confirming data integrity was maintained during transit to Amazon S3. Unlike with checksums for objects in Amazon S3 General Purpose buckets, the checksum value is not stored in the FSx for NetApp ONTAP volume as object metadata and the object itself. This means that the checksum values are not returned in the response and are not used to verify object integrity on download.

**Server-side encryption with Amazon FSx (SSE-FSX)**  
All Amazon FSx file systems have encryption configured by default and are encrypted at rest with keys managed using AWS Key Management Service. Data is automatically encrypted and decrypted on the file system as data is being written to and read from the file system. These processes are handled transparently by Amazon FSx.

**Multipart upload**  
Multipart upload allows you to upload a single object as a set of parts. Each part is a contiguous portion of the object's data. You can upload these object parts independently, and in any order. Multipart upload has the following considerations when using S3 access points with FSx for ONTAP: 
+ The parts associated with in-progress multipart uploads (i.e. incomplete uploads) are not included in FSx for ONTAP volume backups.
+ The used storage associated with in-progress multipart upload (i.e. incomplete upload) parts is not reflected in the destination volume’s `StorageUsed` storage capacity CloudWatch metric but is reflected in the parent file system’s `StorageUsed` storage capacity CloudWatch metric.
+ Once a multipart upload operation is complete, the associated part metadata is no longer stored with the object. This means you cannot retrieve object part metdata using `GetObjectAttributes` or download a single part of an object by the part number of the object being read.

**Access Control List (ACL)**  
Amazon S3 access control lists (ACLs) enable you to manage access to buckets and objects. S3 access points for FSx only support the `bucket-owner-full-control` ACL value. Using any other ACL value will result in a `InvalidArgument` exception.