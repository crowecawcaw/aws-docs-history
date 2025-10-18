# TestType

Tests a registered extension to make sure it meets all necessary requirements for being
 published in the CloudFormation registry.


* For resource types, this includes passing all contracts tests defined for the
 type.
* For modules, this includes determining if the module's model meets all necessary
 requirements.
For more information, see [Testing your public extension before publishing](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing") in the
 *AWS CloudFormation Command Line Interface (CLI) User Guide*.

If you don't specify a version, CloudFormation uses the default version of the extension in
 your account and Region for testing.

To perform testing, CloudFormation assumes the execution role specified when the type was
 registered. For more information, see [RegisterType](API_RegisterType.md "API_RegisterType.md").

Once you've initiated testing on an extension using `TestType`, you can pass
 the returned `TypeVersionArn` into [DescribeType](API_DescribeType.md "API_DescribeType.md") to
 monitor the current test status and test status description for the extension.

An extension must have a test status of `PASSED` before it can be published.
 For more information, see [Publishing extensions
 to make them available for public use](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html") in the
 *AWS CloudFormation Command Line Interface (CLI) User Guide*.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Arn** 


The Amazon Resource Name (ARN) of the extension.


Conditional: You must specify `Arn`, or `TypeName` and
 `Type`.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`



Required: No




**LogDeliveryBucket** 


The S3 bucket to which CloudFormation delivers the contract test execution logs.


CloudFormation delivers the logs by the time contract testing has completed and the extension
 has been assigned a test type status of `PASSED` or `FAILED`.


The user calling `TestType` must be able to access items in the specified S3
 bucket. Specifically, the user needs the following permissions:



* `GetObject`
* `PutObject`

For more information, see [Actions, Resources, and
 Condition Keys for Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html") in the *AWS Identity and Access Management User Guide*.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Pattern: `[\s\S]+`



Required: No




**Type** 


The type of the extension to test.


Conditional: You must specify `Arn`, or `TypeName` and
 `Type`.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`



Required: No




**TypeName** 


The name of the extension to test.


Conditional: You must specify `Arn`, or `TypeName` and
 `Type`.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: No




**VersionId** 


The version of the extension to test.


You can specify the version id with either `Arn`, or with `TypeName`
 and `Type`.


If you don't specify a version, CloudFormation uses the default version of the extension in
 this account and Region for testing.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[A-Za-z0-9-]+`



Required: No




## Response Elements


The following element is returned by the service.





**TypeVersionArn** 


The Amazon Resource Name (ARN) of the extension.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/TestType "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/TestType")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/TestType "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/TestType")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TestType "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TestType")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/TestType "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/TestType")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TestType "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TestType")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/TestType "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/TestType")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/TestType "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/TestType")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/TestType "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/TestType")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/TestType "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/TestType")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TestType "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TestType")
