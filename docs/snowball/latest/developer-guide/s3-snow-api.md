Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Supported REST API actions for Amazon S3 compatible storage on Snowball Edge

The following lists show the API operations that are supported by Amazon S3 compatible storage on Snowball Edge, including
links to the related operations for Amazon S3 in AWS Regions.

Supported bucket API operations for the s3api endpoint:

- [CreateBucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html")
- [DeleteBucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket.html")
- [DeleteBucketLifecycle](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-lifecycle.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-lifecycle.html")
- [GetBucketLifecycleConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-lifecycle-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-lifecycle-configuration.html")
- [ListBuckets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-buckets.html " https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-buckets.html")
- [PutBucketLifecycleConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-lifecycle-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-lifecycle-configuration.html")
  Supported bucket API operations for the s3control endpoint:

- [CreateBucket](../../../AmazonS3/latest/API/API_CreateBucket.md "../../../AmazonS3/latest/API/API_CreateBucket.md")
- [DeleteBucket](../../../AmazonS3/latest/API/API_control_DeleteBucket.md "../../../AmazonS3/latest/API/API_control_DeleteBucket.md")
- [DeleteBucketLifecycle](../../../AmazonS3/latest/API/API_DeleteBucketLifecycle.md "../../../AmazonS3/latest/API/API_DeleteBucketLifecycle.md")
- [GetBucket](../../../AmazonS3/latest/API/API_control_GetBucket.md "../../../AmazonS3/latest/API/API_control_GetBucket.md")
- [GetBucketLifecycleConfiguration](../../../AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.md "../../../AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.md")
- [ListBuckets](../../../AmazonS3/latest/API/API_control_ListRegionalBuckets.md "../../../AmazonS3/latest/API/API_control_ListRegionalBuckets.md")
- [PutBucketLifecycleConfiguration](../../../AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.md "../../../AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.md")
  Supported object API operations:

- [AbortMultipartUpload](../../../AmazonS3/latest/API/API_AbortMultipartUpload.md "../../../AmazonS3/latest/API/API_AbortMultipartUpload.md")
- [CompleteMultipartUpload](../../../AmazonS3/latest/API/API_CompleteMultipartUpload.md "../../../AmazonS3/latest/API/API_CompleteMultipartUpload.md")
- [CopyObject](../../../AmazonS3/latest/API/API_CopyObject.md "../../../AmazonS3/latest/API/API_CopyObject.md")
- [CreateMultipartUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-bucket.html")
- [DeleteObject](../../../AmazonS3/latest/API/API_DeleteObject.md "../../../AmazonS3/latest/API/API_DeleteObject.md")
- [DeleteObjects](../../../AmazonS3/latest/API/API_DeleteObjects.md "../../../AmazonS3/latest/API/API_DeleteObjects.md")
- [DeleteObjectTagging](../../../AmazonS3/latest/API/API_DeleteObjectTagging.md "../../../AmazonS3/latest/API/API_DeleteObjectTagging.md")
- [GetObject](../../../AmazonS3/latest/API/API_GetObject.md "../../../AmazonS3/latest/API/API_GetObject.md")
- [GetObjectTagging](../../../AmazonS3/latest/API/API_GetObjectTagging.md "../../../AmazonS3/latest/API/API_GetObjectTagging.md")
- [HeadBucket](../../../AmazonS3/latest/API/API_HeadBucket.md "../../../AmazonS3/latest/API/API_HeadBucket.md")
- [HeadObject](../../../AmazonS3/latest/API/API_HeadObject.md "../../../AmazonS3/latest/API/API_HeadObject.md")
- [ListMultipartUploads](../../../AmazonS3/latest/API/API_ListMultipartUploads.md "../../../AmazonS3/latest/API/API_ListMultipartUploads.md")
- [ListObjects](../../../AmazonS3/latest/API/API_ListObjects.md "../../../AmazonS3/latest/API/API_ListObjects.md")
- [ListObjectsV2](../../../AmazonS3/latest/API/API_ListObjectsV2.md "../../../AmazonS3/latest/API/API_ListObjectsV2.md")
- [ListParts](../../../AmazonS3/latest/API/API_ListParts.md "../../../AmazonS3/latest/API/API_ListParts.md")
- [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md")
- [PutObjectTagging](../../../AmazonS3/latest/API/API_PutObjectTagging.md "../../../AmazonS3/latest/API/API_PutObjectTagging.md")
- [UploadPart](../../../AmazonS3/latest/API/API_UploadPart.md "../../../AmazonS3/latest/API/API_UploadPart.md")
- [UploadPartCopy](../../../AmazonS3/latest/API/API_UploadPartCopy.md "../../../AmazonS3/latest/API/API_UploadPartCopy.md")
