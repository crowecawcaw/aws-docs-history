# TypeSummary

Contains summary information about the specified CloudFormation extension.


## Contents





**DefaultVersionId** 


The ID of the default version of the extension. The default version is used when the
 extension version isn't specified.


This applies only to private extensions you have registered in your account. For public
 extensions, both those provided by Amazon and published by third parties, CloudFormation returns
 `null`. For more information, see [RegisterType](API_RegisterType.md "API_RegisterType.md").


To set the default version of an extension, use [SetTypeDefaultVersion](API_SetTypeDefaultVersion.md "API_SetTypeDefaultVersion.md").


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[A-Za-z0-9-]+`



Required: No




**Description** 


The description of the extension.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**IsActivated** 


Whether the extension is activated for this account and Region.


This applies only to third-party public extensions. Extensions published by Amazon are
 activated by default.


Type: Boolean


Required: No




**LastUpdated** 


When the specified extension version was registered. This applies only to:



* Private extensions you have registered in your account. For more information, see [RegisterType](API_RegisterType.md "API_RegisterType.md").
* Public extensions you have activated in your account with auto-update specified. For more
 information, see [ActivateType](API_ActivateType.md "API_ActivateType.md").

For all other extension types, CloudFormation returns `null`.


Type: Timestamp


Required: No




**LatestPublicVersion** 


For public extensions that have been activated for this account and Region, the latest
 version of the public extension *that is available*. For any extensions other
 than activated third-party extensions, CloudFormation returns `null`.


How you specified `AutoUpdate` when enabling the extension affects whether
 CloudFormation automatically updates the extension in this account and Region when a new version is
 released. For more information, see [Automatically use new versions of extensions](../UserGuide/registry-public.md#registry-public-enable-auto "../UserGuide/registry-public.md#registry-public-enable-auto") in the
 *AWS CloudFormation User Guide*.


Type: String


Length Constraints: Minimum length of 5.


Pattern: `^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(.*)$`



Required: No




**OriginalTypeName** 


For public extensions that have been activated for this account and Region, the type name of
 the public extension.


If you specified a `TypeNameAlias` when enabling the extension in this account
 and Region, CloudFormation treats that alias as the extension's type name within the account and
 Region, not the type name of the public extension. For more information, see [Use
 aliases to refer to extensions](../UserGuide/registry-public.md#registry-public-enable-alias "../UserGuide/registry-public.md#registry-public-enable-alias") in the *AWS CloudFormation User Guide*.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: No




**PublicVersionNumber** 


For public extensions that have been activated for this account and Region, the version of
 the public extension to be used for CloudFormation operations in this account and Region.


How you specified `AutoUpdate` when enabling the extension affects whether
 CloudFormation automatically updates the extension in this account and Region when a new version is
 released. For more information, see [Automatically use new versions of extensions](../UserGuide/registry-public.md#registry-public-enable-auto "../UserGuide/registry-public.md#registry-public-enable-auto") in the
 *AWS CloudFormation User Guide*.


Type: String


Length Constraints: Minimum length of 5.


Pattern: `^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(.*)$`



Required: No




**PublisherId** 


The ID of the extension publisher, if the extension is published by a third party.
 Extensions published by Amazon don't return a publisher ID.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 40.


Pattern: `[0-9a-zA-Z]{12,40}`



Required: No




**PublisherIdentity** 


The service used to verify the publisher identity.


For more information, see [Publishing extensions to make
 them available for public use](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html") in the *AWS CloudFormation Command Line Interface (CLI) User Guide*.


Type: String


Valid Values: `AWS_Marketplace | GitHub | Bitbucket`



Required: No




**PublisherName** 


The publisher name, as defined in the public profile for that publisher in the service used
 to verify the publisher identity.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Pattern: `[\s\S]+`



Required: No




**Type** 


The kind of extension.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`



Required: No




**TypeArn** 


The ARN of the extension.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`



Required: No




**TypeName** 


The name of the extension.


If you specified a `TypeNameAlias` when you call the [ActivateType](API_ActivateType.md "API_ActivateType.md") API
 operation in your account and Region, CloudFormation considers that alias as the type name.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TypeSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/TypeSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TypeSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/TypeSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TypeSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/TypeSummary")
