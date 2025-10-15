# DeleteStorageLensGroup


Deletes an existing S3 Storage Lens group.

To use this operation, you must have the permission to perform the
 `s3:DeleteStorageLensGroup` action. For more information about the required Storage Lens
 Groups permissions, see [Setting account permissions to use S3 Storage Lens groups](../userguide/storage_lens_iam_permissions.md#storage_lens_groups_permissions "../userguide/storage_lens_iam_permissions.md#storage_lens_groups_permissions").

For information about Storage Lens groups errors, see [List of Amazon S3 Storage
 Lens error codes](ErrorResponses.md#S3LensErrorCodeList "ErrorResponses.md#S3LensErrorCodeList").

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
DELETE /v20180820/storagelensgroup/`name` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_DeleteStorageLensGroup_RequestSyntax "#API_control_DeleteStorageLensGroup_RequestSyntax")**



The name of the Storage Lens group that you're trying to delete.



Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-\_]+`



Required: Yes




**[x-amz-account-id](#API_control_DeleteStorageLensGroup_RequestSyntax "#API_control_DeleteStorageLensGroup_RequestSyntax")**



The AWS account ID used to create the Storage Lens group that you're trying to delete.



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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteStorageLensGroup "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteStorageLensGroup")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteStorageLensGroup "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteStorageLensGroup")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteStorageLensGroup")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteStorageLensGroup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteStorageLensGroup")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteStorageLensGroup")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteStorageLensGroup")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteStorageLensGroup")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteStorageLensGroup "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteStorageLensGroup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteStorageLensGroup")
