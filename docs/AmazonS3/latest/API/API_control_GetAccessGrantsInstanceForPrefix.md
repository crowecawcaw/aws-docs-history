# GetAccessGrantsInstanceForPrefix

Retrieve the S3 Access Grants instance that contains a particular prefix. 



Permissions

You must have the `s3:GetAccessGrantsInstanceForPrefix` permission
 for the caller account to use this operation. 



Additional Permissions

The prefix owner account must grant you the following permissions to their
 S3 Access Grants instance: `s3:GetAccessGrantsInstanceForPrefix`. 



###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accessgrantsinstance/prefix?s3prefix=`S3Prefix` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[s3prefix](#API_control_GetAccessGrantsInstanceForPrefix_RequestSyntax "#API_control_GetAccessGrantsInstanceForPrefix_RequestSyntax")**


The S3 prefix of the access grants that you would like to retrieve.


Length Constraints: Minimum length of 1. Maximum length of 2000.


Pattern: `^.+$`



Required: Yes




**[x-amz-account-id](#API_control_GetAccessGrantsInstanceForPrefix_RequestSyntax "#API_control_GetAccessGrantsInstanceForPrefix_RequestSyntax")**


The ID of the AWS account that is making this request.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetAccessGrantsInstanceForPrefixResult](#AmazonS3-control_GetAccessGrantsInstanceForPrefix-response-GetAccessGrantsInstanceForPrefixResult "#AmazonS3-control_GetAccessGrantsInstanceForPrefix-response-GetAccessGrantsInstanceForPrefixResult")>
   <[AccessGrantsInstanceArn](#AmazonS3-control_GetAccessGrantsInstanceForPrefix-response-AccessGrantsInstanceArn "#AmazonS3-control_GetAccessGrantsInstanceForPrefix-response-AccessGrantsInstanceArn")>***string***</[AccessGrantsInstanceArn](#AmazonS3-control_GetAccessGrantsInstanceForPrefix-response-AccessGrantsInstanceArn "#AmazonS3-control_GetAccessGrantsInstanceForPrefix-response-AccessGrantsInstanceArn")>
   <[AccessGrantsInstanceId](#AmazonS3-control_GetAccessGrantsInstanceForPrefix-response-AccessGrantsInstanceId "#AmazonS3-control_GetAccessGrantsInstanceForPrefix-response-AccessGrantsInstanceId")>***string***</[AccessGrantsInstanceId](#AmazonS3-control_GetAccessGrantsInstanceForPrefix-response-AccessGrantsInstanceId "#AmazonS3-control_GetAccessGrantsInstanceForPrefix-response-AccessGrantsInstanceId")>
</[GetAccessGrantsInstanceForPrefixResult](#AmazonS3-control_GetAccessGrantsInstanceForPrefix-response-GetAccessGrantsInstanceForPrefixResult "#AmazonS3-control_GetAccessGrantsInstanceForPrefix-response-GetAccessGrantsInstanceForPrefixResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetAccessGrantsInstanceForPrefixResult](#API_control_GetAccessGrantsInstanceForPrefix_ResponseSyntax "#API_control_GetAccessGrantsInstanceForPrefix_ResponseSyntax")**


Root level tag for the GetAccessGrantsInstanceForPrefixResult parameters.


Required: Yes




**[AccessGrantsInstanceArn](#API_control_GetAccessGrantsInstanceForPrefix_ResponseSyntax "#API_control_GetAccessGrantsInstanceForPrefix_ResponseSyntax")**


The Amazon Resource Name (ARN) of the S3 Access Grants instance. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/[a-zA-Z0-9\-]+`





**[AccessGrantsInstanceId](#API_control_GetAccessGrantsInstanceForPrefix_ResponseSyntax "#API_control_GetAccessGrantsInstanceForPrefix_ResponseSyntax")**


The ID of the S3 Access Grants instance. The ID is `default`. You can have one S3 Access Grants
 instance per Region per account. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessGrantsInstanceForPrefix")
