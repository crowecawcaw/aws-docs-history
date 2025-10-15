# PutBucketCors

###### Note

This operation is not supported for directory buckets.

Sets the `cors` configuration for your bucket. If the configuration exists, Amazon S3 replaces
 it.

To use this operation, you must be allowed to perform the `s3:PutBucketCORS` action. By
 default, the bucket owner has this permission and can grant it to others.

You set this configuration on a bucket so that the bucket can service cross-origin requests. For
 example, you might want to enable a request whose origin is `http://www.example.com` to
 access your Amazon S3 bucket at `my.example.bucket.com` by using the browser's
 `XMLHttpRequest` capability.

To enable cross-origin resource sharing (CORS) on a bucket, you add the `cors`
 subresource to the bucket. The `cors` subresource is an XML document in which you configure
 rules that identify origins and the HTTP methods that can be executed on your bucket. The document is
 limited to 64 KB in size. 

When Amazon S3 receives a cross-origin request (or a pre-flight OPTIONS request) against a bucket, it
 evaluates the `cors` configuration on the bucket and uses the first `CORSRule`
 rule that matches the incoming browser request to enable a cross-origin request. For a rule to match,
 the following conditions must be met:


* The request's `Origin` header must match `AllowedOrigin` elements.
* The request method (for example, GET, PUT, HEAD, and so on) or the
 `Access-Control-Request-Method` header in case of a pre-flight `OPTIONS`
 request must be one of the `AllowedMethod` elements.
* Every header specified in the `Access-Control-Request-Headers` request header of a
 pre-flight request must match an `AllowedHeader` element.
 For more information about CORS, go to [Enabling Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html") in the
 *Amazon S3 User Guide*.

The following operations are related to `PutBucketCors`:


* [GetBucketCors](API_GetBucketCors.md "API_GetBucketCors.md")
* [DeleteBucketCors](API_DeleteBucketCors.md "API_DeleteBucketCors.md")
* [RESTOPTIONSobject](RESTOPTIONSobject.md "RESTOPTIONSobject.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?cors HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[CORSConfiguration](#AmazonS3-PutBucketCors-request-CORSConfiguration "#AmazonS3-PutBucketCors-request-CORSConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[CORSRule](#AmazonS3-PutBucketCors-request-CORSRules "#AmazonS3-PutBucketCors-request-CORSRules")>
      <[AllowedHeader](API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedHeaders "API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedHeaders")>`string`</[AllowedHeader](API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedHeaders "API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedHeaders")>
      ...
      <[AllowedMethod](API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedMethods "API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedMethods")>`string`</[AllowedMethod](API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedMethods "API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedMethods")>
      ...
      <[AllowedOrigin](API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedOrigins "API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedOrigins")>`string`</[AllowedOrigin](API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedOrigins "API_CORSRule.md#AmazonS3-Type-CORSRule-AllowedOrigins")>
      ...
      <[ExposeHeader](API_CORSRule.md#AmazonS3-Type-CORSRule-ExposeHeaders "API_CORSRule.md#AmazonS3-Type-CORSRule-ExposeHeaders")>`string`</[ExposeHeader](API_CORSRule.md#AmazonS3-Type-CORSRule-ExposeHeaders "API_CORSRule.md#AmazonS3-Type-CORSRule-ExposeHeaders")>
      ...
      <[ID](API_CORSRule.md#AmazonS3-Type-CORSRule-ID "API_CORSRule.md#AmazonS3-Type-CORSRule-ID")>`string`</[ID](API_CORSRule.md#AmazonS3-Type-CORSRule-ID "API_CORSRule.md#AmazonS3-Type-CORSRule-ID")>
      <[MaxAgeSeconds](API_CORSRule.md#AmazonS3-Type-CORSRule-MaxAgeSeconds "API_CORSRule.md#AmazonS3-Type-CORSRule-MaxAgeSeconds")>`integer`</[MaxAgeSeconds](API_CORSRule.md#AmazonS3-Type-CORSRule-MaxAgeSeconds "API_CORSRule.md#AmazonS3-Type-CORSRule-MaxAgeSeconds")>
   </[CORSRule](#AmazonS3-PutBucketCors-request-CORSRules "#AmazonS3-PutBucketCors-request-CORSRules")>
   ...
</[CORSConfiguration](#AmazonS3-PutBucketCors-request-CORSConfiguration "#AmazonS3-PutBucketCors-request-CORSConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketCors_RequestSyntax "#API_PutBucketCors_RequestSyntax")**


Specifies the bucket impacted by the `cors`configuration.


Required: Yes




**[Content-MD5](#API_PutBucketCors_RequestSyntax "#API_PutBucketCors_RequestSyntax")**


The Base64 encoded 128-bit `MD5` digest of the data. This header must be used as a
 message integrity check to verify that the request body was not corrupted in transit. For more
 information, go to [RFC 1864.](http://www.ietf.org/rfc/rfc1864.txt "http://www.ietf.org/rfc/rfc1864.txt")



For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[x-amz-expected-bucket-owner](#API_PutBucketCors_RequestSyntax "#API_PutBucketCors_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-sdk-checksum-algorithm](#API_PutBucketCors_RequestSyntax "#API_PutBucketCors_RequestSyntax")**


Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
 additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
 `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
 information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
 parameter.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[CORSConfiguration](#API_PutBucketCors_RequestSyntax "#API_PutBucketCors_RequestSyntax")**


Root level tag for the CORSConfiguration parameters.


Required: Yes




**[CORSRule](#API_PutBucketCors_RequestSyntax "#API_PutBucketCors_RequestSyntax")**


A set of origins and methods (cross-origin access that you want to allow). You can add up to 100
 rules to the configuration.


Type: Array of [CORSRule](API_CORSRule.md "API_CORSRule.md") data types


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Example: CORS configuration on a bucket with two rules



* The first `CORSRule` allows cross-origin PUT, POST, and DELETE requests whose
 origin is `http://www.example.com` origins. The rule also allows all headers in a
 pre-flight OPTIONS request through the `Access-Control-Request-Headers` header.
 Therefore, in response to any pre-flight OPTIONS request, Amazon S3 will return any requested
 headers.
* The second rule allows cross-origin GET requests from all the origins. The '\*' wildcard
 character refers to all origins.


```
<CORSConfiguration>
 <CORSRule>
   <AllowedOrigin>http://www.example.com</AllowedOrigin>

   <AllowedMethod>PUT</AllowedMethod>
   <AllowedMethod>POST</AllowedMethod>
   <AllowedMethod>DELETE</AllowedMethod>

   <AllowedHeader>*</AllowedHeader>
 </CORSRule>
 <CORSRule>
   <AllowedOrigin>*</AllowedOrigin>
   <AllowedMethod>GET</AllowedMethod>
 </CORSRule>
</CORSConfiguration>
```

### Example: CORS configuration allows cross-origin PUT and POST requests from
 http://www.example.com


The `cors` configuration also allows additional optional configuration parameters as
 shown in the following cors configuration on a bucket. For example, 


In the preceding configuration, `CORSRule` includes the following additional optional
 parameters:



* `MaxAgeSeconds`—Specifies the time in seconds that the browser will cache
 an Amazon S3 response to a pre-flight OPTIONS request for the specified resource. In this example,
 this parameter is 3000 seconds. Caching enables the browsers to avoid sending pre-flight OPTIONS
 request to Amazon S3 for repeated requests.
* `ExposeHeader`—Identifies the response header (in this case
 `x-amz-server-side-encryption`) that you want customers to be able to access from
 their applications (for example, from a JavaScript `XMLHttpRequest` object).


```
<CORSConfiguration>
 <CORSRule>
   <AllowedOrigin>http://www.example.com</AllowedOrigin>
   <AllowedMethod>PUT</AllowedMethod>
   <AllowedMethod>POST</AllowedMethod>
   <AllowedMethod>DELETE</AllowedMethod>
   <AllowedHeader>*</AllowedHeader>
  *<MaxAgeSeconds>3000</MaxAgeSeconds>
 <ExposeHeader>x-amz-server-side-encryption</ExposeHeader>*
 </CORSRule>
</CORSConfiguration>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketCors "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketCors")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketCors "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketCors")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketCors "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketCors")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketCors "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketCors")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketCors "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketCors")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketCors "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketCors")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketCors "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketCors")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketCors "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketCors")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketCors "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketCors")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketCors "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketCors")
