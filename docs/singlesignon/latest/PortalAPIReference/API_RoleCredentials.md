# RoleCredentials

Provides information about the role credentials that are assigned to the user.


## Contents





**accessKeyId** 


The identifier used for the temporary security credentials. For more information, see
 [Using Temporary Security Credentials to Request Access to AWS Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html") in the
 *AWS IAM Identity Center User Guide*.


Type: String


Required: No




**expiration** 


The date on which temporary security credentials expire.


Type: Long


Required: No




**secretAccessKey** 


The key that is used to sign the request. For more information, see [Using Temporary Security Credentials to Request Access to AWS Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html") in the
 *AWS IAM Identity Center User Guide*.


Type: String


Required: No




**sessionToken** 


The token used for temporary credentials. For more information, see [Using Temporary Security Credentials to Request Access to AWS Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html") in the
 *AWS IAM Identity Center User Guide User Guide*.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/sso-2019-06-10/RoleCredentials "https://docs.aws.amazon.com/goto/SdkForCpp/sso-2019-06-10/RoleCredentials")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-2019-06-10/RoleCredentials "https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-2019-06-10/RoleCredentials")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-2019-06-10/RoleCredentials "https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-2019-06-10/RoleCredentials")
