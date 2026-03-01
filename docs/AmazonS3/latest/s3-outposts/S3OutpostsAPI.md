# Amazon S3 on Outposts API operations

This topic lists the Amazon S3, Amazon S3 Control, and Amazon S3 on Outposts API operations that you can
use with Amazon S3 on Outposts.

###### Topics

- [Amazon S3 API operations for managing objects](#S3OutpostsAPIsObject "#S3OutpostsAPIsObject")
- [Amazon S3 Control API operations for managing buckets](#S3OutpostsAPIsBucket "#S3OutpostsAPIsBucket")
- [S3 on Outposts API operations for managing Outposts](#S3OutpostsAPIs "#S3OutpostsAPIs")

## Amazon S3 API operations for managing objects

S3 on Outposts is designed to use the same object API operations as Amazon S3. You must use
access points to access any object in an Outpost bucket. When you use an object API operation
with S3 on Outposts, you provide either the Outposts access point Amazon Resource Name
(ARN) or the access point alias. For more information about access point aliases, see [Using a bucket-style alias for your S3 on Outposts bucket access point](s3-outposts-access-points-alias.md "s3-outposts-access-points-alias.md").

Amazon S3 on Outposts supports the following Amazon S3 API operations:

- [AbortMultipartUpload](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")
- [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
- [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")
- [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")
- [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md")
- [DeleteObjects](../API/API_DeleteObjects.md "../API/API_DeleteObjects.md")
- [DeleteObjectTagging](../API/API_DeleteObjectTagging.md "../API/API_DeleteObjectTagging.md")
- [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")
- [GetObjectTagging](../API/API_GetObjectTagging.md "../API/API_GetObjectTagging.md")
- [HeadBucket](../API/API_HeadBucket.md "../API/API_HeadBucket.md")
- [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")
- [ListMultipartUploads](../API/API_ListMultipartUploads.md "../API/API_ListMultipartUploads.md")
- [ListObjects](../API/API_ListObjects.md "../API/API_ListObjects.md")
- [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md")
- [ListObjectVersions](../API/API_ListObjectVersions.md "../API/API_ListObjectVersions.md")
- [ListParts](../API/API_ListParts.md "../API/API_ListParts.md")
- [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")
- [PutObjectTagging](../API/API_PutObjectTagging.md "../API/API_PutObjectTagging.md")
- [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")
- [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")

## Amazon S3 Control API operations for managing buckets

S3 on Outposts supports the following Amazon S3 Control API operations for working with
buckets.

- [CreateAccessPoint](../API/API_control_CreateAccessPoint.md "../API/API_control_CreateAccessPoint.md")
- [CreateBucket](../API/API_control_CreateBucket.md "../API/API_control_CreateBucket.md")
- [DeleteAccessPoint](../API/API_control_DeleteAccessPoint.md "../API/API_control_DeleteAccessPoint.md")
- [DeleteAccessPointPolicy](../API/API_control_DeleteAccessPointPolicy.md "../API/API_control_DeleteAccessPointPolicy.md")
- [DeleteBucket](../API/API_control_DeleteBucket.md "../API/API_control_DeleteBucket.md")
- [DeleteBucketLifecycleConfiguration](../API/API_control_DeleteBucketLifecycleConfiguration.md "../API/API_control_DeleteBucketLifecycleConfiguration.md")
- [DeleteBucketPolicy](../API/API_control_DeleteBucketPolicy.md "../API/API_control_DeleteBucketPolicy.md")
- [DeleteBucketReplication](../API/API_control_DeleteBucketReplication.md "../API/API_control_DeleteBucketReplication.md")
- [DeleteBucketTagging](../API/API_control_DeleteBucketTagging.md "../API/API_control_DeleteBucketTagging.md")
- [GetAccessPoint](../API/API_control_GetAccessPoint.md "../API/API_control_GetAccessPoint.md")
- [GetAccessPointPolicy](../API/API_control_GetAccessPointPolicy.md "../API/API_control_GetAccessPointPolicy.md")
- [GetBucket](../API/API_control_GetBucket.md "../API/API_control_GetBucket.md")
- [GetBucketLifecycleConfiguration](../API/API_control_GetBucketLifecycleConfiguration.md "../API/API_control_GetBucketLifecycleConfiguration.md")
- [GetBucketPolicy](../API/API_control_GetBucketPolicy.md "../API/API_control_GetBucketPolicy.md")
- [GetBucketReplication](../API/API_control_GetBucketReplication.md "../API/API_control_GetBucketReplication.md")
- [GetBucketTagging](../API/API_control_GetBucketTagging.md "../API/API_control_GetBucketTagging.md")
- [GetBucketVersioning](../API/API_control_GetBucketVersioning.md "../API/API_control_GetBucketVersioning.md")
- [ListAccessPoints](../API/API_control_ListAccessPoints.md "../API/API_control_ListAccessPoints.md")
- [ListRegionalBuckets](../API/API_control_ListRegionalBuckets.md "../API/API_control_ListRegionalBuckets.md")
- [PutAccessPointPolicy](../API/API_control_PutAccessPointPolicy.md "../API/API_control_PutAccessPointPolicy.md")
- [PutBucketLifecycleConfiguration](../API/API_control_PutBucketLifecycleConfiguration.md "../API/API_control_PutBucketLifecycleConfiguration.md")
- [PutBucketPolicy](../API/API_control_PutBucketPolicy.md "../API/API_control_PutBucketPolicy.md")
- [PutBucketReplication](../API/API_control_PutBucketReplication.md "../API/API_control_PutBucketReplication.md")
- [PutBucketTagging](../API/API_control_PutBucketTagging.md "../API/API_control_PutBucketTagging.md")
- [PutBucketVersioning](../API/API_control_PutBucketVersioning.md "../API/API_control_PutBucketVersioning.md")

## S3 on Outposts API operations for managing Outposts

S3 on Outposts supports the following Amazon S3 on Outposts API operations for managing
endpoints.

- [CreateEndpoint](../API/API_s3outposts_CreateEndpoint.md "../API/API_s3outposts_CreateEndpoint.md")
- [DeleteEndpoint](../API/API_s3outposts_DeleteEndpoint.md "../API/API_s3outposts_DeleteEndpoint.md")
- [ListEndpoints](../API/API_s3outposts_ListEndpoints.md "../API/API_s3outposts_ListEndpoints.md")
- [ListOutpostsWithS3](../API/API_s3outposts_ListOutpostsWithS3.md "../API/API_s3outposts_ListOutpostsWithS3.md")
- [ListSharedEndpoints](../API/API_s3outposts_ListSharedEndpoints.md "../API/API_s3outposts_ListSharedEndpoints.md")
