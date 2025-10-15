# DeleteObjectTagging

###### Note

This operation is not supported for directory buckets.

Removes the entire tag set from the specified object. For more information about managing object
 tags, see  [Object
 Tagging](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html").

To use this operation, you must have permission to perform the `s3:DeleteObjectTagging`
 action.

To delete tags of a specific object version, add the `versionId` query parameter in the
 request. You will need permission for the `s3:DeleteObjectVersionTagging` action.

The following operations are related to `DeleteObjectTagging`:


* [PutObjectTagging](API_PutObjectTagging.md "API_PutObjectTagging.md")
* [GetObjectTagging](API_GetObjectTagging.md "API_GetObjectTagging.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /{Key+}?tagging&versionId=`VersionId` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_DeleteObjectTagging_RequestSyntax "#API_DeleteObjectTagging_RequestSyntax")**


The bucket name containing the objects from which to remove the tags. 



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.



**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the 
 form `*AccessPointName*-*AccountId*.*outpostID*.s3-outposts.*Region*.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.


Required: Yes




**[Key](#API_DeleteObjectTagging_RequestSyntax "#API_DeleteObjectTagging_RequestSyntax")**


The key that identifies the object in the bucket from which to remove all tags.


Length Constraints: Minimum length of 1.


Required: Yes




**[versionId](#API_DeleteObjectTagging_RequestSyntax "#API_DeleteObjectTagging_RequestSyntax")**


The versionId of the object that the tag-set will be removed from.




**[x-amz-expected-bucket-owner](#API_DeleteObjectTagging_RequestSyntax "#API_DeleteObjectTagging_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 204
x-amz-version-id: `VersionId`

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response.


The response returns the following HTTP headers.





**[x-amz-version-id](#API_DeleteObjectTagging_ResponseSyntax "#API_DeleteObjectTagging_ResponseSyntax")**


The versionId of the object the tag-set was removed from.




## Examples


### Sample Request


The following DELETE request deletes the tag set from the specified object.



```

             DELETE /exampleobject?tagging HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com  
            Date: Wed, 25 Nov 2016 12:00:00 GMT
            Authorization: signatureValue 
         
```

### Sample Response


The following successful response shows Amazon S3 returning a 204 No Content response. The tag set
 for the object has been removed.



```

           HTTP/1.1 204 No Content
           x-amz-version-id: VersionId
           Date: Wed, 25 Nov 2016 12:00:00 GMT
           Connection: close
           Server: AmazonS3
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteObjectTagging "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/DeleteObjectTagging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteObjectTagging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/DeleteObjectTagging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteObjectTagging "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteObjectTagging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteObjectTagging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/DeleteObjectTagging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteObjectTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteObjectTagging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteObjectTagging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/DeleteObjectTagging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteObjectTagging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/DeleteObjectTagging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteObjectTagging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/DeleteObjectTagging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteObjectTagging "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteObjectTagging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteObjectTagging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteObjectTagging")
