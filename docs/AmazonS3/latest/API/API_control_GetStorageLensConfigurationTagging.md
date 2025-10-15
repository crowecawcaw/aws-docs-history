# GetStorageLensConfigurationTagging

###### Note

This operation is not supported by directory buckets.

Gets the tags of Amazon S3 Storage Lens configuration. For more information about S3 Storage Lens, see
 [Assessing your
 storage activity and usage with Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html")  in the
 *Amazon S3 User Guide*.

###### Note

To use this action, you must have permission to perform the
 `s3:GetStorageLensConfigurationTagging` action. For more information, see
 [Setting permissions to
 use Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html") in the *Amazon S3 User Guide*.

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/storagelens/`storagelensid`/tagging HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[storagelensid](#API_control_GetStorageLensConfigurationTagging_RequestSyntax "#API_control_GetStorageLensConfigurationTagging_RequestSyntax")**


The ID of the Amazon S3 Storage Lens configuration.


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-\_\.]+`



Required: Yes




**[x-amz-account-id](#API_control_GetStorageLensConfigurationTagging_RequestSyntax "#API_control_GetStorageLensConfigurationTagging_RequestSyntax")**


The account ID of the requester.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetStorageLensConfigurationTaggingResult](#AmazonS3-control_GetStorageLensConfigurationTagging-response-GetStorageLensConfigurationTaggingResult "#AmazonS3-control_GetStorageLensConfigurationTagging-response-GetStorageLensConfigurationTaggingResult")>
   <[Tags](#AmazonS3-control_GetStorageLensConfigurationTagging-response-Tags "#AmazonS3-control_GetStorageLensConfigurationTagging-response-Tags")>
      <Tag>
         <[Key](API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Key "API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Key")>***string***</[Key](API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Key "API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Key")>
         <[Value](API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Value "API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Value")>***string***</[Value](API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Value "API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Value")>
      </Tag>
   </[Tags](#AmazonS3-control_GetStorageLensConfigurationTagging-response-Tags "#AmazonS3-control_GetStorageLensConfigurationTagging-response-Tags")>
</[GetStorageLensConfigurationTaggingResult](#AmazonS3-control_GetStorageLensConfigurationTagging-response-GetStorageLensConfigurationTaggingResult "#AmazonS3-control_GetStorageLensConfigurationTagging-response-GetStorageLensConfigurationTaggingResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetStorageLensConfigurationTaggingResult](#API_control_GetStorageLensConfigurationTagging_ResponseSyntax "#API_control_GetStorageLensConfigurationTagging_ResponseSyntax")**


Root level tag for the GetStorageLensConfigurationTaggingResult parameters.


Required: Yes




**[Tags](#API_control_GetStorageLensConfigurationTagging_ResponseSyntax "#API_control_GetStorageLensConfigurationTagging_ResponseSyntax")**


The tags of S3 Storage Lens configuration requested.


Type: Array of [StorageLensTag](API_control_StorageLensTag.md "API_control_StorageLensTag.md") data types




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetStorageLensConfigurationTagging "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetStorageLensConfigurationTagging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetStorageLensConfigurationTagging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetStorageLensConfigurationTagging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetStorageLensConfigurationTagging "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetStorageLensConfigurationTagging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetStorageLensConfigurationTagging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetStorageLensConfigurationTagging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetStorageLensConfigurationTagging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetStorageLensConfigurationTagging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetStorageLensConfigurationTagging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetStorageLensConfigurationTagging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetStorageLensConfigurationTagging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetStorageLensConfigurationTagging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetStorageLensConfigurationTagging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetStorageLensConfigurationTagging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetStorageLensConfigurationTagging "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetStorageLensConfigurationTagging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetStorageLensConfigurationTagging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetStorageLensConfigurationTagging")
