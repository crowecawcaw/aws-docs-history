# AssociateAccessGrantsIdentityCenter

Associate your S3 Access Grants instance with an AWS IAM Identity Center instance. Use this
 action if you want to create access grants for users or groups from your corporate identity
 directory. First, you must add your corporate identity directory to AWS IAM Identity
 Center. Then, you can associate this IAM Identity Center instance with your S3 Access Grants
 instance.



Permissions

You must have the `s3:AssociateAccessGrantsIdentityCenter`
 permission to use this operation. 



Additional Permissions

You must also have the following permissions:
 `sso:CreateApplication`, `sso:PutApplicationGrant`, and
 `sso:PutApplicationAuthenticationMethod`. 



###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /v20180820/accessgrantsinstance/identitycenter HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[AssociateAccessGrantsIdentityCenterRequest](#AmazonS3-control_AssociateAccessGrantsIdentityCenter-request-AssociateAccessGrantsIdentityCenterRequest "#AmazonS3-control_AssociateAccessGrantsIdentityCenter-request-AssociateAccessGrantsIdentityCenterRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[IdentityCenterArn](#AmazonS3-control_AssociateAccessGrantsIdentityCenter-request-IdentityCenterArn "#AmazonS3-control_AssociateAccessGrantsIdentityCenter-request-IdentityCenterArn")>`string`</[IdentityCenterArn](#AmazonS3-control_AssociateAccessGrantsIdentityCenter-request-IdentityCenterArn "#AmazonS3-control_AssociateAccessGrantsIdentityCenter-request-IdentityCenterArn")>
</[AssociateAccessGrantsIdentityCenterRequest](#AmazonS3-control_AssociateAccessGrantsIdentityCenter-request-AssociateAccessGrantsIdentityCenterRequest "#AmazonS3-control_AssociateAccessGrantsIdentityCenter-request-AssociateAccessGrantsIdentityCenterRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[x-amz-account-id](#API_control_AssociateAccessGrantsIdentityCenter_RequestSyntax "#API_control_AssociateAccessGrantsIdentityCenter_RequestSyntax")**


The AWS account ID of the S3 Access Grants instance.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[AssociateAccessGrantsIdentityCenterRequest](#API_control_AssociateAccessGrantsIdentityCenter_RequestSyntax "#API_control_AssociateAccessGrantsIdentityCenter_RequestSyntax")**


Root level tag for the AssociateAccessGrantsIdentityCenterRequest parameters.


Required: Yes




**[IdentityCenterArn](#API_control_AssociateAccessGrantsIdentityCenter_RequestSyntax "#API_control_AssociateAccessGrantsIdentityCenter_RequestSyntax")**


The Amazon Resource Name (ARN) of the AWS IAM Identity Center instance that you are
 associating with your S3 Access Grants instance. An IAM Identity Center instance is your corporate
 identity directory that you added to the IAM Identity Center. You can use the [ListInstances](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html "https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html") API operation to retrieve a list of your Identity Center
 instances and their ARNs.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::(\d{12}){0,1}:instance/.*$`



Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/AssociateAccessGrantsIdentityCenter")
