# BatchDescribeTypeConfigurations

Returns configuration data for the specified CloudFormation extensions, from the CloudFormation
 registry in your current account and Region.

For more information, see [Edit configuration
 data for extensions in your account](../UserGuide/registry-set-configuration.md "../UserGuide/registry-set-configuration.md") in the
 *AWS CloudFormation User Guide*.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**TypeConfigurationIdentifiers.member.N**


The list of identifiers for the desired extension configurations.


Type: Array of [TypeConfigurationIdentifier](API_TypeConfigurationIdentifier.md "API_TypeConfigurationIdentifier.md") objects


Array Members: Minimum number of 1 item.


Required: Yes




## Response Elements


The following elements are returned by the service.





**Errors.member.N**


A list of information concerning any errors generated during the setting of the specified
 configurations.


Type: Array of [BatchDescribeTypeConfigurationsError](API_BatchDescribeTypeConfigurationsError.md "API_BatchDescribeTypeConfigurationsError.md") objects




**TypeConfigurations.member.N**


A list of any of the specified extension configurations from the CloudFormation
 registry.


Type: Array of [TypeConfigurationDetails](API_TypeConfigurationDetails.md "API_TypeConfigurationDetails.md") objects




**UnprocessedTypeConfigurations.member.N**


A list of any of the specified extension configurations that CloudFormation could not process
 for any reason.


Type: Array of [TypeConfigurationIdentifier](API_TypeConfigurationIdentifier.md "API_TypeConfigurationIdentifier.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CFNRegistry** 


An error occurred during a CloudFormation registry operation.





**Message** 


A message with details about the error that occurred.




HTTP Status Code: 400




**TypeConfigurationNotFound** 


The specified extension configuration can't be found.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/BatchDescribeTypeConfigurations "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/BatchDescribeTypeConfigurations")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/BatchDescribeTypeConfigurations "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/BatchDescribeTypeConfigurations")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/BatchDescribeTypeConfigurations "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/BatchDescribeTypeConfigurations")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/BatchDescribeTypeConfigurations "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/BatchDescribeTypeConfigurations")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/BatchDescribeTypeConfigurations "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/BatchDescribeTypeConfigurations")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/BatchDescribeTypeConfigurations "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/BatchDescribeTypeConfigurations")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/BatchDescribeTypeConfigurations "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/BatchDescribeTypeConfigurations")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/BatchDescribeTypeConfigurations "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/BatchDescribeTypeConfigurations")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/BatchDescribeTypeConfigurations "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/BatchDescribeTypeConfigurations")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/BatchDescribeTypeConfigurations "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/BatchDescribeTypeConfigurations")
