# GetBucketCors

###### Note

This operation is not supported for directory buckets.

Returns the Cross-Origin Resource Sharing (CORS) configuration information set for the
 bucket.

 To use this operation, you must have permission to perform the `s3:GetBucketCORS`
 action. By default, the bucket owner has this permission and can grant it to others.

When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.

When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. 
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. 
For more information about `InvalidAccessPointAliasError`, see [List of
 Error Codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").

 For more information about CORS, see  [Enabling Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html").

The following operations are related to `GetBucketCors`:


* [PutBucketCors](API_PutBucketCors.md "API_PutBucketCors.md")
* [DeleteBucketCors](API_DeleteBucketCors.md "API_DeleteBucketCors.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?cors HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketCors_RequestSyntax "#API_GetBucketCors_RequestSyntax")**


The bucket name for which to get the cors configuration.


When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.


When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. 
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. 
For more information about `InvalidAccessPointAliasError`, see [List of
 Error Codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketCors_RequestSyntax "#API_GetBucketCors_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[CORSConfiguration](#AmazonS3-GetBucketCors-response-GetBucketCorsOutput "#AmazonS3-GetBucketCors-response-GetBucketCorsOutput")>
   <[CORSRule](#AmazonS3-GetBucketCors-response-CORSRules "#AmazonS3-GetBucketCors-response-CORSRules")>
      <[AllowedHeader](API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedHeaders "API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedHeaders")>***string***</[AllowedHeader](API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedHeaders "API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedHeaders")>
      ...
      <[AllowedMethod](API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedMethods "API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedMethods")>***string***</[AllowedMethod](API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedMethods "API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedMethods")>
      ...
      <[AllowedOrigin](API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedOrigins "API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedOrigins")>***string***</[AllowedOrigin](API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedOrigins "API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedOrigins")>
      ...
      <[ExposeHeader](API_CORSRule.md#AmazonS3-Type-CORSRule-ExposeHeaders "API_CORSRule.md#AmazonS3-Type-CORSRule-ExposeHeaders")>***string***</[ExposeHeader](API_CORSRule.md#AmazonS3-Type-CORSRule-ExposeHeaders "API_CORSRule.md#AmazonS3-Type-CORSRule-ExposeHeaders")>
      ...
      <[ID](API_CORSRule.md#AmazonS3-Type-CORSRule-ID "API_CORSRule.md#AmazonS3-Type-CORSRule-ID")>***string***</[ID](API_CORSRule.md#AmazonS3-Type-CORSRule-ID "API_CORSRule.md#AmazonS3-Type-CORSRule-ID")>
      <[MaxAgeSeconds](API_CORSRule.md#AmazonS3-Type-CORSRule-MaxAgeSeconds "API_CORSRule.md#AmazonS3-Type-CORSRule-MaxAgeSeconds")>***integer***</[MaxAgeSeconds](API_CORSRule.md#AmazonS3-Type-CORSRule-MaxAgeSeconds "API_CORSRule.md#AmazonS3-Type-CORSRule-MaxAgeSeconds")>
   </[CORSRule](#AmazonS3-GetBucketCors-response-CORSRules "#AmazonS3-GetBucketCors-response-CORSRules")>
   ...
</[CORSConfiguration](#AmazonS3-GetBucketCors-response-GetBucketCorsOutput "#AmazonS3-GetBucketCors-response-GetBucketCorsOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[CORSConfiguration](#API_GetBucketCors_ResponseSyntax "#API_GetBucketCors_ResponseSyntax")**


Root level tag for the CORSConfiguration parameters.


Required: Yes




**[CORSRule](#API_GetBucketCors_ResponseSyntax "#API_GetBucketCors_ResponseSyntax")**


A set of origins and methods (cross-origin access that you want to allow). You can add up to 100
 rules to the configuration.


Type: Array of [CORSRule](API_CORSRule.md "API_CORSRule.md") data types




## Examples


###  Configure CORS Sample Request


The following PUT request adds the `cors` subresource to a bucket
 (`amzn-s3-demo-bucket`).



```

PUT /?cors HTTP/1.1
Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com 
x-amz-date: Tue, 21 Aug 2012 17:54:50 GMT
Content-MD5: 8dYiLewFWZyGgV2Q5FNI4W==
Authorization: authorization string
Content-Length: 216

<CORSConfiguration>
 <CORSRule>
   <AllowedOrigin>http://www.example.com</AllowedOrigin>
   <AllowedMethod>PUT</AllowedMethod>
   <AllowedMethod>POST</AllowedMethod>
   <AllowedMethod>DELETE</AllowedMethod>
   <AllowedHeader>*</AllowedHeader>
   <MaxAgeSeconds>3000</MaxAgeSec>
   <ExposeHeader>x-amz-server-side-encryption</ExposeHeader>
 </CORSRule>
 <CORSRule>
   <AllowedOrigin>*</AllowedOrigin>
   <AllowedMethod>GET</AllowedMethod>
   <AllowedHeader>*</AllowedHeader>
   <MaxAgeSeconds>3000</MaxAgeSeconds>
 </CORSRule>
</CORSConfiguration> 
            
```

### Example


This is the sample response to the preceding request.



```

HTTP/1.1 200 OK
x-amz-id-2: CCshOvbOPfxzhwOADyC4qHj/Ck3F9Q0viXKw3rivZ+GcBoZSOOahvEJfPisZB7B
x-amz-request-id: BDC4B83DF5096BBE
Date: Tue, 21 Aug 2012 17:54:50 GMT
Server: AmazonS3
            
```

### Sample Request: Retrieve cors subresource


The following example gets the cors subresource of a bucket.



```

            GET /?cors HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Tue, 13 Dec 2011 19:14:42 GMT
            Authorization: signatureValue
         
```

### Example


Sample Response



```

            HTTP/1.1 200 OK
            x-amz-id-2: 0FmFIWsh/PpBuzZ0JFRC55ZGVmQW4SHJ7xVDqKwhEdJmf3q63RtrvH8ZuxW1Bol5
            x-amz-request-id: 0CF038E9BCF63097
            Date: Tue, 13 Dec 2011 19:14:42 GMT
            Server: AmazonS3
            Content-Length: 280
            <CORSConfiguration>
                 <CORSRule>
                   <AllowedOrigin>http://www.example.com</AllowedOrigin>
                   <AllowedMethod>GET</AllowedMethod>
                   <MaxAgeSeconds>3000</MaxAgeSec>
                  <ExposeHeader>x-amz-server-side-encryption</ExposeHeader>
                </CORSRule>
            </CORSConfiguration>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketCors "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketCors")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketCors "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketCors")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketCors "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketCors")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketCors "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketCors")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketCors "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketCors")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketCors "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketCors")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketCors "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketCors")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketCors "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketCors")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketCors "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketCors")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketCors "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketCors")
