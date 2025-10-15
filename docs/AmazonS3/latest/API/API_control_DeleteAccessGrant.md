# DeleteAccessGrant

Deletes the access grant from the S3 Access Grants instance. You cannot undo an access grant
 deletion and the grantee will no longer have access to the S3 data.



Permissions

You must have the `s3:DeleteAccessGrant` permission to use this
 operation. 



###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /v20180820/accessgrantsinstance/grant/`id` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[id](#API_control_DeleteAccessGrant_RequestSyntax "#API_control_DeleteAccessGrant_RequestSyntax")**


The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access
 grant.


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`



Required: Yes




**[x-amz-account-id](#API_control_DeleteAccessGrant_RequestSyntax "#API_control_DeleteAccessGrant_RequestSyntax")**


The AWS account ID of the S3 Access Grants instance.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteAccessGrant "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteAccessGrant")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteAccessGrant "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteAccessGrant")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteAccessGrant "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteAccessGrant")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteAccessGrant "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteAccessGrant")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteAccessGrant "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteAccessGrant")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteAccessGrant "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteAccessGrant")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteAccessGrant "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteAccessGrant")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteAccessGrant "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteAccessGrant")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteAccessGrant "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteAccessGrant")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteAccessGrant "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteAccessGrant")
