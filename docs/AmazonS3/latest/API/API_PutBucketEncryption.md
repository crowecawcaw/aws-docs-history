# PutBucketEncryption

This operation configures default encryption and Amazon S3 Bucket Keys for an existing bucket.

###### Note


**Directory buckets**  - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.*region-code*.amazonaws.com/*bucket-name*`. Virtual-hosted-style requests aren't supported. 
For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](../userguide/endpoint-directory-buckets-AZ.md "../userguide/endpoint-directory-buckets-AZ.md") in the
 *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](../userguide/s3-lzs-for-directory-buckets.md "../userguide/s3-lzs-for-directory-buckets.md") in the
 *Amazon S3 User Guide*.

By default, all buckets have a default encryption configuration that uses server-side encryption
 with Amazon S3 managed keys (SSE-S3).

###### Note


* **General purpose buckets**





	+ You can optionally configure default encryption for a bucket by using server-side
	 encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) or dual-layer server-side encryption with
	 AWS KMS keys (DSSE-KMS). If you specify default encryption by using SSE-KMS, you can also
	 configure [Amazon S3 Bucket
	 Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html"). For information about the bucket default encryption feature, see [Amazon S3 Bucket Default
	 Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html") in the *Amazon S3 User Guide*.
	+ If you use PutBucketEncryption to set your [default bucket encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html") to
	 SSE-KMS, you should verify that your KMS key ID is correct. Amazon S3 doesn't validate the
	 KMS key ID provided in PutBucketEncryption requests.
* **Directory buckets**  - You can optionally configure
 default encryption for a bucket by using server-side encryption with AWS Key Management Service (AWS KMS) keys
 (SSE-KMS).




	+ We recommend that the bucket's default encryption uses the desired encryption
	 configuration and you don't override the bucket default encryption in your
	 `CreateSession` requests or `PUT` object requests. Then, new objects
	 are automatically encrypted with the desired encryption settings.
	 For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with AWS KMS for new object uploads](../userguide/s3-express-specifying-kms-encryption.md "../userguide/s3-express-specifying-kms-encryption.md").
	+ Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") per directory bucket's lifetime. 
	The [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk") (`aws/s3`) isn't supported.
	+ S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets 
	to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](API_CopyObject.md "API_CopyObject.md"), [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md"), [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops "https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops"), or 
	 [the import jobs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job "https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.
	+ When you specify an [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") for encryption in your directory bucket, only use the key ID or key ARN. The key alias format of the KMS key isn't supported.
	+ For directory buckets, if you use PutBucketEncryption to set your [default bucket
	 encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html") to SSE-KMS, Amazon S3 validates the KMS key ID provided in
	 PutBucketEncryption requests.
###### Important

If you're specifying a customer managed KMS key, we recommend using a fully qualified KMS key
 ARN. If you use a KMS key alias instead, then AWS KMS resolves the key within the requester’s account.
 This behavior can result in data that's encrypted with a KMS key that belongs to the requester, and
 not the bucket owner.

Also, this action requires AWS Signature Version 4. For more information, see  [Authenticating
 Requests (AWS Signature Version 4)](sig-v4-authenticating-requests.md "sig-v4-authenticating-requests.md"). 



Permissions


* **General purpose bucket permissions** - The
 `s3:PutEncryptionConfiguration` permission is required in a policy. The bucket
 owner has this permission by default. The bucket owner can grant this permission to others.
 For more information about permissions, see [Permissions Related to Bucket Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your
 Amazon S3 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md") in the *Amazon S3 User Guide*.
* **Directory bucket permissions** - To grant access to
 this API operation, you must have the `s3express:PutEncryptionConfiguration`
 permission in an IAM identity-based policy instead of a bucket policy. Cross-account access to this API operation isn't supported. This operation can only be performed by the AWS account that owns the resource.
 For more information about directory bucket policies and permissions, see [AWS Identity and Access Management (IAM) for S3 Express One Zone](../userguide/s3-express-security-iam.md "../userguide/s3-express-security-iam.md") in the *Amazon S3 User Guide*.


To set a directory bucket default encryption with SSE-KMS, you must also have the
 `kms:GenerateDataKey` and the `kms:Decrypt` permissions in IAM
 identity-based policies and AWS KMS key policies for the target AWS KMS key.


HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is `s3express-control.*region-code*.amazonaws.com`.



The following operations are related to `PutBucketEncryption`:


* [GetBucketEncryption](API_GetBucketEncryption.md "API_GetBucketEncryption.md")
* [DeleteBucketEncryption](API_DeleteBucketEncryption.md "API_DeleteBucketEncryption.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?encryption HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[ServerSideEncryptionConfiguration](#AmazonS3-PutBucketEncryption-request-ServerSideEncryptionConfiguration "#AmazonS3-PutBucketEncryption-request-ServerSideEncryptionConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[Rule](#AmazonS3-PutBucketEncryption-request-Rules "#AmazonS3-PutBucketEncryption-request-Rules")>
      <[ApplyServerSideEncryptionByDefault](API_ServerSideEncryptionRule.md#AmazonS3-Type-ServerSideEncryptionRule-ApplyServerSideEncryptionByDefault "API_ServerSideEncryptionRule.md#AmazonS3-Type-ServerSideEncryptionRule-ApplyServerSideEncryptionByDefault")>
         <[KMSMasterKeyID](API_ServerSideEncryptionByDefault.md#AmazonS3-Type-ServerSideEncryptionByDefault-KMSMasterKeyID "API_ServerSideEncryptionByDefault.md#AmazonS3-Type-ServerSideEncryptionByDefault-KMSMasterKeyID")>`string`</[KMSMasterKeyID](API_ServerSideEncryptionByDefault.md#AmazonS3-Type-ServerSideEncryptionByDefault-KMSMasterKeyID "API_ServerSideEncryptionByDefault.md#AmazonS3-Type-ServerSideEncryptionByDefault-KMSMasterKeyID")>
         <[SSEAlgorithm](API_ServerSideEncryptionByDefault.md#AmazonS3-Type-ServerSideEncryptionByDefault-SSEAlgorithm "API_ServerSideEncryptionByDefault.md#AmazonS3-Type-ServerSideEncryptionByDefault-SSEAlgorithm")>`string`</[SSEAlgorithm](API_ServerSideEncryptionByDefault.md#AmazonS3-Type-ServerSideEncryptionByDefault-SSEAlgorithm "API_ServerSideEncryptionByDefault.md#AmazonS3-Type-ServerSideEncryptionByDefault-SSEAlgorithm")>
      </[ApplyServerSideEncryptionByDefault](API_ServerSideEncryptionRule.md#AmazonS3-Type-ServerSideEncryptionRule-ApplyServerSideEncryptionByDefault "API_ServerSideEncryptionRule.md#AmazonS3-Type-ServerSideEncryptionRule-ApplyServerSideEncryptionByDefault")>
      <[BucketKeyEnabled](API_ServerSideEncryptionRule.md#AmazonS3-Type-ServerSideEncryptionRule-BucketKeyEnabled "API_ServerSideEncryptionRule.md#AmazonS3-Type-ServerSideEncryptionRule-BucketKeyEnabled")>`boolean`</[BucketKeyEnabled](API_ServerSideEncryptionRule.md#AmazonS3-Type-ServerSideEncryptionRule-BucketKeyEnabled "API_ServerSideEncryptionRule.md#AmazonS3-Type-ServerSideEncryptionRule-BucketKeyEnabled")>
   </[Rule](#AmazonS3-PutBucketEncryption-request-Rules "#AmazonS3-PutBucketEncryption-request-Rules")>
   ...
</[ServerSideEncryptionConfiguration](#AmazonS3-PutBucketEncryption-request-ServerSideEncryptionConfiguration "#AmazonS3-PutBucketEncryption-request-ServerSideEncryptionConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketEncryption_RequestSyntax "#API_PutBucketEncryption_RequestSyntax")**


Specifies default encryption for a bucket using server-side encryption with different key
 options.



**Directory buckets**  - When you use this operation with a directory bucket, you must use path-style requests in the format `https://s3express-control.*region-code*.amazonaws.com/*bucket-name*`. Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format `*bucket-base-name*--*zone-id*--x-s3` (for example, `*DOC-EXAMPLE-BUCKET*--*usw2-az1*--x-s3`). For information about bucket naming restrictions, see [Directory bucket naming rules](../userguide/directory-bucket-naming-rules.md "../userguide/directory-bucket-naming-rules.md") in the *Amazon S3 User Guide*



Required: Yes




**[Content-MD5](#API_PutBucketEncryption_RequestSyntax "#API_PutBucketEncryption_RequestSyntax")**


The Base64 encoded 128-bit `MD5` digest of the server-side encryption
 configuration.


For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-expected-bucket-owner](#API_PutBucketEncryption_RequestSyntax "#API_PutBucketEncryption_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).


###### Note

For directory buckets, this header is not supported in this API operation. If you specify this header, the request fails with the HTTP status code 
`501 Not Implemented`.




**[x-amz-sdk-checksum-algorithm](#API_PutBucketEncryption_RequestSyntax "#API_PutBucketEncryption_RequestSyntax")**


Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
 additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
 `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
 information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
 parameter.


###### Note

For directory buckets, when you use AWS SDKs, `CRC32` is the default checksum algorithm that's used for performance.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[ServerSideEncryptionConfiguration](#API_PutBucketEncryption_RequestSyntax "#API_PutBucketEncryption_RequestSyntax")**


Root level tag for the ServerSideEncryptionConfiguration parameters.


Required: Yes




**[Rule](#API_PutBucketEncryption_RequestSyntax "#API_PutBucketEncryption_RequestSyntax")**


Container for information about a particular server-side encryption configuration rule.


Type: Array of [ServerSideEncryptionRule](API_ServerSideEncryptionRule.md "API_ServerSideEncryptionRule.md") data types


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


In the request, you specify the encryption configuration in the request body. The encryption
 configuration is specified as XML, as shown in the following examples that show setting encryption
 using SSE-S3, SSE-KMS, or DSSE-KMS.


### Request Body for Setting SSE-S3 for general purpose buckets


This example illustrates one usage of PutBucketEncryption.



```

           <ServerSideEncryptionConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
               <Rule>
                  <ApplyServerSideEncryptionByDefault>
                     <SSEAlgorithm>AES256</SSEAlgorithm>
                  </ApplyServerSideEncryptionByDefault>
               </Rule>
            </ServerSideEncryptionConfiguration>
        
```

### Request Body for Setting SSE-KMS for general purpose buckets


This example illustrates one usage of PutBucketEncryption.



```

           <ServerSideEncryptionConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
               <Rule>
                  <ApplyServerSideEncryptionByDefault>
                      <SSEAlgorithm>aws:kms:dsse</SSEAlgorithm>
                      <KMSKeyID>arn:aws:kms:us-east-1:1234/5678example</KMSKeyID>
                  </ApplyServerSideEncryptionByDefault>
               </Rule>
            </ServerSideEncryptionConfiguration>
        
```

### Set the Default Encryption Configuration for an S3 general purpose bucket


The following is an example of a PUT /? encryption request that specifies to use SSE-KMS
 encryption.



```
PUT /?encryption HTTP/1.1
Host: examplebucket.<Region>s3.amazonaws.com
Date: Wed, 06 Sep 2017 12:00:00 GMT
Authorization: authorization 
Content-Length: length

<ServerSideEncryptionConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Rule>
    <ApplyServerSideEncryptionByDefault>
        <SSEAlgorithm>aws:kms</SSEAlgorithm>
        <KMSKeyID>arn:aws:kms:us-east-1:1234/5678example</KMSKeyID>
    </ApplyServerSideEncryptionByDefault>
</Rule>
</ServerSideEncryptionConfiguration>
        
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketEncryption "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketEncryption")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketEncryption "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketEncryption")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketEncryption "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketEncryption")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketEncryption "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketEncryption")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketEncryption "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketEncryption")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketEncryption "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketEncryption")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketEncryption "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketEncryption")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketEncryption "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketEncryption")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketEncryption "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketEncryption")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketEncryption "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketEncryption")
