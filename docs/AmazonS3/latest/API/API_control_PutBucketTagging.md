# PutBucketTagging

###### Note

This action puts tags on an Amazon S3 on Outposts bucket. To put tags on an S3 bucket, see
 [PutBucketTagging](API_PutBucketTagging.md "API_PutBucketTagging.md") in the *Amazon S3 API Reference*. 

Sets the tags for an S3 on Outposts bucket. For more information, see [Using
 Amazon S3 on Outposts](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.

Use tags to organize your AWS bill to reflect your own cost structure. To do this,
 sign up to get your AWS account bill with tag key values included. Then, to see the cost
 of combined resources, organize your billing information according to resources with the
 same tag key values. For example, you can tag several resources with a specific application
 name, and then organize your billing information to see the total cost of that application
 across several services. For more information, see [Cost allocation and
 tagging](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html").

###### Note

Within a bucket, if you add a tag that has the same key as an existing tag, the new
 value overwrites the old value. For more information, see  [Using cost allocation in Amazon S3
 bucket tags](../userguide/CostAllocTagging.md "../userguide/CostAllocTagging.md").

To use this action, you must have permissions to perform the
 `s3-outposts:PutBucketTagging` action. The Outposts bucket owner has this
 permission by default and can grant this permission to others. For more information about
 permissions, see  [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing
 access permissions to your Amazon S3 resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").


`PutBucketTagging` has the following special errors:


* Error code: `InvalidTagError`





	+ Description: The tag provided was not a valid tag. This error can occur if
	 the tag did not pass input validation. For information about tag restrictions,
	 see [User-Defined Tag Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html") and [AWS-Generated Cost Allocation Tag Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tag-restrictions.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tag-restrictions.html").
* Error code: `MalformedXMLError`





	+ Description: The XML provided does not match the schema.
* Error code: `OperationAbortedError` 





	+ Description: A conflicting conditional action is currently in progress
	 against this resource. Try again.
* Error code: `InternalError`





	+ Description: The service was unable to apply the provided tag to the
	 bucket.
All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_PutBucketTagging.md#API_control_PutBucketTagging_Examples "API_control_PutBucketTagging.md#API_control_PutBucketTagging_Examples") section.

The following actions are related to `PutBucketTagging`:


* [GetBucketTagging](API_control_GetBucketTagging.md "API_control_GetBucketTagging.md")
* [DeleteBucketTagging](API_control_DeleteBucketTagging.md "API_control_DeleteBucketTagging.md")

## Request Syntax



```
PUT /v20180820/bucket/`name`/tagging HTTP/1.1
Host: `Bucket`.s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[Tagging](#AmazonS3-control_PutBucketTagging-request-Tagging "#AmazonS3-control_PutBucketTagging-request-Tagging") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[TagSet](#AmazonS3-control_PutBucketTagging-request-TagSet "#AmazonS3-control_PutBucketTagging-request-TagSet")>
      <S3Tag>
         <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>`string`</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
         <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>`string`</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
      </S3Tag>
   </[TagSet](#AmazonS3-control_PutBucketTagging-request-TagSet "#AmazonS3-control_PutBucketTagging-request-TagSet")>
</[Tagging](#AmazonS3-control_PutBucketTagging-request-Tagging "#AmazonS3-control_PutBucketTagging-request-Tagging")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_PutBucketTagging_RequestSyntax "#API_control_PutBucketTagging_RequestSyntax")**


The Amazon Resource Name (ARN) of the bucket.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded. 


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_PutBucketTagging_RequestSyntax "#API_control_PutBucketTagging_RequestSyntax")**


The AWS account ID of the Outposts bucket.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[Tagging](#API_control_PutBucketTagging_RequestSyntax "#API_control_PutBucketTagging_RequestSyntax")**


Root level tag for the Tagging parameters.


Required: Yes




**[TagSet](#API_control_PutBucketTagging_RequestSyntax "#API_control_PutBucketTagging_RequestSyntax")**


A collection for a set of tags.


Type: Array of [S3Tag](API_control_S3Tag.md "API_control_S3Tag.md") data types


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample request: Add tag set to an Amazon S3 on Outposts bucket


The following request adds a tag set to the existing
 `example-outpost-bucket` bucket.



```

PUT v20180820/bucket/example-outpost-bucket/tagging HTTP/1.1
Host: s3-outposts.<Region>.amazonaws.com
Content-Length: 1660
x-amz-date: Thu, 12 Nov 2020 20:04:21 GMT
x-amz-account-id: example-account-id
x-amz-outpost-id: op-01ac5d28a6a232904
Authorization: authorization string

<Tagging>
  <TagSet>
    <Tag>
      <Key>Project</Key>
      <Value>Project One</Value>
    </Tag>
    <Tag>
      <Key>User</Key>
      <Value>jsmith</Value>
    </Tag>
  </TagSet>
</Tagging>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutBucketTagging "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutBucketTagging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutBucketTagging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutBucketTagging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutBucketTagging "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutBucketTagging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutBucketTagging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutBucketTagging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutBucketTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutBucketTagging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutBucketTagging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutBucketTagging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutBucketTagging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutBucketTagging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutBucketTagging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutBucketTagging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutBucketTagging "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutBucketTagging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutBucketTagging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutBucketTagging")
