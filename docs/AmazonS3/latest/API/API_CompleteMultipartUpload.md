# CompleteMultipartUpload

Completes a multipart upload by assembling previously uploaded parts.

You first initiate the multipart upload and then upload all parts using the [UploadPart](API_UploadPart.md "API_UploadPart.md") operation or the
 [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md")
 operation. After successfully uploading all relevant parts of an upload, you call this
 `CompleteMultipartUpload` operation to complete the upload. Upon receiving this request,
 Amazon S3 concatenates all the parts in ascending order by part number to create a new object. In the
 CompleteMultipartUpload request, you must provide the parts list and ensure that the parts list is
 complete. The CompleteMultipartUpload API operation concatenates the parts that you provide in the list.
 For each part in the list, you must provide the `PartNumber` value and the `ETag`
 value that are returned after that part was uploaded.

The processing of a CompleteMultipartUpload request could take several minutes to finalize. After
 Amazon S3 begins processing the request, it sends an HTTP response header that specifies a `200
 OK` response. While processing is in progress, Amazon S3 periodically sends white space characters to
 keep the connection from timing out. A request could fail after the initial `200 OK` response
 has been sent. This means that a `200 OK` response can contain either a success or an error.
 The error response might be embedded in the `200 OK` response. If you call this API operation
 directly, make sure to design your application to parse the contents of the response and handle it
 appropriately. If you use AWS SDKs, SDKs handle this condition. The SDKs detect the embedded error and
 apply error handling per your configuration settings (including automatically retrying the request as
 appropriate). If the condition persists, the SDKs throw an exception (or, for the SDKs that don't use
 exceptions, they return an error). 

Note that if `CompleteMultipartUpload` fails, applications should be prepared to retry
 any failed requests (including 500 error responses). For more information, see [Amazon S3 Error Best
 Practices](https://docs.aws.amazon.com/AmazonS3/latest/dev/ErrorBestPractices.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ErrorBestPractices.html").

###### Important

You can't use `Content-Type: application/x-www-form-urlencoded` for the
 CompleteMultipartUpload requests. Also, if you don't provide a `Content-Type` header,
 `CompleteMultipartUpload` can still return a `200 OK` response.

For more information about multipart uploads, see [Uploading Objects Using Multipart Upload](https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html") in
 the *Amazon S3 User Guide*.

###### Note


**Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://*amzn-s3-demo-bucket*.s3express-*zone-id*.*region-code*.amazonaws.com/*key-name*`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](../userguide/endpoint-directory-buckets-AZ.md "../userguide/endpoint-directory-buckets-AZ.md") in the
 *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](../userguide/s3-lzs-for-directory-buckets.md "../userguide/s3-lzs-for-directory-buckets.md") in the
 *Amazon S3 User Guide*.



Permissions


* **General purpose bucket permissions** - For information
 about permissions required to use the multipart upload API, see [Multipart Upload and Permissions](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html") in
 the *Amazon S3 User Guide*.


If you provide an [additional checksum value](API_Checksum.md "API_Checksum.md") in your `MultipartUpload` requests and the
 object is encrypted with AWS Key Management Service, you must have permission to use the
 `kms:Decrypt` action for the `CompleteMultipartUpload` request to
 succeed.
* **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](API_CreateSession.md "API_CreateSession.md") API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use. 
AWS CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](API_CreateSession.md "API_CreateSession.md").


If the object is encrypted with SSE-KMS, you must also have the
 `kms:GenerateDataKey` and `kms:Decrypt` permissions in IAM
 identity-based policies and AWS KMS key policies for the AWS KMS key.


Special errors


* Error Code: `EntityTooSmall`





	+ Description: Your proposed upload is smaller than the minimum allowed object size.
	 Each part must be at least 5 MB in size, except the last part.
	+ HTTP Status Code: 400 Bad Request
* Error Code: `InvalidPart`





	+ Description: One or more of the specified parts could not be found. The part might not
	 have been uploaded, or the specified ETag might not have matched the uploaded part's
	 ETag.
	+ HTTP Status Code: 400 Bad Request
* Error Code: `InvalidPartOrder`





	+ Description: The list of parts was not in ascending order. The parts list must be
	 specified in order by part number.
	+ HTTP Status Code: 400 Bad Request
* Error Code: `NoSuchUpload`





	+ Description: The specified multipart upload does not exist. The upload ID might be
	 invalid, or the multipart upload might have been aborted or completed.
	+ HTTP Status Code: 404 Not Found


HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`.



The following operations are related to `CompleteMultipartUpload`:


* [CreateMultipartUpload](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md")
* [UploadPart](API_UploadPart.md "API_UploadPart.md")
* [AbortMultipartUpload](API_AbortMultipartUpload.md "API_AbortMultipartUpload.md")
* [ListParts](API_ListParts.md "API_ListParts.md")
* [ListMultipartUploads](API_ListMultipartUploads.md "API_ListMultipartUploads.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /`Key+`?uploadId=`UploadId` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-checksum-crc32: `ChecksumCRC32`
x-amz-checksum-crc32c: `ChecksumCRC32C`
x-amz-checksum-crc64nvme: `ChecksumCRC64NVME`
x-amz-checksum-sha1: `ChecksumSHA1`
x-amz-checksum-sha256: `ChecksumSHA256`
x-amz-checksum-type: `ChecksumType`
x-amz-mp-object-size: `MpuObjectSize`
x-amz-request-payer: `RequestPayer`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
If-Match: `IfMatch`
If-None-Match: `IfNoneMatch`
x-amz-server-side-encryption-customer-algorithm: `SSECustomerAlgorithm`
x-amz-server-side-encryption-customer-key: `SSECustomerKey`
x-amz-server-side-encryption-customer-key-MD5: `SSECustomerKeyMD5`
<?xml version="1.0" encoding="UTF-8"?>
<[CompleteMultipartUpload](#AmazonS3-CompleteMultipartUpload-request-MultipartUpload "#AmazonS3-CompleteMultipartUpload-request-MultipartUpload") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[Part](#AmazonS3-CompleteMultipartUpload-request-Parts "#AmazonS3-CompleteMultipartUpload-request-Parts")>
      <[ChecksumCRC32](API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumCRC32 "API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumCRC32")>`string`</[ChecksumCRC32](API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumCRC32 "API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumCRC32")>
      <[ChecksumCRC32C](API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumCRC32C "API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumCRC32C")>`string`</[ChecksumCRC32C](API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumCRC32C "API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumCRC32C")>
      <[ChecksumCRC64NVME](API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumCRC64NVME "API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumCRC64NVME")>`string`</[ChecksumCRC64NVME](API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumCRC64NVME "API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumCRC64NVME")>
      <[ChecksumSHA1](API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumSHA1 "API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumSHA1")>`string`</[ChecksumSHA1](API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumSHA1 "API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumSHA1")>
      <[ChecksumSHA256](API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumSHA256 "API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumSHA256")>`string`</[ChecksumSHA256](API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumSHA256 "API_CompletedPart.md#AmazonS3-Type-CompletedPart-ChecksumSHA256")>
      <[ETag](API_CompletedPart.md#AmazonS3-Type-CompletedPart-ETag "API_CompletedPart.md#AmazonS3-Type-CompletedPart-ETag")>`string`</[ETag](API_CompletedPart.md#AmazonS3-Type-CompletedPart-ETag "API_CompletedPart.md#AmazonS3-Type-CompletedPart-ETag")>
      <[PartNumber](API_CompletedPart.md#AmazonS3-Type-CompletedPart-PartNumber "API_CompletedPart.md#AmazonS3-Type-CompletedPart-PartNumber")>`integer`</[PartNumber](API_CompletedPart.md#AmazonS3-Type-CompletedPart-PartNumber "API_CompletedPart.md#AmazonS3-Type-CompletedPart-PartNumber")>
   </[Part](#AmazonS3-CompleteMultipartUpload-request-Parts "#AmazonS3-CompleteMultipartUpload-request-Parts")>
   ...
</[CompleteMultipartUpload](#AmazonS3-CompleteMultipartUpload-request-MultipartUpload "#AmazonS3-CompleteMultipartUpload-request-MultipartUpload")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


Name of the bucket to which the multipart upload was initiated.



**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `*bucket-base-name*--*zone-id*--x-s3` (for example, `*amzn-s3-demo-bucket*--*usw2-az1*--x-s3`). For information about bucket naming
 restrictions, see [Directory bucket naming
 rules](../userguide/directory-bucket-naming-rules.md "../userguide/directory-bucket-naming-rules.md") in the *Amazon S3 User Guide*.



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.


###### Note

Object Lambda access points are not supported by directory buckets.



**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the 
 form `*AccessPointName*-*AccountId*.*outpostID*.s3-outposts.*Region*.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.


Required: Yes




**[If-Match](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


Uploads the object only if the ETag (entity tag) value provided during the WRITE operation matches
 the ETag of the object in S3. If the ETag values do not match, the operation returns a `412
 Precondition Failed` error.


If a conflicting operation occurs during the upload S3 returns a `409
 ConditionalRequestConflict` response. On a 409 failure you should fetch the object's ETag,
 re-initiate the multipart upload with `CreateMultipartUpload`, and re-upload each
 part.


Expects the ETag value as a string.


For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232 "https://tools.ietf.org/html/rfc7232"), or [Conditional requests](../userguide/conditional-requests.md "../userguide/conditional-requests.md") in the
 *Amazon S3 User Guide*.




**[If-None-Match](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


Uploads the object only if the object key name does not already exist in the bucket specified.
 Otherwise, Amazon S3 returns a `412 Precondition Failed` error.


If a conflicting operation occurs during the upload S3 returns a `409
 ConditionalRequestConflict` response. On a 409 failure you should re-initiate the multipart
 upload with `CreateMultipartUpload` and re-upload each part.


Expects the '\*' (asterisk) character.


For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232 "https://tools.ietf.org/html/rfc7232"), or [Conditional requests](../userguide/conditional-requests.md "../userguide/conditional-requests.md") in the
 *Amazon S3 User Guide*.




**[Key](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


Object key for which the multipart upload was initiated.


Length Constraints: Minimum length of 1.


Required: Yes




**[uploadId](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


ID for the initiated multipart upload.


Required: Yes




**[x-amz-checksum-crc32](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


This header can be used as a data integrity check to verify that the data received is the same data that was originally sent.
 This header specifies the Base64 encoded, 32-bit `CRC32` checksum of the object. For more information, see
 [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the
 *Amazon S3 User Guide*.




**[x-amz-checksum-crc32c](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


This header can be used as a data integrity check to verify that the data received is the same data that was originally sent.
 This header specifies the Base64 encoded, 32-bit `CRC32C` checksum of the object. For more information, see
 [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the
 *Amazon S3 User Guide*.




**[x-amz-checksum-crc64nvme](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


This header can be used as a data integrity check to verify that the data received is the same data
 that was originally sent. This header specifies the Base64 encoded, 64-bit `CRC64NVME`
 checksum of the object. The `CRC64NVME` checksum is always a full object checksum. For more
 information, see [Checking object integrity in the Amazon S3
 User Guide](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md").




**[x-amz-checksum-sha1](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


This header can be used as a data integrity check to verify that the data received is the same data that was originally sent.
 This header specifies the Base64 encoded, 160-bit `SHA1` digest of the object. For more information, see
 [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the
 *Amazon S3 User Guide*.




**[x-amz-checksum-sha256](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


This header can be used as a data integrity check to verify that the data received is the same data that was originally sent.
 This header specifies the Base64 encoded, 256-bit `SHA256` digest of the object. For more information, see
 [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the
 *Amazon S3 User Guide*.




**[x-amz-checksum-type](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


This header specifies the checksum type of the object, which determines how part-level checksums are
 combined to create an object-level checksum for multipart objects. You can use this header as a data
 integrity check to verify that the checksum type that is received is the same checksum that was
 specified. If the checksum type doesn’t match the checksum type that was specified for the object during
 the `CreateMultipartUpload` request, it’ll result in a `BadDigest` error. For more
 information, see Checking object integrity in the Amazon S3 User Guide. 


Valid Values: `COMPOSITE | FULL_OBJECT`





**[x-amz-expected-bucket-owner](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-mp-object-size](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


 The expected total object size of the multipart upload request. If there’s a mismatch between the
 specified object size value and the actual object size value, it results in an `HTTP 400
 InvalidRequest` error. 




**[x-amz-request-payer](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


Confirms that the requester knows that they will be charged for the request. Bucket owners need not
 specify this parameter in their requests. If either the source or destination S3 bucket has Requester
 Pays enabled, the requester will pay for corresponding charges to copy the object. For information about
 downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-server-side-encryption-customer-algorithm](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


The server-side encryption (SSE) algorithm used to encrypt the object. This parameter is required
 only when the object was created using a checksum algorithm or if your bucket policy requires the use of
 SSE-C. For more information, see [Protecting data using SSE-C keys](../userguide/ServerSideEncryptionCustomerKeys.md#ssec-require-condition-key "../userguide/ServerSideEncryptionCustomerKeys.md#ssec-require-condition-key") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-server-side-encryption-customer-key](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


The server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm. 
 For more information, see
 [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html") in the
 *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-server-side-encryption-customer-key-MD5](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


The MD5 server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum 
 algorithm. For more information,
 see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html") in the
 *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.




## Request Body


The request accepts the following data in XML format.





**[CompleteMultipartUpload](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


Root level tag for the CompleteMultipartUpload parameters.


Required: Yes




**[Part](#API_CompleteMultipartUpload_RequestSyntax "#API_CompleteMultipartUpload_RequestSyntax")**


Array of CompletedPart data types.


If you do not supply a valid `Part` with your request, the service sends back an HTTP 400
 response.


Type: Array of [CompletedPart](API_CompletedPart.md "API_CompletedPart.md") data types


Required: No




## Response Syntax



```
HTTP/1.1 200
x-amz-expiration: `Expiration`
x-amz-server-side-encryption: `ServerSideEncryption`
x-amz-version-id: `VersionId`
x-amz-server-side-encryption-aws-kms-key-id: `SSEKMSKeyId`
x-amz-server-side-encryption-bucket-key-enabled: `BucketKeyEnabled`
x-amz-request-charged: `RequestCharged`
<?xml version="1.0" encoding="UTF-8"?>
<[CompleteMultipartUploadResult](#AmazonS3-CompleteMultipartUpload-response-CompleteMultipartUploadOutput "#AmazonS3-CompleteMultipartUpload-response-CompleteMultipartUploadOutput")>
   <[Location](#AmazonS3-CompleteMultipartUpload-response-Location "#AmazonS3-CompleteMultipartUpload-response-Location")>***string***</[Location](#AmazonS3-CompleteMultipartUpload-response-Location "#AmazonS3-CompleteMultipartUpload-response-Location")>
   <[Bucket](#AmazonS3-CompleteMultipartUpload-response-Bucket "#AmazonS3-CompleteMultipartUpload-response-Bucket")>***string***</[Bucket](#AmazonS3-CompleteMultipartUpload-response-Bucket "#AmazonS3-CompleteMultipartUpload-response-Bucket")>
   <[Key](#AmazonS3-CompleteMultipartUpload-response-Key "#AmazonS3-CompleteMultipartUpload-response-Key")>***string***</[Key](#AmazonS3-CompleteMultipartUpload-response-Key "#AmazonS3-CompleteMultipartUpload-response-Key")>
   <[ETag](#AmazonS3-CompleteMultipartUpload-response-ETag "#AmazonS3-CompleteMultipartUpload-response-ETag")>***string***</[ETag](#AmazonS3-CompleteMultipartUpload-response-ETag "#AmazonS3-CompleteMultipartUpload-response-ETag")>
   <[ChecksumCRC32](#AmazonS3-CompleteMultipartUpload-response-ChecksumCRC32 "#AmazonS3-CompleteMultipartUpload-response-ChecksumCRC32")>***string***</[ChecksumCRC32](#AmazonS3-CompleteMultipartUpload-response-ChecksumCRC32 "#AmazonS3-CompleteMultipartUpload-response-ChecksumCRC32")>
   <[ChecksumCRC32C](#AmazonS3-CompleteMultipartUpload-response-ChecksumCRC32C "#AmazonS3-CompleteMultipartUpload-response-ChecksumCRC32C")>***string***</[ChecksumCRC32C](#AmazonS3-CompleteMultipartUpload-response-ChecksumCRC32C "#AmazonS3-CompleteMultipartUpload-response-ChecksumCRC32C")>
   <[ChecksumCRC64NVME](#AmazonS3-CompleteMultipartUpload-response-ChecksumCRC64NVME "#AmazonS3-CompleteMultipartUpload-response-ChecksumCRC64NVME")>***string***</[ChecksumCRC64NVME](#AmazonS3-CompleteMultipartUpload-response-ChecksumCRC64NVME "#AmazonS3-CompleteMultipartUpload-response-ChecksumCRC64NVME")>
   <[ChecksumSHA1](#AmazonS3-CompleteMultipartUpload-response-ChecksumSHA1 "#AmazonS3-CompleteMultipartUpload-response-ChecksumSHA1")>***string***</[ChecksumSHA1](#AmazonS3-CompleteMultipartUpload-response-ChecksumSHA1 "#AmazonS3-CompleteMultipartUpload-response-ChecksumSHA1")>
   <[ChecksumSHA256](#AmazonS3-CompleteMultipartUpload-response-ChecksumSHA256 "#AmazonS3-CompleteMultipartUpload-response-ChecksumSHA256")>***string***</[ChecksumSHA256](#AmazonS3-CompleteMultipartUpload-response-ChecksumSHA256 "#AmazonS3-CompleteMultipartUpload-response-ChecksumSHA256")>
   <[ChecksumType](#AmazonS3-CompleteMultipartUpload-response-ChecksumType "#AmazonS3-CompleteMultipartUpload-response-ChecksumType")>***string***</[ChecksumType](#AmazonS3-CompleteMultipartUpload-response-ChecksumType "#AmazonS3-CompleteMultipartUpload-response-ChecksumType")>
</[CompleteMultipartUploadResult](#AmazonS3-CompleteMultipartUpload-response-CompleteMultipartUploadOutput "#AmazonS3-CompleteMultipartUpload-response-CompleteMultipartUploadOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-expiration](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


If the object expiration is configured, this will contain the expiration date
 (`expiry-date`) and rule ID (`rule-id`). The value of `rule-id` is
 URL-encoded.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-request-charged](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-server-side-encryption](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


The server-side encryption algorithm used when storing this object in Amazon S3.


###### Note

When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side
 encryption option is `aws:fsx`.



Valid Values: `AES256 | aws:fsx | aws:kms | aws:kms:dsse`





**[x-amz-server-side-encryption-aws-kms-key-id](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


If present, indicates the ID of the KMS key that was used for object encryption.




**[x-amz-server-side-encryption-bucket-key-enabled](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


Indicates whether the multipart upload uses an S3 Bucket Key for server-side encryption with
 AWS Key Management Service (AWS KMS) keys (SSE-KMS).




**[x-amz-version-id](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


Version ID of the newly created object, in case the bucket has versioning turned on.


###### Note

This functionality is not supported for directory buckets.




The following data is returned in XML format by the service.





**[CompleteMultipartUploadResult](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


Root level tag for the CompleteMultipartUploadResult parameters.


Required: Yes




**[Bucket](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


The name of the bucket that contains the newly created object. Does not return the access point ARN or access point
 alias if used.


###### Note

Access points are not supported by directory buckets.


Type: String




**[ChecksumCRC32](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


The Base64 encoded, 32-bit `CRC32 checksum` of the object. This checksum is only present if the checksum was uploaded
 with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
 with multipart uploads, see [Checking object integrity](../userguide/checking-object-integrity.md#large-object-checksums "../userguide/checking-object-integrity.md#large-object-checksums") in the *Amazon S3 User Guide*.


Type: String




**[ChecksumCRC32C](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


The Base64 encoded, 32-bit `CRC32C` checksum of the object. This checksum is only present if the checksum was uploaded
 with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
 with multipart uploads, see [Checking object integrity](../userguide/checking-object-integrity.md#large-object-checksums "../userguide/checking-object-integrity.md#large-object-checksums") in the *Amazon S3 User Guide*.


Type: String




**[ChecksumCRC64NVME](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


This header can be used as a data integrity check to verify that the data received is the same data
 that was originally sent. This header specifies the Base64 encoded, 64-bit `CRC64NVME`
 checksum of the object. The `CRC64NVME` checksum is always a full object checksum. For more
 information, see [Checking object integrity in the Amazon S3
 User Guide](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md"). 


Type: String




**[ChecksumSHA1](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


The Base64 encoded, 160-bit `SHA1` digest of the object. This checksum is only present if the checksum was uploaded
 with the object. When you use the API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
 with multipart uploads, see [Checking object integrity](../userguide/checking-object-integrity.md#large-object-checksums "../userguide/checking-object-integrity.md#large-object-checksums") in the *Amazon S3 User Guide*.


Type: String




**[ChecksumSHA256](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


The Base64 encoded, 256-bit `SHA256` digest of the object. This checksum is only present if the checksum was uploaded
 with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, it's a calculation based on the checksum values of each individual part. For more information about how checksums are calculated
 with multipart uploads, see [Checking object integrity](../userguide/checking-object-integrity.md#large-object-checksums "../userguide/checking-object-integrity.md#large-object-checksums") in the *Amazon S3 User Guide*.


Type: String




**[ChecksumType](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


The checksum type, which determines how part-level checksums are combined to create an object-level
 checksum for multipart objects. You can use this header as a data integrity check to verify that the
 checksum type that is received is the same checksum type that was specified during the
 `CreateMultipartUpload` request. For more information, see [Checking object integrity in the Amazon S3
 User Guide](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md").


Type: String


Valid Values: `COMPOSITE | FULL_OBJECT`





**[ETag](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


Entity tag that identifies the newly created object's data. Objects with different object data will
 have different entity tags. The entity tag is an opaque string. The entity tag may or may not be an MD5
 digest of the object data. If the entity tag is not an MD5 digest of the object data, it will contain
 one or more nonhexadecimal characters and/or will consist of less than 32 or more than 32 hexadecimal
 digits. For more information about how the entity tag is calculated, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


Type: String




**[Key](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


The object key of the newly created object.


Type: String


Length Constraints: Minimum length of 1.




**[Location](#API_CompleteMultipartUpload_ResponseSyntax "#API_CompleteMultipartUpload_ResponseSyntax")**


The URI that identifies the newly created object.


Type: String




## Examples


### Sample Request for general purpose buckets


The following Complete Multipart Upload request specifies three parts in the
 `CompleteMultipartUpload` element.



```

            POST /example-object?uploadId=AAAsb2FkIElEIGZvciBlbHZpbmcncyWeeS1tb3ZpZS5tMnRzIRRwbG9hZA HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date:  Mon, 1 Nov 2010 20:34:56 GMT
            Content-Length: 391
            Authorization: authorization string

            <CompleteMultipartUpload>
             <Part>
                <PartNumber>1</PartNumber>
               <ETag>"a54357aff0632cce46d942af68356b38"</ETag>
             </Part>
             <Part>
                <PartNumber>2</PartNumber>
               <ETag>"0c78aef83f66abc1fa1e8477f296d394"</ETag>
             </Part>
             <Part>
               <PartNumber>3</PartNumber>
               <ETag>"acbd18db4cc2f85cedef654fccc4a4d8"</ETag>
             </Part>
            </CompleteMultipartUpload>
         
```

### Sample Response for general purpose buckets


The following response indicates that an object was successfully assembled.



```

            HTTP/1.1 200 OK
            x-amz-id-2: Uuag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg==
            x-amz-request-id: 656c76696e6727732072657175657374
            Date: Mon, 1 Nov 2010 20:34:56 GMT
            Connection: close
            Server: AmazonS3

            <?xml version="1.0" encoding="UTF-8"?>
            <CompleteMultipartUploadResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
             <Location>http://amzn-s3-demo-bucket.s3.<Region>.amazonaws.com/Example-Object</Location>
             <Bucket>amzn-s3-demo-bucket</Bucket>
             <Key>Example-Object</Key>
             <ETag>"3858f62230ac3c915f300c664312c11f-9"</ETag>
            </CompleteMultipartUploadResult>
         
```

### Sample Response for general purpose buckets: Error specified in header


The following response indicates that an error occurred before the HTTP response header was
 sent.



```

            HTTP/1.1 403 Forbidden
            x-amz-id-2: Uuag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg==
            x-amz-request-id: 656c76696e6727732072657175657374
            Date:  Mon, 1 Nov 2010 20:34:56 GMT
            Content-Length: 237
            Connection: keep-alive
            Server: AmazonS3

            <?xml version="1.0" encoding="UTF-8"?>
            <Error>
              <Code>AccessDenied</Code>
             <Message>Access Denied</Message>
             <RequestId>656c76696e6727732072657175657374</RequestId>
             <HostId>Uuag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg==</HostId>
            </Error>
         
```

### Sample Response for general purpose buckets: Error specified in body


The following response indicates that an error occurred after the HTTP response header was sent.
 Note that while the HTTP status code is 200 OK, the request actually failed as described in the
 `Error` element.



```

         HTTP/1.1 200 OK
         x-amz-id-2: Uuag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg==
         x-amz-request-id: 656c76696e6727732072657175657374
         Date:  Mon, 1 Nov 2010 20:34:56 GMT
         Connection: close
         Server: AmazonS3

         <?xml version="1.0" encoding="UTF-8"?>

         <Error>
          <Code>InternalError</Code>
          <Message>We encountered an internal error. Please try again.</Message>
          <RequestId>656c76696e6727732072657175657374</RequestId>
          <HostId>Uuag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg==</HostId>
         </Error>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/CompleteMultipartUpload "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/CompleteMultipartUpload")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/CompleteMultipartUpload "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/CompleteMultipartUpload")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CompleteMultipartUpload "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CompleteMultipartUpload")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/CompleteMultipartUpload "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/CompleteMultipartUpload")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CompleteMultipartUpload "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CompleteMultipartUpload")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/CompleteMultipartUpload "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/CompleteMultipartUpload")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/CompleteMultipartUpload "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/CompleteMultipartUpload")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/CompleteMultipartUpload "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/CompleteMultipartUpload")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/CompleteMultipartUpload "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/CompleteMultipartUpload")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CompleteMultipartUpload "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CompleteMultipartUpload")
