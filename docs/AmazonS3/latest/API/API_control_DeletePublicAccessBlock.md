# DeletePublicAccessBlock

###### Note

This operation is not supported by directory buckets.

Removes the `PublicAccessBlock` configuration for an AWS account. For more
 information, see  [Using Amazon S3 block
 public access](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html").

Related actions include:


* [GetPublicAccessBlock](API_control_GetPublicAccessBlock.md "API_control_GetPublicAccessBlock.md")
* [PutPublicAccessBlock](API_control_PutPublicAccessBlock.md "API_control_PutPublicAccessBlock.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /v20180820/configuration/publicAccessBlock HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[x-amz-account-id](#API_control_DeletePublicAccessBlock_RequestSyntax "#API_control_DeletePublicAccessBlock_RequestSyntax")**


The account ID for the AWS account whose `PublicAccessBlock` configuration
 you want to remove.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeletePublicAccessBlock")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeletePublicAccessBlock")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeletePublicAccessBlock")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeletePublicAccessBlock")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeletePublicAccessBlock")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeletePublicAccessBlock")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeletePublicAccessBlock")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeletePublicAccessBlock")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeletePublicAccessBlock")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeletePublicAccessBlock "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeletePublicAccessBlock")
