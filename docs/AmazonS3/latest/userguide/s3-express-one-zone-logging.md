# Logging with AWS CloudTrail for directory buckets

 Amazon S3 is integrated with AWS CloudTrail, a service that provides a record of actions
 taken by a user, role, or an AWS service. CloudTrail captures all API calls for Amazon S3
 as events. Using the information collected by CloudTrail, you can determine the request that
 was made to Amazon S3, the IP address from which the request was made, when it was made, and
 additional details. When a supported event activity occurs in Amazon S3, that activity is
 recorded in a CloudTrail event. You can use AWS CloudTrail trail to log management events
 and data events for directory buckets. For more information, see [Amazon S3 CloudTrail events](cloudtrail-logging-s3-info.md "cloudtrail-logging-s3-info.md") and [What is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html")  in the *AWS CloudTrail User
 Guide*.


## CloudTrail management events for directory
 buckets


 By default, CloudTrail logs bucket-level actions for directory buckets as management
 events. The `eventsource` for CloudTrail management events for directory buckets is `s3express.amazonaws.com`. 
 When you set up your AWS account,
 CloudTrail management events are enabled by default. The following Regional endpoint API
 operations (bucket-level, or control plane, API operations) are logged to CloudTrail. 



* [`CreateBucket`](../API/API_CreateBucket.md "../API/API_CreateBucket.md")
* [`DeleteBucket`](../API/API_DeleteBucket.md "../API/API_DeleteBucket.md")
* [`DeleteBucketPolicy`](../API/API_DeleteBucketPolicy.md "../API/API_DeleteBucketPolicy.md")
* [`PutBucketPolicy`](../API/API_PutBucketPolicy.md "../API/API_PutBucketPolicy.md")
* [`GetBucketPolicy`](../API/API_GetBucketPolicy.md "../API/API_GetBucketPolicy.md")
* [`ListDirectoryBuckets`](../API/API_ListDirectoryBuckets.md "../API/API_ListDirectoryBuckets.md")
* [`ListMultipartUploads`](../API/API_ListMultipartUploads.md "../API/API_ListMultipartUploads.md")
* [`GetBucketEncryption`](../API/API_GetBucketEncryption.md "../API/API_GetBucketEncryption.md")
* [`PutBucketEncryption`](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md")
* [`DeleteBucketEncryption`](../API/API_DeleteBucketEncryption.md "../API/API_DeleteBucketEncryption.md")

###### Note


`ListMultipartUploads` is a Zonal endpoint API operation. However, this
 API operation is logged to CloudTrail as a management event. For more information,
 see [`ListMultipartUploads`](../API/API_ListMultipartUploads.md "../API/API_ListMultipartUploads.md") in the *Amazon Simple
 Storage Service API Reference*.


For more information on CloudTrail management events, see [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html")  in the *AWS CloudTrail User
 Guide.*


## CloudTrail data events for directory
 buckets


Data events provide information about the resource operations performed on or in a
 resource (for example, reading or writing to an Amazon S3 object). These are also known
 as data plane operations. Data events are often high-volume activities. By default,
 CloudTrail trails don't log data events, but you can configure trails to log data events
 for objects stored in general purpose buckets and directory buckets. For more
 information, see [Enable logging for objects in a bucket using the console](enable-cloudtrail-logging-for-s3.md#enable-cloudtrail-events "enable-cloudtrail-logging-for-s3.md#enable-cloudtrail-events") .


When you log data events for a trail in CloudTrail, you can choose to use advanced
 event selectors or basic event selectors. To log data events for objects stored in
 directory buckets, you must use advanced event selectors. When configuring advanced
 resource selectors, you will choose or specify the resource type 
 which is `AWS::S3Express::Object`. 


The following Zonal endpoint API operations (object-level , or. data plane, API
 operations) are logged to CloudTrail. 



* [`AbortMultipartUpload`](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")
* [`CompleteMultipartUpload`](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
* [`CreateSession`](../API/API_CreateSession.md "../API/API_CreateSession.md")
* [`CopyObject`](../API/API_CopyObject.md "../API/API_CopyObject.md")
* [`CreateMultipartUpload`](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")
* [`DeleteObject`](../API/API_DeleteObject.md "../API/API_DeleteObject.md")
* [`DeleteObjects`](../API/API_DeleteObjects.md "../API/API_DeleteObjects.md")
* [`GetObject`](../API/API_GetObject.md "../API/API_GetObject.md")
* [`GetObjectAttributes`](../API/API_GetObjectAttributes.md "../API/API_GetObjectAttributes.md")
* [`HeadBucket`](../API/API_HeadBucket.md "../API/API_HeadBucket.md")
* [`HeadObject`](../API/API_HeadObject.md "../API/API_HeadObject.md")
* [`ListObjectsV2`](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md")
* [`ListParts`](../API/API_ListParts.md "../API/API_ListParts.md")
* [`PutObject`](../API/API_PutObject.md "../API/API_PutObject.md")
* [`RenameObject`](../API/API_RenameObject.md "../API/API_RenameObject.md")
* [`UploadPart`](../API/API_UploadPart.md "../API/API_UploadPart.md")
* [`UploadPartCopy`](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")

For more information on CloudTrail data events, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html") in the *AWS CloudTrail User
 Guide*. 


For additional information about CloudTrail events for directory buckets, see the
 following topics: 

###### Topics

* [CloudTrail log file examples for directory buckets](s3-express-log-files.md "s3-express-log-files.md")
