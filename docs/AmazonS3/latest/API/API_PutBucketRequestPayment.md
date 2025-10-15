# PutBucketRequestPayment

###### Note

This operation is not supported for directory buckets.

Sets the request payment configuration for a bucket. By default, the bucket owner pays for downloads
 from the bucket. This configuration parameter enables the bucket owner (only) to specify that the person
 requesting the download will be charged for the download. For more information, see [Requester Pays
 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html").

The following operations are related to `PutBucketRequestPayment`:


* [CreateBucket](API_CreateBucket.md "API_CreateBucket.md")
* [GetBucketRequestPayment](API_GetBucketRequestPayment.md "API_GetBucketRequestPayment.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?requestPayment HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[RequestPaymentConfiguration](#AmazonS3-PutBucketRequestPayment-request-RequestPaymentConfiguration "#AmazonS3-PutBucketRequestPayment-request-RequestPaymentConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[Payer](#AmazonS3-PutBucketRequestPayment-request-Payer "#AmazonS3-PutBucketRequestPayment-request-Payer")>`string`</[Payer](#AmazonS3-PutBucketRequestPayment-request-Payer "#AmazonS3-PutBucketRequestPayment-request-Payer")>
</[RequestPaymentConfiguration](#AmazonS3-PutBucketRequestPayment-request-RequestPaymentConfiguration "#AmazonS3-PutBucketRequestPayment-request-RequestPaymentConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketRequestPayment_RequestSyntax "#API_PutBucketRequestPayment_RequestSyntax")**


The bucket name.


Required: Yes




**[Content-MD5](#API_PutBucketRequestPayment_RequestSyntax "#API_PutBucketRequestPayment_RequestSyntax")**


The Base64 encoded 128-bit `MD5` digest of the data. You must use this header as a
 message integrity check to verify that the request body was not corrupted in transit. For more
 information, see [RFC 1864](http://www.ietf.org/rfc/rfc1864.txt "http://www.ietf.org/rfc/rfc1864.txt").


For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[x-amz-expected-bucket-owner](#API_PutBucketRequestPayment_RequestSyntax "#API_PutBucketRequestPayment_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-sdk-checksum-algorithm](#API_PutBucketRequestPayment_RequestSyntax "#API_PutBucketRequestPayment_RequestSyntax")**


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





**[RequestPaymentConfiguration](#API_PutBucketRequestPayment_RequestSyntax "#API_PutBucketRequestPayment_RequestSyntax")**


Root level tag for the RequestPaymentConfiguration parameters.


Required: Yes




**[Payer](#API_PutBucketRequestPayment_RequestSyntax "#API_PutBucketRequestPayment_RequestSyntax")**


Specifies who pays for the download and request fees.


Type: String


Valid Values: `Requester | BucketOwner`



Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample Request


This request creates a Requester Pays bucket named `colorpictures`.



```

PUT ?requestPayment HTTP/1.1
Host: colorpictures.s3.<Region>.amazonaws.com
Content-Length: 173
Date: Wed, 01 Mar  2006 12:00:00 GMT
Authorization: authorization string

<RequestPaymentConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Payer>Requester</Payer>
</RequestPaymentConfiguration>

         
```

### Sample Response


Delete the metric configuration with a specified ID, which disables the CloudWatch metrics with
 the `ExampleMetrics` value for the `FilterId` dimension. 



```

HTTP/1.1 200 OK
x-amz-id-2: YgIPIfBiKa2bj0KMg95r/0zo3emzU4dzsD4rcKCHQUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A01
Date: Wed, 01 Mar  2006 12:00:00 GMT
Location: /colorpictures
Content-Length: 0
Connection: close
Server: AmazonS3
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketRequestPayment "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketRequestPayment")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketRequestPayment "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketRequestPayment")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketRequestPayment")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketRequestPayment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketRequestPayment")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketRequestPayment")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketRequestPayment")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketRequestPayment")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketRequestPayment "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketRequestPayment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketRequestPayment "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketRequestPayment")
