# GetObjectAttributes

Retrieves all of the metadata from an object without returning the object itself. This operation is
 useful if you're interested only in an object's metadata. 


`GetObjectAttributes` combines the functionality of `HeadObject` and
 `ListParts`. All of the data returned with both of those individual calls can be returned
 with a single call to `GetObjectAttributes`.

###### Note


**Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://*amzn-s3-demo-bucket*.s3express-*zone-id*.*region-code*.amazonaws.com/*key-name*`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](../userguide/endpoint-directory-buckets-AZ.md "../userguide/endpoint-directory-buckets-AZ.md") in the
 *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](../userguide/s3-lzs-for-directory-buckets.md "../userguide/s3-lzs-for-directory-buckets.md") in the
 *Amazon S3 User Guide*.



Permissions


* **General purpose bucket permissions** - To use
 `GetObjectAttributes`, you must have READ access to the object.


The other permissions that you need to use this operation depend on whether the bucket is
 versioned and if a version ID is passed in the `GetObjectAttributes` request. 




	+ If you pass a version ID in your request, you need both the
	 `s3:GetObjectVersion` and `s3:GetObjectVersionAttributes`
	 permissions.
	+ If you do not pass a version ID in your request, you need the
	 `s3:GetObject` and `s3:GetObjectAttributes` permissions.
For more information, see [Specifying Permissions in a
 Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html") in the *Amazon S3 User Guide*.


If the object that you request does not exist, the error Amazon S3 returns depends on whether
 you also have the `s3:ListBucket` permission.




	+ If you have the `s3:ListBucket` permission on the bucket, Amazon S3 returns an
	 HTTP status code `404 Not Found` ("no such key") error.
	+ If you don't have the `s3:ListBucket` permission, Amazon S3 returns an HTTP
	 status code `403 Forbidden` ("access denied") error.
* **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](API_CreateSession.md "API_CreateSession.md") API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use. 
AWS CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](API_CreateSession.md "API_CreateSession.md").


If
 the
 object is encrypted with SSE-KMS, you must also have the `kms:GenerateDataKey` and
 `kms:Decrypt` permissions in IAM identity-based policies and AWS KMS key policies
 for the AWS KMS key.


Encryption

###### Note

Encryption request headers, like `x-amz-server-side-encryption`, should not be
 sent for `HEAD` requests if your object uses server-side encryption with AWS Key Management Service
 (AWS KMS) keys (SSE-KMS), dual-layer server-side encryption with AWS KMS keys (DSSE-KMS), or
 server-side encryption with Amazon S3 managed encryption keys (SSE-S3). The
 `x-amz-server-side-encryption` header is used when you `PUT` an object
 to S3 and want to specify the encryption method. If you include this header in a
 `GET` request for an object that uses these types of keys, you’ll get an HTTP
 `400 Bad Request` error. It's because the encryption method can't be changed when
 you retrieve the object.


If you encrypted an object when you stored the object in Amazon S3 by using server-side encryption
 with customer-provided encryption keys (SSE-C), then when you retrieve the metadata from the
 object, you must use the following headers. These headers provide the server with the encryption
 key required to retrieve the object's metadata. The headers are: 



* `x-amz-server-side-encryption-customer-algorithm`
* `x-amz-server-side-encryption-customer-key`
* `x-amz-server-side-encryption-customer-key-MD5`

For more information about SSE-C, see [Server-Side Encryption (Using
 Customer-Provided Encryption Keys)](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html") in the *Amazon S3 User Guide*.


###### Note


**Directory bucket permissions** -
 For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256`) and server-side encryption with AWS KMS keys (SSE-KMS) (`aws:kms`). We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your 
 `CreateSession` requests or `PUT` object requests. Then, new objects 
 are automatically encrypted with the desired encryption settings. For more
 information, see [Protecting data with server-side encryption](../userguide/s3-express-serv-side-encryption.md "../userguide/s3-express-serv-side-encryption.md") in the *Amazon S3 User Guide*. For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with AWS KMS for new object uploads](../userguide/s3-express-specifying-kms-encryption.md "../userguide/s3-express-specifying-kms-encryption.md").



Versioning


**Directory buckets** - S3 Versioning isn't enabled and supported for directory buckets. For this API operation, only the `null` value of the version ID is supported by directory buckets.
 You can only specify `null` to the `versionId` query parameter in the
 request.



Conditional request headers

Consider the following when using request headers:



* If both of the `If-Match` and `If-Unmodified-Since` headers are
 present in the request as follows, then Amazon S3 returns the HTTP status code `200 OK`
 and the data requested:




	+ `If-Match` condition evaluates to `true`.
	+ `If-Unmodified-Since` condition evaluates to `false`.
For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232 "https://tools.ietf.org/html/rfc7232").
* If both of the `If-None-Match` and `If-Modified-Since` headers are
 present in the request as follows, then Amazon S3 returns the HTTP status code `304 Not
 Modified`:




	+ `If-None-Match` condition evaluates to `false`.
	+ `If-Modified-Since` condition evaluates to `true`.
For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232 "https://tools.ietf.org/html/rfc7232").


HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`.



The following actions are related to `GetObjectAttributes`:


* [GetObject](API_GetObject.md "API_GetObject.md")
* [GetObjectAcl](API_GetObjectAcl.md "API_GetObjectAcl.md")
* [GetObjectLegalHold](API_GetObjectLegalHold.md "API_GetObjectLegalHold.md")
* [GetObjectLockConfiguration](API_GetObjectLockConfiguration.md "API_GetObjectLockConfiguration.md")
* [GetObjectRetention](API_GetObjectRetention.md "API_GetObjectRetention.md")
* [GetObjectTagging](API_GetObjectTagging.md "API_GetObjectTagging.md")
* [HeadObject](API_HeadObject.md "API_HeadObject.md")
* [ListParts](API_ListParts.md "API_ListParts.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /{Key+}?attributes&versionId=`VersionId` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-max-parts: `MaxParts`
x-amz-part-number-marker: `PartNumberMarker`
x-amz-server-side-encryption-customer-algorithm: `SSECustomerAlgorithm`
x-amz-server-side-encryption-customer-key: `SSECustomerKey`
x-amz-server-side-encryption-customer-key-MD5: `SSECustomerKeyMD5`
x-amz-request-payer: `RequestPayer`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
x-amz-object-attributes: `ObjectAttributes`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


The name of the bucket that contains the object.



**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `*bucket-base-name*--*zone-id*--x-s3` (for example, `*amzn-s3-demo-bucket*--*usw2-az1*--x-s3`). For information about bucket naming
 restrictions, see [Directory bucket naming
 rules](../userguide/directory-bucket-naming-rules.md "../userguide/directory-bucket-naming-rules.md") in the *Amazon S3 User Guide*.



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.


###### Note

Object Lambda access points are not supported by directory buckets.



**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the 
 form `*AccessPointName*-*AccountId*.*outpostID*.s3-outposts.*Region*.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.


Required: Yes




**[Key](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


The object key.


Length Constraints: Minimum length of 1.


Required: Yes




**[versionId](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


The version ID used to reference a specific version of the object.


###### Note

S3 Versioning isn't enabled and supported for directory buckets. For this API operation, only the `null` value of the version ID is supported by directory buckets. You can only specify `null` to the
 `versionId` query parameter in the request.




**[x-amz-expected-bucket-owner](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-max-parts](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


Sets the maximum number of parts to return. For more information, see [Uploading and copying objects using multipart upload
 in Amazon S3](../userguide/mpuoverview.md "../userguide/mpuoverview.md")  in the *Amazon Simple Storage Service user guide*.




**[x-amz-object-attributes](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


Specifies the fields at the root level that you want returned in the response. Fields that you do
 not specify are not returned.


Valid Values: `ETag | Checksum | ObjectParts | StorageClass | ObjectSize`



Required: Yes




**[x-amz-part-number-marker](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


Specifies the part after which listing should begin. Only parts with higher part numbers will be
 listed. For more information, see [Uploading and copying objects using multipart upload
 in Amazon S3](../userguide/mpuoverview.md "../userguide/mpuoverview.md")  in the *Amazon Simple Storage Service user guide*.




**[x-amz-request-payer](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


Confirms that the requester knows that they will be charged for the request. Bucket owners need not
 specify this parameter in their requests. If either the source or destination S3 bucket has Requester
 Pays enabled, the requester will pay for corresponding charges to copy the object. For information about
 downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-server-side-encryption-customer-algorithm](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


Specifies the algorithm to use when encrypting the object (for example, AES256).


###### Note

This functionality is not supported for directory buckets.




**[x-amz-server-side-encryption-customer-key](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is
 used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must
 be appropriate for use with the algorithm specified in the
 `x-amz-server-side-encryption-customer-algorithm` header.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-server-side-encryption-customer-key-MD5](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header
 for a message integrity check to ensure that the encryption key was transmitted without error.


###### Note

This functionality is not supported for directory buckets.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
x-amz-delete-marker: `DeleteMarker`
Last-Modified: `LastModified`
x-amz-version-id: `VersionId`
x-amz-request-charged: `RequestCharged`
<?xml version="1.0" encoding="UTF-8"?>
<[GetObjectAttributesResponse](#AmazonS3-GetObjectAttributes-response-GetObjectAttributesOutput "#AmazonS3-GetObjectAttributes-response-GetObjectAttributesOutput")>
   <[ETag](#AmazonS3-GetObjectAttributes-response-ETag "#AmazonS3-GetObjectAttributes-response-ETag")>***string***</[ETag](#AmazonS3-GetObjectAttributes-response-ETag "#AmazonS3-GetObjectAttributes-response-ETag")>
   <[Checksum](#AmazonS3-GetObjectAttributes-response-Checksum "#AmazonS3-GetObjectAttributes-response-Checksum")>
      <[ChecksumCRC32](API_Checksum.md#AmazonS3-Type-Checksum-ChecksumCRC32 "API_Checksum.md#AmazonS3-Type-Checksum-ChecksumCRC32")>***string***</[ChecksumCRC32](API_Checksum.md#AmazonS3-Type-Checksum-ChecksumCRC32 "API_Checksum.md#AmazonS3-Type-Checksum-ChecksumCRC32")>
      <[ChecksumCRC32C](API_Checksum.md#AmazonS3-Type-Checksum-ChecksumCRC32C "API_Checksum.md#AmazonS3-Type-Checksum-ChecksumCRC32C")>***string***</[ChecksumCRC32C](API_Checksum.md#AmazonS3-Type-Checksum-ChecksumCRC32C "API_Checksum.md#AmazonS3-Type-Checksum-ChecksumCRC32C")>
      <[ChecksumCRC64NVME](API_Checksum.md#AmazonS3-Type-Checksum-ChecksumCRC64NVME "API_Checksum.md#AmazonS3-Type-Checksum-ChecksumCRC64NVME")>***string***</[ChecksumCRC64NVME](API_Checksum.md#AmazonS3-Type-Checksum-ChecksumCRC64NVME "API_Checksum.md#AmazonS3-Type-Checksum-ChecksumCRC64NVME")>
      <[ChecksumSHA1](API_Checksum.md#AmazonS3-Type-Checksum-ChecksumSHA1 "API_Checksum.md#AmazonS3-Type-Checksum-ChecksumSHA1")>***string***</[ChecksumSHA1](API_Checksum.md#AmazonS3-Type-Checksum-ChecksumSHA1 "API_Checksum.md#AmazonS3-Type-Checksum-ChecksumSHA1")>
      <[ChecksumSHA256](API_Checksum.md#AmazonS3-Type-Checksum-ChecksumSHA256 "API_Checksum.md#AmazonS3-Type-Checksum-ChecksumSHA256")>***string***</[ChecksumSHA256](API_Checksum.md#AmazonS3-Type-Checksum-ChecksumSHA256 "API_Checksum.md#AmazonS3-Type-Checksum-ChecksumSHA256")>
      <[ChecksumType](API_Checksum.md#AmazonS3-Type-Checksum-ChecksumType "API_Checksum.md#AmazonS3-Type-Checksum-ChecksumType")>***string***</[ChecksumType](API_Checksum.md#AmazonS3-Type-Checksum-ChecksumType "API_Checksum.md#AmazonS3-Type-Checksum-ChecksumType")>
   </[Checksum](#AmazonS3-GetObjectAttributes-response-Checksum "#AmazonS3-GetObjectAttributes-response-Checksum")>
   <[ObjectParts](#AmazonS3-GetObjectAttributes-response-ObjectParts "#AmazonS3-GetObjectAttributes-response-ObjectParts")>
      <[IsTruncated](API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-IsTruncated "API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-IsTruncated")>***boolean***</[IsTruncated](API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-IsTruncated "API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-IsTruncated")>
      <[MaxParts](API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-MaxParts "API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-MaxParts")>***integer***</[MaxParts](API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-MaxParts "API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-MaxParts")>
      <[NextPartNumberMarker](API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-NextPartNumberMarker "API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-NextPartNumberMarker")>***integer***</[NextPartNumberMarker](API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-NextPartNumberMarker "API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-NextPartNumberMarker")>
      <[PartNumberMarker](API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-PartNumberMarker "API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-PartNumberMarker")>***integer***</[PartNumberMarker](API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-PartNumberMarker "API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-PartNumberMarker")>
      <[Part](API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-Parts "API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-Parts")>
         <[ChecksumCRC32](API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumCRC32 "API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumCRC32")>***string***</[ChecksumCRC32](API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumCRC32 "API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumCRC32")>
         <[ChecksumCRC32C](API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumCRC32C "API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumCRC32C")>***string***</[ChecksumCRC32C](API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumCRC32C "API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumCRC32C")>
         <[ChecksumCRC64NVME](API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumCRC64NVME "API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumCRC64NVME")>***string***</[ChecksumCRC64NVME](API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumCRC64NVME "API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumCRC64NVME")>
         <[ChecksumSHA1](API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumSHA1 "API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumSHA1")>***string***</[ChecksumSHA1](API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumSHA1 "API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumSHA1")>
         <[ChecksumSHA256](API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumSHA256 "API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumSHA256")>***string***</[ChecksumSHA256](API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumSHA256 "API_ObjectPart.md#AmazonS3-Type-ObjectPart-ChecksumSHA256")>
         <[PartNumber](API_ObjectPart.md#AmazonS3-Type-ObjectPart-PartNumber "API_ObjectPart.md#AmazonS3-Type-ObjectPart-PartNumber")>***integer***</[PartNumber](API_ObjectPart.md#AmazonS3-Type-ObjectPart-PartNumber "API_ObjectPart.md#AmazonS3-Type-ObjectPart-PartNumber")>
         <[Size](API_ObjectPart.md#AmazonS3-Type-ObjectPart-Size "API_ObjectPart.md#AmazonS3-Type-ObjectPart-Size")>***long***</[Size](API_ObjectPart.md#AmazonS3-Type-ObjectPart-Size "API_ObjectPart.md#AmazonS3-Type-ObjectPart-Size")>
      </[Part](API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-Parts "API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-Parts")>
      ...
      <[PartsCount](API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-TotalPartsCount "API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-TotalPartsCount")>***integer***</[PartsCount](API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-TotalPartsCount "API_GetObjectAttributesParts.md#AmazonS3-Type-GetObjectAttributesParts-TotalPartsCount")>
   </[ObjectParts](#AmazonS3-GetObjectAttributes-response-ObjectParts "#AmazonS3-GetObjectAttributes-response-ObjectParts")>
   <[StorageClass](#AmazonS3-GetObjectAttributes-response-StorageClass "#AmazonS3-GetObjectAttributes-response-StorageClass")>***string***</[StorageClass](#AmazonS3-GetObjectAttributes-response-StorageClass "#AmazonS3-GetObjectAttributes-response-StorageClass")>
   <[ObjectSize](#AmazonS3-GetObjectAttributes-response-ObjectSize "#AmazonS3-GetObjectAttributes-response-ObjectSize")>***long***</[ObjectSize](#AmazonS3-GetObjectAttributes-response-ObjectSize "#AmazonS3-GetObjectAttributes-response-ObjectSize")>
</[GetObjectAttributesResponse](#AmazonS3-GetObjectAttributes-response-GetObjectAttributesOutput "#AmazonS3-GetObjectAttributes-response-GetObjectAttributesOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[Last-Modified](#API_GetObjectAttributes_ResponseSyntax "#API_GetObjectAttributes_ResponseSyntax")**


Date and time when the object was last modified.




**[x-amz-delete-marker](#API_GetObjectAttributes_ResponseSyntax "#API_GetObjectAttributes_ResponseSyntax")**


Specifies whether the object retrieved was (`true`) or was not (`false`) a
 delete marker. If `false`, this response header does not appear in the response. To learn
 more about delete markers, see [Working with delete markers](../userguide/DeleteMarker.md "../userguide/DeleteMarker.md").


###### Note

This functionality is not supported for directory buckets.




**[x-amz-request-charged](#API_GetObjectAttributes_ResponseSyntax "#API_GetObjectAttributes_ResponseSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-version-id](#API_GetObjectAttributes_ResponseSyntax "#API_GetObjectAttributes_ResponseSyntax")**


The version ID of the object.


###### Note

This functionality is not supported for directory buckets.




The following data is returned in XML format by the service.





**[GetObjectAttributesResponse](#API_GetObjectAttributes_ResponseSyntax "#API_GetObjectAttributes_ResponseSyntax")**


Root level tag for the GetObjectAttributesResponse parameters.


Required: Yes




**[Checksum](#API_GetObjectAttributes_ResponseSyntax "#API_GetObjectAttributes_ResponseSyntax")**


The checksum or digest of the object.


Type: [Checksum](API_Checksum.md "API_Checksum.md") data type




**[ETag](#API_GetObjectAttributes_ResponseSyntax "#API_GetObjectAttributes_ResponseSyntax")**


An ETag is an opaque identifier assigned by a web server to a specific version of a resource found
 at a URL.


Type: String




**[ObjectParts](#API_GetObjectAttributes_ResponseSyntax "#API_GetObjectAttributes_ResponseSyntax")**


A collection of parts associated with a multipart upload.


Type: [GetObjectAttributesParts](API_GetObjectAttributesParts.md "API_GetObjectAttributesParts.md") data type




**[ObjectSize](#API_GetObjectAttributes_ResponseSyntax "#API_GetObjectAttributes_ResponseSyntax")**


The size of the object in bytes.


Type: Long




**[StorageClass](#API_GetObjectAttributes_ResponseSyntax "#API_GetObjectAttributes_ResponseSyntax")**


Provides the storage class information of the object. Amazon S3 returns this header for all objects
 except for S3 Standard storage class objects.


For more information, see [Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html").


###### Note


**Directory buckets** -
 Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.


Type: String


Valid Values: `STANDARD | REDUCED_REDUNDANCY | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | OUTPOSTS | GLACIER_IR | SNOW | EXPRESS_ONEZONE | FSX_OPENZFS`





## Errors





**NoSuchKey** 


The specified key does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectAttributes "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectAttributes")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetObjectAttributes "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetObjectAttributes")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectAttributes")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectAttributes")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectAttributes")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectAttributes")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectAttributes")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectAttributes")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectAttributes "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectAttributes")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectAttributes")
