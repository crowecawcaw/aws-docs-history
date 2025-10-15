# CreateBucket

###### Note

This action creates an Amazon S3 on Outposts bucket. To create an S3 bucket, see [Create
 Bucket](API_CreateBucket.md "API_CreateBucket.md") in the *Amazon S3 API Reference*. 

Creates a new Outposts bucket. By creating the bucket, you become the bucket owner. To
 create an Outposts bucket, you must have S3 on Outposts. For more information, see [Using
 Amazon S3 on Outposts](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in *Amazon S3 User Guide*.

Not every string is an acceptable bucket name. For information on bucket naming
 restrictions, see [Working with
 Amazon S3 Buckets](../userguide/BucketRestrictions.md#bucketnamingrules "../userguide/BucketRestrictions.md#bucketnamingrules").

S3 on Outposts buckets support:


* Tags
* LifecycleConfigurations for deleting expired objects
For a complete list of restrictions and Amazon S3 feature limitations on S3 on Outposts, see
 [Amazon S3 on Outposts Restrictions and Limitations](../userguide/S3OnOutpostsRestrictionsLimitations.md "../userguide/S3OnOutpostsRestrictionsLimitations.md").

For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts
 endpoint hostname prefix and `x-amz-outpost-id` in your API request, see the
 [Examples](API_control_CreateBucket.md#API_control_CreateBucket_Examples "API_control_CreateBucket.md#API_control_CreateBucket_Examples") section.

The following actions are related to `CreateBucket` for
 Amazon S3 on Outposts:


* [PutObject](API_PutObject.md "API_PutObject.md")
* [GetBucket](API_control_GetBucket.md "API_control_GetBucket.md")
* [DeleteBucket](API_control_DeleteBucket.md "API_control_DeleteBucket.md")
* [CreateAccessPoint](API_control_CreateAccessPoint.md "API_control_CreateAccessPoint.md")
* [PutAccessPointPolicy](API_control_PutAccessPointPolicy.md "API_control_PutAccessPointPolicy.md")

## Request Syntax



```
PUT /v20180820/bucket/`name` HTTP/1.1
Host: `Bucket`.s3-control.amazonaws.com
x-amz-acl: `ACL`
x-amz-grant-full-control: `GrantFullControl`
x-amz-grant-read: `GrantRead`
x-amz-grant-read-acp: `GrantReadACP`
x-amz-grant-write: `GrantWrite`
x-amz-grant-write-acp: `GrantWriteACP`
x-amz-bucket-object-lock-enabled: `ObjectLockEnabledForBucket`
x-amz-outpost-id: `OutpostId`
<?xml version="1.0" encoding="UTF-8"?>
<[CreateBucketConfiguration](#AmazonS3-control_CreateBucket-request-CreateBucketConfiguration "#AmazonS3-control_CreateBucket-request-CreateBucketConfiguration") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[LocationConstraint](#AmazonS3-control_CreateBucket-request-LocationConstraint "#AmazonS3-control_CreateBucket-request-LocationConstraint")>`string`</[LocationConstraint](#AmazonS3-control_CreateBucket-request-LocationConstraint "#AmazonS3-control_CreateBucket-request-LocationConstraint")>
</[CreateBucketConfiguration](#AmazonS3-control_CreateBucket-request-CreateBucketConfiguration "#AmazonS3-control_CreateBucket-request-CreateBucketConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_CreateBucket_RequestSyntax "#API_control_CreateBucket_RequestSyntax")**


The name of the bucket.


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-acl](#API_control_CreateBucket_RequestSyntax "#API_control_CreateBucket_RequestSyntax")**


The canned ACL to apply to the bucket.


###### Note

This is not supported by Amazon S3 on Outposts buckets.


Valid Values: `private | public-read | public-read-write | authenticated-read`





**[x-amz-bucket-object-lock-enabled](#API_control_CreateBucket_RequestSyntax "#API_control_CreateBucket_RequestSyntax")**


Specifies whether you want S3 Object Lock to be enabled for the new bucket.


###### Note

This is not supported by Amazon S3 on Outposts buckets.




**[x-amz-grant-full-control](#API_control_CreateBucket_RequestSyntax "#API_control_CreateBucket_RequestSyntax")**


Allows grantee the read, write, read ACP, and write ACP permissions on the
 bucket.


###### Note

This is not supported by Amazon S3 on Outposts buckets.




**[x-amz-grant-read](#API_control_CreateBucket_RequestSyntax "#API_control_CreateBucket_RequestSyntax")**


Allows grantee to list the objects in the bucket.


###### Note

This is not supported by Amazon S3 on Outposts buckets.




**[x-amz-grant-read-acp](#API_control_CreateBucket_RequestSyntax "#API_control_CreateBucket_RequestSyntax")**


Allows grantee to read the bucket ACL.


###### Note

This is not supported by Amazon S3 on Outposts buckets.




**[x-amz-grant-write](#API_control_CreateBucket_RequestSyntax "#API_control_CreateBucket_RequestSyntax")**


Allows grantee to create, overwrite, and delete any object in the bucket.


###### Note

This is not supported by Amazon S3 on Outposts buckets.




**[x-amz-grant-write-acp](#API_control_CreateBucket_RequestSyntax "#API_control_CreateBucket_RequestSyntax")**


Allows grantee to write the ACL for the applicable bucket.


###### Note

This is not supported by Amazon S3 on Outposts buckets.




**[x-amz-outpost-id](#API_control_CreateBucket_RequestSyntax "#API_control_CreateBucket_RequestSyntax")**


The ID of the Outposts where the bucket is being created.


###### Note

This ID is required by Amazon S3 on Outposts buckets.


Length Constraints: Minimum length of 1. Maximum length of 64.




## Request Body


The request accepts the following data in XML format.





**[CreateBucketConfiguration](#API_control_CreateBucket_RequestSyntax "#API_control_CreateBucket_RequestSyntax")**


Root level tag for the CreateBucketConfiguration parameters.


Required: Yes




**[LocationConstraint](#API_control_CreateBucket_RequestSyntax "#API_control_CreateBucket_RequestSyntax")**


Specifies the Region where the bucket will be created. If you are creating a bucket on
 the US East (N. Virginia) Region (us-east-1), you do not need to specify the location. 


###### Note

This is not supported by Amazon S3 on Outposts buckets.


Type: String


Valid Values: `EU | eu-west-1 | us-west-1 | us-west-2 | ap-south-1 | ap-southeast-1 | ap-southeast-2 | ap-northeast-1 | sa-east-1 | cn-north-1 | eu-central-1`



Required: No




## Response Syntax



```
HTTP/1.1 200
Location: `Location`
<?xml version="1.0" encoding="UTF-8"?>
<[CreateBucketResult](#AmazonS3-control_CreateBucket-response-CreateBucketResult "#AmazonS3-control_CreateBucket-response-CreateBucketResult")>
   <[BucketArn](#AmazonS3-control_CreateBucket-response-BucketArn "#AmazonS3-control_CreateBucket-response-BucketArn")>***string***</[BucketArn](#AmazonS3-control_CreateBucket-response-BucketArn "#AmazonS3-control_CreateBucket-response-BucketArn")>
</[CreateBucketResult](#AmazonS3-control_CreateBucket-response-CreateBucketResult "#AmazonS3-control_CreateBucket-response-CreateBucketResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[Location](#API_control_CreateBucket_ResponseSyntax "#API_control_CreateBucket_ResponseSyntax")**


The location of the bucket.




The following data is returned in XML format by the service.





**[CreateBucketResult](#API_control_CreateBucket_ResponseSyntax "#API_control_CreateBucket_ResponseSyntax")**


Root level tag for the CreateBucketResult parameters.


Required: Yes




**[BucketArn](#API_control_CreateBucket_ResponseSyntax "#API_control_CreateBucket_ResponseSyntax")**


The Amazon Resource Name (ARN) of the bucket.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded. 


Type: String


Length Constraints: Minimum length of 4. Maximum length of 128.




## Errors





**BucketAlreadyExists** 


The requested Outposts bucket name is not available. The bucket namespace is shared by
 all users of the AWS Outposts in this Region. Select a different name and try
 again.


HTTP Status Code: 400




**BucketAlreadyOwnedByYou** 


The Outposts bucket you tried to create already exists, and you own it. 


HTTP Status Code: 400




## Examples


### Sample request to create an Amazon S3 on Outposts bucket


This request creates an Outposts bucket named
 `example-outpost-bucket`.



```

            PUT /v20180820/bucket/example-outpost-bucket/  HTTP/1.1
            Host:s3-outposts.<Region>.amazonaws.com
            x-amz-outpost-id: op-01ac5d28a6a232904
            Content-Length: 
            Date: Wed, 01 Mar  2006 12:00:00 GMT
            Authorization: authorization string
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateBucket "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateBucket")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateBucket "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateBucket")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateBucket "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateBucket")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateBucket "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateBucket")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateBucket "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateBucket")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateBucket "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateBucket")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateBucket "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateBucket")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateBucket "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateBucket")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateBucket "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateBucket")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateBucket "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateBucket")
