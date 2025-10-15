# ListMultipartUploads

###### Important

End of support notice: Beginning November 21, 2025, Amazon S3 will stop returning `DisplayName`. Update your applications to use canonical IDs (unique identifier for 
 AWS accounts), AWS account ID (12 digit identifier) or IAM ARNs (full resource naming) as a direct replacement of `DisplayName`.


Between July 15, 2025 and November 21, 2025, you will begin to see an increasing rate of missing `DisplayName` in the Owner object.

This change affects the following AWS Regions: US East (N. Virginia) Region, US West (N. California) Region, US West (Oregon) Region, Asia Pacific (Singapore) Region, Asia Pacific (Sydney) Region, 
 Asia Pacific (Tokyo) Region, Europe (Ireland) Region, and South America (São Paulo) Region.

This operation lists in-progress multipart uploads in a bucket. An in-progress multipart upload is a
 multipart upload that has been initiated by the `CreateMultipartUpload` request, but has not
 yet been completed or aborted.

###### Note


**Directory buckets** - If multipart uploads in a
 directory bucket are in progress, you can't delete the bucket until all the in-progress multipart
 uploads are aborted or completed. To delete these in-progress multipart uploads, use the
 `ListMultipartUploads` operation to list the in-progress multipart uploads in the bucket
 and use the `AbortMultipartUpload` operation to abort all the in-progress multipart
 uploads. 

The `ListMultipartUploads` operation returns a maximum of 1,000 multipart uploads in the
 response. The limit of 1,000 multipart uploads is also the default value. You can further limit the
 number of uploads in a response by specifying the `max-uploads` request parameter. If there
 are more than 1,000 multipart uploads that satisfy your `ListMultipartUploads` request, the
 response returns an `IsTruncated` element with the value of `true`, a
 `NextKeyMarker` element, and a `NextUploadIdMarker` element. To list the
 remaining multipart uploads, you need to make subsequent `ListMultipartUploads` requests. In
 these requests, include two query parameters: `key-marker` and `upload-id-marker`.
 Set the value of `key-marker` to the `NextKeyMarker` value from the previous
 response. Similarly, set the value of `upload-id-marker` to the
 `NextUploadIdMarker` value from the previous response.

###### Note


**Directory buckets** - The `upload-id-marker`
 element and the `NextUploadIdMarker` element aren't supported by directory buckets. To
 list the additional multipart uploads, you only need to set the value of `key-marker` to
 the `NextKeyMarker` value from the previous response. 

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
* **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](API_CreateSession.md "API_CreateSession.md") API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use. 
AWS CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](API_CreateSession.md "API_CreateSession.md").


Sorting of multipart uploads in response


* **General purpose bucket** - In the
 `ListMultipartUploads` response, the multipart uploads are sorted based on two
 criteria:




	+ Key-based sorting - Multipart uploads are initially sorted in ascending order
	 based on their object keys.
	+ Time-based sorting - For uploads that share the same object key, they are
	 further sorted in ascending order based on the upload initiation time. Among uploads with
	 the same key, the one that was initiated first will appear before the ones that were
	 initiated later.
* **Directory bucket** - In the
 `ListMultipartUploads` response, the multipart uploads aren't sorted
 lexicographically based on the object keys.


HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`.



The following operations are related to `ListMultipartUploads`:


* [CreateMultipartUpload](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md")
* [UploadPart](API_UploadPart.md "API_UploadPart.md")
* [CompleteMultipartUpload](API_CompleteMultipartUpload.md "API_CompleteMultipartUpload.md")
* [ListParts](API_ListParts.md "API_ListParts.md")
* [AbortMultipartUpload](API_AbortMultipartUpload.md "API_AbortMultipartUpload.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?uploads&delimiter=`Delimiter`&encoding-type=`EncodingType`&key-marker=`KeyMarker`&max-uploads=`MaxUploads`&prefix=`Prefix`&upload-id-marker=`UploadIdMarker` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
x-amz-request-payer: `RequestPayer`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_ListMultipartUploads_RequestSyntax "#API_ListMultipartUploads_RequestSyntax")**


The name of the bucket to which the multipart upload was initiated. 



**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `*bucket-base-name*--*zone-id*--x-s3` (for example, `*amzn-s3-demo-bucket*--*usw2-az1*--x-s3`). For information about bucket naming
 restrictions, see [Directory bucket naming
 rules](../userguide/directory-bucket-naming-rules.md "../userguide/directory-bucket-naming-rules.md") in the *Amazon S3 User Guide*.



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.


###### Note

Object Lambda access points are not supported by directory buckets.



**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the 
 form `*AccessPointName*-*AccountId*.*outpostID*.s3-outposts.*Region*.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.


Required: Yes




**[delimiter](#API_ListMultipartUploads_RequestSyntax "#API_ListMultipartUploads_RequestSyntax")**


Character you use to group keys.


All keys that contain the same string between the prefix, if specified, and the first occurrence of
 the delimiter after the prefix are grouped under a single result element, `CommonPrefixes`.
 If you don't specify the prefix parameter, then the substring starts at the beginning of the key. The
 keys that are grouped under `CommonPrefixes` result element are not returned elsewhere in the
 response.



`CommonPrefixes` is filtered out from results if it is not lexicographically greater than
 the key-marker.


###### Note


**Directory buckets** - For directory buckets, `/` is the only supported delimiter.




**[encoding-type](#API_ListMultipartUploads_RequestSyntax "#API_ListMultipartUploads_RequestSyntax")**


Encoding type used by Amazon S3 to encode the [object keys](../userguide/object-keys.md "../userguide/object-keys.md") in the response. Responses are
 encoded only in UTF-8. An object key can contain any Unicode character. However, the XML 1.0 parser
 can't parse certain characters, such as characters with an ASCII value from 0 to 10. For characters that
 aren't supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the
 response. For more information about characters to avoid in object key names, see [Object key
 naming guidelines](../userguide/object-keys.md#object-key-guidelines "../userguide/object-keys.md#object-key-guidelines").


###### Note

When using the URL encoding type, non-ASCII characters that are used in an object's key name will
 be percent-encoded according to UTF-8 code values. For example, the object
 `test_file(3).png` will appear as `test_file%283%29.png`.


Valid Values: `url`





**[key-marker](#API_ListMultipartUploads_RequestSyntax "#API_ListMultipartUploads_RequestSyntax")**


Specifies the multipart upload after which listing should begin.


###### Note


* **General purpose buckets** - For general purpose buckets,
 `key-marker` is an object key. Together with `upload-id-marker`, this
 parameter specifies the multipart upload after which listing should begin.


If `upload-id-marker` is not specified, only the keys lexicographically greater
 than the specified `key-marker` will be included in the list.


If `upload-id-marker` is specified, any multipart uploads for a key equal to the
 `key-marker` might also be included, provided those multipart uploads have upload IDs
 lexicographically greater than the specified `upload-id-marker`.
* **Directory buckets** - For directory buckets,
 `key-marker` is obfuscated and isn't a real object key. The
 `upload-id-marker` parameter isn't supported by directory buckets. To list the
 additional multipart uploads, you only need to set the value of `key-marker` to the
 `NextKeyMarker` value from the previous response. 


In the `ListMultipartUploads` response, the multipart uploads aren't sorted
 lexicographically based on the object keys.



**[max-uploads](#API_ListMultipartUploads_RequestSyntax "#API_ListMultipartUploads_RequestSyntax")**


Sets the maximum number of multipart uploads, from 1 to 1,000, to return in the response body. 1,000
 is the maximum number of uploads that can be returned in a response.




**[prefix](#API_ListMultipartUploads_RequestSyntax "#API_ListMultipartUploads_RequestSyntax")**


Lists in-progress uploads only for those keys that begin with the specified prefix. You can use
 prefixes to separate a bucket into different grouping of keys. (You can think of using
 `prefix` to make groups in the same way that you'd use a folder in a file system.)


###### Note


**Directory buckets** - For directory buckets, only prefixes that end in a delimiter (`/`) are supported.




**[upload-id-marker](#API_ListMultipartUploads_RequestSyntax "#API_ListMultipartUploads_RequestSyntax")**


Together with key-marker, specifies the multipart upload after which listing should begin. If
 key-marker is not specified, the upload-id-marker parameter is ignored. Otherwise, any multipart uploads
 for a key equal to the key-marker might be included in the list only if they have an upload ID
 lexicographically greater than the specified `upload-id-marker`.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-expected-bucket-owner](#API_ListMultipartUploads_RequestSyntax "#API_ListMultipartUploads_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-request-payer](#API_ListMultipartUploads_RequestSyntax "#API_ListMultipartUploads_RequestSyntax")**


Confirms that the requester knows that they will be charged for the request. Bucket owners need not
 specify this parameter in their requests. If either the source or destination S3 bucket has Requester
 Pays enabled, the requester will pay for corresponding charges to copy the object. For information about
 downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
x-amz-request-charged: `RequestCharged`
<?xml version="1.0" encoding="UTF-8"?>
<[ListMultipartUploadsResult](#AmazonS3-ListMultipartUploads-response-ListMultipartUploadsOutput "#AmazonS3-ListMultipartUploads-response-ListMultipartUploadsOutput")>
   <[Bucket](#AmazonS3-ListMultipartUploads-response-Bucket "#AmazonS3-ListMultipartUploads-response-Bucket")>***string***</[Bucket](#AmazonS3-ListMultipartUploads-response-Bucket "#AmazonS3-ListMultipartUploads-response-Bucket")>
   <[KeyMarker](#AmazonS3-ListMultipartUploads-response-KeyMarker "#AmazonS3-ListMultipartUploads-response-KeyMarker")>***string***</[KeyMarker](#AmazonS3-ListMultipartUploads-response-KeyMarker "#AmazonS3-ListMultipartUploads-response-KeyMarker")>
   <[UploadIdMarker](#AmazonS3-ListMultipartUploads-response-UploadIdMarker "#AmazonS3-ListMultipartUploads-response-UploadIdMarker")>***string***</[UploadIdMarker](#AmazonS3-ListMultipartUploads-response-UploadIdMarker "#AmazonS3-ListMultipartUploads-response-UploadIdMarker")>
   <[NextKeyMarker](#AmazonS3-ListMultipartUploads-response-NextKeyMarker "#AmazonS3-ListMultipartUploads-response-NextKeyMarker")>***string***</[NextKeyMarker](#AmazonS3-ListMultipartUploads-response-NextKeyMarker "#AmazonS3-ListMultipartUploads-response-NextKeyMarker")>
   <[Prefix](#AmazonS3-ListMultipartUploads-response-Prefix "#AmazonS3-ListMultipartUploads-response-Prefix")>***string***</[Prefix](#AmazonS3-ListMultipartUploads-response-Prefix "#AmazonS3-ListMultipartUploads-response-Prefix")>
   <[Delimiter](#AmazonS3-ListMultipartUploads-response-Delimiter "#AmazonS3-ListMultipartUploads-response-Delimiter")>***string***</[Delimiter](#AmazonS3-ListMultipartUploads-response-Delimiter "#AmazonS3-ListMultipartUploads-response-Delimiter")>
   <[NextUploadIdMarker](#AmazonS3-ListMultipartUploads-response-NextUploadIdMarker "#AmazonS3-ListMultipartUploads-response-NextUploadIdMarker")>***string***</[NextUploadIdMarker](#AmazonS3-ListMultipartUploads-response-NextUploadIdMarker "#AmazonS3-ListMultipartUploads-response-NextUploadIdMarker")>
   <[MaxUploads](#AmazonS3-ListMultipartUploads-response-MaxUploads "#AmazonS3-ListMultipartUploads-response-MaxUploads")>***integer***</[MaxUploads](#AmazonS3-ListMultipartUploads-response-MaxUploads "#AmazonS3-ListMultipartUploads-response-MaxUploads")>
   <[IsTruncated](#AmazonS3-ListMultipartUploads-response-IsTruncated "#AmazonS3-ListMultipartUploads-response-IsTruncated")>***boolean***</[IsTruncated](#AmazonS3-ListMultipartUploads-response-IsTruncated "#AmazonS3-ListMultipartUploads-response-IsTruncated")>
   <[Upload](#AmazonS3-ListMultipartUploads-response-Uploads "#AmazonS3-ListMultipartUploads-response-Uploads")>
      <[ChecksumAlgorithm](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-ChecksumAlgorithm "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-ChecksumAlgorithm")>***string***</[ChecksumAlgorithm](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-ChecksumAlgorithm "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-ChecksumAlgorithm")>
      <[ChecksumType](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-ChecksumType "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-ChecksumType")>***string***</[ChecksumType](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-ChecksumType "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-ChecksumType")>
      <[Initiated](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Initiated "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Initiated")>***timestamp***</[Initiated](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Initiated "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Initiated")>
      <[Initiator](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Initiator "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Initiator")>
         <[DisplayName](API_Initiator.md#AmazonS3-Type-Initiator-DisplayName "API_Initiator.md#AmazonS3-Type-Initiator-DisplayName")>***string***</[DisplayName](API_Initiator.md#AmazonS3-Type-Initiator-DisplayName "API_Initiator.md#AmazonS3-Type-Initiator-DisplayName")>
         <[ID](API_Initiator.md#AmazonS3-Type-Initiator-ID "API_Initiator.md#AmazonS3-Type-Initiator-ID")>***string***</[ID](API_Initiator.md#AmazonS3-Type-Initiator-ID "API_Initiator.md#AmazonS3-Type-Initiator-ID")>
      </[Initiator](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Initiator "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Initiator")>
      <[Key](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Key "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Key")>***string***</[Key](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Key "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Key")>
      <[Owner](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Owner "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Owner")>
         <[DisplayName](API_Owner.md#AmazonS3-Type-Owner-DisplayName "API_Owner.md#AmazonS3-Type-Owner-DisplayName")>***string***</[DisplayName](API_Owner.md#AmazonS3-Type-Owner-DisplayName "API_Owner.md#AmazonS3-Type-Owner-DisplayName")>
         <[ID](API_Owner.md#AmazonS3-Type-Owner-ID "API_Owner.md#AmazonS3-Type-Owner-ID")>***string***</[ID](API_Owner.md#AmazonS3-Type-Owner-ID "API_Owner.md#AmazonS3-Type-Owner-ID")>
      </[Owner](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Owner "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-Owner")>
      <[StorageClass](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-StorageClass "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-StorageClass")>***string***</[StorageClass](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-StorageClass "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-StorageClass")>
      <[UploadId](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-UploadId "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-UploadId")>***string***</[UploadId](API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-UploadId "API_MultipartUpload.md#AmazonS3-Type-MultipartUpload-UploadId")>
   </[Upload](#AmazonS3-ListMultipartUploads-response-Uploads "#AmazonS3-ListMultipartUploads-response-Uploads")>
   ...
   <[CommonPrefixes](#AmazonS3-ListMultipartUploads-response-CommonPrefixes "#AmazonS3-ListMultipartUploads-response-CommonPrefixes")>
      <[Prefix](API_CommonPrefix.md#AmazonS3-Type-CommonPrefix-Prefix "API_CommonPrefix.md#AmazonS3-Type-CommonPrefix-Prefix")>***string***</[Prefix](API_CommonPrefix.md#AmazonS3-Type-CommonPrefix-Prefix "API_CommonPrefix.md#AmazonS3-Type-CommonPrefix-Prefix")>
   </[CommonPrefixes](#AmazonS3-ListMultipartUploads-response-CommonPrefixes "#AmazonS3-ListMultipartUploads-response-CommonPrefixes")>
   ...
   <[EncodingType](#AmazonS3-ListMultipartUploads-response-EncodingType "#AmazonS3-ListMultipartUploads-response-EncodingType")>***string***</[EncodingType](#AmazonS3-ListMultipartUploads-response-EncodingType "#AmazonS3-ListMultipartUploads-response-EncodingType")>
</[ListMultipartUploadsResult](#AmazonS3-ListMultipartUploads-response-ListMultipartUploadsOutput "#AmazonS3-ListMultipartUploads-response-ListMultipartUploadsOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-request-charged](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





The following data is returned in XML format by the service.





**[ListMultipartUploadsResult](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


Root level tag for the ListMultipartUploadsResult parameters.


Required: Yes




**[Bucket](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


The name of the bucket to which the multipart upload was initiated. Does not return the access point ARN or
 access point alias if used.


Type: String




**[CommonPrefixes](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


If you specify a delimiter in the request, then the result returns each distinct key prefix
 containing the delimiter in a `CommonPrefixes` element. The distinct key prefixes are
 returned in the `Prefix` child element.


###### Note


**Directory buckets** - For directory buckets, only prefixes that end in a delimiter (`/`) are supported.


Type: Array of [CommonPrefix](API_CommonPrefix.md "API_CommonPrefix.md") data types




**[Delimiter](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


Contains the delimiter you specified in the request. If you don't specify a delimiter in your
 request, this element is absent from the response.


###### Note


**Directory buckets** - For directory buckets, `/` is the only supported delimiter.


Type: String




**[EncodingType](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


Encoding type used by Amazon S3 to encode object keys in the response.


If you specify the `encoding-type` request parameter, Amazon S3 includes this element in the
 response, and returns encoded key name values in the following response elements:



`Delimiter`, `KeyMarker`, `Prefix`, `NextKeyMarker`,
 `Key`.


Type: String


Valid Values: `url`





**[IsTruncated](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


Indicates whether the returned list of multipart uploads is truncated. A value of true indicates
 that the list was truncated. The list can be truncated if the number of multipart uploads exceeds the
 limit allowed or specified by max uploads.


Type: Boolean




**[KeyMarker](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


The key at or after which the listing began.


Type: String




**[MaxUploads](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


Maximum number of multipart uploads that could have been included in the response.


Type: Integer




**[NextKeyMarker](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


When a list is truncated, this element specifies the value that should be used for the key-marker
 request parameter in a subsequent request.


Type: String




**[NextUploadIdMarker](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


When a list is truncated, this element specifies the value that should be used for the
 `upload-id-marker` request parameter in a subsequent request.


###### Note

This functionality is not supported for directory buckets.


Type: String




**[Prefix](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


When a prefix is provided in the request, this field contains the specified prefix. The result
 contains only keys starting with the specified prefix.


###### Note


**Directory buckets** - For directory buckets, only prefixes that end in a delimiter (`/`) are supported.


Type: String




**[Upload](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


Container for elements related to a particular multipart upload. A response can contain zero or more
 `Upload` elements.


Type: Array of [MultipartUpload](API_MultipartUpload.md "API_MultipartUpload.md") data types




**[UploadIdMarker](#API_ListMultipartUploads_ResponseSyntax "#API_ListMultipartUploads_ResponseSyntax")**


Together with key-marker, specifies the multipart upload after which listing should begin. If
 key-marker is not specified, the upload-id-marker parameter is ignored. Otherwise, any multipart uploads
 for a key equal to the key-marker might be included in the list only if they have an upload ID
 lexicographically greater than the specified `upload-id-marker`.


###### Note

This functionality is not supported for directory buckets.


Type: String




## Examples


### Sample Request for general purpose buckets


The following request lists three multipart uploads. The request specifies the
 `max-uploads` request parameter to set the maximum number of multipart uploads to
 return in the response body.



```

GET /?uploads&max-uploads=3 HTTP/1.1
Host: example-bucket.s3.<Region>.amazonaws.com
Date: Mon, 1 Nov 2010 20:34:56 GMT
Authorization: authorization string
         
```

### Sample Response for general purpose buckets


The following sample response indicates that the multipart upload list was truncated and
 provides the `NextKeyMarker` and the `NextUploadIdMarker` elements. You
 specify these values in your subsequent requests to read the next set of multipart uploads. That is,
 send a subsequent request specifying `key-marker=my-movie2.m2ts` (value of the
 `NextKeyMarker` element) and
 `upload-id-marker=YW55IGlkZWEgd2h5IGVsdmluZydzIHVwbG9hZCBmYWlsZWQ` (value of the
 `NextUploadIdMarker`).


The sample response also shows a case of two multipart uploads in progress with the same key
 (`my-movie.m2ts`). That is, the response shows two uploads with the same key. This
 response shows the uploads sorted by key, and within each key the uploads are sorted in ascending
 order by the time the multipart upload was initiated. 



```

HTTP/1.1 200 OK
x-amz-id-2: Uuag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg==
x-amz-request-id: 656c76696e6727732072657175657374
Date: Mon, 1 Nov 2010 20:34:56 GMT
Content-Length: 1330
Connection: keep-alive
Server: AmazonS3

<?xml version="1.0" encoding="UTF-8"?>
<ListMultipartUploadsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Bucket>bucket</Bucket>
  <KeyMarker></KeyMarker>
  <UploadIdMarker></UploadIdMarker>
  <NextKeyMarker>my-movie.m2ts</NextKeyMarker>
  <NextUploadIdMarker>YW55IGlkZWEgd2h5IGVsdmluZydzIHVwbG9hZCBmYWlsZWQ</NextUploadIdMarker>
  <MaxUploads>3</MaxUploads>
  <IsTruncated>true</IsTruncated>
  <Upload>
    <Key>my-divisor</Key>
    <UploadId>XMgbGlrZSBlbHZpbmcncyBub3QgaGF2aW5nIG11Y2ggbHVjaw</UploadId>
    <Initiator>
      <ID>arn:aws:iam::111122223333:user/user1-11111a31-17b5-4fb7-9df5-b111111f13de</ID>
      <DisplayName>user1-11111a31-17b5-4fb7-9df5-b111111f13de</DisplayName>
    </Initiator>
    <Owner>
      <ID>75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID>
      <DisplayName>OwnerDisplayName</DisplayName>
    </Owner>
    <StorageClass>STANDARD</StorageClass>
    <Initiated>2010-11-10T20:48:33.000Z</Initiated>  
  </Upload>
  <Upload>
    <Key>my-movie.m2ts</Key>
    <UploadId>VXBsb2FkIElEIGZvciBlbHZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA</UploadId>
    <Initiator>
      <ID>b1d16700c70b0b05597d7acd6a3f92be</ID>
      <DisplayName>InitiatorDisplayName</DisplayName>
    </Initiator>
    <Owner>
      <ID>b1d16700c70b0b05597d7acd6a3f92be</ID>
      <DisplayName>OwnerDisplayName</DisplayName>
    </Owner>
    <StorageClass>STANDARD</StorageClass>
    <Initiated>2010-11-10T20:48:33.000Z</Initiated>
  </Upload>
  <Upload>
    <Key>my-movie.m2ts</Key>
    <UploadId>YW55IGlkZWEgd2h5IGVsdmluZydzIHVwbG9hZCBmYWlsZWQ</UploadId>
    <Initiator>
      <ID>arn:aws:iam::444455556666:user/user1-22222a31-17b5-4fb7-9df5-b222222f13de</ID>
      <DisplayName>user1-22222a31-17b5-4fb7-9df5-b222222f13de</DisplayName>
    </Initiator>
    <Owner>
      <ID>b1d16700c70b0b05597d7acd6a3f92be</ID>
      <DisplayName>OwnerDisplayName</DisplayName>
    </Owner>
    <StorageClass>STANDARD</StorageClass>
    <Initiated>2010-11-10T20:49:33.000Z</Initiated>
  </Upload>
</ListMultipartUploadsResult>
         
```

### Sample Request for general purpose buckets: Using the delimiter and the prefix parameters


Assume you have a multipart upload in progress for the following keys in your bucket,
 `example-bucket`.



* photos/2006/January/sample.jpg
* photos/2006/February/sample.jpg
* photos/2006/March/sample.jpg
* videos/2006/March/sample.wmv
* sample.jpg

 The following list multipart upload request specifies the delimiter parameter with value
 "/".



```

GET /?uploads&delimiter=/ HTTP/1.1
Host: example-bucket.s3.<Region>.amazonaws.com
Date: Mon, 1 Nov 2010 20:34:56 GMT
Authorization: authorization string
         
```

### Sample Response for general purpose buckets


The following sample response lists multipart uploads on the specified bucket,
 `example-bucket`.


The response returns multipart upload for the `sample.jpg` key in an
 `<Upload>` element.


However, because all the other keys contain the specified delimiter, a distinct substring, from
 the beginning of the key to the first occurrence of the delimiter, from each of these keys is
 returned in a <CommonPrefixes> element. The key substrings, `photos/` and
 `videos/` in the <CommonPrefixes> element, indicate that there are one or more
 in-progress multipart uploads with these key prefixes.


This is a useful scenario if you use key prefixes for your objects to create a logical folder
 like structure. In this case, you can interpret the result as the folders `photos/` and
 `videos/` have one or more multipart uploads in progress.



```

<ListMultipartUploadsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Bucket>example-bucket</Bucket>
  <KeyMarker/>
  <UploadIdMarker/>
  <NextKeyMarker>sample.jpg</NextKeyMarker>
  <NextUploadIdMarker>Agw4MJT6ZPAVxpY0SAuGN7q4uWJJM22ZYg1N99trdp4tpO88.PT6.MhO0w2E17eutfAvQfQWoajgE_W2gpcxQw--</NextUploadIdMarker>
  <Delimiter>/</Delimiter>
  <Prefix/>
  <MaxUploads>1000</MaxUploads>
  <IsTruncated>false</IsTruncated>
  <Upload>
    <Key>sample.jpg</Key>
    <UploadId>Agw4MJT6ZPAVxpY0SAuGN7q4uWJJM22ZYg1N99trdp4tpO88.PT6.MhO0w2E17eutfAvQfQWoajgE_W2gpcxQw--</UploadId>
    <Initiator>
      <ID>314133b66967d86f031c7249d1d9a80249109428335cd0ef1cdc487b4566cb1b</ID>
      <DisplayName>string</DisplayName>
    </Initiator>
    <Owner>
      <ID>314133b66967d86f031c7249d1d9a80249109428335cd0ef1cdc487b4566cb1b</ID>
      <DisplayName>string</DisplayName>
    </Owner>
    <StorageClass>STANDARD</StorageClass>
    <Initiated>2010-11-26T19:24:17.000Z</Initiated>
  </Upload>
  <CommonPrefixes>
    <Prefix>photos/</Prefix>
  </CommonPrefixes>
  <CommonPrefixes>
    <Prefix>videos/</Prefix>
  </CommonPrefixes>
  </ListMultipartUploadsResult>
         
```

### Sample Request for general purpose buckets


In addition to the delimiter parameter, you can filter results by adding a prefix parameter as
 shown in the following request.



```

GET /?uploads&delimiter=/&prefix=photos/2006/ HTTP/1.1
Host: example-bucket.s3.<Region>.amazonaws.com
Date: Mon, 1 Nov 2010 20:34:56 GMT
Authorization: authorization string
         
```

### Sample Response for general purpose buckets


In this case, the response will include only multipart uploads for keys that start with the
 specified prefix. The value returned in the <CommonPrefixes> element is a substring from the
 beginning of the key to the first occurrence of the specified delimiter after the prefix.



```

<?xml version="1.0" encoding="UTF-8"?>
<ListMultipartUploadsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Bucket>example-bucket</Bucket>
  <KeyMarker/>
  <UploadIdMarker/>
  <NextKeyMarker/>
  <NextUploadIdMarker/>
  <Delimiter>/</Delimiter>
  <Prefix>photos/2006/</Prefix>
  <MaxUploads>1000</MaxUploads>
  <IsTruncated>false</IsTruncated>
  <CommonPrefixes>
    <Prefix>photos/2006/February/</Prefix>
  </CommonPrefixes>
  <CommonPrefixes>
    <Prefix>photos/2006/January/</Prefix>
  </CommonPrefixes>
  <CommonPrefixes>
    <Prefix>photos/2006/March/</Prefix>
  </CommonPrefixes>
</ListMultipartUploadsResult>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListMultipartUploads "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/ListMultipartUploads")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListMultipartUploads "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/ListMultipartUploads")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListMultipartUploads "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ListMultipartUploads")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListMultipartUploads "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/ListMultipartUploads")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListMultipartUploads "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ListMultipartUploads")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListMultipartUploads "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/ListMultipartUploads")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListMultipartUploads "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/ListMultipartUploads")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListMultipartUploads "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/ListMultipartUploads")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListMultipartUploads "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListMultipartUploads")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListMultipartUploads "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ListMultipartUploads")
