# Directory bucket API operations

To manage directory buckets, you can use Regional (bucket level, or control plane) endpoint API operations. To manage objects in
your directory buckets, you can use Zonal (object level, or data plane) endpoint API operations. For more information, see [Networking for directory buckets](s3-express-networking.md "s3-express-networking.md") and [Endpoints and gateway VPC endpoints](directory-bucket-high-performance.md#s3-express-overview-endpoints "directory-bucket-high-performance.md#s3-express-overview-endpoints").

###### Regional endpoint API operations

The following Regional endpoint API operations are supported for directory buckets:

- [CreateAccessPoint](../API/API_control_CreateAccessPoint.md "../API/API_control_CreateAccessPoint.md")
- [CreateBucket](../API/API_CreateBucket.md "../API/API_CreateBucket.md")
- [DeleteAccessPoint](../API/API_control_DeleteAccessPoint.md "../API/API_control_DeleteAccessPoint.md")
- [DeleteAccessPointPolicy](../API/API_control_DeleteAccessPointPolicy.md "../API/API_control_DeleteAccessPointPolicy.md")
- [DeleteAccessPointScope](../API/API_control_DeleteAccessPointScope.md "../API/API_control_DeleteAccessPointScope.md")
- [DeleteBucket](../API/API_DeleteBucket.md "../API/API_DeleteBucket.md")
- [DeleteBucketLifecycle](../API/API_DeleteBucketLifecycle.md "../API/API_DeleteBucketLifecycle.md")
- [DeleteBucketPolicy](../API/API_DeleteBucketPolicy.md "../API/API_DeleteBucketPolicy.md")
- [GetAccessPoint](../API/API_control_GetAccessPoint.md "../API/API_control_GetAccessPoint.md")
- [GetAccessPointPolicy](../API/API_control_GetAccessPointPolicy.md "../API/API_control_GetAccessPointPolicy.md")
- [GetAccessPointScope](../API/API_control_GetAccessPointScope.md "../API/API_control_GetAccessPointScope.md")
- [GetBucketLifecycleConfiguration](../API/API_GetBucketLifecycleConfiguration.md "../API/API_GetBucketLifecycleConfiguration.md")
- [GetBucketPolicy](../API/API_GetBucketPolicy.md "../API/API_GetBucketPolicy.md")
- [ListAccessPointsForDirectoryBuckets](../API/API_control_ListAccessPointsForDirectoryBuckets.md "../API/API_control_ListAccessPointsForDirectoryBuckets.md")
- [ListDirectoryBuckets](../API/API_ListDirectoryBuckets.md "../API/API_ListDirectoryBuckets.md")
- [ListTagsForResource](../API/API_control_ListTagsForResource.md "../API/API_control_ListTagsForResource.md")
- [PutAccessPointPolicy](../API/API_control_PutAccessPointPolicy.md "../API/API_control_PutAccessPointPolicy.md")
- [PutAccessPointScope](../API/API_control_PutAccessPointScope.md "../API/API_control_PutAccessPointScope.md")
- [PutBucketLifecycleConfiguration](../API/API_PutBucketLifecycleConfiguration.md "../API/API_PutBucketLifecycleConfiguration.md")
- [PutBucketPolicy](../API/API_PutBucketPolicy.md "../API/API_PutBucketPolicy.md")
- [DeleteBucketEncryption](../API/API_DeleteBucketEncryption.md "../API/API_DeleteBucketEncryption.md")
- [GetBucketEncryption](../API/API_GetBucketEncryption.md "../API/API_GetBucketEncryption.md")
- [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md")
- [TagResource](../API/API_control_TagResource.md "../API/API_control_TagResource.md")
- [UntagResource](../API/API_control_UntagResource.md "../API/API_control_UntagResource.md")

###### Zonal endpoint API operations

The following Zonal endpoint API operations are supported for directory buckets:

- [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md")
- [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")
- [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md")
- [DeleteObjects](../API/API_DeleteObjects.md "../API/API_DeleteObjects.md")
- [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")
- [GetObjectAttributes](../API/API_GetObjectAttributes.md "../API/API_GetObjectAttributes.md")
- [HeadBucket](../API/API_HeadBucket.md "../API/API_HeadBucket.md")
- [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")
- [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md")
- [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")
- [RenameObject](../API/API_RenameObject.md "../API/API_RenameObject.md")
- [AbortMultipartUpload](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")
- [CompleteMultiPartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
- [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")
- [ListMultipartUploads](../API/API_ListMultipartUploads.md "../API/API_ListMultipartUploads.md")
- [ListParts](../API/API_ListParts.md "../API/API_ListParts.md")
- [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")
- [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")
