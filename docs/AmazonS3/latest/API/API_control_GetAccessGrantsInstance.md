# GetAccessGrantsInstance

Retrieves the S3 Access Grants instance for a Region in your account. 



Permissions

You must have the `s3:GetAccessGrantsInstance` permission to use
 this operation. 



###### Note


`GetAccessGrantsInstance` is not supported for cross-account access. You can only call the API from the account that owns the S3 Access Grants instance.

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accessgrantsinstance HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[x-amz-account-id](#API_control_GetAccessGrantsInstance_RequestSyntax "#API_control_GetAccessGrantsInstance_RequestSyntax")**


The AWS account ID of the S3 Access Grants instance.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetAccessGrantsInstanceResult](#AmazonS3-control_GetAccessGrantsInstance-response-GetAccessGrantsInstanceResult "#AmazonS3-control_GetAccessGrantsInstance-response-GetAccessGrantsInstanceResult")>
   <[AccessGrantsInstanceArn](#AmazonS3-control_GetAccessGrantsInstance-response-AccessGrantsInstanceArn "#AmazonS3-control_GetAccessGrantsInstance-response-AccessGrantsInstanceArn")>***string***</[AccessGrantsInstanceArn](#AmazonS3-control_GetAccessGrantsInstance-response-AccessGrantsInstanceArn "#AmazonS3-control_GetAccessGrantsInstance-response-AccessGrantsInstanceArn")>
   <[AccessGrantsInstanceId](#AmazonS3-control_GetAccessGrantsInstance-response-AccessGrantsInstanceId "#AmazonS3-control_GetAccessGrantsInstance-response-AccessGrantsInstanceId")>***string***</[AccessGrantsInstanceId](#AmazonS3-control_GetAccessGrantsInstance-response-AccessGrantsInstanceId "#AmazonS3-control_GetAccessGrantsInstance-response-AccessGrantsInstanceId")>
   <[IdentityCenterArn](#AmazonS3-control_GetAccessGrantsInstance-response-IdentityCenterArn "#AmazonS3-control_GetAccessGrantsInstance-response-IdentityCenterArn")>***string***</[IdentityCenterArn](#AmazonS3-control_GetAccessGrantsInstance-response-IdentityCenterArn "#AmazonS3-control_GetAccessGrantsInstance-response-IdentityCenterArn")>
   <[IdentityCenterInstanceArn](#AmazonS3-control_GetAccessGrantsInstance-response-IdentityCenterInstanceArn "#AmazonS3-control_GetAccessGrantsInstance-response-IdentityCenterInstanceArn")>***string***</[IdentityCenterInstanceArn](#AmazonS3-control_GetAccessGrantsInstance-response-IdentityCenterInstanceArn "#AmazonS3-control_GetAccessGrantsInstance-response-IdentityCenterInstanceArn")>
   <[IdentityCenterApplicationArn](#AmazonS3-control_GetAccessGrantsInstance-response-IdentityCenterApplicationArn "#AmazonS3-control_GetAccessGrantsInstance-response-IdentityCenterApplicationArn")>***string***</[IdentityCenterApplicationArn](#AmazonS3-control_GetAccessGrantsInstance-response-IdentityCenterApplicationArn "#AmazonS3-control_GetAccessGrantsInstance-response-IdentityCenterApplicationArn")>
   <[CreatedAt](#AmazonS3-control_GetAccessGrantsInstance-response-CreatedAt "#AmazonS3-control_GetAccessGrantsInstance-response-CreatedAt")>***timestamp***</[CreatedAt](#AmazonS3-control_GetAccessGrantsInstance-response-CreatedAt "#AmazonS3-control_GetAccessGrantsInstance-response-CreatedAt")>
</[GetAccessGrantsInstanceResult](#AmazonS3-control_GetAccessGrantsInstance-response-GetAccessGrantsInstanceResult "#AmazonS3-control_GetAccessGrantsInstance-response-GetAccessGrantsInstanceResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetAccessGrantsInstanceResult](#API_control_GetAccessGrantsInstance_ResponseSyntax "#API_control_GetAccessGrantsInstance_ResponseSyntax")**


Root level tag for the GetAccessGrantsInstanceResult parameters.


Required: Yes




**[AccessGrantsInstanceArn](#API_control_GetAccessGrantsInstance_ResponseSyntax "#API_control_GetAccessGrantsInstance_ResponseSyntax")**


The Amazon Resource Name (ARN) of the S3 Access Grants instance. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/[a-zA-Z0-9\-]+`





**[AccessGrantsInstanceId](#API_control_GetAccessGrantsInstance_ResponseSyntax "#API_control_GetAccessGrantsInstance_ResponseSyntax")**


The ID of the S3 Access Grants instance. The ID is `default`. You can have one S3 Access Grants
 instance per Region per account. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`





**[CreatedAt](#API_control_GetAccessGrantsInstance_ResponseSyntax "#API_control_GetAccessGrantsInstance_ResponseSyntax")**


The date and time when you created the S3 Access Grants instance. 


Type: Timestamp




**[IdentityCenterApplicationArn](#API_control_GetAccessGrantsInstance_ResponseSyntax "#API_control_GetAccessGrantsInstance_ResponseSyntax")**


If you associated your S3 Access Grants instance with an AWS IAM Identity Center instance,
 this field returns the Amazon Resource Name (ARN) of the IAM Identity Center instance
 application; a subresource of the original Identity Center instance. S3 Access Grants creates this
 Identity Center application for the specific S3 Access Grants instance. 


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::\d{12}:application/.*$`





**[IdentityCenterArn](#API_control_GetAccessGrantsInstance_ResponseSyntax "#API_control_GetAccessGrantsInstance_ResponseSyntax")**



*This parameter has been deprecated.*



If you associated your S3 Access Grants instance with an AWS IAM Identity Center instance,
 this field returns the Amazon Resource Name (ARN) of the IAM Identity Center instance
 application; a subresource of the original Identity Center instance. S3 Access Grants creates this
 Identity Center application for the specific S3 Access Grants instance. 


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::(\d{12}){0,1}:instance/.*$`





**[IdentityCenterInstanceArn](#API_control_GetAccessGrantsInstance_ResponseSyntax "#API_control_GetAccessGrantsInstance_ResponseSyntax")**


The Amazon Resource Name (ARN) of the AWS IAM Identity Center instance that you are
 associating with your S3 Access Grants instance. An IAM Identity Center instance is your corporate
 identity directory that you added to the IAM Identity Center. You can use the [ListInstances](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html "https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html") API operation to retrieve a list of your Identity Center
 instances and their ARNs.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::(\d{12}){0,1}:instance/.*$`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessGrantsInstance "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessGrantsInstance")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessGrantsInstance "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessGrantsInstance")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessGrantsInstance")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessGrantsInstance")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessGrantsInstance")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessGrantsInstance")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessGrantsInstance")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessGrantsInstance")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessGrantsInstance "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessGrantsInstance")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessGrantsInstance")
