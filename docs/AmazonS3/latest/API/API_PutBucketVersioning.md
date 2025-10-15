# PutBucketVersioning

###### Note

This operation is not supported for directory buckets.

###### Note

When you enable versioning on a bucket for the first time, it might take a short amount of time
 for the change to be fully propagated. While this change is propagating, you might encounter
 intermittent `HTTP 404 NoSuchKey` errors for requests to objects created or updated after
 enabling versioning. We recommend that you wait for 15 minutes after enabling versioning before
 issuing write operations (`PUT` or `DELETE`) on objects in the bucket. 

Sets the versioning state of an existing bucket.

You can set the versioning state with one of the following values:


**Enabled**—Enables versioning for the objects in the bucket. All
 objects added to the bucket receive a unique version ID.


**Suspended**—Disables versioning for the objects in the bucket. All
 objects added to the bucket receive the version ID null.

If the versioning state has never been set on a bucket, it has no versioning state; a [GetBucketVersioning](API_GetBucketVersioning.md "API_GetBucketVersioning.md") request does not return a versioning state value.

In order to enable MFA Delete, you must be the bucket owner. If you are the bucket owner and want to
 enable MFA Delete in the bucket versioning configuration, you must include the `x-amz-mfa
 request` header and the `Status` and the `MfaDelete` request elements in a
 request to set the versioning state of the bucket.

###### Important

If you have an object expiration lifecycle configuration in your non-versioned bucket and you want
 to maintain the same permanent delete behavior when you enable versioning, you must add a noncurrent
 expiration policy. The noncurrent expiration lifecycle configuration will manage the deletes of the
 noncurrent object versions in the version-enabled bucket. (A version-enabled bucket maintains one
 current and zero or more noncurrent object versions.) For more information, see [Lifecycle and
 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html#lifecycle-and-other-bucket-config "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html#lifecycle-and-other-bucket-config").

The following operations are related to `PutBucketVersioning`:


* [CreateBucket](API_CreateBucket.md "API_CreateBucket.md")
* [DeleteBucket](API_DeleteBucket.md "API_DeleteBucket.md")
* [GetBucketVersioning](API_GetBucketVersioning.md "API_GetBucketVersioning.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?versioning HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-mfa: `MFA`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[VersioningConfiguration](#AmazonS3-PutBucketVersioning-request-VersioningConfiguration "#AmazonS3-PutBucketVersioning-request-VersioningConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[MfaDelete](#AmazonS3-PutBucketVersioning-request-MFADelete "#AmazonS3-PutBucketVersioning-request-MFADelete")>`string`</[MfaDelete](#AmazonS3-PutBucketVersioning-request-MFADelete "#AmazonS3-PutBucketVersioning-request-MFADelete")>
   <[Status](#AmazonS3-PutBucketVersioning-request-Status "#AmazonS3-PutBucketVersioning-request-Status")>`string`</[Status](#AmazonS3-PutBucketVersioning-request-Status "#AmazonS3-PutBucketVersioning-request-Status")>
</[VersioningConfiguration](#AmazonS3-PutBucketVersioning-request-VersioningConfiguration "#AmazonS3-PutBucketVersioning-request-VersioningConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketVersioning_RequestSyntax "#API_PutBucketVersioning_RequestSyntax")**


The bucket name.


Required: Yes




**[Content-MD5](#API_PutBucketVersioning_RequestSyntax "#API_PutBucketVersioning_RequestSyntax")**


>The Base64 encoded 128-bit `MD5` digest of the data. You must use this header as a
 message integrity check to verify that the request body was not corrupted in transit. For more
 information, see [RFC 1864](http://www.ietf.org/rfc/rfc1864.txt "http://www.ietf.org/rfc/rfc1864.txt").


For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[x-amz-expected-bucket-owner](#API_PutBucketVersioning_RequestSyntax "#API_PutBucketVersioning_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-mfa](#API_PutBucketVersioning_RequestSyntax "#API_PutBucketVersioning_RequestSyntax")**


The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device. The serial number is the number that uniquely identifies the MFA device. For physical MFA devices, this is the unique serial number that's provided with the device. For virtual MFA devices, the serial number is the device ARN. For more information, see [Enabling versioning on buckets](../userguide/manage-versioning-examples.md "../userguide/manage-versioning-examples.md") and [Configuring MFA delete](../userguide/MultiFactorAuthenticationDelete.md "../userguide/MultiFactorAuthenticationDelete.md") in the *Amazon Simple Storage Service User Guide*.




**[x-amz-sdk-checksum-algorithm](#API_PutBucketVersioning_RequestSyntax "#API_PutBucketVersioning_RequestSyntax")**


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





**[VersioningConfiguration](#API_PutBucketVersioning_RequestSyntax "#API_PutBucketVersioning_RequestSyntax")**


Root level tag for the VersioningConfiguration parameters.


Required: Yes




**[MFADelete](#API_PutBucketVersioning_RequestSyntax "#API_PutBucketVersioning_RequestSyntax")**


Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only
 returned if the bucket has been configured with MFA delete. If the bucket has never been so configured,
 this element is not returned.


Type: String


Valid Values: `Enabled | Disabled`



Required: No




**[Status](#API_PutBucketVersioning_RequestSyntax "#API_PutBucketVersioning_RequestSyntax")**


The versioning state of the bucket.


Type: String


Valid Values: `Enabled | Suspended`



Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample Request


The following request enables versioning for the specified bucket.



```

PUT /?versioning HTTP/1.1
Host: bucket.s3.<Region>.amazonaws.com
Date: Wed, 01 Mar  2006 12:00:00 GMT
Authorization: authorization string
Content-Type: text/plain
Content-Length: 124
 
<VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/"> 
  <Status>Enabled</Status> 
</VersioningConfiguration>
         
```

### Sample Response


This example illustrates one usage of PutBucketVersioning.



```

HTTP/1.1 200 OK
x-amz-id-2: YgIPIfBiKa2bj0KMg95r/0zo3emzU4dzsD4rcKCHQUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A01
Date: Wed, 01 Mar  2006 12:00:00 GMT3
         
```

### Sample Request


The following request suspends versioning for the specified bucket.



```

PUT /?versioning HTTP/1.1
Host: bucket.s3.<Region>.amazonaws.com
Date: Wed, 12 Oct 2009 17:50:00 GMT
Authorization: authorization string
Content-Type: text/plain
Content-Length: 124
 
<VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/"> 
   <Status>Suspended</Status> 
</VersioningConfiguration>
         
```

### Sample Response


This example illustrates one usage of PutBucketVersioning.



```

HTTP/1.1 200 OK
x-amz-id-2: YgIPIfBiKa2bj0KMg95r/0zo3emzU4dzsD4rcKCHQUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A01
Date: Wed, 01 Mar  2006 12:00:00 GMT
         
```

### Sample Request


The following request enables versioning and MFA Delete on a bucket. Note the space between
 `[SerialNumber]` and `[TokenCode]` and that you must include
 `Status` whenever you use `MfaDelete`.



```

PUT /?versioning HTTP/1.1
Host: bucket.s3.<Region>.amazonaws.com
Date: Wed, 12 Oct 2009 17:50:00 GMT
x-amz-mfa:[SerialNumber] [TokenCode]
Authorization: authorization string
Content-Type: text/plain
Content-Length: 124
 
<VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/"> 
   <Status>Enabled</Status> 
   <MfaDelete>Enabled</MfaDelete>
</VersioningConfiguration>
         
```

### Sample Response


This example illustrates one usage of PutBucketVersioning.



```

HTTPS/1.1 200 OK
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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketVersioning "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketVersioning")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketVersioning "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketVersioning")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketVersioning "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketVersioning")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketVersioning "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketVersioning")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketVersioning "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketVersioning")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketVersioning "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketVersioning")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketVersioning "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketVersioning")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketVersioning "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketVersioning")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketVersioning "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketVersioning")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketVersioning "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketVersioning")
