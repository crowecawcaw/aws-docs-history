# PutObjectTagging

###### Note

This operation is not supported for directory buckets.

Sets the supplied tag-set to an object that already exists in a bucket. A tag is a key-value pair.
 For more information, see [Object Tagging](../userguide/object-tagging.md "../userguide/object-tagging.md").

You can associate tags with an object by sending a PUT request against the tagging subresource that
 is associated with the object. You can retrieve tags by sending a GET request. For more information, see
 [GetObjectTagging](API_GetObjectTagging.md "API_GetObjectTagging.md").

For tagging-related restrictions related to characters and encodings, see [Tag
 Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html"). Note that Amazon S3 limits the maximum number of tags to 10 tags per object.

To use this operation, you must have permission to perform the `s3:PutObjectTagging`
 action. By default, the bucket owner has this permission and can grant this permission to others.

To put tags of any other version, use the `versionId` query parameter. You also need
 permission for the `s3:PutObjectVersionTagging` action.


`PutObjectTagging` has the following special errors. For more Amazon S3 errors see, [Error Responses](ErrorResponses.md "ErrorResponses.md").


* `InvalidTag` - The tag provided was not a valid tag. This error can occur if
 the tag did not pass input validation. For more information, see [Object Tagging](../userguide/object-tagging.md "../userguide/object-tagging.md").
* `MalformedXML` - The XML provided does not match the schema.
* `OperationAborted` - A conflicting conditional action is currently in progress
 against this resource. Please try again.
* `InternalError` - The service was unable to apply the provided tag to the
 object.
The following operations are related to `PutObjectTagging`:


* [GetObjectTagging](API_GetObjectTagging.md "API_GetObjectTagging.md")
* [DeleteObjectTagging](API_DeleteObjectTagging.md "API_DeleteObjectTagging.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /{Key+}?tagging&versionId=`VersionId` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
x-amz-request-payer: `RequestPayer`
<?xml version="1.0" encoding="UTF-8"?>
<[Tagging](#AmazonS3-PutObjectTagging-request-Tagging "#AmazonS3-PutObjectTagging-request-Tagging") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[TagSet](#AmazonS3-PutObjectTagging-request-TagSet "#AmazonS3-PutObjectTagging-request-TagSet")>
      <Tag>
         <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>`string`</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
         <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>`string`</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
      </Tag>
   </[TagSet](#AmazonS3-PutObjectTagging-request-TagSet "#AmazonS3-PutObjectTagging-request-TagSet")>
</[Tagging](#AmazonS3-PutObjectTagging-request-Tagging "#AmazonS3-PutObjectTagging-request-Tagging")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutObjectTagging_RequestSyntax "#API_PutObjectTagging_RequestSyntax")**


The bucket name containing the object. 



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.



**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the 
 form `*AccessPointName*-*AccountId*.*outpostID*.s3-outposts.*Region*.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.


Required: Yes




**[Content-MD5](#API_PutObjectTagging_RequestSyntax "#API_PutObjectTagging_RequestSyntax")**


The MD5 hash for the request body.


For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[Key](#API_PutObjectTagging_RequestSyntax "#API_PutObjectTagging_RequestSyntax")**


Name of the object key.


Length Constraints: Minimum length of 1.


Required: Yes




**[versionId](#API_PutObjectTagging_RequestSyntax "#API_PutObjectTagging_RequestSyntax")**


The versionId of the object that the tag-set will be added to.




**[x-amz-expected-bucket-owner](#API_PutObjectTagging_RequestSyntax "#API_PutObjectTagging_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-request-payer](#API_PutObjectTagging_RequestSyntax "#API_PutObjectTagging_RequestSyntax")**


Confirms that the requester knows that she or he will be charged for the tagging object
 request. Bucket owners need not specify this parameter in their requests.


Valid Values: `requester`





**[x-amz-sdk-checksum-algorithm](#API_PutObjectTagging_RequestSyntax "#API_PutObjectTagging_RequestSyntax")**


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





**[Tagging](#API_PutObjectTagging_RequestSyntax "#API_PutObjectTagging_RequestSyntax")**


Root level tag for the Tagging parameters.


Required: Yes




**[TagSet](#API_PutObjectTagging_RequestSyntax "#API_PutObjectTagging_RequestSyntax")**


A collection for a set of tags


Type: Array of [Tag](API_Tag.md "API_Tag.md") data types


Required: Yes




## Response Syntax



```
HTTP/1.1 200
x-amz-version-id: `VersionId`

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-version-id](#API_PutObjectTagging_ResponseSyntax "#API_PutObjectTagging_ResponseSyntax")**


The versionId of the object the tag-set was added to.




## Examples


### Sample Request: Add tag set to an object


The following request adds a tag set to the existing object object-key in the
 `examplebucket` bucket.



```

PUT object-key?tagging HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Content-Length: length
Content-MD5: pUNXr/BjKK5G2UKExample==
x-amz-date: 20160923T001956Z
Authorization: authorization string
<Tagging>
   <TagSet>
      <Tag>
         <Key>tag1</Key>
         <Value>val1</Value>
      </Tag>
      <Tag>
         <Key>tag2</Key>
         <Value>val2</Value>
      </Tag>
   </TagSet>
</Tagging>
         
```

### Sample Response


This example illustrates one usage of PutObjectTagging.



```

HTTP/1.1 200 OK
x-amz-id-2: YgIPIfBiKa2bj0KMgUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A01
Date: Fri, 23 Sep 2016 00:20:19 GMT
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutObjectTagging "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutObjectTagging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutObjectTagging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutObjectTagging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutObjectTagging "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutObjectTagging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutObjectTagging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutObjectTagging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutObjectTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutObjectTagging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutObjectTagging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutObjectTagging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutObjectTagging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutObjectTagging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutObjectTagging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutObjectTagging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutObjectTagging "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutObjectTagging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutObjectTagging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutObjectTagging")
