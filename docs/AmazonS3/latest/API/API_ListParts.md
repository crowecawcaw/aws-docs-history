# ListParts

###### Important

End of support notice: Beginning November 21, 2025, Amazon S3 will stop returning `DisplayName`. Update your applications to use canonical IDs (unique identifier for 
 AWS accounts), AWS account ID (12 digit identifier) or IAM ARNs (full resource naming) as a direct replacement of `DisplayName`.


Between July 15, 2025 and November 21, 2025, you will begin to see an increasing rate of missing `DisplayName` in the Owner object.

This change affects the following AWS Regions: US East (N. Virginia) Region, US West (N. California) Region, US West (Oregon) Region, Asia Pacific (Singapore) Region, Asia Pacific (Sydney) Region, 
 Asia Pacific (Tokyo) Region, Europe (Ireland) Region, and South America (São Paulo) Region.

Lists the parts that have been uploaded for a specific multipart upload.

To use this operation, you must provide the `upload ID` in the request. You obtain this
 uploadID by sending the initiate multipart upload request through [CreateMultipartUpload](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md").

The `ListParts` request returns a maximum of 1,000 uploaded parts. The limit of 1,000
 parts is also the default value. You can restrict the number of parts in a response by specifying the
 `max-parts` request parameter. If your multipart upload consists of more than 1,000 parts,
 the response returns an `IsTruncated` field with the value of `true`, and a
 `NextPartNumberMarker` element. To list remaining uploaded parts, in subsequent
 `ListParts` requests, include the `part-number-marker` query string parameter
 and set its value to the `NextPartNumberMarker` field value from the previous
 response.

For more information on multipart uploads, see [Uploading Objects Using Multipart Upload](https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html") in
 the *Amazon S3 User Guide*.

###### Note


**Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://*amzn-s3-demo-bucket*.s3express-*zone-id*.*region-code*.amazonaws.com/*key-name*`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](../userguide/endpoint-directory-buckets-AZ.md "../userguide/endpoint-directory-buckets-AZ.md") in the
 *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](../userguide/s3-lzs-for-directory-buckets.md "../userguide/s3-lzs-for-directory-buckets.md") in the
 *Amazon S3 User Guide*.



Permissions


* **General purpose bucket permissions** - For information
 about permissions required to use the multipart upload API, see [Multipart Upload and Permissions](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html") in
 the *Amazon S3 User Guide*.


If the upload was created using server-side encryption with AWS Key Management Service (AWS KMS) keys
 (SSE-KMS) or dual-layer server-side encryption with AWS KMS keys (DSSE-KMS), you must have
 permission to the `kms:Decrypt` action for the `ListParts` request to
 succeed.
* **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](API_CreateSession.md "API_CreateSession.md") API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use. 
AWS CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](API_CreateSession.md "API_CreateSession.md").


HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`.



The following operations are related to `ListParts`:


* [CreateMultipartUpload](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md")
* [UploadPart](API_UploadPart.md "API_UploadPart.md")
* [CompleteMultipartUpload](API_CompleteMultipartUpload.md "API_CompleteMultipartUpload.md")
* [AbortMultipartUpload](API_AbortMultipartUpload.md "API_AbortMultipartUpload.md")
* [GetObjectAttributes](API_GetObjectAttributes.md "API_GetObjectAttributes.md")
* [ListMultipartUploads](API_ListMultipartUploads.md "API_ListMultipartUploads.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /`Key+`?max-parts=`MaxParts`&part-number-marker=`PartNumberMarker`&uploadId=`UploadId` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-request-payer: `RequestPayer`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
x-amz-server-side-encryption-customer-algorithm: `SSECustomerAlgorithm`
x-amz-server-side-encryption-customer-key: `SSECustomerKey`
x-amz-server-side-encryption-customer-key-MD5: `SSECustomerKeyMD5`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_ListParts_RequestSyntax "#API_ListParts_RequestSyntax")**


The name of the bucket to which the parts are being uploaded. 



**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `*bucket-base-name*--*zone-id*--x-s3` (for example, `*amzn-s3-demo-bucket*--*usw2-az1*--x-s3`). For information about bucket naming
 restrictions, see [Directory bucket naming
 rules](../userguide/directory-bucket-naming-rules.md "../userguide/directory-bucket-naming-rules.md") in the *Amazon S3 User Guide*.



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.


###### Note

Object Lambda access points are not supported by directory buckets.



**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the 
 form `*AccessPointName*-*AccountId*.*outpostID*.s3-outposts.*Region*.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.


Required: Yes




**[Key](#API_ListParts_RequestSyntax "#API_ListParts_RequestSyntax")**


Object key for which the multipart upload was initiated.


Length Constraints: Minimum length of 1.


Required: Yes




**[max-parts](#API_ListParts_RequestSyntax "#API_ListParts_RequestSyntax")**


Sets the maximum number of parts to return.




**[part-number-marker](#API_ListParts_RequestSyntax "#API_ListParts_RequestSyntax")**


Specifies the part after which listing should begin. Only parts with higher part numbers will be
 listed.




**[uploadId](#API_ListParts_RequestSyntax "#API_ListParts_RequestSyntax")**


Upload ID identifying the multipart upload whose parts are being listed.


Required: Yes




**[x-amz-expected-bucket-owner](#API_ListParts_RequestSyntax "#API_ListParts_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-request-payer](#API_ListParts_RequestSyntax "#API_ListParts_RequestSyntax")**


Confirms that the requester knows that they will be charged for the request. Bucket owners need not
 specify this parameter in their requests. If either the source or destination S3 bucket has Requester
 Pays enabled, the requester will pay for corresponding charges to copy the object. For information about
 downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-server-side-encryption-customer-algorithm](#API_ListParts_RequestSyntax "#API_ListParts_RequestSyntax")**


The server-side encryption (SSE) algorithm used to encrypt the object. This parameter is needed only when the object was created 
 using a checksum algorithm. For more information,
 see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html") in the
 *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-server-side-encryption-customer-key](#API_ListParts_RequestSyntax "#API_ListParts_RequestSyntax")**


The server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm. 
 For more information, see
 [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html") in the
 *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-server-side-encryption-customer-key-MD5](#API_ListParts_RequestSyntax "#API_ListParts_RequestSyntax")**


The MD5 server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum 
 algorithm. For more information,
 see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html") in the
 *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
x-amz-abort-date: `AbortDate`
x-amz-abort-rule-id: `AbortRuleId`
x-amz-request-charged: `RequestCharged`
<?xml version="1.0" encoding="UTF-8"?>
<[ListPartsResult](#AmazonS3-ListParts-response-ListPartsOutput "#AmazonS3-ListParts-response-ListPartsOutput")>
   <[Bucket](#AmazonS3-ListParts-response-Bucket "#AmazonS3-ListParts-response-Bucket")>***string***</[Bucket](#AmazonS3-ListParts-response-Bucket "#AmazonS3-ListParts-response-Bucket")>
   <[Key](#AmazonS3-ListParts-response-Key "#AmazonS3-ListParts-response-Key")>***string***</[Key](#AmazonS3-ListParts-response-Key "#AmazonS3-ListParts-response-Key")>
   <[UploadId](#AmazonS3-ListParts-response-UploadId "#AmazonS3-ListParts-response-UploadId")>***string***</[UploadId](#AmazonS3-ListParts-response-UploadId "#AmazonS3-ListParts-response-UploadId")>
   <[PartNumberMarker](#AmazonS3-ListParts-response-PartNumberMarker "#AmazonS3-ListParts-response-PartNumberMarker")>***integer***</[PartNumberMarker](#AmazonS3-ListParts-response-PartNumberMarker "#AmazonS3-ListParts-response-PartNumberMarker")>
   <[NextPartNumberMarker](#AmazonS3-ListParts-response-NextPartNumberMarker "#AmazonS3-ListParts-response-NextPartNumberMarker")>***integer***</[NextPartNumberMarker](#AmazonS3-ListParts-response-NextPartNumberMarker "#AmazonS3-ListParts-response-NextPartNumberMarker")>
   <[MaxParts](#AmazonS3-ListParts-response-MaxParts "#AmazonS3-ListParts-response-MaxParts")>***integer***</[MaxParts](#AmazonS3-ListParts-response-MaxParts "#AmazonS3-ListParts-response-MaxParts")>
   <[IsTruncated](#AmazonS3-ListParts-response-IsTruncated "#AmazonS3-ListParts-response-IsTruncated")>***boolean***</[IsTruncated](#AmazonS3-ListParts-response-IsTruncated "#AmazonS3-ListParts-response-IsTruncated")>
   <[Part](#AmazonS3-ListParts-response-Parts "#AmazonS3-ListParts-response-Parts")>
      <[ChecksumCRC32](API_Part.md#AmazonS3-Type-Part-ChecksumCRC32 "API_Part.md#AmazonS3-Type-Part-ChecksumCRC32")>***string***</[ChecksumCRC32](API_Part.md#AmazonS3-Type-Part-ChecksumCRC32 "API_Part.md#AmazonS3-Type-Part-ChecksumCRC32")>
      <[ChecksumCRC32C](API_Part.md#AmazonS3-Type-Part-ChecksumCRC32C "API_Part.md#AmazonS3-Type-Part-ChecksumCRC32C")>***string***</[ChecksumCRC32C](API_Part.md#AmazonS3-Type-Part-ChecksumCRC32C "API_Part.md#AmazonS3-Type-Part-ChecksumCRC32C")>
      <[ChecksumCRC64NVME](API_Part.md#AmazonS3-Type-Part-ChecksumCRC64NVME "API_Part.md#AmazonS3-Type-Part-ChecksumCRC64NVME")>***string***</[ChecksumCRC64NVME](API_Part.md#AmazonS3-Type-Part-ChecksumCRC64NVME "API_Part.md#AmazonS3-Type-Part-ChecksumCRC64NVME")>
      <[ChecksumSHA1](API_Part.md#AmazonS3-Type-Part-ChecksumSHA1 "API_Part.md#AmazonS3-Type-Part-ChecksumSHA1")>***string***</[ChecksumSHA1](API_Part.md#AmazonS3-Type-Part-ChecksumSHA1 "API_Part.md#AmazonS3-Type-Part-ChecksumSHA1")>
      <[ChecksumSHA256](API_Part.md#AmazonS3-Type-Part-ChecksumSHA256 "API_Part.md#AmazonS3-Type-Part-ChecksumSHA256")>***string***</[ChecksumSHA256](API_Part.md#AmazonS3-Type-Part-ChecksumSHA256 "API_Part.md#AmazonS3-Type-Part-ChecksumSHA256")>
      <[ETag](API_Part.md#AmazonS3-Type-Part-ETag "API_Part.md#AmazonS3-Type-Part-ETag")>***string***</[ETag](API_Part.md#AmazonS3-Type-Part-ETag "API_Part.md#AmazonS3-Type-Part-ETag")>
      <[LastModified](API_Part.md#AmazonS3-Type-Part-LastModified "API_Part.md#AmazonS3-Type-Part-LastModified")>***timestamp***</[LastModified](API_Part.md#AmazonS3-Type-Part-LastModified "API_Part.md#AmazonS3-Type-Part-LastModified")>
      <[PartNumber](API_Part.md#AmazonS3-Type-Part-PartNumber "API_Part.md#AmazonS3-Type-Part-PartNumber")>***integer***</[PartNumber](API_Part.md#AmazonS3-Type-Part-PartNumber "API_Part.md#AmazonS3-Type-Part-PartNumber")>
      <[Size](API_Part.md#AmazonS3-Type-Part-Size "API_Part.md#AmazonS3-Type-Part-Size")>***long***</[Size](API_Part.md#AmazonS3-Type-Part-Size "API_Part.md#AmazonS3-Type-Part-Size")>
   </[Part](#AmazonS3-ListParts-response-Parts "#AmazonS3-ListParts-response-Parts")>
   ...
   <[Initiator](#AmazonS3-ListParts-response-Initiator "#AmazonS3-ListParts-response-Initiator")>
      <[DisplayName](API_Initiator.md#AmazonS3-Type-Initiator-DisplayName "API_Initiator.md#AmazonS3-Type-Initiator-DisplayName")>***string***</[DisplayName](API_Initiator.md#AmazonS3-Type-Initiator-DisplayName "API_Initiator.md#AmazonS3-Type-Initiator-DisplayName")>
      <[ID](API_Initiator.md#AmazonS3-Type-Initiator-ID "API_Initiator.md#AmazonS3-Type-Initiator-ID")>***string***</[ID](API_Initiator.md#AmazonS3-Type-Initiator-ID "API_Initiator.md#AmazonS3-Type-Initiator-ID")>
   </[Initiator](#AmazonS3-ListParts-response-Initiator "#AmazonS3-ListParts-response-Initiator")>
   <[Owner](#AmazonS3-ListParts-response-Owner "#AmazonS3-ListParts-response-Owner")>
      <[DisplayName](API_Owner.md#AmazonS3-Type-Owner-DisplayName "API_Owner.md#AmazonS3-Type-Owner-DisplayName")>***string***</[DisplayName](API_Owner.md#AmazonS3-Type-Owner-DisplayName "API_Owner.md#AmazonS3-Type-Owner-DisplayName")>
      <[ID](API_Owner.md#AmazonS3-Type-Owner-ID "API_Owner.md#AmazonS3-Type-Owner-ID")>***string***</[ID](API_Owner.md#AmazonS3-Type-Owner-ID "API_Owner.md#AmazonS3-Type-Owner-ID")>
   </[Owner](#AmazonS3-ListParts-response-Owner "#AmazonS3-ListParts-response-Owner")>
   <[StorageClass](#AmazonS3-ListParts-response-StorageClass "#AmazonS3-ListParts-response-StorageClass")>***string***</[StorageClass](#AmazonS3-ListParts-response-StorageClass "#AmazonS3-ListParts-response-StorageClass")>
   <[ChecksumAlgorithm](#AmazonS3-ListParts-response-ChecksumAlgorithm "#AmazonS3-ListParts-response-ChecksumAlgorithm")>***string***</[ChecksumAlgorithm](#AmazonS3-ListParts-response-ChecksumAlgorithm "#AmazonS3-ListParts-response-ChecksumAlgorithm")>
   <[ChecksumType](#AmazonS3-ListParts-response-ChecksumType "#AmazonS3-ListParts-response-ChecksumType")>***string***</[ChecksumType](#AmazonS3-ListParts-response-ChecksumType "#AmazonS3-ListParts-response-ChecksumType")>
</[ListPartsResult](#AmazonS3-ListParts-response-ListPartsOutput "#AmazonS3-ListParts-response-ListPartsOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-abort-date](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


If the bucket has a lifecycle rule configured with an action to abort incomplete multipart uploads
 and the prefix in the lifecycle rule matches the object name in the request, then the response includes
 this header indicating when the initiated multipart upload will become eligible for abort operation. For
 more information, see [Aborting
 Incomplete Multipart Uploads Using a Bucket Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config "https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config").


The response will also include the `x-amz-abort-rule-id` header that will provide the ID
 of the lifecycle configuration rule that defines this action.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-abort-rule-id](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


This header is returned along with the `x-amz-abort-date` header. It identifies
 applicable lifecycle configuration rule that defines the action to abort incomplete multipart
 uploads.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-request-charged](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





The following data is returned in XML format by the service.





**[ListPartsResult](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


Root level tag for the ListPartsResult parameters.


Required: Yes




**[Bucket](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


The name of the bucket to which the multipart upload was initiated. Does not return the access point ARN or
 access point alias if used.


Type: String




**[ChecksumAlgorithm](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


The algorithm that was used to create a checksum of the object.


Type: String


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





**[ChecksumType](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


The checksum type, which determines how part-level checksums are combined to create an object-level
 checksum for multipart objects. You can use this header response to verify that the checksum type that
 is received is the same checksum type that was specified in `CreateMultipartUpload` request.
 For more information, see [Checking object integrity in the Amazon S3
 User Guide](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md").


Type: String


Valid Values: `COMPOSITE | FULL_OBJECT`





**[Initiator](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


Container element that identifies who initiated the multipart upload. If the initiator is an
 AWS account, this element provides the same information as the `Owner` element. If the
 initiator is an IAM User, this element provides the user ARN and display name.


Type: [Initiator](API_Initiator.md "API_Initiator.md") data type




**[IsTruncated](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


 Indicates whether the returned list of parts is truncated. A true value indicates that the list was
 truncated. A list can be truncated if the number of parts exceeds the limit returned in the MaxParts
 element.


Type: Boolean




**[Key](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


Object key for which the multipart upload was initiated.


Type: String


Length Constraints: Minimum length of 1.




**[MaxParts](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


Maximum number of parts that were allowed in the response.


Type: Integer




**[NextPartNumberMarker](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


When a list is truncated, this element specifies the last part in the list, as well as the value to
 use for the `part-number-marker` request parameter in a subsequent request.


Type: Integer




**[Owner](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


Container element that identifies the object owner, after the object is created. If multipart upload
 is initiated by an IAM user, this element provides the parent account ID and display name.


###### Note


**Directory buckets** - The bucket owner is returned as the
 object owner for all the parts.


Type: [Owner](API_Owner.md "API_Owner.md") data type




**[Part](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


Container for elements related to a particular part. A response can contain zero or more
 `Part` elements.


Type: Array of [Part](API_Part.md "API_Part.md") data types




**[PartNumberMarker](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


Specifies the part after which listing should begin. Only parts with higher part numbers will be
 listed.


Type: Integer




**[StorageClass](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


The class of storage used to store the uploaded object.


###### Note


**Directory buckets** -
 Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.


Type: String


Valid Values: `STANDARD | REDUCED_REDUNDANCY | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | OUTPOSTS | GLACIER_IR | SNOW | EXPRESS_ONEZONE | FSX_OPENZFS`





**[UploadId](#API_ListParts_ResponseSyntax "#API_ListParts_ResponseSyntax")**


Upload ID identifying the multipart upload whose parts are being listed.


Type: String




## Examples


### Sample Request for general purpose buckets


Assume you have uploaded parts with sequential part numbers starting with 1. The following List
 Parts request specifies `max-parts` and `part-number-marker` query parameters.
 The request lists the first two parts that follow part number 1, that is, you will get parts 2 and 3
 in the response. If more parts exist, the result is a truncated result and therefore the response
 will return an `IsTruncated` element with the value `true`. The response will
 also return the `NextPartNumberMarker` element with the value `3`, which
 should be used for the value of the `part-number-marker` request query string parameter
 in the next ListParts request. 



```

GET /example-object?uploadId=XXBsb2FkIElEIGZvciBlbHZpbmcncyVcdS1tb3ZpZS5tMnRzEEEwbG9hZA&max-parts=2&part-number-marker=1 HTTP/1.1
Host: example-bucket.s3.<Region>.amazonaws.com
Date: Mon, 1 Nov 2010 20:34:56 GMT
Authorization: authorization string
         
```

### Sample Response for general purpose buckets


This example illustrates one usage of ListParts.



```

HTTP/1.1 200 OK
x-amz-id-2: Uuag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg==
x-amz-request-id: 656c76696e6727732072657175657374
Date: Mon, 1 Nov 2010 20:34:56 GMT
Content-Length: 985
Connection: keep-alive
Server: AmazonS3

<?xml version="1.0" encoding="UTF-8"?>
<ListPartsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Bucket>example-bucket</Bucket>
  <Key>example-object</Key>
  <UploadId>XXBsb2FkIElEIGZvciBlbHZpbmcncyVcdS1tb3ZpZS5tMnRzEEEwbG9hZA</UploadId>
  <Initiator>
      <ID>arn:aws:iam::111122223333:user/some-user-11116a31-17b5-4fb7-9df5-b288870f11xx</ID>
      <DisplayName>umat-user-11116a31-17b5-4fb7-9df5-b288870f11xx</DisplayName>
  </Initiator>
  <Owner>
    <ID>75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID>
    <DisplayName>someName</DisplayName>
  </Owner>
  <StorageClass>STANDARD</StorageClass>
  <PartNumberMarker>1</PartNumberMarker>
  <NextPartNumberMarker>3</NextPartNumberMarker>
  <MaxParts>2</MaxParts>
  <IsTruncated>true</IsTruncated>
  <Part>
    <PartNumber>2</PartNumber>
    <LastModified>2010-11-10T20:48:34.000Z</LastModified>
    <ETag>"7778aef83f66abc1fa1e8477f296d394"</ETag>
    <Size>10485760</Size>
  </Part>
  <Part>
    <PartNumber>3</PartNumber>
    <LastModified>2010-11-10T20:48:33.000Z</LastModified>
    <ETag>"aaaa18db4cc2f85cedef654fccc4a4x8"</ETag>
    <Size>10485760</Size>
  </Part>
</ListPartsResult>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListParts "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListParts")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListParts "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListParts")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListParts "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListParts")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListParts "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListParts")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListParts "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListParts")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListParts "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListParts")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListParts "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListParts")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListParts "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListParts")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListParts "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListParts")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListParts "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListParts")
