

# Directory bucket API operations
<a name="s3-express-APIs"></a>

To manage directory buckets, you can use Regional (bucket level, or control plane) endpoint API operations. To manage objects in your directory buckets, you can use Zonal (object level, or data plane) endpoint API operations. For more information, see [Networking for directory buckets](s3-express-networking.md) and [Endpoints and gateway VPC endpoints](directory-bucket-high-performance.md#s3-express-overview-endpoints).

**Regional endpoint API operations**  
The following Regional endpoint API operations are supported for directory buckets: 
+ [CreateAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html)
+ [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
+ [DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html)
+ [DeleteAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html)
+ [DeleteAccessPointScope](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointScope.html)
+ [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)
+ [DeleteBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketInventoryConfiguration.html)
+ [DeleteBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html)
+ [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html)
+ [GetAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html)
+ [GetAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html)
+ [GetAccessPointScope](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointScope.html)
+ [GetBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html)
+ [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)
+ [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html)
+ [ListAccessPointsForDirectoryBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForDirectoryBuckets.html)
+ [ListBucketInventoryConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketInventoryConfigurations.html)
+ [ListDirectoryBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html)
+ [ListTagsForResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListTagsForResource.html)
+ [PutAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html)
+ [PutAccessPointScope](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointScope.html)
+ [PutBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketInventoryConfiguration.html)
+ [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)
+ [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html)
+ [DeleteBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html)
+ [GetBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html)
+ [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html)
+ [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html)

**Zonal endpoint API operations**  
The following Zonal endpoint API operations are supported for directory buckets: 
+ [CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html)
+ [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)
+ [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)
+ [DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html)
+ [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
+ [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)
+ [HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html)
+ [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html)
+ [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)
+ [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
+ [RenameObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RenameObject.html)
+ [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)
+ [CompleteMultiPartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)
+ [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)
+ [ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads)
+ [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)
+ [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)
+ [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html)