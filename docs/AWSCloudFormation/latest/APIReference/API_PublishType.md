# PublishType

Publishes the specified extension to the CloudFormation registry as a public extension in this
 Region. Public extensions are available for use by all CloudFormation users. For more information
 about publishing extensions, see [Publishing extensions to
 make them available for public use](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html") in the
 *AWS CloudFormation Command Line Interface (CLI) User Guide*.

To publish an extension, you must be registered as a publisher with CloudFormation. For more
 information, see [RegisterPublisher](API_RegisterPublisher.md "API_RegisterPublisher.md").


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Arn** 


The Amazon Resource Name (ARN) of the extension.


Conditional: You must specify `Arn`, or `TypeName` and
 `Type`.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:[0-9]{12}:type/.+`



Required: No




**PublicVersionNumber** 


The version number to assign to this version of the extension.


Use the following format, and adhere to semantic versioning when assigning a version
 number to your extension:



`MAJOR.MINOR.PATCH`



For more information, see [Semantic Versioning
 2.0.0](https://semver.org/ "https://semver.org/").


If you don't specify a version number, CloudFormation increments the version number by one
 minor version release.


You cannot specify a version number the first time you publish a type. CloudFormation
 automatically sets the first version number to be `1.0.0`.


Type: String


Length Constraints: Minimum length of 5.


Pattern: `^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(.*)$`



Required: No




**Type** 


The type of the extension.


Conditional: You must specify `Arn`, or `TypeName` and
 `Type`.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`



Required: No




**TypeName** 


The name of the extension.


Conditional: You must specify `Arn`, or `TypeName` and
 `Type`.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: No




## Response Elements


The following element is returned by the service.





**PublicTypeArn** 


The Amazon Resource Name (ARN) assigned to the public extension upon publication.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`





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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/PublishType "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/PublishType")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/PublishType "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/PublishType")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/PublishType "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/PublishType")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/PublishType "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/PublishType")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/PublishType "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/PublishType")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/PublishType "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/PublishType")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/PublishType "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/PublishType")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/PublishType "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/PublishType")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/PublishType "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/PublishType")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/PublishType "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/PublishType")
