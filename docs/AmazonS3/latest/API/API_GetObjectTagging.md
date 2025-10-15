# GetObjectTagging

###### Note

This operation is not supported for directory buckets.

Returns the tag-set of an object. You send the GET request against the tagging subresource
 associated with the object.

To use this operation, you must have permission to perform the `s3:GetObjectTagging`
 action. By default, the GET action returns information about current version of an object. For a
 versioned bucket, you can have multiple versions of an object in your bucket. To retrieve tags of any
 other version, use the versionId query parameter. You also need permission for the
 `s3:GetObjectVersionTagging` action.

 By default, the bucket owner has this permission and can grant this permission to others.

 For information about the Amazon S3 object tagging feature, see [Object Tagging](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html").

The following actions are related to `GetObjectTagging`:


* [DeleteObjectTagging](API_DeleteObjectTagging.md "API_DeleteObjectTagging.md")
* [GetObjectAttributes](API_GetObjectAttributes.md "API_GetObjectAttributes.md")
* [PutObjectTagging](API_PutObjectTagging.md "API_PutObjectTagging.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /{Key+}?tagging&versionId=`VersionId` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
x-amz-request-payer: `RequestPayer`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetObjectTagging_RequestSyntax "#API_GetObjectTagging_RequestSyntax")**


The bucket name containing the object for which to get the tagging information. 



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.



**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the 
 form `*AccessPointName*-*AccountId*.*outpostID*.s3-outposts.*Region*.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.


Required: Yes




**[Key](#API_GetObjectTagging_RequestSyntax "#API_GetObjectTagging_RequestSyntax")**


Object key for which to get the tagging information.


Length Constraints: Minimum length of 1.


Required: Yes




**[versionId](#API_GetObjectTagging_RequestSyntax "#API_GetObjectTagging_RequestSyntax")**


The versionId of the object for which to get the tagging information.




**[x-amz-expected-bucket-owner](#API_GetObjectTagging_RequestSyntax "#API_GetObjectTagging_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-request-payer](#API_GetObjectTagging_RequestSyntax "#API_GetObjectTagging_RequestSyntax")**


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
x-amz-version-id: `VersionId`
<?xml version="1.0" encoding="UTF-8"?>
<[Tagging](#AmazonS3-GetObjectTagging-response-GetObjectTaggingOutput "#AmazonS3-GetObjectTagging-response-GetObjectTaggingOutput")>
   <[TagSet](#AmazonS3-GetObjectTagging-response-TagSet "#AmazonS3-GetObjectTagging-response-TagSet")>
      <Tag>
         <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>***string***</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
         <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>***string***</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
      </Tag>
   </[TagSet](#AmazonS3-GetObjectTagging-response-TagSet "#AmazonS3-GetObjectTagging-response-TagSet")>
</[Tagging](#AmazonS3-GetObjectTagging-response-GetObjectTaggingOutput "#AmazonS3-GetObjectTagging-response-GetObjectTaggingOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-version-id](#API_GetObjectTagging_ResponseSyntax "#API_GetObjectTagging_ResponseSyntax")**


The versionId of the object for which you got the tagging information.




The following data is returned in XML format by the service.





**[Tagging](#API_GetObjectTagging_ResponseSyntax "#API_GetObjectTagging_ResponseSyntax")**


Root level tag for the Tagging parameters.


Required: Yes




**[TagSet](#API_GetObjectTagging_ResponseSyntax "#API_GetObjectTagging_ResponseSyntax")**


Contains the tag set.


Type: Array of [Tag](API_Tag.md "API_Tag.md") data types




## Examples


### Sample Request


The following request returns the tag set of the specified object.



```

            GET /example-object?tagging HTTP/1.1
            Host: examplebucket.s3.<Region>.amazonaws.com
            Date: Thu, 22 Sep 2016 21:33:08 GMT
            Authorization: authorization string
         
```

### Sample Response


This example illustrates one usage of GetObjectTagging.



```

            HTTP/1.1 200 OK
            Date: Thu, 22 Sep 2016 21:33:08 GMT
            Connection: close
            Server: AmazonS3
            <?xml version="1.0" encoding="UTF-8"?>
            <Tagging xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
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

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectTagging "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectTagging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetObjectTagging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetObjectTagging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectTagging "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectTagging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectTagging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectTagging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectTagging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectTagging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectTagging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectTagging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectTagging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectTagging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectTagging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectTagging "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectTagging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectTagging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectTagging")
