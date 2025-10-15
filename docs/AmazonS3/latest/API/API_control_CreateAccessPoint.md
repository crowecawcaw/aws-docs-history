# CreateAccessPoint

Creates an access point and associates it to a specified bucket. For more information, see
 [Managing
 access to shared datasets with access points](../userguide/access-points.md "../userguide/access-points.md") or [Managing access to
 shared datasets in directory buckets with access points](../userguide/access-points-directory-buckets.md "../userguide/access-points-directory-buckets.md") in the
 *Amazon S3 User Guide*.

To create an access point and attach it to a volume on an Amazon FSx file system, see [CreateAndAttachS3AccessPoint](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateAndAttachS3AccessPoint.html "https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateAndAttachS3AccessPoint.html") in the *Amazon FSx API
 Reference*.

###### Note

S3 on Outposts only supports VPC-style access points. 

For more information, see  [Accessing Amazon S3 on Outposts using
 virtual private cloud (VPC) only access points](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the
 *Amazon S3 User Guide*.

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_CreateAccessPoint.md#API_control_CreateAccessPoint_Examples "API_control_CreateAccessPoint.md#API_control_CreateAccessPoint_Examples") section.

The following actions are related to `CreateAccessPoint`:


* [GetAccessPoint](API_control_GetAccessPoint.md "API_control_GetAccessPoint.md")
* [DeleteAccessPoint](API_control_DeleteAccessPoint.md "API_control_DeleteAccessPoint.md")
* [ListAccessPoints](API_control_ListAccessPoints.md "API_control_ListAccessPoints.md")
* [ListAccessPointsForDirectoryBuckets](API_control_ListAccessPointsForDirectoryBuckets.md "API_control_ListAccessPointsForDirectoryBuckets.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /v20180820/accesspoint/`name` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[CreateAccessPointRequest](#AmazonS3-control_CreateAccessPoint-request-CreateAccessPointRequest "#AmazonS3-control_CreateAccessPoint-request-CreateAccessPointRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[Bucket](#AmazonS3-control_CreateAccessPoint-request-Bucket "#AmazonS3-control_CreateAccessPoint-request-Bucket")>`string`</[Bucket](#AmazonS3-control_CreateAccessPoint-request-Bucket "#AmazonS3-control_CreateAccessPoint-request-Bucket")>
   <[VpcConfiguration](#AmazonS3-control_CreateAccessPoint-request-VpcConfiguration "#AmazonS3-control_CreateAccessPoint-request-VpcConfiguration")>
      <[VpcId](API_control_VpcConfiguration.md#AmazonS3-Type-control_VpcConfiguration-VpcId "API_control_VpcConfiguration.md#AmazonS3-Type-control_VpcConfiguration-VpcId")>`string`</[VpcId](API_control_VpcConfiguration.md#AmazonS3-Type-control_VpcConfiguration-VpcId "API_control_VpcConfiguration.md#AmazonS3-Type-control_VpcConfiguration-VpcId")>
   </[VpcConfiguration](#AmazonS3-control_CreateAccessPoint-request-VpcConfiguration "#AmazonS3-control_CreateAccessPoint-request-VpcConfiguration")>
   <[PublicAccessBlockConfiguration](#AmazonS3-control_CreateAccessPoint-request-PublicAccessBlockConfiguration "#AmazonS3-control_CreateAccessPoint-request-PublicAccessBlockConfiguration")>
      <[BlockPublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls")>`boolean`</[BlockPublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls")>
      <[BlockPublicPolicy](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy")>`boolean`</[BlockPublicPolicy](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy")>
      <[IgnorePublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls")>`boolean`</[IgnorePublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls")>
      <[RestrictPublicBuckets](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets")>`boolean`</[RestrictPublicBuckets](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets")>
   </[PublicAccessBlockConfiguration](#AmazonS3-control_CreateAccessPoint-request-PublicAccessBlockConfiguration "#AmazonS3-control_CreateAccessPoint-request-PublicAccessBlockConfiguration")>
   <[BucketAccountId](#AmazonS3-control_CreateAccessPoint-request-BucketAccountId "#AmazonS3-control_CreateAccessPoint-request-BucketAccountId")>`string`</[BucketAccountId](#AmazonS3-control_CreateAccessPoint-request-BucketAccountId "#AmazonS3-control_CreateAccessPoint-request-BucketAccountId")>
   <[Scope](#AmazonS3-control_CreateAccessPoint-request-Scope "#AmazonS3-control_CreateAccessPoint-request-Scope")>
      <[Permissions](API_control_Scope.md#AmazonS3-Type-control_Scope-Permissions "API_control_Scope.md#AmazonS3-Type-control_Scope-Permissions")>
         <Permission>`string`</Permission>
      </[Permissions](API_control_Scope.md#AmazonS3-Type-control_Scope-Permissions "API_control_Scope.md#AmazonS3-Type-control_Scope-Permissions")>
      <[Prefixes](API_control_Scope.md#AmazonS3-Type-control_Scope-Prefixes "API_control_Scope.md#AmazonS3-Type-control_Scope-Prefixes")>
         <Prefix>`string`</Prefix>
      </[Prefixes](API_control_Scope.md#AmazonS3-Type-control_Scope-Prefixes "API_control_Scope.md#AmazonS3-Type-control_Scope-Prefixes")>
   </[Scope](#AmazonS3-control_CreateAccessPoint-request-Scope "#AmazonS3-control_CreateAccessPoint-request-Scope")>
   <[Tags](#AmazonS3-control_CreateAccessPoint-request-Tags "#AmazonS3-control_CreateAccessPoint-request-Tags")>
      <Tag>
         <[Key](API_control_Tag.md#AmazonS3-Type-control_Tag-Key "API_control_Tag.md#AmazonS3-Type-control_Tag-Key")>`string`</[Key](API_control_Tag.md#AmazonS3-Type-control_Tag-Key "API_control_Tag.md#AmazonS3-Type-control_Tag-Key")>
         <[Value](API_control_Tag.md#AmazonS3-Type-control_Tag-Value "API_control_Tag.md#AmazonS3-Type-control_Tag-Value")>`string`</[Value](API_control_Tag.md#AmazonS3-Type-control_Tag-Value "API_control_Tag.md#AmazonS3-Type-control_Tag-Value")>
      </Tag>
   </[Tags](#AmazonS3-control_CreateAccessPoint-request-Tags "#AmazonS3-control_CreateAccessPoint-request-Tags")>
</[CreateAccessPointRequest](#AmazonS3-control_CreateAccessPoint-request-CreateAccessPointRequest "#AmazonS3-control_CreateAccessPoint-request-CreateAccessPointRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_CreateAccessPoint_RequestSyntax "#API_control_CreateAccessPoint_RequestSyntax")**


The name you want to assign to this access point.


For directory buckets, the access point name must consist of a base name that you provide and
 suffix that includes the `ZoneID` (AWS Availability Zone or Local Zone) of your bucket location,
 followed by `--xa-s3`. For more information, see [Managing access to shared datasets in directory buckets with
 access points](../userguide/access-points-directory-buckets.md "../userguide/access-points-directory-buckets.md") in the *Amazon S3 User Guide*.


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_CreateAccessPoint_RequestSyntax "#API_control_CreateAccessPoint_RequestSyntax")**


The AWS account ID for the account that owns the specified access point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[CreateAccessPointRequest](#API_control_CreateAccessPoint_RequestSyntax "#API_control_CreateAccessPoint_RequestSyntax")**


Root level tag for the CreateAccessPointRequest parameters.


Required: Yes




**[Bucket](#API_control_CreateAccessPoint_RequestSyntax "#API_control_CreateAccessPoint_RequestSyntax")**


The name of the bucket that you want to associate this access point with.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded. 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[BucketAccountId](#API_control_CreateAccessPoint_RequestSyntax "#API_control_CreateAccessPoint_RequestSyntax")**


The AWS account ID associated with the S3 bucket associated with this access point.


For same account access point when your bucket and access point belong to the same account owner, the
 `BucketAccountId` is not required. For cross-account access point when your bucket
 and access point are not in the same account, the `BucketAccountId` is required. 


Type: String


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: No




**[PublicAccessBlockConfiguration](#API_control_CreateAccessPoint_RequestSyntax "#API_control_CreateAccessPoint_RequestSyntax")**


 The `PublicAccessBlock` configuration that you want to apply to the access point.
 


Type: [PublicAccessBlockConfiguration](API_control_PublicAccessBlockConfiguration.md "API_control_PublicAccessBlockConfiguration.md") data type


Required: No




**[Scope](#API_control_CreateAccessPoint_RequestSyntax "#API_control_CreateAccessPoint_RequestSyntax")**


For directory buckets, you can filter access control to specific prefixes, API
 operations, or a combination of both. For more information, see [Managing access to shared datasets in directory buckets with
 access points](../userguide/access-points-directory-buckets.md "../userguide/access-points-directory-buckets.md") in the *Amazon S3 User Guide*.


###### Note

Scope is only supported for access points attached to directory buckets.


Type: [Scope](API_control_Scope.md "API_control_Scope.md") data type


Required: No




**[Tags](#API_control_CreateAccessPoint_RequestSyntax "#API_control_CreateAccessPoint_RequestSyntax")**


An array of tags that you can apply to an access point. Tags are key-value pairs of metadata used to control access to your access points. For more information about tags, see [Using tags with Amazon S3](../userguide/tagging.md "../userguide/tagging.md"). For information about tagging access points, see [Using tags for attribute-based access control (ABAC)](../userguide/tagging.md#using-tags-for-abac "../userguide/tagging.md#using-tags-for-abac").


###### Note


* You must have the `s3:TagResource` permission to create an access point with tags for a general purpose bucket.
* You must have the `s3express:TagResource` permission to create an access point with tags for a directory bucket.

Type: Array of [Tag](API_control_Tag.md "API_control_Tag.md") data types


Array Members: Minimum number of 0 items. Maximum number of 50 items.


Required: No




**[VpcConfiguration](#API_control_CreateAccessPoint_RequestSyntax "#API_control_CreateAccessPoint_RequestSyntax")**


If you include this field, Amazon S3 restricts access to this access point to requests from the
 specified virtual private cloud (VPC).


###### Note

This is required for creating an access point for Amazon S3 on Outposts buckets.


Type: [VpcConfiguration](API_control_VpcConfiguration.md "API_control_VpcConfiguration.md") data type


Required: No




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[CreateAccessPointResult](#AmazonS3-control_CreateAccessPoint-response-CreateAccessPointResult "#AmazonS3-control_CreateAccessPoint-response-CreateAccessPointResult")>
   <[AccessPointArn](#AmazonS3-control_CreateAccessPoint-response-AccessPointArn "#AmazonS3-control_CreateAccessPoint-response-AccessPointArn")>***string***</[AccessPointArn](#AmazonS3-control_CreateAccessPoint-response-AccessPointArn "#AmazonS3-control_CreateAccessPoint-response-AccessPointArn")>
   <[Alias](#AmazonS3-control_CreateAccessPoint-response-Alias "#AmazonS3-control_CreateAccessPoint-response-Alias")>***string***</[Alias](#AmazonS3-control_CreateAccessPoint-response-Alias "#AmazonS3-control_CreateAccessPoint-response-Alias")>
</[CreateAccessPointResult](#AmazonS3-control_CreateAccessPoint-response-CreateAccessPointResult "#AmazonS3-control_CreateAccessPoint-response-CreateAccessPointResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[CreateAccessPointResult](#API_control_CreateAccessPoint_ResponseSyntax "#API_control_CreateAccessPoint_ResponseSyntax")**


Root level tag for the CreateAccessPointResult parameters.


Required: Yes




**[AccessPointArn](#API_control_CreateAccessPoint_ResponseSyntax "#API_control_CreateAccessPoint_ResponseSyntax")**


The ARN of the access point.


###### Note

This is only supported by Amazon S3 on Outposts.


Type: String


Length Constraints: Minimum length of 4. Maximum length of 128.




**[Alias](#API_control_CreateAccessPoint_ResponseSyntax "#API_control_CreateAccessPoint_ResponseSyntax")**


The name or alias of the access point.


Type: String


Length Constraints: Maximum length of 63.


Pattern: `^[0-9a-z\\-]{63}`





## Examples


### Sample request for creating an access point for an Amazon S3 on Outposts bucket


This request creates an access point for S3 on Outposts bucket.



```

            PUT /v20180820/accesspoint/example-access-point HTTP/1.1
            Host:s3-outposts.<Region>.amazonaws.com
            x-amz-account-id: example-account-id
            x-amz-outpost-id: op-01ac5d28a6a232904
            <?xml version="1.0" encoding="UTF-8"?>
               <CreateAccessPointRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
                  <Bucket>example-outpost-bucket </Bucket>
               </CreateAccessPointRequest>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessPoint "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessPoint")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateAccessPoint "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateAccessPoint")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessPoint "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessPoint")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessPoint "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessPoint")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessPoint "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessPoint")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessPoint "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessPoint")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessPoint "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessPoint")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessPoint "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessPoint")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessPoint "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessPoint")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessPoint "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessPoint")
