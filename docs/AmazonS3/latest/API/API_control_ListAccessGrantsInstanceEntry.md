# ListAccessGrantsInstanceEntry

Information about the S3 Access Grants instance.


## Contents





**AccessGrantsInstanceArn** 


The Amazon Resource Name (ARN) of the S3 Access Grants instance. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/[a-zA-Z0-9\-]+`



Required: No




**AccessGrantsInstanceId** 


The ID of the S3 Access Grants instance. The ID is `default`. You can have one S3 Access Grants
 instance per Region per account. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`



Required: No




**CreatedAt** 


The date and time when you created the S3 Access Grants instance. 


Type: Timestamp


Required: No




**IdentityCenterApplicationArn** 


If you associated your S3 Access Grants instance with an AWS IAM Identity Center instance,
 this field returns the Amazon Resource Name (ARN) of the IAM Identity Center instance
 application; a subresource of the original Identity Center instance. S3 Access Grants creates this
 Identity Center application for the specific S3 Access Grants instance. 


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::\d{12}:application/.*$`



Required: No




**IdentityCenterArn** 



*This member has been deprecated.*



If you associated your S3 Access Grants instance with an AWS IAM Identity Center instance,
 this field returns the Amazon Resource Name (ARN) of the IAM Identity Center instance
 application; a subresource of the original Identity Center instance. S3 Access Grants creates this
 Identity Center application for the specific S3 Access Grants instance. 


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::(\d{12}){0,1}:instance/.*$`



Required: No




**IdentityCenterInstanceArn** 


The Amazon Resource Name (ARN) of the AWS IAM Identity Center instance that you are
 associating with your S3 Access Grants instance. An IAM Identity Center instance is your corporate
 identity directory that you added to the IAM Identity Center. You can use the [ListInstances](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html "https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html") API operation to retrieve a list of your Identity Center
 instances and their ARNs.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::(\d{12}){0,1}:instance/.*$`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessGrantsInstanceEntry "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessGrantsInstanceEntry")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessGrantsInstanceEntry "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessGrantsInstanceEntry")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessGrantsInstanceEntry "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessGrantsInstanceEntry")
