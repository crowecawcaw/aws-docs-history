# UntagResource

This operation removes the specified user-defined tags from an S3 resource. You can pass
 one or more tag keys. 

###### Note

This operation is only supported for the following Amazon S3 resources:


* [Access Points for directory buckets](../userguide/access-points-db-tagging.md "../userguide/access-points-db-tagging.md")
* [Access Points for general purpose buckets](../userguide/access-points-tagging.md "../userguide/access-points-tagging.md")
* [Directory buckets](../userguide/directory-buckets-tagging.md "../userguide/directory-buckets-tagging.md")
* [Storage Lens groups](../userguide/storage-lens-groups.md "../userguide/storage-lens-groups.md")
* [S3 Access Grants instances, registered locations, and grants](../userguide/access-grants-tagging.md "../userguide/access-grants-tagging.md").


Permissions

For Storage Lens groups and S3 Access Grants, you must have the
 `s3:UntagResource` permission to use this operation. 


For more information about the required Storage Lens Groups permissions, see
 [Setting account permissions to use S3 Storage Lens groups](../userguide/storage_lens_iam_permissions.md#storage_lens_groups_permissions "../userguide/storage_lens_iam_permissions.md#storage_lens_groups_permissions").



Directory bucket permissions

For directory buckets and access points for directory buckets, you must have
 the `s3express:UntagResource` permission to use this operation.
 For more information about directory buckets policies and permissions, see [Identity and Access Management (IAM) for S3 Express One Zone](../userguide/s3-express-permissions.md "../userguide/s3-express-permissions.md") in the *Amazon S3 User Guide*.



HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is `s3express-control.*region*.amazonaws.com`.



For information about S3 Tagging errors, see [List of Amazon S3
 Tagging error codes](ErrorResponses.md#S3TaggingErrorCodeList "ErrorResponses.md#S3TaggingErrorCodeList").

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /v20180820/tags/`resourceArn+`?tagKeys=`TagKeys` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[resourceArn](#API_control_UntagResource_RequestSyntax "#API_control_UntagResource_RequestSyntax")**


The Amazon Resource Name (ARN) of the S3 resource that you're removing tags from. The
 tagged resource can be a directory bucket, S3 Storage Lens group or S3 Access Grants instance,
 registered location, or grant.


Length Constraints: Maximum length of 1011.


Pattern: `arn:[^:]+:s3(express)?:[^:].*`



Required: Yes




**[tagKeys](#API_control_UntagResource_RequestSyntax "#API_control_UntagResource_RequestSyntax")**


 The array of tag key-value pairs that you're trying to remove from of the S3 resource.
 


Array Members: Minimum number of 0 items. Maximum number of 50 items.


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`



Required: Yes




**[x-amz-account-id](#API_control_UntagResource_RequestSyntax "#API_control_UntagResource_RequestSyntax")**


 The AWS account ID that owns the resource that you're trying to remove the tags from.
 


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/UntagResource "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/UntagResource")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/UntagResource "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/UntagResource")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/UntagResource "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/UntagResource")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/UntagResource "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/UntagResource")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UntagResource "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UntagResource")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/UntagResource "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/UntagResource")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/UntagResource "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/UntagResource")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/UntagResource "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/UntagResource")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UntagResource "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UntagResource")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/UntagResource "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/UntagResource")
