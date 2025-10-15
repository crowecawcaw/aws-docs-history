# PutObjectLegalHold

###### Note

This operation is not supported for directory buckets.

Applies a legal hold configuration to the specified object. For more information, see [Locking Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html").

This functionality is not supported for Amazon S3 on Outposts.

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /{Key+}?legal-hold&versionId=`VersionId` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-request-payer: `RequestPayer`
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[LegalHold](#AmazonS3-PutObjectLegalHold-request-LegalHold "#AmazonS3-PutObjectLegalHold-request-LegalHold") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[Status](#AmazonS3-PutObjectLegalHold-request-Status "#AmazonS3-PutObjectLegalHold-request-Status")>`string`</[Status](#AmazonS3-PutObjectLegalHold-request-Status "#AmazonS3-PutObjectLegalHold-request-Status")>
</[LegalHold](#AmazonS3-PutObjectLegalHold-request-LegalHold "#AmazonS3-PutObjectLegalHold-request-LegalHold")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutObjectLegalHold_RequestSyntax "#API_PutObjectLegalHold_RequestSyntax")**


The bucket name containing the object that you want to place a legal hold on. 



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.


Required: Yes




**[Content-MD5](#API_PutObjectLegalHold_RequestSyntax "#API_PutObjectLegalHold_RequestSyntax")**


The MD5 hash for the request body.


For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[Key](#API_PutObjectLegalHold_RequestSyntax "#API_PutObjectLegalHold_RequestSyntax")**


The key name for the object that you want to place a legal hold on.


Length Constraints: Minimum length of 1.


Required: Yes




**[versionId](#API_PutObjectLegalHold_RequestSyntax "#API_PutObjectLegalHold_RequestSyntax")**


The version ID of the object that you want to place a legal hold on.




**[x-amz-expected-bucket-owner](#API_PutObjectLegalHold_RequestSyntax "#API_PutObjectLegalHold_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-request-payer](#API_PutObjectLegalHold_RequestSyntax "#API_PutObjectLegalHold_RequestSyntax")**


Confirms that the requester knows that they will be charged for the request. Bucket owners need not
 specify this parameter in their requests. If either the source or destination S3 bucket has Requester
 Pays enabled, the requester will pay for corresponding charges to copy the object. For information about
 downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-sdk-checksum-algorithm](#API_PutObjectLegalHold_RequestSyntax "#API_PutObjectLegalHold_RequestSyntax")**


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





**[LegalHold](#API_PutObjectLegalHold_RequestSyntax "#API_PutObjectLegalHold_RequestSyntax")**


Root level tag for the LegalHold parameters.


Required: Yes




**[Status](#API_PutObjectLegalHold_RequestSyntax "#API_PutObjectLegalHold_RequestSyntax")**


Indicates whether the specified object has a legal hold in place.


Type: String


Valid Values: `ON | OFF`



Required: No




## Response Syntax



```
HTTP/1.1 200
x-amz-request-charged: `RequestCharged`

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-request-charged](#API_PutObjectLegalHold_ResponseSyntax "#API_PutObjectLegalHold_ResponseSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutObjectLegalHold "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutObjectLegalHold")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutObjectLegalHold "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutObjectLegalHold")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutObjectLegalHold")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutObjectLegalHold")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutObjectLegalHold")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutObjectLegalHold")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutObjectLegalHold")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutObjectLegalHold")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutObjectLegalHold "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutObjectLegalHold")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutObjectLegalHold "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutObjectLegalHold")
