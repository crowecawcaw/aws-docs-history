# RegisterPublisher

Registers your account as a publisher of public extensions in the CloudFormation registry.
 Public extensions are available for use by all CloudFormation users. This publisher ID applies to
 your account in all AWS Regions.

For information about requirements for registering as a public extension publisher, see
 [Prerequisite: Registering your account to publish CloudFormation extensions](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs") in the
 *AWS CloudFormation Command Line Interface (CLI) User Guide*.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**AcceptTermsAndConditions** 


Whether you accept the [Terms and Conditions](https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf "https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf") for publishing extensions in the CloudFormation registry. You must
 accept the terms and conditions in order to register to publish public extensions to the
 CloudFormation registry.


The default is `false`.


Type: Boolean


Required: No




**ConnectionArn** 


If you are using a Bitbucket or GitHub account for identity verification, the Amazon
 Resource Name (ARN) for your connection to that account.


For more information, see [Prerequisite: Registering your account to publish CloudFormation extensions](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs") in the
 *AWS CloudFormation Command Line Interface (CLI) User Guide*.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Pattern: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`



Required: No




## Response Elements


The following element is returned by the service.





**PublisherId** 


The ID assigned this account by CloudFormation for publishing extensions.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 40.


Pattern: `[0-9a-zA-Z]{12,40}`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CFNRegistry** 


An error occurred during a CloudFormation registry operation.





**Message** 


A message with details about the error that occurred.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/RegisterPublisher "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/RegisterPublisher")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/RegisterPublisher "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/RegisterPublisher")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RegisterPublisher "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RegisterPublisher")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/RegisterPublisher "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/RegisterPublisher")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RegisterPublisher "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RegisterPublisher")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/RegisterPublisher "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/RegisterPublisher")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/RegisterPublisher "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/RegisterPublisher")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/RegisterPublisher "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/RegisterPublisher")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/RegisterPublisher "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/RegisterPublisher")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RegisterPublisher "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RegisterPublisher")
