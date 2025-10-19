# SetTypeConfiguration

Specifies the configuration data for a CloudFormation extension, such as a resource or Hook,
 in the given account and Region.

For more information, see [Edit configuration
 data for extensions in your account](../UserGuide/registry-set-configuration.md "../UserGuide/registry-set-configuration.md") in the
 *AWS CloudFormation User Guide*.

To view the current configuration data for an extension, refer to the
 `ConfigurationSchema` element of [DescribeType](API_DescribeType.md "API_DescribeType.md").

###### Important

It's strongly recommended that you use dynamic references to restrict sensitive
 configuration definitions, such as third-party credentials. For more information, see [Specify values stored in other services using dynamic references](../UserGuide/dynamic-references.md "../UserGuide/dynamic-references.md") in the
 *AWS CloudFormation User Guide*.

For more information about setting the configuration data for resource types, see [Defining the account-level configuration of an extension](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html#resource-type-howto-configuration "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html#resource-type-howto-configuration") in the
 *AWS CloudFormation Command Line Interface (CLI) User Guide*. For more information about setting the configuration
 data for Hooks, see the [AWS CloudFormation
 Hooks User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html "https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html").


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Configuration** 


The configuration data for the extension in this account and Region.


The configuration data must be formatted as JSON and validate against the extension's
 schema returned in the `Schema` response element of [DescribeType](API_DescribeType.md "API_DescribeType.md").


Type: String


Length Constraints: Minimum length of 1. Maximum length of 204800.


Pattern: `[\s\S]+`



Required: Yes




**ConfigurationAlias** 


An alias by which to refer to this extension configuration data.


Conditional: Specifying a configuration alias is required when setting a configuration for
 a resource type extension.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Pattern: `^[a-zA-Z0-9]{1,256}$`



Required: No




**Type** 


The type of extension.


Conditional: You must specify `ConfigurationArn`, or `Type` and
 `TypeName`.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`



Required: No




**TypeArn** 


The Amazon Resource Name (ARN) for the extension in this account and Region.


For public extensions, this will be the ARN assigned when you call the [ActivateType](API_ActivateType.md "API_ActivateType.md") API operation in this account and Region. For private extensions, this
 will be the ARN assigned when you call the [RegisterType](API_RegisterType.md "API_RegisterType.md") API
 operation in this account and Region.


Do not include the extension versions suffix at the end of the ARN. You can set the
 configuration for an extension, but not for a specific extension version.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`



Required: No




**TypeName** 


The name of the extension.


Conditional: You must specify `ConfigurationArn`, or `Type` and
 `TypeName`.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: No




## Response Elements


The following element is returned by the service.





**ConfigurationArn** 


The Amazon Resource Name (ARN) for the configuration data in this account and
 Region.


Conditional: You must specify `ConfigurationArn`, or `Type` and
 `TypeName`.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type-configuration/.+`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CFNRegistry** 


An error occurred during a CloudFormation registry operation.





**Message** 


A message with details about the error that occurred.




HTTP Status Code: 400




**TypeNotFound** 


The specified extension doesn't exist in the CloudFormation registry.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/SetTypeConfiguration "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/SetTypeConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/SetTypeConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/SetTypeConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/SetTypeConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/SetTypeConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/SetTypeConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/SetTypeConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/SetTypeConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/SetTypeConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/SetTypeConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/SetTypeConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/SetTypeConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/SetTypeConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/SetTypeConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/SetTypeConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/SetTypeConfiguration "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/SetTypeConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/SetTypeConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/SetTypeConfiguration")
