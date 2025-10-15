# DeleteBucketTagging

###### Note

This operation is not supported for directory buckets.

Deletes the tags from the bucket.

To use this operation, you must have permission to perform the `s3:PutBucketTagging`
 action. By default, the bucket owner has this permission and can grant this permission to others. 

The following operations are related to `DeleteBucketTagging`:


* [GetBucketTagging](API_GetBucketTagging.md "API_GetBucketTagging.md")
* [PutBucketTagging](API_PutBucketTagging.md "API_PutBucketTagging.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /?tagging HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_DeleteBucketTagging_RequestSyntax "#API_DeleteBucketTagging_RequestSyntax")**


The bucket that has the tag set to be removed.


Required: Yes




**[x-amz-expected-bucket-owner](#API_DeleteBucketTagging_RequestSyntax "#API_DeleteBucketTagging_RequestSyntax")**


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


The following DELETE request deletes the tag set from the specified bucket. 



```

            DELETE /?tagging HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com  
            Date: Wed, 14 Dec 2011 05:37:16 GMT
            Authorization: signatureValue 
         
```

### Sample Response


The following successful response shows Amazon S3 returning a `204 No Content` response.
 The tag set for the bucket has been removed. 



```

            HTTP/1.1 204 No Content
            Date: Wed, 25 Nov 2009 12:00:00 GMT
            Connection: close
            Server: AmazonS3
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketTagging "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteBucketTagging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketTagging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteBucketTagging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteBucketTagging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteBucketTagging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteBucketTagging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteBucketTagging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteBucketTagging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteBucketTagging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketTagging "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteBucketTagging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketTagging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteBucketTagging")
