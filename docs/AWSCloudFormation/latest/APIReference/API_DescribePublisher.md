# DescribePublisher

Returns information about a CloudFormation extension publisher.

If you don't supply a `PublisherId`, and you have registered as an extension
 publisher, `DescribePublisher` returns information about your own publisher
 account.

For more information about registering as a publisher, see:


* [RegisterPublisher](API_RegisterPublisher.md "API_RegisterPublisher.md")
* [Publishing extensions
 to make them available for public use](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html") in the
 *AWS CloudFormation Command Line Interface (CLI) User Guide*

## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**PublisherId** 


The ID of the extension publisher.


If you don't supply a `PublisherId`, and you have registered as an extension
 publisher, `DescribePublisher` returns information about your own publisher
 account.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 40.


Pattern: `[0-9a-zA-Z]{12,40}`



Required: No




## Response Elements


The following elements are returned by the service.





**IdentityProvider** 


The type of account used as the identity provider when registering this publisher with
 CloudFormation.


Type: String


Valid Values: `AWS_Marketplace | GitHub | Bitbucket`





**PublisherId** 


The ID of the extension publisher.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 40.


Pattern: `[0-9a-zA-Z]{12,40}`





**PublisherProfile** 


The URL to the publisher's profile with the identity provider.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `(http:|https:)+[^\s]+[\w]`





**PublisherStatus** 


Whether the publisher is verified. Currently, all registered publishers are
 verified.


Type: String


Valid Values: `VERIFIED | UNVERIFIED`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CFNRegistry** 


An error occurred during a CloudFormation registry operation.





**Message** 


A message with details about the error that occurred.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribePublisher "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribePublisher")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribePublisher "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribePublisher")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribePublisher "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribePublisher")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribePublisher "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribePublisher")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribePublisher "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribePublisher")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribePublisher "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribePublisher")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribePublisher "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribePublisher")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribePublisher "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribePublisher")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribePublisher "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribePublisher")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribePublisher "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribePublisher")
