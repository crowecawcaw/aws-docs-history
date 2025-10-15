# PutPublicAccessBlock

###### Note

This operation is not supported by directory buckets.

Creates or modifies the `PublicAccessBlock` configuration for an
 AWS account. For this operation, users must have the
 `s3:PutAccountPublicAccessBlock` permission. For more information, see [Using Amazon S3 block public access](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html").

Related actions include:


* [GetPublicAccessBlock](API_control_GetPublicAccessBlock.md "API_control_GetPublicAccessBlock.md")
* [DeletePublicAccessBlock](API_control_DeletePublicAccessBlock.md "API_control_DeletePublicAccessBlock.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /v20180820/configuration/publicAccessBlock HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[PublicAccessBlockConfiguration](#AmazonS3-control_PutPublicAccessBlock-request-PublicAccessBlockConfiguration "#AmazonS3-control_PutPublicAccessBlock-request-PublicAccessBlockConfiguration") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[BlockPublicAcls](#AmazonS3-control_PutPublicAccessBlock-request-BlockPublicAcls "#AmazonS3-control_PutPublicAccessBlock-request-BlockPublicAcls")>`boolean`</[BlockPublicAcls](#AmazonS3-control_PutPublicAccessBlock-request-BlockPublicAcls "#AmazonS3-control_PutPublicAccessBlock-request-BlockPublicAcls")>
   <[IgnorePublicAcls](#AmazonS3-control_PutPublicAccessBlock-request-IgnorePublicAcls "#AmazonS3-control_PutPublicAccessBlock-request-IgnorePublicAcls")>`boolean`</[IgnorePublicAcls](#AmazonS3-control_PutPublicAccessBlock-request-IgnorePublicAcls "#AmazonS3-control_PutPublicAccessBlock-request-IgnorePublicAcls")>
   <[BlockPublicPolicy](#AmazonS3-control_PutPublicAccessBlock-request-BlockPublicPolicy "#AmazonS3-control_PutPublicAccessBlock-request-BlockPublicPolicy")>`boolean`</[BlockPublicPolicy](#AmazonS3-control_PutPublicAccessBlock-request-BlockPublicPolicy "#AmazonS3-control_PutPublicAccessBlock-request-BlockPublicPolicy")>
   <[RestrictPublicBuckets](#AmazonS3-control_PutPublicAccessBlock-request-RestrictPublicBuckets "#AmazonS3-control_PutPublicAccessBlock-request-RestrictPublicBuckets")>`boolean`</[RestrictPublicBuckets](#AmazonS3-control_PutPublicAccessBlock-request-RestrictPublicBuckets "#AmazonS3-control_PutPublicAccessBlock-request-RestrictPublicBuckets")>
</[PublicAccessBlockConfiguration](#AmazonS3-control_PutPublicAccessBlock-request-PublicAccessBlockConfiguration "#AmazonS3-control_PutPublicAccessBlock-request-PublicAccessBlockConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[x-amz-account-id](#API_control_PutPublicAccessBlock_RequestSyntax "#API_control_PutPublicAccessBlock_RequestSyntax")**


The account ID for the AWS account whose `PublicAccessBlock` configuration
 you want to set.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[PublicAccessBlockConfiguration](#API_control_PutPublicAccessBlock_RequestSyntax "#API_control_PutPublicAccessBlock_RequestSyntax")**


Root level tag for the PublicAccessBlockConfiguration parameters.


Required: Yes




**[BlockPublicAcls](#API_control_PutPublicAccessBlock_RequestSyntax "#API_control_PutPublicAccessBlock_RequestSyntax")**


Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets in
 this account. Setting this element to `TRUE` causes the following
 behavior:



* `PutBucketAcl` and `PutObjectAcl` calls fail if the
 specified ACL is public.
* PUT Object calls fail if the request includes a public ACL.
* PUT Bucket calls fail if the request includes a public ACL.

Enabling this setting doesn't affect existing policies or ACLs.


This property is not supported for Amazon S3 on Outposts.


Type: Boolean


Required: No




**[BlockPublicPolicy](#API_control_PutPublicAccessBlock_RequestSyntax "#API_control_PutPublicAccessBlock_RequestSyntax")**


Specifies whether Amazon S3 should block public bucket policies for buckets in this account.
 Setting this element to `TRUE` causes Amazon S3 to reject calls to PUT Bucket policy
 if the specified bucket policy allows public access. 


Enabling this setting doesn't affect existing bucket policies.


This property is not supported for Amazon S3 on Outposts.


Type: Boolean


Required: No




**[IgnorePublicAcls](#API_control_PutPublicAccessBlock_RequestSyntax "#API_control_PutPublicAccessBlock_RequestSyntax")**


Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting
 this element to `TRUE` causes Amazon S3 to ignore all public ACLs on buckets in this
 account and any objects that they contain. 


Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't
 prevent new public ACLs from being set.


This property is not supported for Amazon S3 on Outposts.


Type: Boolean


Required: No




**[RestrictPublicBuckets](#API_control_PutPublicAccessBlock_RequestSyntax "#API_control_PutPublicAccessBlock_RequestSyntax")**


Specifies whether Amazon S3 should restrict public bucket policies for buckets in this
 account. Setting this element to `TRUE` restricts access to buckets with public
 policies to only AWS service principals and authorized users within this
 account.


Enabling this setting doesn't affect previously stored bucket policies, except that
 public and cross-account access within any public bucket policy, including non-public
 delegation to specific accounts, is blocked.


This property is not supported for Amazon S3 on Outposts.


Type: Boolean


Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutPublicAccessBlock "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutPublicAccessBlock")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutPublicAccessBlock "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutPublicAccessBlock")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutPublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutPublicAccessBlock")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutPublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutPublicAccessBlock")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutPublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutPublicAccessBlock")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutPublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutPublicAccessBlock")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutPublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutPublicAccessBlock")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutPublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutPublicAccessBlock")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutPublicAccessBlock "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutPublicAccessBlock")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutPublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutPublicAccessBlock")
