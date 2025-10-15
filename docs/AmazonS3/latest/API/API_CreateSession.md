# CreateSession

Creates a session that establishes temporary security credentials to support fast authentication and
 authorization for the Zonal endpoint API operations on directory buckets. For more information about Zonal endpoint API operations that
 include the Availability Zone in the request endpoint, see [S3 Express One Zone APIs](../userguide/s3-express-APIs.md "../userguide/s3-express-APIs.md") in the
 *Amazon S3 User Guide*. 

To make Zonal endpoint API requests on a directory bucket, use the `CreateSession` API
 operation. Specifically, you grant `s3express:CreateSession` permission to a bucket in
 a bucket policy or an IAM identity-based policy. Then, you use IAM credentials to make the `CreateSession`
 API request on the bucket, which returns temporary security credentials that include the access key ID,
 secret access key, session token, and expiration. These credentials have associated permissions to
 access the Zonal endpoint API operations. After the session is created, you don’t need to use other policies to grant
 permissions to each Zonal endpoint API individually. Instead, in your Zonal endpoint API requests, you sign your
 requests by applying the temporary security credentials of the session to the request headers and
 following the SigV4 protocol for authentication. You also apply the session token to the
 `x-amz-s3session-token` request header for authorization. Temporary security credentials
 are scoped to the bucket and expire after 5 minutes. After the expiration time, any calls that you make
 with those credentials will fail. You must use IAM credentials again to make a
 `CreateSession` API request that generates a new set of temporary credentials for use.
 Temporary credentials cannot be extended or refreshed beyond the original specified interval.

If you use AWS SDKs, SDKs handle the session token refreshes automatically to avoid service
 interruptions when a session expires. We recommend that you use the AWS SDKs to initiate and manage
 requests to the CreateSession API. For more information, see [Performance guidelines and design patterns](../userguide/s3-express-optimizing-performance-guidelines-design-patterns.md#s3-express-optimizing-performance-session-authentication "../userguide/s3-express-optimizing-performance-guidelines-design-patterns.md#s3-express-optimizing-performance-session-authentication") in the
 *Amazon S3 User Guide*.

###### Note


* You must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://*bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](../userguide/endpoint-directory-buckets-AZ.md "../userguide/endpoint-directory-buckets-AZ.md") in the
 *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](../userguide/s3-lzs-for-directory-buckets.md "../userguide/s3-lzs-for-directory-buckets.md") in the
 *Amazon S3 User Guide*.
* **`CopyObject` API operation** - Unlike other
 Zonal endpoint API operations, the `CopyObject` API operation doesn't use the temporary security
 credentials returned from the `CreateSession` API operation for authentication and
 authorization. For information about authentication and authorization of the
 `CopyObject` API operation on directory buckets, see [CopyObject](API_CopyObject.md "API_CopyObject.md").
* **`HeadBucket` API operation** - Unlike other
 Zonal endpoint API operations, the `HeadBucket` API operation doesn't use the temporary security
 credentials returned from the `CreateSession` API operation for authentication and
 authorization. For information about authentication and authorization of the
 `HeadBucket` API operation on directory buckets, see [HeadBucket](API_HeadBucket.md "API_HeadBucket.md").


Permissions

To obtain temporary security credentials, you must create a bucket policy or an IAM identity-based policy that
 grants `s3express:CreateSession` permission to the bucket. In a policy, you can have
 the `s3express:SessionMode` condition key to control who can create a
 `ReadWrite` or `ReadOnly` session. For more information about
 `ReadWrite` or `ReadOnly` sessions, see [`x-amz-create-session-mode`](API_CreateSession.md#API_CreateSession_RequestParameters "API_CreateSession.md#API_CreateSession_RequestParameters"). For example policies, see [Example
 bucket policies for S3 Express One Zone](../userguide/s3-express-security-iam-example-bucket-policies.md "../userguide/s3-express-security-iam-example-bucket-policies.md") and [AWS Identity
 and Access Management (IAM) identity-based policies for S3 Express One Zone](../userguide/s3-express-security-iam-identity-policies.md "../userguide/s3-express-security-iam-identity-policies.md") in the
 *Amazon S3 User Guide*. 


To grant cross-account access to Zonal endpoint API operations, the bucket policy should also grant both
 accounts the `s3express:CreateSession` permission.


If you want to encrypt objects with SSE-KMS, you must also have the
 `kms:GenerateDataKey` and the `kms:Decrypt` permissions in IAM
 identity-based policies and AWS KMS key policies for the target AWS KMS key.



Encryption

For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256`) and server-side encryption with AWS KMS keys (SSE-KMS) (`aws:kms`). We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your 
 `CreateSession` requests or `PUT` object requests. Then, new objects 
 are automatically encrypted with the desired encryption settings. For more
 information, see [Protecting data with server-side encryption](../userguide/s3-express-serv-side-encryption.md "../userguide/s3-express-serv-side-encryption.md") in the *Amazon S3 User Guide*. For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with AWS KMS for new object uploads](../userguide/s3-express-specifying-kms-encryption.md "../userguide/s3-express-specifying-kms-encryption.md").


For [Zonal endpoint (object-level) API operations](../userguide/s3-express-differences.md#s3-express-differences-api-operations "../userguide/s3-express-differences.md#s3-express-differences-api-operations") except [CopyObject](API_CopyObject.md "API_CopyObject.md") and [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md"), 
you authenticate and authorize requests through [CreateSession](API_CreateSession.md "API_CreateSession.md") for low latency. 
 To encrypt new objects in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk")). Then, when a session is created for Zonal endpoint API operations, new objects are automatically encrypted and decrypted with SSE-KMS and S3 Bucket Keys during the session.


###### Note


 Only 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") is supported per directory bucket for the lifetime of the bucket. The [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk") (`aws/s3`) isn't supported. 
 After you specify SSE-KMS as your bucket's default encryption configuration with a customer managed key, you can't change the customer managed key for the bucket's SSE-KMS configuration.
 


In the Zonal endpoint API calls (except [CopyObject](API_CopyObject.md "API_CopyObject.md") and [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md")) using the REST API, 
 you can't override the values of the encryption settings (`x-amz-server-side-encryption`, `x-amz-server-side-encryption-aws-kms-key-id`, `x-amz-server-side-encryption-context`, and `x-amz-server-side-encryption-bucket-key-enabled`) from the `CreateSession` request. 
 You don't need to explicitly specify these encryption settings values in Zonal endpoint API calls, and 
 Amazon S3 will use the encryption settings values from the `CreateSession` request to protect new objects in the directory bucket. 
 


###### Note

When you use the CLI or the AWS SDKs, for `CreateSession`, the session token refreshes automatically to avoid service interruptions when a session expires. The CLI or the AWS SDKs use the bucket's default encryption configuration for the 
 `CreateSession` request. It's not supported to override the encryption settings values in the `CreateSession` request. 
 Also, in the Zonal endpoint API calls (except [CopyObject](API_CopyObject.md "API_CopyObject.md") and [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md")), 
 it's not supported to override the values of the encryption settings from the `CreateSession` request. 





HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`.



###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?session HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-create-session-mode: `SessionMode`
x-amz-server-side-encryption: `ServerSideEncryption`
x-amz-server-side-encryption-aws-kms-key-id: `SSEKMSKeyId`
x-amz-server-side-encryption-context: `SSEKMSEncryptionContext`
x-amz-server-side-encryption-bucket-key-enabled: `BucketKeyEnabled`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_CreateSession_RequestSyntax "#API_CreateSession_RequestSyntax")**


The name of the bucket that you create a session for.


Required: Yes




**[x-amz-create-session-mode](#API_CreateSession_RequestSyntax "#API_CreateSession_RequestSyntax")**


Specifies the mode of the session that will be created, either `ReadWrite` or
 `ReadOnly`. By default, a `ReadWrite` session is created. A
 `ReadWrite` session is capable of executing all the Zonal endpoint API operations on a directory bucket. A
 `ReadOnly` session is constrained to execute the following Zonal endpoint API operations:
 `GetObject`, `HeadObject`, `ListObjectsV2`,
 `GetObjectAttributes`, `ListParts`, and
 `ListMultipartUploads`.


Valid Values: `ReadOnly | ReadWrite`





**[x-amz-server-side-encryption](#API_CreateSession_RequestSyntax "#API_CreateSession_RequestSyntax")**


The server-side encryption algorithm to use when you store objects in the directory bucket.


For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256`) and server-side encryption with AWS KMS keys (SSE-KMS) (`aws:kms`). By default, Amazon S3 encrypts data with SSE-S3. 
 For more
 information, see [Protecting data with server-side encryption](../userguide/serv-side-encryption.md "../userguide/serv-side-encryption.md") in the *Amazon S3 User Guide*.



**S3 access points for Amazon FSx**  - When accessing data stored in Amazon FSx
 file systems using S3 access points, the only valid server side encryption option is `aws:fsx`. All
 Amazon FSx file systems have encryption configured by default and are encrypted at rest. Data is
 automatically encrypted before being written to the file system, and automatically decrypted as it is
 read. These processes are handled transparently by Amazon FSx.


Valid Values: `AES256 | aws:fsx | aws:kms | aws:kms:dsse`





**[x-amz-server-side-encryption-aws-kms-key-id](#API_CreateSession_RequestSyntax "#API_CreateSession_RequestSyntax")**


If you specify `x-amz-server-side-encryption` with `aws:kms`, you must specify the `x-amz-server-side-encryption-aws-kms-key-id` header with the ID (Key ID or Key ARN) of the AWS KMS 
 symmetric encryption customer managed key to use. Otherwise, you get an HTTP `400 Bad Request` error. Only use the key ID or key ARN. The key alias format of the KMS key isn't supported. Also, if the KMS key doesn't exist in the same
 account that't issuing the command, you must use the full Key ARN not the Key ID. 


Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") per directory bucket's lifetime. 
The [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk") (`aws/s3`) isn't supported. 





**[x-amz-server-side-encryption-bucket-key-enabled](#API_CreateSession_RequestSyntax "#API_CreateSession_RequestSyntax")**


Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with
 server-side encryption using AWS KMS keys (SSE-KMS).


S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets 
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](API_CopyObject.md "API_CopyObject.md"), [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md"), [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops "https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops"), or 
 [the import jobs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job "https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.




**[x-amz-server-side-encryption-context](#API_CreateSession_RequestSyntax "#API_CreateSession_RequestSyntax")**


Specifies the AWS KMS Encryption Context as an additional encryption context to use for object encryption. The value of
 this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs. 
 This value is stored as object metadata and automatically gets passed on
 to AWS KMS for future `GetObject` operations on
 this object.



**General purpose buckets** - This value must be explicitly added during `CopyObject` operations if you want an additional encryption context for your object. For more information, see [Encryption context](../userguide/UsingKMSEncryption.md#encryption-context "../userguide/UsingKMSEncryption.md#encryption-context") in the *Amazon S3 User Guide*.



**Directory buckets** - You can optionally provide an explicit encryption context value. The value must match the default encryption context - the bucket Amazon Resource Name (ARN). An additional encryption context value is not supported. 




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
x-amz-server-side-encryption: `ServerSideEncryption`
x-amz-server-side-encryption-aws-kms-key-id: `SSEKMSKeyId`
x-amz-server-side-encryption-context: `SSEKMSEncryptionContext`
x-amz-server-side-encryption-bucket-key-enabled: `BucketKeyEnabled`
<?xml version="1.0" encoding="UTF-8"?>
<[CreateSessionResult](#AmazonS3-CreateSession-response-CreateSessionOutput "#AmazonS3-CreateSession-response-CreateSessionOutput")>
   <[Credentials](#AmazonS3-CreateSession-response-Credentials "#AmazonS3-CreateSession-response-Credentials")>
      <[AccessKeyId](API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-AccessKeyId "API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-AccessKeyId")>***string***</[AccessKeyId](API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-AccessKeyId "API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-AccessKeyId")>
      <[Expiration](API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-Expiration "API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-Expiration")>***timestamp***</[Expiration](API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-Expiration "API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-Expiration")>
      <[SecretAccessKey](API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-SecretAccessKey "API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-SecretAccessKey")>***string***</[SecretAccessKey](API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-SecretAccessKey "API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-SecretAccessKey")>
      <[SessionToken](API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-SessionToken "API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-SessionToken")>***string***</[SessionToken](API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-SessionToken "API_SessionCredentials.md#AmazonS3-Type-SessionCredentials-SessionToken")>
   </[Credentials](#AmazonS3-CreateSession-response-Credentials "#AmazonS3-CreateSession-response-Credentials")>
</[CreateSessionResult](#AmazonS3-CreateSession-response-CreateSessionOutput "#AmazonS3-CreateSession-response-CreateSessionOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-server-side-encryption](#API_CreateSession_ResponseSyntax "#API_CreateSession_ResponseSyntax")**


The server-side encryption algorithm used when you store objects in the directory bucket.


###### Note

When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side
 encryption option is `aws:fsx`.


Valid Values: `AES256 | aws:fsx | aws:kms | aws:kms:dsse`





**[x-amz-server-side-encryption-aws-kms-key-id](#API_CreateSession_ResponseSyntax "#API_CreateSession_ResponseSyntax")**


If you specify `x-amz-server-side-encryption` with `aws:kms`, this header indicates the ID of the AWS KMS 
 symmetric encryption customer managed key that was used for object encryption.




**[x-amz-server-side-encryption-bucket-key-enabled](#API_CreateSession_ResponseSyntax "#API_CreateSession_ResponseSyntax")**


Indicates whether to use an S3 Bucket Key for server-side encryption
 with AWS KMS keys (SSE-KMS).




**[x-amz-server-side-encryption-context](#API_CreateSession_ResponseSyntax "#API_CreateSession_ResponseSyntax")**


If present, indicates the AWS KMS Encryption Context to use for object encryption. The value of
 this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs. 
 This value is stored as object metadata and automatically gets
 passed on to AWS KMS for future `GetObject` 
 operations on this object.




The following data is returned in XML format by the service.





**[CreateSessionResult](#API_CreateSession_ResponseSyntax "#API_CreateSession_ResponseSyntax")**


Root level tag for the CreateSessionResult parameters.


Required: Yes




**[Credentials](#API_CreateSession_ResponseSyntax "#API_CreateSession_ResponseSyntax")**


The established temporary security credentials for the created session.


Type: [SessionCredentials](API_SessionCredentials.md "API_SessionCredentials.md") data type




## Errors





**NoSuchBucket** 


The specified bucket does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/CreateSession "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/CreateSession")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/CreateSession "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/CreateSession")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateSession "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateSession")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/CreateSession "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/CreateSession")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateSession "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateSession")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/CreateSession "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/CreateSession")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/CreateSession "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/CreateSession")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/CreateSession "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/CreateSession")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/CreateSession "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/CreateSession")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CreateSession "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CreateSession")
