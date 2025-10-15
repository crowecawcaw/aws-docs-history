# TypeVersionSummary

Contains summary information about a specific version of a CloudFormation extension.


## Contents





**Arn** 


The ARN of the extension version.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`



Required: No




**Description** 


The description of the extension version.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**IsDefaultVersion** 


Whether the specified extension version is set as the default version.


This applies only to private extensions you have registered in your account, and extensions
 published by Amazon. For public third-party extensions, CloudFormation returns
 `null`.


Type: Boolean


Required: No




**PublicVersionNumber** 


For public extensions that have been activated for this account and Region, the version of
 the public extension to be used for CloudFormation operations in this account and Region. For any
 extensions other than activated third-party extensions, CloudFormation returns
 `null`.


How you specified `AutoUpdate` when enabling the extension affects whether
 CloudFormation automatically updates the extension in this account and Region when a new version is
 released. For more information, see [Automatically use new versions of extensions](../UserGuide/registry-public.md#registry-public-enable-auto "../UserGuide/registry-public.md#registry-public-enable-auto") in the
 *AWS CloudFormation User Guide*.


Type: String


Length Constraints: Minimum length of 5.


Pattern: `^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(.*)$`



Required: No




**TimeCreated** 


When the version was registered.


Type: Timestamp


Required: No




**Type** 


The kind of extension.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`



Required: No




**TypeName** 


The name of the extension.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: No




**VersionId** 


The ID of a specific version of the extension. The version ID is the value at the end of the
 ARN assigned to the extension version when it's registered.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[A-Za-z0-9-]+`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TypeVersionSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TypeVersionSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TypeVersionSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TypeVersionSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TypeVersionSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TypeVersionSummary")
