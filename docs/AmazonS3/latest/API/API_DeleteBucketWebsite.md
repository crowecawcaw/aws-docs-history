# DeleteBucketWebsite

###### Note

This operation is not supported for directory buckets.

This action removes the website configuration for a bucket. Amazon S3 returns a `200 OK`
 response upon successfully deleting a website configuration on the specified bucket. You will get a
 `200 OK` response if the website configuration you are trying to delete does not exist on
 the bucket. Amazon S3 returns a `404` response if the bucket specified in the request does not
 exist.

This DELETE action requires the `S3:DeleteBucketWebsite` permission. By default, only the
 bucket owner can delete the website configuration attached to a bucket. However, bucket owners can grant
 other users permission to delete the website configuration by writing a bucket policy granting them the
 `S3:DeleteBucketWebsite` permission. 

For more information about hosting websites, see [Hosting Websites on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html"). 

The following operations are related to `DeleteBucketWebsite`:


* [GetBucketWebsite](API_GetBucketWebsite.md "API_GetBucketWebsite.md")
* [PutBucketWebsite](API_PutBucketWebsite.md "API_PutBucketWebsite.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /?website HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_DeleteBucketWebsite_RequestSyntax "#API_DeleteBucketWebsite_RequestSyntax")**


The bucket name for which you want to remove the website configuration. 


Required: Yes




**[x-amz-expected-bucket-owner](#API_DeleteBucketWebsite_RequestSyntax "#API_DeleteBucketWebsite_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


## Examples


### Sample Request


This request deletes the website configuration on the specified bucket.



```

            DELETE ?website HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Thu, 27 Jan 2011 12:00:00 GMT
            Authorization: signatureValue
         
```

### Sample Response


This example illustrates one usage of DeleteBucketWebsite.



```

         HTTP/1.1 204 No Content
         x-amz-id-2: aws-s3integ-s3ws-31008.sea31.amazon.com
         x-amz-request-id: AF1DD829D3B49707
         Date: Thu, 03 Feb 2011 22:10:26 GMT
         Server: AmazonS3
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketWebsite "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketWebsite")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketWebsite "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketWebsite")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketWebsite "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketWebsite")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketWebsite "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketWebsite")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketWebsite "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketWebsite")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketWebsite "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketWebsite")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketWebsite "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketWebsite")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketWebsite "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketWebsite")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketWebsite "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketWebsite")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketWebsite "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketWebsite")
