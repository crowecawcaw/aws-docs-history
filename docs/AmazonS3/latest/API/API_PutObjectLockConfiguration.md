# PutObjectLockConfiguration

###### Note

This operation is not supported for directory buckets.

Places an Object Lock configuration on the specified bucket. The rule specified in the Object Lock
 configuration will be applied by default to every new object placed in the specified bucket. For more
 information, see [Locking
 Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html"). 

###### Note


* The `DefaultRetention` settings require both a mode and a period.
* The `DefaultRetention` period can be either `Days` or `Years`
 but you must select one. You cannot specify `Days` and `Years` at the same
 time.
* You can enable Object Lock for new or existing buckets. For more information, see [Configuring
 Object Lock](../userguide/object-lock-configure.md "../userguide/object-lock-configure.md").
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?object-lock HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-request-payer: `RequestPayer`
x-amz-bucket-object-lock-token: `Token`
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[ObjectLockConfiguration](#AmazonS3-PutObjectLockConfiguration-request-ObjectLockConfiguration "#AmazonS3-PutObjectLockConfiguration-request-ObjectLockConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[ObjectLockEnabled](#AmazonS3-PutObjectLockConfiguration-request-ObjectLockEnabled "#AmazonS3-PutObjectLockConfiguration-request-ObjectLockEnabled")>`string`</[ObjectLockEnabled](#AmazonS3-PutObjectLockConfiguration-request-ObjectLockEnabled "#AmazonS3-PutObjectLockConfiguration-request-ObjectLockEnabled")>
   <[Rule](#AmazonS3-PutObjectLockConfiguration-request-Rule "#AmazonS3-PutObjectLockConfiguration-request-Rule")>
      <[DefaultRetention](API_ObjectLockRule.md#AmazonS3-Type-ObjectLockRule-DefaultRetention "API_ObjectLockRule.md#AmazonS3-Type-ObjectLockRule-DefaultRetention")>
         <[Days](API_DefaultRetention.md#AmazonS3-Type-DefaultRetention-Days "API_DefaultRetention.md#AmazonS3-Type-DefaultRetention-Days")>`integer`</[Days](API_DefaultRetention.md#AmazonS3-Type-DefaultRetention-Days "API_DefaultRetention.md#AmazonS3-Type-DefaultRetention-Days")>
         <[Mode](API_DefaultRetention.md#AmazonS3-Type-DefaultRetention-Mode "API_DefaultRetention.md#AmazonS3-Type-DefaultRetention-Mode")>`string`</[Mode](API_DefaultRetention.md#AmazonS3-Type-DefaultRetention-Mode "API_DefaultRetention.md#AmazonS3-Type-DefaultRetention-Mode")>
         <[Years](API_DefaultRetention.md#AmazonS3-Type-DefaultRetention-Years "API_DefaultRetention.md#AmazonS3-Type-DefaultRetention-Years")>`integer`</[Years](API_DefaultRetention.md#AmazonS3-Type-DefaultRetention-Years "API_DefaultRetention.md#AmazonS3-Type-DefaultRetention-Years")>
      </[DefaultRetention](API_ObjectLockRule.md#AmazonS3-Type-ObjectLockRule-DefaultRetention "API_ObjectLockRule.md#AmazonS3-Type-ObjectLockRule-DefaultRetention")>
   </[Rule](#AmazonS3-PutObjectLockConfiguration-request-Rule "#AmazonS3-PutObjectLockConfiguration-request-Rule")>
</[ObjectLockConfiguration](#AmazonS3-PutObjectLockConfiguration-request-ObjectLockConfiguration "#AmazonS3-PutObjectLockConfiguration-request-ObjectLockConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutObjectLockConfiguration_RequestSyntax "#API_PutObjectLockConfiguration_RequestSyntax")**


The bucket whose Object Lock configuration you want to create or replace.


Required: Yes




**[Content-MD5](#API_PutObjectLockConfiguration_RequestSyntax "#API_PutObjectLockConfiguration_RequestSyntax")**


The MD5 hash for the request body.


For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[x-amz-bucket-object-lock-token](#API_PutObjectLockConfiguration_RequestSyntax "#API_PutObjectLockConfiguration_RequestSyntax")**


A token to allow Object Lock to be enabled for an existing bucket.




**[x-amz-expected-bucket-owner](#API_PutObjectLockConfiguration_RequestSyntax "#API_PutObjectLockConfiguration_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-request-payer](#API_PutObjectLockConfiguration_RequestSyntax "#API_PutObjectLockConfiguration_RequestSyntax")**


Confirms that the requester knows that they will be charged for the request. Bucket owners need not
 specify this parameter in their requests. If either the source or destination S3 bucket has Requester
 Pays enabled, the requester will pay for corresponding charges to copy the object. For information about
 downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-sdk-checksum-algorithm](#API_PutObjectLockConfiguration_RequestSyntax "#API_PutObjectLockConfiguration_RequestSyntax")**


Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any
 additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
 `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
 information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
 parameter.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[ObjectLockConfiguration](#API_PutObjectLockConfiguration_RequestSyntax "#API_PutObjectLockConfiguration_RequestSyntax")**


Root level tag for the ObjectLockConfiguration parameters.


Required: Yes




**[ObjectLockEnabled](#API_PutObjectLockConfiguration_RequestSyntax "#API_PutObjectLockConfiguration_RequestSyntax")**


Indicates whether this bucket has an Object Lock configuration enabled. Enable
 `ObjectLockEnabled` when you apply `ObjectLockConfiguration` to a bucket.
 


Type: String


Valid Values: `Enabled`



Required: No




**[Rule](#API_PutObjectLockConfiguration_RequestSyntax "#API_PutObjectLockConfiguration_RequestSyntax")**


Specifies the Object Lock rule for the specified object. Enable the this rule when you apply
 `ObjectLockConfiguration` to a bucket. Bucket settings require both a mode and a period.
 The period can be either `Days` or `Years` but you must select one. You cannot
 specify `Days` and `Years` at the same time.


Type: [ObjectLockRule](API_ObjectLockRule.md "API_ObjectLockRule.md") data type


Required: No




## Response Syntax



```
HTTP/1.1 200
x-amz-request-charged: `RequestCharged`

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-request-charged](#API_PutObjectLockConfiguration_ResponseSyntax "#API_PutObjectLockConfiguration_ResponseSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutObjectLockConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutObjectLockConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutObjectLockConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutObjectLockConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutObjectLockConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutObjectLockConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutObjectLockConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutObjectLockConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutObjectLockConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutObjectLockConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutObjectLockConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutObjectLockConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutObjectLockConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutObjectLockConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutObjectLockConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutObjectLockConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutObjectLockConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutObjectLockConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutObjectLockConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutObjectLockConfiguration")
