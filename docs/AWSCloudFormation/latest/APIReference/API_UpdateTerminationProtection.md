# UpdateTerminationProtection

Updates termination protection for the specified stack. If a user attempts to delete a
 stack with termination protection enabled, the operation fails and the stack remains
 unchanged. For more information, see [Protect a CloudFormation
 stack from being deleted](../UserGuide/using-cfn-protect-stacks.md "../UserGuide/using-cfn-protect-stacks.md") in the *AWS CloudFormation User Guide*.

For [nested stacks](../UserGuide/using-cfn-nested-stacks.md "../UserGuide/using-cfn-nested-stacks.md"),
 termination protection is set on the root stack and can't be changed directly on the nested
 stack.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**EnableTerminationProtection** 


Whether to enable termination protection on the specified stack.


Type: Boolean


Required: Yes




**StackName** 


The name or unique ID of the stack for which you want to set termination
 protection.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`



Required: Yes




## Response Elements


The following element is returned by the service.





**StackId** 


The unique ID of the stack.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/UpdateTerminationProtection "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/UpdateTerminationProtection")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/UpdateTerminationProtection "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/UpdateTerminationProtection")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/UpdateTerminationProtection "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/UpdateTerminationProtection")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/UpdateTerminationProtection "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/UpdateTerminationProtection")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/UpdateTerminationProtection "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/UpdateTerminationProtection")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/UpdateTerminationProtection "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/UpdateTerminationProtection")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/UpdateTerminationProtection "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/UpdateTerminationProtection")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/UpdateTerminationProtection "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/UpdateTerminationProtection")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/UpdateTerminationProtection "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/UpdateTerminationProtection")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/UpdateTerminationProtection "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/UpdateTerminationProtection")
