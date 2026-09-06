

# Logging with AWS CloudTrail for directory buckets
<a name="s3-express-one-zone-logging"></a>

 Amazon S3 is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all API calls for Amazon S3 as events. Using the information collected by CloudTrail, you can determine the request that was made to Amazon S3, the IP address from which the request was made, when it was made, and additional details. When a supported event activity occurs in Amazon S3, that activity is recorded in a CloudTrail event. You can use AWS CloudTrail trail to log management events and data events for directory buckets. For more information, see [Amazon S3 CloudTrail events](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-logging-s3-info.html) and [What is AWS CloudTrail? ](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) in the *AWS CloudTrail User Guide*.

## CloudTrail management events for directory buckets
<a name="s3-express-management"></a>

 By default, CloudTrail logs bucket-level actions for directory buckets as management events. The `eventsource` for CloudTrail management events for directory buckets is `s3express.amazonaws.com`. When you set up your AWS account, CloudTrail management events are enabled by default. The following Regional endpoint API operations (bucket-level, or control plane, API operations) are logged to CloudTrail. 
+ [`CreateBucket`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
+ [`DeleteBucket`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)
+ [`DeleteBucketPolicy`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html)
+ [`PutBucketPolicy`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html)
+ [`GetBucketPolicy`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html)
+ [`ListDirectoryBuckets`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html)
+ [`ListMultipartUploads`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html)
+ [`GetBucketEncryption`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html)
+ [`PutBucketEncryption`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html)
+ [`DeleteBucketEncryption`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html)

**Note**  
 `ListMultipartUploads` is a Zonal endpoint API operation. However, this API operation is logged to CloudTrail as a management event. For more information, see [`ListMultipartUploads`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html) in the *Amazon Simple Storage Service API Reference*.

For more information on CloudTrail management events, see [Logging management events ](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide.*

## CloudTrail data events for directory buckets
<a name="s3-express-data-events"></a>

Data events provide information about the resource operations performed on or in a resource (for example, reading or writing to an Amazon S3 object). These are also known as data plane operations. Data events are often high-volume activities. By default, CloudTrail trails don't log data events, but you can configure trails to log data events for objects stored in general purpose buckets and directory buckets. For more information, see [Enable logging for objects in a bucket using the console ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.html#enable-cloudtrail-events).

When you log data events for a trail in CloudTrail, you can choose to use advanced event selectors or basic event selectors. To log data events for objects stored in directory buckets, you must use advanced event selectors. When configuring advanced resource selectors, you will choose or specify the resource type which is `AWS::S3Express::Object`. 

The following Zonal endpoint API operations (object-level , or. data plane, API operations) are logged to CloudTrail. 
+ [`AbortMultipartUpload`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)
+ [`CompleteMultipartUpload`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)
+ [`CreateSession`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html)
+ [`CopyObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)
+ [`CreateMultipartUpload`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)
+ [`DeleteObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)
+ [`DeleteObjects`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html)
+ [`GetObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
+ [`GetObjectAttributes`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)
+ [`HeadBucket`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html)
+ [`HeadObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html)
+ [`ListObjectsV2`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)
+ [`ListParts`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)
+ [`PutObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
+ [`RenameObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RenameObject.html)
+ [`UploadPart`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)
+ [`UploadPartCopy`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html)

For more information on CloudTrail data events, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*. 

For additional information about CloudTrail events for directory buckets, see the following topics: 

**Topics**
+ [CloudTrail management events for directory buckets](#s3-express-management)
+ [CloudTrail data events for directory buckets](#s3-express-data-events)
+ [CloudTrail log file examples for directory buckets](s3-express-log-files.md)