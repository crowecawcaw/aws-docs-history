# CreateAccessGrantsInstance

Creates an S3 Access Grants instance, which serves as a logical grouping for access grants. You
 can create one S3 Access Grants instance per Region per account. 



Permissions

You must have the `s3:CreateAccessGrantsInstance` permission to use
 this operation. 



Additional Permissions

To associate an IAM Identity Center instance with your S3 Access Grants instance, you
 must also have the `sso:DescribeInstance`,
 `sso:CreateApplication`, `sso:PutApplicationGrant`, and
 `sso:PutApplicationAuthenticationMethod` permissions. 



###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /v20180820/accessgrantsinstance HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[CreateAccessGrantsInstanceRequest](#AmazonS3-control_CreateAccessGrantsInstance-request-CreateAccessGrantsInstanceRequest "#AmazonS3-control_CreateAccessGrantsInstance-request-CreateAccessGrantsInstanceRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[IdentityCenterArn](#AmazonS3-control_CreateAccessGrantsInstance-request-IdentityCenterArn "#AmazonS3-control_CreateAccessGrantsInstance-request-IdentityCenterArn")>`string`</[IdentityCenterArn](#AmazonS3-control_CreateAccessGrantsInstance-request-IdentityCenterArn "#AmazonS3-control_CreateAccessGrantsInstance-request-IdentityCenterArn")>
   <[Tags](#AmazonS3-control_CreateAccessGrantsInstance-request-Tags "#AmazonS3-control_CreateAccessGrantsInstance-request-Tags")>
      <Tag>
         <[Key](API_control_Tag.md#AmazonS3-Type-control_Tag-Key "API_control_Tag.md#AmazonS3-Type-control_Tag-Key")>`string`</[Key](API_control_Tag.md#AmazonS3-Type-control_Tag-Key "API_control_Tag.md#AmazonS3-Type-control_Tag-Key")>
         <[Value](API_control_Tag.md#AmazonS3-Type-control_Tag-Value "API_control_Tag.md#AmazonS3-Type-control_Tag-Value")>`string`</[Value](API_control_Tag.md#AmazonS3-Type-control_Tag-Value "API_control_Tag.md#AmazonS3-Type-control_Tag-Value")>
      </Tag>
   </[Tags](#AmazonS3-control_CreateAccessGrantsInstance-request-Tags "#AmazonS3-control_CreateAccessGrantsInstance-request-Tags")>
</[CreateAccessGrantsInstanceRequest](#AmazonS3-control_CreateAccessGrantsInstance-request-CreateAccessGrantsInstanceRequest "#AmazonS3-control_CreateAccessGrantsInstance-request-CreateAccessGrantsInstanceRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[x-amz-account-id](#API_control_CreateAccessGrantsInstance_RequestSyntax "#API_control_CreateAccessGrantsInstance_RequestSyntax")**


The AWS account ID of the S3 Access Grants instance.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[CreateAccessGrantsInstanceRequest](#API_control_CreateAccessGrantsInstance_RequestSyntax "#API_control_CreateAccessGrantsInstance_RequestSyntax")**


Root level tag for the CreateAccessGrantsInstanceRequest parameters.


Required: Yes




**[IdentityCenterArn](#API_control_CreateAccessGrantsInstance_RequestSyntax "#API_control_CreateAccessGrantsInstance_RequestSyntax")**


If you would like to associate your S3 Access Grants instance with an AWS IAM Identity Center
 instance, use this field to pass the Amazon Resource Name (ARN) of the AWS IAM Identity
 Center instance that you are associating with your S3 Access Grants instance. An IAM Identity
 Center instance is your corporate identity directory that you added to the IAM Identity
 Center. You can use the [ListInstances](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html "https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html") API
 operation to retrieve a list of your Identity Center instances and their ARNs. 


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::(\d{12}){0,1}:instance/.*$`



Required: No




**[Tags](#API_control_CreateAccessGrantsInstance_RequestSyntax "#API_control_CreateAccessGrantsInstance_RequestSyntax")**


The AWS resource tags that you are adding to the S3 Access Grants instance. Each tag is a label
 consisting of a user-defined key and value. Tags can help you manage, identify, organize,
 search for, and filter resources. 


Type: Array of [Tag](API_control_Tag.md "API_control_Tag.md") data types


Array Members: Minimum number of 0 items. Maximum number of 50 items.


Required: No




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[CreateAccessGrantsInstanceResult](#AmazonS3-control_CreateAccessGrantsInstance-response-CreateAccessGrantsInstanceResult "#AmazonS3-control_CreateAccessGrantsInstance-response-CreateAccessGrantsInstanceResult")>
   <[CreatedAt](#AmazonS3-control_CreateAccessGrantsInstance-response-CreatedAt "#AmazonS3-control_CreateAccessGrantsInstance-response-CreatedAt")>***timestamp***</[CreatedAt](#AmazonS3-control_CreateAccessGrantsInstance-response-CreatedAt "#AmazonS3-control_CreateAccessGrantsInstance-response-CreatedAt")>
   <[AccessGrantsInstanceId](#AmazonS3-control_CreateAccessGrantsInstance-response-AccessGrantsInstanceId "#AmazonS3-control_CreateAccessGrantsInstance-response-AccessGrantsInstanceId")>***string***</[AccessGrantsInstanceId](#AmazonS3-control_CreateAccessGrantsInstance-response-AccessGrantsInstanceId "#AmazonS3-control_CreateAccessGrantsInstance-response-AccessGrantsInstanceId")>
   <[AccessGrantsInstanceArn](#AmazonS3-control_CreateAccessGrantsInstance-response-AccessGrantsInstanceArn "#AmazonS3-control_CreateAccessGrantsInstance-response-AccessGrantsInstanceArn")>***string***</[AccessGrantsInstanceArn](#AmazonS3-control_CreateAccessGrantsInstance-response-AccessGrantsInstanceArn "#AmazonS3-control_CreateAccessGrantsInstance-response-AccessGrantsInstanceArn")>
   <[IdentityCenterArn](#AmazonS3-control_CreateAccessGrantsInstance-response-IdentityCenterArn "#AmazonS3-control_CreateAccessGrantsInstance-response-IdentityCenterArn")>***string***</[IdentityCenterArn](#AmazonS3-control_CreateAccessGrantsInstance-response-IdentityCenterArn "#AmazonS3-control_CreateAccessGrantsInstance-response-IdentityCenterArn")>
   <[IdentityCenterInstanceArn](#AmazonS3-control_CreateAccessGrantsInstance-response-IdentityCenterInstanceArn "#AmazonS3-control_CreateAccessGrantsInstance-response-IdentityCenterInstanceArn")>***string***</[IdentityCenterInstanceArn](#AmazonS3-control_CreateAccessGrantsInstance-response-IdentityCenterInstanceArn "#AmazonS3-control_CreateAccessGrantsInstance-response-IdentityCenterInstanceArn")>
   <[IdentityCenterApplicationArn](#AmazonS3-control_CreateAccessGrantsInstance-response-IdentityCenterApplicationArn "#AmazonS3-control_CreateAccessGrantsInstance-response-IdentityCenterApplicationArn")>***string***</[IdentityCenterApplicationArn](#AmazonS3-control_CreateAccessGrantsInstance-response-IdentityCenterApplicationArn "#AmazonS3-control_CreateAccessGrantsInstance-response-IdentityCenterApplicationArn")>
</[CreateAccessGrantsInstanceResult](#AmazonS3-control_CreateAccessGrantsInstance-response-CreateAccessGrantsInstanceResult "#AmazonS3-control_CreateAccessGrantsInstance-response-CreateAccessGrantsInstanceResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[CreateAccessGrantsInstanceResult](#API_control_CreateAccessGrantsInstance_ResponseSyntax "#API_control_CreateAccessGrantsInstance_ResponseSyntax")**


Root level tag for the CreateAccessGrantsInstanceResult parameters.


Required: Yes




**[AccessGrantsInstanceArn](#API_control_CreateAccessGrantsInstance_ResponseSyntax "#API_control_CreateAccessGrantsInstance_ResponseSyntax")**


The Amazon Resource Name (ARN) of the AWS IAM Identity Center instance that you are
 associating with your S3 Access Grants instance. An IAM Identity Center instance is your corporate
 identity directory that you added to the IAM Identity Center. You can use the [ListInstances](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html "https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html") API operation to retrieve a list of your Identity Center
 instances and their ARNs.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/[a-zA-Z0-9\-]+`





**[AccessGrantsInstanceId](#API_control_CreateAccessGrantsInstance_ResponseSyntax "#API_control_CreateAccessGrantsInstance_ResponseSyntax")**


The ID of the S3 Access Grants instance. The ID is `default`. You can have one S3 Access Grants
 instance per Region per account. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`





**[CreatedAt](#API_control_CreateAccessGrantsInstance_ResponseSyntax "#API_control_CreateAccessGrantsInstance_ResponseSyntax")**


The date and time when you created the S3 Access Grants instance. 


Type: Timestamp




**[IdentityCenterApplicationArn](#API_control_CreateAccessGrantsInstance_ResponseSyntax "#API_control_CreateAccessGrantsInstance_ResponseSyntax")**


If you associated your S3 Access Grants instance with an AWS IAM Identity Center instance,
 this field returns the Amazon Resource Name (ARN) of the IAM Identity Center instance
 application; a subresource of the original Identity Center instance. S3 Access Grants creates this
 Identity Center application for the specific S3 Access Grants instance. 


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::\d{12}:application/.*$`





**[IdentityCenterArn](#API_control_CreateAccessGrantsInstance_ResponseSyntax "#API_control_CreateAccessGrantsInstance_ResponseSyntax")**



*This parameter has been deprecated.*



If you associated your S3 Access Grants instance with an AWS IAM Identity Center instance,
 this field returns the Amazon Resource Name (ARN) of the IAM Identity Center instance
 application; a subresource of the original Identity Center instance. S3 Access Grants creates this
 Identity Center application for the specific S3 Access Grants instance. 


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::(\d{12}){0,1}:instance/.*$`





**[IdentityCenterInstanceArn](#API_control_CreateAccessGrantsInstance_ResponseSyntax "#API_control_CreateAccessGrantsInstance_ResponseSyntax")**


The Amazon Resource Name (ARN) of the AWS IAM Identity Center instance that you are
 associating with your S3 Access Grants instance. An IAM Identity Center instance is your corporate
 identity directory that you added to the IAM Identity Center. You can use the [ListInstances](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html "https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html") API operation to retrieve a list of your Identity Center
 instances and their ARNs.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::(\d{12}){0,1}:instance/.*$`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessGrantsInstance "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessGrantsInstance")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateAccessGrantsInstance "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateAccessGrantsInstance")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessGrantsInstance")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessGrantsInstance")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessGrantsInstance")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessGrantsInstance")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessGrantsInstance")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessGrantsInstance")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessGrantsInstance "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessGrantsInstance")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessGrantsInstance "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessGrantsInstance")
