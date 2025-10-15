# DeleteObject

Removes an object from a bucket. The behavior depends on the bucket's versioning state: 


* If bucket versioning is not enabled, the operation permanently deletes the object.
* If bucket versioning is enabled, the operation inserts a delete marker, which becomes the
 current version of the object. To permanently delete an object in a versioned bucket, you must
 include the object’s `versionId` in the request. For more information about
 versioning-enabled buckets, see [Deleting object versions from a
 versioning-enabled bucket](../userguide/DeletingObjectVersions.md "../userguide/DeletingObjectVersions.md").
* If bucket versioning is suspended, the operation removes the object that has a null
 `versionId`, if there is one, and inserts a delete marker that becomes the current
 version of the object. If there isn't an object with a null `versionId`, and all versions
 of the object have a `versionId`, Amazon S3 does not remove the object and only inserts a
 delete marker. To permanently delete an object that has a `versionId`, you must include
 the object’s `versionId` in the request. For more information about versioning-suspended
 buckets, see [Deleting
 objects from versioning-suspended buckets](../userguide/DeletingObjectsfromVersioningSuspendedBuckets.md "../userguide/DeletingObjectsfromVersioningSuspendedBuckets.md").
###### Note


* **Directory buckets** - S3 Versioning isn't enabled and supported for directory buckets. For this API operation, only the `null` value of the version ID is supported by directory buckets.
 You can only specify `null` to the `versionId` query parameter in the
 request.
* **Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format `https://*amzn-s3-demo-bucket*.s3express-*zone-id*.*region-code*.amazonaws.com/*key-name*`. Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](../userguide/endpoint-directory-buckets-AZ.md "../userguide/endpoint-directory-buckets-AZ.md") in the
 *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](../userguide/s3-lzs-for-directory-buckets.md "../userguide/s3-lzs-for-directory-buckets.md") in the
 *Amazon S3 User Guide*.
To remove a specific version, you must use the `versionId` query parameter. Using this
 query parameter permanently deletes the version. If the object deleted is a delete marker, Amazon S3 sets the
 response header `x-amz-delete-marker` to true. 

If the object you want to delete is in a bucket where the bucket versioning configuration is MFA
 Delete enabled, you must include the `x-amz-mfa` request header in the DELETE
 `versionId` request. Requests that include `x-amz-mfa` must use HTTPS. For more
 information about MFA Delete, see [Using MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMFADelete.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMFADelete.html") in the *Amazon S3 User
 Guide*. To see sample requests that use versioning, see [Sample Request](RESTObjectDELETE.md#ExampleVersionObjectDelete "RESTObjectDELETE.md#ExampleVersionObjectDelete"). 

###### Note


**Directory buckets** - MFA delete is not supported by directory buckets.

You can delete objects by explicitly calling DELETE Object or calling ([PutBucketLifecycle](API_PutBucketLifecycle.md "API_PutBucketLifecycle.md")) to enable Amazon S3 to
 remove them for you. If you want to block users or accounts from removing or deleting objects from your
 bucket, you must deny them the `s3:DeleteObject`, `s3:DeleteObjectVersion`, and
 `s3:PutLifeCycleConfiguration` actions. 

###### Note


**Directory buckets** -
 S3 Lifecycle is not supported by directory buckets.



Permissions


* **General purpose bucket permissions** - The following
 permissions are required in your policies when your `DeleteObjects` request
 includes specific headers.




	+ **`s3:DeleteObject`** - To delete an
	 object from a bucket, you must always have the `s3:DeleteObject`
	 permission.
	+ **`s3:DeleteObjectVersion`** - To delete a specific version of an object from a versioning-enabled
	 bucket, you must have the `s3:DeleteObjectVersion` permission.
* **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the [`CreateSession`](API_CreateSession.md "API_CreateSession.md") API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use. 
AWS CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see [`CreateSession`](API_CreateSession.md "API_CreateSession.md").


HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`.



The following action is related to `DeleteObject`:


* [PutObject](API_PutObject.md "API_PutObject.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

###### Note

The `If-Match` header is supported for both general purpose and directory buckets. `IfMatchLastModifiedTime` and `IfMatchSize` is only supported for directory buckets. 


## Request Syntax



```
DELETE /`Key+`?versionId=`VersionId` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-mfa: `MFA`
x-amz-request-payer: `RequestPayer`
x-amz-bypass-governance-retention: `BypassGovernanceRetention`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
If-Match: `IfMatch`
x-amz-if-match-last-modified-time: `IfMatchLastModifiedTime`
x-amz-if-match-size: `IfMatchSize`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_DeleteObject_RequestSyntax "#API_DeleteObject_RequestSyntax")**


The bucket name of the bucket containing the object. 



**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `*Bucket-name*.s3express-*zone-id*.*region-code*.amazonaws.com`. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `*bucket-base-name*--*zone-id*--x-s3` (for example, `*amzn-s3-demo-bucket*--*usw2-az1*--x-s3`). For information about bucket naming
 restrictions, see [Directory bucket naming
 rules](../userguide/directory-bucket-naming-rules.md "../userguide/directory-bucket-naming-rules.md") in the *Amazon S3 User Guide*.



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.


###### Note

Object Lambda access points are not supported by directory buckets.



**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the 
 form `*AccessPointName*-*AccountId*.*outpostID*.s3-outposts.*Region*.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.


Required: Yes




**[If-Match](#API_DeleteObject_RequestSyntax "#API_DeleteObject_RequestSyntax")**


Deletes the object if the ETag (entity tag) value provided during the delete operation matches the ETag of the object in S3. 
 If the ETag values do not match, the operation returns a `412 Precondition Failed` error.


Expects the ETag value as a string. `If-Match` does accept a string value of an '\*' (asterisk) character to denote a match of any ETag.


For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232 "https://tools.ietf.org/html/rfc7232").




**[Key](#API_DeleteObject_RequestSyntax "#API_DeleteObject_RequestSyntax")**


Key name of the object to delete.


Length Constraints: Minimum length of 1.


Required: Yes




**[versionId](#API_DeleteObject_RequestSyntax "#API_DeleteObject_RequestSyntax")**


Version ID used to reference a specific version of the object.


###### Note

For directory buckets in this API operation, only the `null` value of the version ID is supported.




**[x-amz-bypass-governance-retention](#API_DeleteObject_RequestSyntax "#API_DeleteObject_RequestSyntax")**


Indicates whether S3 Object Lock should bypass Governance-mode restrictions to process this
 operation. To use this header, you must have the `s3:BypassGovernanceRetention`
 permission.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-expected-bucket-owner](#API_DeleteObject_RequestSyntax "#API_DeleteObject_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-if-match-last-modified-time](#API_DeleteObject_RequestSyntax "#API_DeleteObject_RequestSyntax")**


If present, the object is deleted only if its modification times matches the provided
 `Timestamp`. If the `Timestamp` values do not match, the operation returns a
 `412 Precondition Failed` error. If the `Timestamp` matches or if the object
 doesn’t exist, the operation returns a `204 Success (No Content)` response.


###### Note

This functionality is only supported for directory buckets.




**[x-amz-if-match-size](#API_DeleteObject_RequestSyntax "#API_DeleteObject_RequestSyntax")**


If present, the object is deleted only if its size matches the provided size in bytes. If the
 `Size` value does not match, the operation returns a `412 Precondition Failed`
 error. If the `Size` matches or if the object doesn’t exist, the operation returns a
 `204 Success (No Content)` response.


###### Note

This functionality is only supported for directory buckets.


###### Important

You can use the `If-Match`, `x-amz-if-match-last-modified-time` and
 `x-amz-if-match-size` conditional headers in conjunction with each-other or
 individually.




**[x-amz-mfa](#API_DeleteObject_RequestSyntax "#API_DeleteObject_RequestSyntax")**


The concatenation of the authentication device's serial number, a space, and the value that is
 displayed on your authentication device. Required to permanently delete a versioned object if versioning
 is configured with MFA delete enabled.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-request-payer](#API_DeleteObject_RequestSyntax "#API_DeleteObject_RequestSyntax")**


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
HTTP/1.1 204
x-amz-delete-marker: `DeleteMarker`
x-amz-version-id: `VersionId`
x-amz-request-charged: `RequestCharged`

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response.


The response returns the following HTTP headers.





**[x-amz-delete-marker](#API_DeleteObject_ResponseSyntax "#API_DeleteObject_ResponseSyntax")**


Indicates whether the specified object version that was permanently deleted was (true) or was not
 (false) a delete marker before deletion. In a simple DELETE, this header indicates whether (true) or not
 (false) the current version of the object is a delete marker. To learn more about delete markers, see
 [Working with delete
 markers](../userguide/DeleteMarker.md "../userguide/DeleteMarker.md").


###### Note

This functionality is not supported for directory buckets.




**[x-amz-request-charged](#API_DeleteObject_ResponseSyntax "#API_DeleteObject_ResponseSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-version-id](#API_DeleteObject_ResponseSyntax "#API_DeleteObject_ResponseSyntax")**


Returns the version ID of the delete marker created as a result of the DELETE operation.


###### Note

This functionality is not supported for directory buckets.




## Examples


### Sample Request for general purpose buckets


The following request deletes the object `my-second-image.jpg`. 



```

            DELETE /my-second-image.jpg HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Wed, 12 Oct 2009 17:50:00 GMT
            Authorization: authorization string
            Content-Type: text/plain
         
```

### Sample Response for general purpose buckets


This example illustrates one usage of DeleteObject.



```

           HTTP/1.1 204 NoContent
           x-amz-id-2: LriYPLdmOdAiIfgSm/F1YsViT1LW94/xUQxMsF7xiEb1a0wiIOIxl+zbwZ163pt7
           x-amz-request-id: 0A49CE4060975EAC
           Date: Wed, 12 Oct 2009 17:50:00 GMT
           Content-Length: 0
           Connection: close
           Server: AmazonS3
         
```

### Sample Request for general purpose buckets: Deleting a specified version of an object


The following request deletes the specified version of the object
 `my-third-image.jpg`. 



```

           DELETE /my-third-image.jpg?versionId=UIORUnfndfiufdisojhr398493jfdkjFJjkndnqUifhnw89493jJFJ HTTP/1.1 
           Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
           Date: Wed, 12 Oct 2009 17:50:00 GMT
           Authorization: authorization string
           Content-Type: text/plain
           Content-Length: 0
         
```

### Sample Response for general purpose buckets


This example illustrates one usage of DeleteObject.



```

           HTTP/1.1 204 NoContent
           x-amz-id-2: LriYPLdmOdAiIfgSm/F1YsViT1LW94/xUQxMsF7xiEb1a0wiIOIxl+zbwZ163pt7
           x-amz-request-id: 0A49CE4060975EAC
           x-amz-version-id: UIORUnfndfiufdisojhr398493jfdkjFJjkndnqUifhnw89493jJFJ
           Date: Wed, 12 Oct 2009 17:50:00 GMT
           Content-Length: 0
           Connection: close
           Server: AmazonS3
         
```

### Sample Response for general purpose buckets: If the object deleted is a delete marker


This example illustrates one usage of DeleteObject.



```

            HTTP/1.1 204 NoContent
            x-amz-id-2: LriYPLdmOdAiIfgSm/F1YsViT1LW94/xUQxMsF7xiEb1a0wiIOIxl+zbwZ163pt7
            x-amz-request-id: 0A49CE4060975EAC
            x-amz-version-id: 3/L4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo
            x-amz-delete-marker: true
            Date: Wed, 12 Oct 2009 17:50:00 GMT
            Content-Length: 0
            Connection: close
            Server: AmazonS3
         
```

### Sample Request for general purpose buckets: Deleting a specified version of an object in an
 MFA-enabled bucket


The following request deletes the specified version of the object
 `my-third-image.jpg`, which is stored in an MFA-enabled bucket. 



```

            DELETE /my-third-image.jpg?versionId=UIORUnfndfiuf HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Wed, 12 Oct 2009 17:50:00 GMT
            x-amz-mfa:[SerialNumber] [AuthenticationCode]
            Authorization: authorization string
            Content-Type: text/plain
            Content-Length: 0
         
```

### Sample Response for general purpose buckets


This example illustrates one usage of DeleteObject.



```

            HTTP/1.1 204 NoContent
            x-amz-id-2: LriYPLdmOdAiIfgSm/F1YsViT1LW94/xUQxMsF7xiEb1a0wiIOIxl+zbwZ163pt7
            x-amz-request-id: 0A49CE4060975EAC
            x-amz-version-id: UIORUnfndfiuf
            Date: Wed, 12 Oct 2009 17:50:00 GMT
            Content-Length: 0
            Connection: close
            Server: AmazonS3
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteObject "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteObject")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteObject "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteObject")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteObject "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteObject")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteObject "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteObject")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteObject "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteObject")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteObject "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteObject")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteObject "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteObject")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteObject "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteObject")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteObject "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteObject")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteObject "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteObject")
