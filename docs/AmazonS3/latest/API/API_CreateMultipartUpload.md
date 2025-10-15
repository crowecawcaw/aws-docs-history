# CreateMultipartUpload

###### Important

End of support notice: As of October 1, 2025, Amazon S3 has discontinued support for Email Grantee Access Control Lists (ACLs). If you attempt to use an Email Grantee ACL in a request after October 1, 2025, 
 the request will receive an `HTTP 405` (Method Not Allowed) error.

This change affects the following AWS Regions: US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Ireland), and South America (São Paulo).

This action initiates a multipart upload and returns an upload ID. This upload ID is used to
 associate all of the parts in the specific multipart upload. You specify this upload ID in each of your
 subsequent upload part requests (see [UploadPart](API_UploadPart.md "API_UploadPart.md")). You also include this upload ID in
 the final request to either complete or abort the multipart upload request. For more information about
 multipart uploads, see [Multipart
 Upload Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html") in the *Amazon S3 User Guide*.

###### Note

After you initiate a multipart upload and upload one or more parts, to stop being charged for
 storing the uploaded parts, you must either complete or abort the multipart upload. Amazon S3 frees up the
 space used to store the parts and stops charging you for storing them only after you either complete
 or abort a multipart upload. 

If you have configured a lifecycle rule to abort incomplete multipart uploads, the created multipart
 upload must be completed within the number of days specified in the bucket lifecycle configuration.
 Otherwise, the incomplete multipart upload becomes eligible for an abort action and Amazon S3 aborts the
 multipart upload. For more information, see [Aborting
 Incomplete Multipart Uploads Using a Bucket Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config "https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config").

###### Note


* **Directory buckets**  -
 S3 Lifecycle is not supported by directory buckets.
* **Directory buckets**  - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://*amzn-s3-demo-bucket*.s3express-*zone-id*.*region-code*.amazonaws.com/*key-name*`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](../userguide/endpoint-directory-buckets-AZ.md "../userguide/endpoint-directory-buckets-AZ.md") in the
 *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](../userguide/s3-lzs-for-directory-buckets.md "../userguide/s3-lzs-for-directory-buckets.md") in the
 *Amazon S3 User Guide*.


Request signing

For request signing, multipart upload is just a series of regular requests. You initiate a
 multipart upload, send one or more requests to upload parts, and then complete the multipart
 upload process. You sign each request individually. There is nothing special about signing
 multipart upload requests. For more information about signing, see [Authenticating Requests (AWS
 Signature Version 4)](sig-v4-authenticating-requests.md "sig-v4-authenticating-requests.md") in the *Amazon S3 User Guide*.



Permissions


* **General purpose bucket permissions** - To perform a
 multipart upload with encryption using an AWS Key Management Service (AWS KMS) KMS key, the requester must have
 permission to the `kms:Decrypt` and `kms:GenerateDataKey` actions on the
 key. The requester must also have permissions for the `kms:GenerateDataKey` action
 for the `CreateMultipartUpload` API. Then, the requester needs permissions for the
 `kms:Decrypt` action on the `UploadPart` and
 `UploadPartCopy` APIs. These permissions are required because Amazon S3 must decrypt
 and read data from the encrypted file parts before it completes the multipart upload. For more
 information, see [Multipart upload API and
 permissions](../userguide/mpuoverview.md#mpuAndPermissions "../userguide/mpuoverview.md#mpuAndPermissions") and [Protecting data using server-side
 encryption with AWS KMS](../userguide/UsingKMSEncryption.md "../userguide/UsingKMSEncryption.md") in the *Amazon S3 User Guide*.
* **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](API_CreateSession.md "API_CreateSession.md") API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use. 
AWS CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](API_CreateSession.md "API_CreateSession.md").


Encryption


* **General purpose buckets** - Server-side encryption is for
 data encryption at rest. Amazon S3 encrypts your data as it writes it to disks in its data centers
 and decrypts it when you access it. Amazon S3 automatically encrypts all new objects that are
 uploaded to an S3 bucket. When doing a multipart upload, if you don't specify encryption
 information in your request, the encryption setting of the uploaded parts is set to the
 default encryption configuration of the destination bucket. By default, all buckets have a
 base level of encryption configuration that uses server-side encryption with Amazon S3 managed keys
 (SSE-S3). If the destination bucket has a default encryption configuration that uses
 server-side encryption with an AWS Key Management Service (AWS KMS) key (SSE-KMS), or a customer-provided
 encryption key (SSE-C), Amazon S3 uses the corresponding KMS key, or a customer-provided key to
 encrypt the uploaded parts. When you perform a CreateMultipartUpload operation, if you want to
 use a different type of encryption setting for the uploaded parts, you can request that Amazon S3
 encrypts the object with a different encryption key (such as an Amazon S3 managed key, a KMS key,
 or a customer-provided key). When the encryption setting in your request is different from the
 default encryption configuration of the destination bucket, the encryption setting in your
 request takes precedence. If you choose to provide your own encryption key, the request
 headers you provide in [UploadPart](API_UploadPart.md "API_UploadPart.md") and [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md") requests must match the headers you used in the
 `CreateMultipartUpload` request.




	+ Use KMS keys (SSE-KMS) that include the AWS managed key (`aws/s3`) and
	 AWS KMS customer managed keys stored in AWS Key Management Service (AWS KMS) – If you want AWS to manage the keys used
	 to encrypt data, specify the following headers in the request.
	
	
	
	
		- `x-amz-server-side-encryption`
		- `x-amz-server-side-encryption-aws-kms-key-id`
		- `x-amz-server-side-encryption-context`
	###### Note
	
	
	
		- If you specify `x-amz-server-side-encryption:aws:kms`, but don't
		 provide `x-amz-server-side-encryption-aws-kms-key-id`, Amazon S3 uses the
		 AWS managed key (`aws/s3` key) in AWS KMS to protect the data.
		- To perform a multipart upload with encryption by using an AWS KMS key, the
		 requester must have permission to the `kms:Decrypt` and
		 `kms:GenerateDataKey*` actions on the key. These permissions are
		 required because Amazon S3 must decrypt and read data from the encrypted file parts
		 before it completes the multipart upload. For more information, see [Multipart
		 upload API and permissions](../userguide/mpuoverview.md#mpuAndPermissions "../userguide/mpuoverview.md#mpuAndPermissions") and [Protecting data using
		 server-side encryption with AWS KMS](../userguide/UsingKMSEncryption.md "../userguide/UsingKMSEncryption.md") in the
		 *Amazon S3 User Guide*.
		- If your AWS Identity and Access Management (IAM) user or role is in the same AWS account as the
		 KMS key, then you must have these permissions on the key policy. If your IAM
		 user or role is in a different account from the key, then you must have the
		 permissions on both the key policy and your IAM user or role.
		- All `GET` and `PUT` requests for an object protected by
		 AWS KMS fail if you don't make them by using Secure Sockets Layer (SSL), Transport
		 Layer Security (TLS), or Signature Version 4. For information about configuring any
		 of the officially supported AWS SDKs and AWS CLI, see [Specifying the Signature Version in Request
		 Authentication](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version "https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version") in the *Amazon S3 User Guide*.
	For more information about server-side encryption with AWS KMS keys (SSE-KMS), see
	 [Protecting Data Using Server-Side Encryption with KMS keys](../userguide/UsingKMSEncryption.md "../userguide/UsingKMSEncryption.md") in the
	 *Amazon S3 User Guide*.
	+ Use customer-provided encryption keys (SSE-C) – If you want to manage your own
	 encryption keys, provide all the following headers in the request.
	
	
	
	
		- `x-amz-server-side-encryption-customer-algorithm`
		- `x-amz-server-side-encryption-customer-key`
		- `x-amz-server-side-encryption-customer-key-MD5`
	For more information about server-side encryption with customer-provided encryption
	 keys (SSE-C), see  [Protecting data
	 using server-side encryption with customer-provided encryption keys (SSE-C)](../userguide/ServerSideEncryptionCustomerKeys.md "../userguide/ServerSideEncryptionCustomerKeys.md") in
	 the *Amazon S3 User Guide*.
* **Directory buckets** -
 For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256`) and server-side encryption with AWS KMS keys (SSE-KMS) (`aws:kms`). We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your 
 `CreateSession` requests or `PUT` object requests. Then, new objects 
 are automatically encrypted with the desired encryption settings. For more
 information, see [Protecting data with server-side encryption](../userguide/s3-express-serv-side-encryption.md "../userguide/s3-express-serv-side-encryption.md") in the *Amazon S3 User Guide*. For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with AWS KMS for new object uploads](../userguide/s3-express-specifying-kms-encryption.md "../userguide/s3-express-specifying-kms-encryption.md").


In the Zonal endpoint API calls (except [CopyObject](API_CopyObject.md "API_CopyObject.md") and [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md")) using the REST API, the encryption request headers must match the encryption settings that are specified in the `CreateSession` request. 
 You can't override the values of the encryption settings (`x-amz-server-side-encryption`, `x-amz-server-side-encryption-aws-kms-key-id`, `x-amz-server-side-encryption-context`, and `x-amz-server-side-encryption-bucket-key-enabled`) that are specified in the `CreateSession` request. 
 You don't need to explicitly specify these encryption settings values in Zonal endpoint API calls, and 
 Amazon S3 will use the encryption settings values from the `CreateSession` request to protect new objects in the directory bucket. 
 


###### Note

When you use the CLI or the AWS SDKs, for `CreateSession`, the session token refreshes automatically to avoid service interruptions when a session expires. The CLI or the AWS SDKs use the bucket's default encryption configuration for the 
 `CreateSession` request. It's not supported to override the encryption settings values in the `CreateSession` request. 
 So in the Zonal endpoint API calls (except [CopyObject](API_CopyObject.md "API_CopyObject.md") and [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md")), 
 the encryption request headers must match the default encryption configuration of the directory bucket.




###### Note

For directory buckets, when you perform a `CreateMultipartUpload` operation
 and an `UploadPartCopy` operation, the request headers you provide in the
 `CreateMultipartUpload` request must match the default encryption configuration
 of the destination bucket.


HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`.



The following operations are related to `CreateMultipartUpload`:


* [UploadPart](API_UploadPart.md "API_UploadPart.md")
* [CompleteMultipartUpload](API_CompleteMultipartUpload.md "API_CompleteMultipartUpload.md")
* [AbortMultipartUpload](API_AbortMultipartUpload.md "API_AbortMultipartUpload.md")
* [ListParts](API_ListParts.md "API_ListParts.md")
* [ListMultipartUploads](API_ListMultipartUploads.md "API_ListMultipartUploads.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /{Key+}?uploads HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-acl: `ACL`
Cache-Control: `CacheControl`
Content-Disposition: `ContentDisposition`
Content-Encoding: `ContentEncoding`
Content-Language: `ContentLanguage`
Content-Type: `ContentType`
Expires: `Expires`
x-amz-grant-full-control: `GrantFullControl`
x-amz-grant-read: `GrantRead`
x-amz-grant-read-acp: `GrantReadACP`
x-amz-grant-write-acp: `GrantWriteACP`
x-amz-server-side-encryption: `ServerSideEncryption`
x-amz-storage-class: `StorageClass`
x-amz-website-redirect-location: `WebsiteRedirectLocation`
x-amz-server-side-encryption-customer-algorithm: `SSECustomerAlgorithm`
x-amz-server-side-encryption-customer-key: `SSECustomerKey`
x-amz-server-side-encryption-customer-key-MD5: `SSECustomerKeyMD5`
x-amz-server-side-encryption-aws-kms-key-id: `SSEKMSKeyId`
x-amz-server-side-encryption-context: `SSEKMSEncryptionContext`
x-amz-server-side-encryption-bucket-key-enabled: `BucketKeyEnabled`
x-amz-request-payer: `RequestPayer`
x-amz-tagging: `Tagging`
x-amz-object-lock-mode: `ObjectLockMode`
x-amz-object-lock-retain-until-date: `ObjectLockRetainUntilDate`
x-amz-object-lock-legal-hold: `ObjectLockLegalHoldStatus`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
x-amz-checksum-algorithm: `ChecksumAlgorithm`
x-amz-checksum-type: `ChecksumType`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


The name of the bucket where the multipart upload is initiated and where the object is
 uploaded.



**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `*bucket-base-name*--*zone-id*--x-s3` (for example, `*amzn-s3-demo-bucket*--*usw2-az1*--x-s3`). For information about bucket naming
 restrictions, see [Directory bucket naming
 rules](../userguide/directory-bucket-naming-rules.md "../userguide/directory-bucket-naming-rules.md") in the *Amazon S3 User Guide*.



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.


###### Note

Object Lambda access points are not supported by directory buckets.



**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the 
 form `*AccessPointName*-*AccountId*.*outpostID*.s3-outposts.*Region*.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.


Required: Yes




**[Cache-Control](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specifies caching behavior along the request/reply chain.




**[Content-Disposition](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specifies presentational information for the object.




**[Content-Encoding](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specifies what content encodings have been applied to the object and thus what decoding mechanisms
 must be applied to obtain the media-type referenced by the Content-Type header field.


###### Note

For directory buckets, only the `aws-chunked` value is supported in this header field.




**[Content-Language](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


The language that the content is in.




**[Content-Type](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


A standard MIME type describing the format of the object data.




**[Expires](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


The date and time at which the object is no longer cacheable.




**[Key](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Object key for which the multipart upload is to be initiated.


Length Constraints: Minimum length of 1.


Required: Yes




**[x-amz-acl](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


The canned ACL to apply to the object. Amazon S3 supports a set of predefined ACLs, known as
 *canned ACLs*. Each canned ACL has a predefined set of grantees and permissions.
 For more information, see [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL "https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL") in the
 *Amazon S3 User Guide*.


By default, all objects are private. Only the owner has full access control. When uploading an
 object, you can grant access permissions to individual AWS accounts or to predefined groups defined by
 Amazon S3. These permissions are then added to the access control list (ACL) on the new object. For more
 information, see [Using
 ACLs](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html"). One way to grant the permissions using the request headers is to specify a canned ACL
 with the `x-amz-acl` request header.


###### Note


* This functionality is not supported for directory buckets.
* This functionality is not supported for Amazon S3 on Outposts.

Valid Values: `private | public-read | public-read-write | authenticated-read | aws-exec-read | bucket-owner-read | bucket-owner-full-control`





**[x-amz-checksum-algorithm](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Indicates the algorithm that you want Amazon S3 to use to create the checksum for the object. For more information, see
 [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





**[x-amz-checksum-type](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Indicates the checksum type that you want Amazon S3 to use to calculate the object’s checksum value. For
 more information, see [Checking object integrity in the Amazon S3
 User Guide](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md").


Valid Values: `COMPOSITE | FULL_OBJECT`





**[x-amz-expected-bucket-owner](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-grant-full-control](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specify access permissions explicitly to give the grantee READ, READ\_ACP, and WRITE\_ACP permissions
 on the object.


By default, all objects are private. Only the owner has full access control. When uploading an
 object, you can use this header to explicitly grant access permissions to specific AWS accounts or
 groups. This header maps to specific permissions that Amazon S3 supports in an ACL. For more information, see
 [Access Control List (ACL)
 Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html") in the *Amazon S3 User Guide*.


You specify each grantee as a type=value pair, where the type is one of the following:



* `id` – if the value specified is the canonical user ID of an AWS account
* `uri` – if you are granting permissions to a predefined group
* `emailAddress` – if the value specified is the email address of an
 AWS account
 


###### Note

Using email addresses to specify a grantee is only supported in the following AWS Regions: 



	+ US East (N. Virginia)
	+ US West (N. California)
	+ US West (Oregon)
	+ Asia Pacific (Singapore)
	+ Asia Pacific (Sydney)
	+ Asia Pacific (Tokyo)
	+ Europe (Ireland)
	+ South America (São Paulo)For a list of all the Amazon S3 supported Regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the AWS General Reference.

For example, the following `x-amz-grant-read` header grants the AWS accounts identified by account IDs permissions to read object data and its metadata:



`x-amz-grant-read: id="11112222333", id="444455556666"` 



###### Note


* This functionality is not supported for directory buckets.
* This functionality is not supported for Amazon S3 on Outposts.



**[x-amz-grant-read](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specify access permissions explicitly to allow grantee to read the object data and its
 metadata.


By default, all objects are private. Only the owner has full access control. When uploading an
 object, you can use this header to explicitly grant access permissions to specific AWS accounts or
 groups. This header maps to specific permissions that Amazon S3 supports in an ACL. For more information, see
 [Access Control List (ACL)
 Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html") in the *Amazon S3 User Guide*.


You specify each grantee as a type=value pair, where the type is one of the following:



* `id` – if the value specified is the canonical user ID of an AWS account
* `uri` – if you are granting permissions to a predefined group
* `emailAddress` – if the value specified is the email address of an
 AWS account
 


###### Note

Using email addresses to specify a grantee is only supported in the following AWS Regions: 



	+ US East (N. Virginia)
	+ US West (N. California)
	+ US West (Oregon)
	+ Asia Pacific (Singapore)
	+ Asia Pacific (Sydney)
	+ Asia Pacific (Tokyo)
	+ Europe (Ireland)
	+ South America (São Paulo)For a list of all the Amazon S3 supported Regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the AWS General Reference.

For example, the following `x-amz-grant-read` header grants the AWS accounts identified by account IDs permissions to read object data and its metadata:



`x-amz-grant-read: id="11112222333", id="444455556666"` 



###### Note


* This functionality is not supported for directory buckets.
* This functionality is not supported for Amazon S3 on Outposts.



**[x-amz-grant-read-acp](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specify access permissions explicitly to allows grantee to read the object ACL.


By default, all objects are private. Only the owner has full access control. When uploading an
 object, you can use this header to explicitly grant access permissions to specific AWS accounts or
 groups. This header maps to specific permissions that Amazon S3 supports in an ACL. For more information, see
 [Access Control List (ACL)
 Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html") in the *Amazon S3 User Guide*.


You specify each grantee as a type=value pair, where the type is one of the following:



* `id` – if the value specified is the canonical user ID of an AWS account
* `uri` – if you are granting permissions to a predefined group
* `emailAddress` – if the value specified is the email address of an
 AWS account
 


###### Note

Using email addresses to specify a grantee is only supported in the following AWS Regions: 



	+ US East (N. Virginia)
	+ US West (N. California)
	+ US West (Oregon)
	+ Asia Pacific (Singapore)
	+ Asia Pacific (Sydney)
	+ Asia Pacific (Tokyo)
	+ Europe (Ireland)
	+ South America (São Paulo)For a list of all the Amazon S3 supported Regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the AWS General Reference.

For example, the following `x-amz-grant-read` header grants the AWS accounts identified by account IDs permissions to read object data and its metadata:



`x-amz-grant-read: id="11112222333", id="444455556666"` 



###### Note


* This functionality is not supported for directory buckets.
* This functionality is not supported for Amazon S3 on Outposts.



**[x-amz-grant-write-acp](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specify access permissions explicitly to allows grantee to allow grantee to write the ACL for the
 applicable object.


By default, all objects are private. Only the owner has full access control. When uploading an
 object, you can use this header to explicitly grant access permissions to specific AWS accounts or
 groups. This header maps to specific permissions that Amazon S3 supports in an ACL. For more information, see
 [Access Control List (ACL)
 Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html") in the *Amazon S3 User Guide*.


You specify each grantee as a type=value pair, where the type is one of the following:



* `id` – if the value specified is the canonical user ID of an AWS account
* `uri` – if you are granting permissions to a predefined group
* `emailAddress` – if the value specified is the email address of an
 AWS account
 


###### Note

Using email addresses to specify a grantee is only supported in the following AWS Regions: 



	+ US East (N. Virginia)
	+ US West (N. California)
	+ US West (Oregon)
	+ Asia Pacific (Singapore)
	+ Asia Pacific (Sydney)
	+ Asia Pacific (Tokyo)
	+ Europe (Ireland)
	+ South America (São Paulo)For a list of all the Amazon S3 supported Regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the AWS General Reference.

For example, the following `x-amz-grant-read` header grants the AWS accounts identified by account IDs permissions to read object data and its metadata:



`x-amz-grant-read: id="11112222333", id="444455556666"` 



###### Note


* This functionality is not supported for directory buckets.
* This functionality is not supported for Amazon S3 on Outposts.



**[x-amz-object-lock-legal-hold](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specifies whether you want to apply a legal hold to the uploaded object.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `ON | OFF`





**[x-amz-object-lock-mode](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specifies the Object Lock mode that you want to apply to the uploaded object.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `GOVERNANCE | COMPLIANCE`





**[x-amz-object-lock-retain-until-date](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specifies the date and time when you want the Object Lock to expire.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-request-payer](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Confirms that the requester knows that they will be charged for the request. Bucket owners need not
 specify this parameter in their requests. If either the source or destination S3 bucket has Requester
 Pays enabled, the requester will pay for corresponding charges to copy the object. For information about
 downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-server-side-encryption](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


The server-side encryption algorithm used when you store this object in Amazon S3 or Amazon FSx.



* **Directory buckets**  -
 For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256`) and server-side encryption with AWS KMS keys (SSE-KMS) (`aws:kms`). We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your 
 `CreateSession` requests or `PUT` object requests. Then, new objects 
 are automatically encrypted with the desired encryption settings. For more
 information, see [Protecting data with server-side encryption](../userguide/s3-express-serv-side-encryption.md "../userguide/s3-express-serv-side-encryption.md") in the *Amazon S3 User Guide*. For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with AWS KMS for new object uploads](../userguide/s3-express-specifying-kms-encryption.md "../userguide/s3-express-specifying-kms-encryption.md"). 


In the Zonal endpoint API calls (except [CopyObject](API_CopyObject.md "API_CopyObject.md") and [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md")) using the REST API, the encryption request headers must match the encryption settings that are specified in the `CreateSession` request. 
 You can't override the values of the encryption settings (`x-amz-server-side-encryption`, `x-amz-server-side-encryption-aws-kms-key-id`, `x-amz-server-side-encryption-context`, and `x-amz-server-side-encryption-bucket-key-enabled`) that are specified in the `CreateSession` request. 
 You don't need to explicitly specify these encryption settings values in Zonal endpoint API calls, and 
 Amazon S3 will use the encryption settings values from the `CreateSession` request to protect new objects in the directory bucket. 
 


###### Note

When you use the CLI or the AWS SDKs, for `CreateSession`, the session token refreshes automatically to avoid service interruptions when a session expires. The CLI or the AWS SDKs use the bucket's default encryption configuration for the 
 `CreateSession` request. It's not supported to override the encryption settings values in the `CreateSession` request. 
 So in the Zonal endpoint API calls (except [CopyObject](API_CopyObject.md "API_CopyObject.md") and [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md")), 
 the encryption request headers must match the default encryption configuration of the directory bucket.
* **S3 access points for Amazon FSx**  - When accessing data stored in
 Amazon FSx file systems using S3 access points, the only valid server side encryption option is
 `aws:fsx`. All Amazon FSx file systems have encryption configured by default and are
 encrypted at rest. Data is automatically encrypted before being written to the file system, and
 automatically decrypted as it is read. These processes are handled transparently by Amazon FSx.

Valid Values: `AES256 | aws:fsx | aws:kms | aws:kms:dsse`





**[x-amz-server-side-encryption-aws-kms-key-id](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specifies the AWS KMS key ID (Key ID, Key ARN, or Key Alias) to use for object encryption. If the KMS key doesn't exist in the same
 account that's issuing the command, you must use the full Key ARN not the Key ID.



**General purpose buckets** - If you specify `x-amz-server-side-encryption` with `aws:kms` or `aws:kms:dsse`, this header specifies the ID (Key ID, Key ARN, or Key Alias) of the AWS KMS 
 key to use. If you specify
 `x-amz-server-side-encryption:aws:kms` or
 `x-amz-server-side-encryption:aws:kms:dsse`, but do not provide `x-amz-server-side-encryption-aws-kms-key-id`, Amazon S3 uses the AWS managed key
 (`aws/s3`) to protect the data.



**Directory buckets** - To encrypt data using SSE-KMS, it's recommended to specify the 
`x-amz-server-side-encryption` header to `aws:kms`. Then, the `x-amz-server-side-encryption-aws-kms-key-id` header implicitly uses 
the bucket's default KMS customer managed key ID. If you want to explicitly set the `x-amz-server-side-encryption-aws-kms-key-id` header, it must match the bucket's default customer managed key (using key ID or ARN, not alias). Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") per directory bucket's lifetime. 
The [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk") (`aws/s3`) isn't supported. 
 
 Incorrect key specification results in an HTTP `400 Bad Request` error. 




**[x-amz-server-side-encryption-bucket-key-enabled](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with
 server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS).



**General purpose buckets** - Setting this header to
 `true` causes Amazon S3 to use an S3 Bucket Key for object encryption with
 SSE-KMS. Also, specifying this header with a PUT action doesn't affect bucket-level settings for S3
 Bucket Key.



**Directory buckets** - S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets 
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](API_CopyObject.md "API_CopyObject.md"), [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md"), [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops "https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops"), or 
 [the import jobs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job "https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.




**[x-amz-server-side-encryption-context](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specifies the AWS KMS Encryption Context to use for object encryption. The value of
 this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs.



**Directory buckets** - You can optionally provide an explicit encryption context value. The value must match the default encryption context - the bucket Amazon Resource Name (ARN). An additional encryption context value is not supported. 




**[x-amz-server-side-encryption-customer-algorithm](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specifies the algorithm to use when encrypting the object (for example, AES256).


###### Note

This functionality is not supported for directory buckets.




**[x-amz-server-side-encryption-customer-key](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is
 used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must
 be appropriate for use with the algorithm specified in the
 `x-amz-server-side-encryption-customer-algorithm` header.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-server-side-encryption-customer-key-MD5](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


Specifies the 128-bit MD5 digest of the customer-provided encryption key according to RFC 1321. Amazon S3
 uses this header for a message integrity check to ensure that the encryption key was transmitted without
 error.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-storage-class](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


By default, Amazon S3 uses the STANDARD Storage Class to store newly created objects. The STANDARD
 storage class provides high durability and high availability. Depending on performance needs, you can
 specify a different Storage Class. For more information, see [Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html") in the
 *Amazon S3 User Guide*.


###### Note


* Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in
 Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in
 Dedicated Local Zones.
* Amazon S3 on Outposts only uses the OUTPOSTS Storage Class.

Valid Values: `STANDARD | REDUCED_REDUNDANCY | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | OUTPOSTS | GLACIER_IR | SNOW | EXPRESS_ONEZONE | FSX_OPENZFS`





**[x-amz-tagging](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


The tag-set for the object. The tag-set must be encoded as URL Query parameters.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-website-redirect-location](#API_CreateMultipartUpload_RequestSyntax "#API_CreateMultipartUpload_RequestSyntax")**


If the bucket is configured as a website, redirects requests for this object to another object in
 the same bucket or to an external URL. Amazon S3 stores the value of this header in the object
 metadata.


###### Note

This functionality is not supported for directory buckets.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
x-amz-abort-date: `AbortDate`
x-amz-abort-rule-id: `AbortRuleId`
x-amz-server-side-encryption: `ServerSideEncryption`
x-amz-server-side-encryption-customer-algorithm: `SSECustomerAlgorithm`
x-amz-server-side-encryption-customer-key-MD5: `SSECustomerKeyMD5`
x-amz-server-side-encryption-aws-kms-key-id: `SSEKMSKeyId`
x-amz-server-side-encryption-context: `SSEKMSEncryptionContext`
x-amz-server-side-encryption-bucket-key-enabled: `BucketKeyEnabled`
x-amz-request-charged: `RequestCharged`
x-amz-checksum-algorithm: `ChecksumAlgorithm`
x-amz-checksum-type: `ChecksumType`
<?xml version="1.0" encoding="UTF-8"?>
<[InitiateMultipartUploadResult](#AmazonS3-CreateMultipartUpload-response-CreateMultipartUploadOutput "#AmazonS3-CreateMultipartUpload-response-CreateMultipartUploadOutput")>
   <[Bucket](#AmazonS3-CreateMultipartUpload-response-Bucket "#AmazonS3-CreateMultipartUpload-response-Bucket")>***string***</[Bucket](#AmazonS3-CreateMultipartUpload-response-Bucket "#AmazonS3-CreateMultipartUpload-response-Bucket")>
   <[Key](#AmazonS3-CreateMultipartUpload-response-Key "#AmazonS3-CreateMultipartUpload-response-Key")>***string***</[Key](#AmazonS3-CreateMultipartUpload-response-Key "#AmazonS3-CreateMultipartUpload-response-Key")>
   <[UploadId](#AmazonS3-CreateMultipartUpload-response-UploadId "#AmazonS3-CreateMultipartUpload-response-UploadId")>***string***</[UploadId](#AmazonS3-CreateMultipartUpload-response-UploadId "#AmazonS3-CreateMultipartUpload-response-UploadId")>
</[InitiateMultipartUploadResult](#AmazonS3-CreateMultipartUpload-response-CreateMultipartUploadOutput "#AmazonS3-CreateMultipartUpload-response-CreateMultipartUploadOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-abort-date](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


If the bucket has a lifecycle rule configured with an action to abort incomplete multipart uploads
 and the prefix in the lifecycle rule matches the object name in the request, the response includes this
 header. The header indicates when the initiated multipart upload becomes eligible for an abort
 operation. For more information, see  [Aborting
 Incomplete Multipart Uploads Using a Bucket Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config "https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config") in the
 *Amazon S3 User Guide*.


The response also includes the `x-amz-abort-rule-id` header that provides the ID of the
 lifecycle configuration rule that defines the abort action.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-abort-rule-id](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


This header is returned along with the `x-amz-abort-date` header. It identifies the
 applicable lifecycle configuration rule that defines the action to abort incomplete multipart
 uploads.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-checksum-algorithm](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


The algorithm that was used to create a checksum of the object.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





**[x-amz-checksum-type](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


 Indicates the checksum type that you want Amazon S3 to use to calculate the object’s checksum
 value. For more information, see [Checking object integrity in the Amazon S3
 User Guide](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md").


Valid Values: `COMPOSITE | FULL_OBJECT`





**[x-amz-request-charged](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-server-side-encryption](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


The server-side encryption algorithm used when you store this object in Amazon S3 or Amazon FSx.


###### Note

When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side
 encryption option is `aws:fsx`.


Valid Values: `AES256 | aws:fsx | aws:kms | aws:kms:dsse`





**[x-amz-server-side-encryption-aws-kms-key-id](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


If present, indicates the ID of the KMS key that was used for object encryption.




**[x-amz-server-side-encryption-bucket-key-enabled](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


Indicates whether the multipart upload uses an S3 Bucket Key for server-side encryption with
 AWS Key Management Service (AWS KMS) keys (SSE-KMS).




**[x-amz-server-side-encryption-context](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


If present, indicates the AWS KMS Encryption Context to use for object encryption. The value of
 this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs.




**[x-amz-server-side-encryption-customer-algorithm](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


If server-side encryption with a customer-provided encryption key was requested, the response will
 include this header to confirm the encryption algorithm that's used.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-server-side-encryption-customer-key-MD5](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


If server-side encryption with a customer-provided encryption key was requested, the response will
 include this header to provide the round-trip message integrity verification of the customer-provided
 encryption key.


###### Note

This functionality is not supported for directory buckets.




The following data is returned in XML format by the service.





**[InitiateMultipartUploadResult](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


Root level tag for the InitiateMultipartUploadResult parameters.


Required: Yes




**[Bucket](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


The name of the bucket to which the multipart upload was initiated. Does not return the access point ARN or
 access point alias if used.


###### Note

Access points are not supported by directory buckets.


Type: String




**[Key](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


Object key for which the multipart upload was initiated.


Type: String


Length Constraints: Minimum length of 1.




**[UploadId](#API_CreateMultipartUpload_ResponseSyntax "#API_CreateMultipartUpload_ResponseSyntax")**


ID for the initiated multipart upload.


Type: String




## Examples


### Sample Request for general purpose buckets


This action initiates a multipart upload for the `amzn-s3-demo-bucket` object.



```

            POST /example-object?uploads HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Mon, 1 Nov 2010 20:34:56 GMT
            Authorization: authorization string
         
```

### Sample Response for general purpose buckets


This example illustrates one usage of CreateMultipartUpload.



```

            HTTP/1.1 200 OK
            x-amz-id-2: Uuag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg==
            x-amz-request-id: 656c76696e6727732072657175657374
            Date:  Mon, 1 Nov 2010 20:34:56 GMT
            Transfer-Encoding: chunked
            Connection: keep-alive
            Server: AmazonS3

            <?xml version="1.0" encoding="UTF-8"?>
            <InitiateMultipartUploadResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
              <Bucket>amzn-s3-demo-bucket</Bucket>
              <Key>example-object</Key>
              <UploadId>VXBsb2FkIElEIGZvciA2aWWpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA</UploadId>
            </InitiateMultipartUploadResult>
         
```

### Example for general purpose buckets: Initiate a multipart upload using server-side encryption with
 customer-provided encryption keys


This example, which initiates a multipart upload request, specifies server-side encryption with
 customer-provided encryption keys by adding relevant headers.



```

            POST /example-object?uploads HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com  
            Authorization:authorization string  
            Date: Wed, 28 May 2014 19:34:57 +0000   
            x-amz-server-side-encryption-customer-key: g0lCfA3Dv40jZz5SQJ1ZukLRFqtI5WorC/8SEEXAMPLE   
            x-amz-server-side-encryption-customer-key-MD5: ZjQrne1X/iTcskbY2example   
            x-amz-server-side-encryption-customer-algorithm: AES256 
         
```

### Sample Response for general purpose buckets


In the response, Amazon S3 returns an `UploadId`. In addition, Amazon S3 returns the encryption
 algorithm and the MD5 digest of the encryption key that you provided in the request.



```

           HTTP/1.1 200 OK   
            x-amz-id-2: 36HRCaIGp57F1FvWvVRrvd3hNn9WoBGfEaCVHTCt8QWf00qxdHazQUgfoXAbhFWD   
            x-amz-request-id: 50FA1D691B62CA43   
            Date: Wed, 28 May 2014 19:34:58 GMT   
            x-amz-server-side-encryption-customer-algorithm: AES256   
            x-amz-server-side-encryption-customer-key-MD5: ZjQrne1X/iTcskbY2m3tFg==   
            Transfer-Encoding: chunked   
 
            <?xml version="1.0" encoding="UTF-8"?>
            <InitiateMultipartUploadResult
            xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
              <Bucket>amzn-s3-demo-bucket</Bucket>
              <Key>example-object</Key>
               <UploadId>EXAMPLEJZ6e0YupT2h66iePQCc9IEbYbDUy4RTpMeoSMLPRp8Z5o1u8feSRonpvnWsKKG35tI2LB9VDPiCgTy.Gq2VxQLYjrue4Nq.NBdqI-</UploadId>
</InitiateMultipartUploadResult>  
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/CreateMultipartUpload "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/CreateMultipartUpload")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/CreateMultipartUpload "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/CreateMultipartUpload")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateMultipartUpload "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateMultipartUpload")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/CreateMultipartUpload "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/CreateMultipartUpload")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateMultipartUpload "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateMultipartUpload")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/CreateMultipartUpload "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/CreateMultipartUpload")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/CreateMultipartUpload "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/CreateMultipartUpload")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/CreateMultipartUpload "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/CreateMultipartUpload")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/CreateMultipartUpload "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/CreateMultipartUpload")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CreateMultipartUpload "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CreateMultipartUpload")
