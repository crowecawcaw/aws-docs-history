# GetBucketLocation

###### Important

Using the `GetBucketLocation` operation is no longer a best practice. To return the 
 Region that a bucket resides in, we recommend that you use the 
 [HeadBucket](API_HeadBucket.md "API_HeadBucket.md") 
 operation instead. For backward compatibility, Amazon S3 continues to support the 
 `GetBucketLocation` operation.

Returns the Region the bucket resides in. You set the bucket's Region using the
 `LocationConstraint` request parameter in a `CreateBucket` request. For more
 information, see [CreateBucket](API_CreateBucket.md "API_CreateBucket.md").

###### Note

In a bucket's home Region, calls to the `GetBucketLocation` operation are governed 
 by the bucket's policy. In other Regions, the bucket policy doesn't apply, which means that 
 cross-account access won't be authorized. However, calls to the `HeadBucket` operation 
 always return the bucket’s location through an HTTP response header, whether access to the bucket 
 is authorized or not. Therefore, we recommend using the `HeadBucket` operation for 
 bucket Region discovery and to avoid using the `GetBucketLocation` operation.

When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.

When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. 
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. 
For more information about `InvalidAccessPointAliasError`, see [List of
 Error Codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").

###### Note

This operation is not supported for directory buckets.

The following operations are related to `GetBucketLocation`:


* [GetObject](API_GetObject.md "API_GetObject.md")
* [CreateBucket](API_CreateBucket.md "API_CreateBucket.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?location HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketLocation_RequestSyntax "#API_GetBucketLocation_RequestSyntax")**


The name of the bucket for which to get the location.


When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.


When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. 
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. 
For more information about `InvalidAccessPointAliasError`, see [List of
 Error Codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketLocation_RequestSyntax "#API_GetBucketLocation_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[LocationConstraint](#AmazonS3-GetBucketLocation-response-GetBucketLocationOutput "#AmazonS3-GetBucketLocation-response-GetBucketLocationOutput")>
   <[LocationConstraint](#AmazonS3-GetBucketLocation-response-LocationConstraint "#AmazonS3-GetBucketLocation-response-LocationConstraint")>***string***</[LocationConstraint](#AmazonS3-GetBucketLocation-response-LocationConstraint "#AmazonS3-GetBucketLocation-response-LocationConstraint")>
</[LocationConstraint](#AmazonS3-GetBucketLocation-response-GetBucketLocationOutput "#AmazonS3-GetBucketLocation-response-GetBucketLocationOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[LocationConstraint](#API_GetBucketLocation_ResponseSyntax "#API_GetBucketLocation_ResponseSyntax")**


Root level tag for the LocationConstraint parameters.


Required: Yes




**[LocationConstraint](#API_GetBucketLocation_ResponseSyntax "#API_GetBucketLocation_ResponseSyntax")**


Specifies the Region where the bucket resides. For a list of all the Amazon S3 supported location
 constraints by Region, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region").


Buckets in Region `us-east-1` have a LocationConstraint of `null`. Buckets
 with a LocationConstraint of `EU` reside in `eu-west-1`.


Type: String


Valid Values: `af-south-1 | ap-east-1 | ap-northeast-1 | ap-northeast-2 | ap-northeast-3 | ap-south-1 | ap-south-2 | ap-southeast-1 | ap-southeast-2 | ap-southeast-3 | ap-southeast-4 | ap-southeast-5 | ca-central-1 | cn-north-1 | cn-northwest-1 | EU | eu-central-1 | eu-central-2 | eu-north-1 | eu-south-1 | eu-south-2 | eu-west-1 | eu-west-2 | eu-west-3 | il-central-1 | me-central-1 | me-south-1 | sa-east-1 | us-east-2 | us-gov-east-1 | us-gov-west-1 | us-west-1 | us-west-2`





## Examples


### Sample Request


The following request returns the Region of the specified bucket.



```

         GET /?location HTTP/1.1
         Host: amzn-s3-demo-bucket.s3.amazonaws.com
         Date: Tue, 09 Oct 2007 20:26:04 +0000
         Authorization: signatureValue
         
```

### Sample Response


This example illustrates one usage of GetBucketLocation.



```

         <?xml version="1.0" encoding="UTF-8"?>
         <LocationConstraint xmlns="http://s3.amazonaws.com/doc/2006-03-01/">us-west-2</LocationConstraint>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketLocation "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketLocation")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketLocation "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketLocation")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketLocation "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketLocation")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketLocation "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketLocation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketLocation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketLocation")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketLocation "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketLocation")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketLocation "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketLocation")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketLocation "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketLocation")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketLocation "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketLocation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketLocation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketLocation")
