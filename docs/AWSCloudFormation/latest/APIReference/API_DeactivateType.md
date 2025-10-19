# DeactivateType

Deactivates a public third-party extension, such as a resource or module, or a CloudFormation
 Hook when you no longer use it.

Deactivating an extension deletes the configuration details that are associated with it.
 To temporarily disable a CloudFormation Hook instead, you can use [SetTypeConfiguration](API_SetTypeConfiguration.md "API_SetTypeConfiguration.md").

Once deactivated, an extension can't be used in any CloudFormation operation. This includes
 stack update operations where the stack template includes the extension, even if no updates
 are being made to the extension. In addition, deactivated extensions aren't automatically
 updated if a new version of the extension is released.

To see which extensions are currently activated, use [ListTypes](API_ListTypes.md "API_ListTypes.md").


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Arn** 


The Amazon Resource Name (ARN) for the extension in this account and Region.


Conditional: You must specify either `Arn`, or `TypeName` and
 `Type`.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:[0-9]{12}:type/.+`



Required: No




**Type** 


The extension type.


Conditional: You must specify either `Arn`, or `TypeName` and
 `Type`.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`



Required: No




**TypeName** 


The type name of the extension in this account and Region. If you specified a type name
 alias when enabling the extension, use the type name alias.


Conditional: You must specify either `Arn`, or `TypeName` and
 `Type`.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: No




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DeactivateType "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DeactivateType")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DeactivateType "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DeactivateType")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DeactivateType "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DeactivateType")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DeactivateType "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DeactivateType")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DeactivateType "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DeactivateType")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DeactivateType "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DeactivateType")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DeactivateType "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DeactivateType")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DeactivateType "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DeactivateType")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DeactivateType "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DeactivateType")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DeactivateType "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DeactivateType")
