# GetBucketVersioning

###### Note

This operation is not supported for directory buckets.

Returns the versioning state of a bucket.

To retrieve the versioning state of a bucket, you must be the bucket owner.

This implementation also returns the MFA Delete status of the versioning state. If the MFA Delete
 status is `enabled`, the bucket owner must use an authentication device to change the
 versioning state of the bucket.

The following operations are related to `GetBucketVersioning`:


* [GetObject](API_GetObject.md "API_GetObject.md")
* [PutObject](API_PutObject.md "API_PutObject.md")
* [DeleteObject](API_DeleteObject.md "API_DeleteObject.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?versioning HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketVersioning_RequestSyntax "#API_GetBucketVersioning_RequestSyntax")**


The name of the bucket for which to get the versioning information.


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketVersioning_RequestSyntax "#API_GetBucketVersioning_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[VersioningConfiguration](#AmazonS3-GetBucketVersioning-response-GetBucketVersioningOutput "#AmazonS3-GetBucketVersioning-response-GetBucketVersioningOutput")>
   <[Status](#AmazonS3-GetBucketVersioning-response-Status "#AmazonS3-GetBucketVersioning-response-Status")>***string***</[Status](#AmazonS3-GetBucketVersioning-response-Status "#AmazonS3-GetBucketVersioning-response-Status")>
   <[MfaDelete](#AmazonS3-GetBucketVersioning-response-MFADelete "#AmazonS3-GetBucketVersioning-response-MFADelete")>***string***</[MfaDelete](#AmazonS3-GetBucketVersioning-response-MFADelete "#AmazonS3-GetBucketVersioning-response-MFADelete")>
</[VersioningConfiguration](#AmazonS3-GetBucketVersioning-response-GetBucketVersioningOutput "#AmazonS3-GetBucketVersioning-response-GetBucketVersioningOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[VersioningConfiguration](#API_GetBucketVersioning_ResponseSyntax "#API_GetBucketVersioning_ResponseSyntax")**


Root level tag for the VersioningConfiguration parameters.


Required: Yes




**[MFADelete](#API_GetBucketVersioning_ResponseSyntax "#API_GetBucketVersioning_ResponseSyntax")**


Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only
 returned if the bucket has been configured with MFA delete. If the bucket has never been so configured,
 this element is not returned.


Type: String


Valid Values: `Enabled | Disabled`





**[Status](#API_GetBucketVersioning_ResponseSyntax "#API_GetBucketVersioning_ResponseSyntax")**


The versioning state of the bucket.


Type: String


Valid Values: `Enabled | Suspended`





## Examples


### Example


This example returns the versioning state of `amzn-s3-demo-bucket`.



```

         GET /?versioning HTTP/1.1
         Host:amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
         Date: Wed, 12 Oct 2009 17:50:00 GMT
         Authorization: authorization string
         Content-Type: text/plain
        
```

### Example


There are three versioning states:


If you enabled versioning on a bucket, the response is:



```

     <VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
        <Status>Enabled</Status>
     </VersioningConfiguration>
        
```

### Example


If you suspended versioning on a bucket, the response is:



```

     <VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
        <Status>Suspended</Status>
     </VersioningConfiguration>
     
```

### Example


If you never enabled (or suspended) versioning on a bucket, the response is:



```

     <VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/"/>
     
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketVersioning "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketVersioning")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketVersioning "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketVersioning")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketVersioning "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketVersioning")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketVersioning "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketVersioning")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketVersioning "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketVersioning")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketVersioning "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketVersioning")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketVersioning "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketVersioning")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketVersioning "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketVersioning")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketVersioning "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketVersioning")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketVersioning "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketVersioning")
