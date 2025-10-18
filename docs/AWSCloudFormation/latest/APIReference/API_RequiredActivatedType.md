# RequiredActivatedType

For extensions that are modules, a public third-party extension that must be activated in
 your account in order for the module itself to be activated.

For more information, see [Requirements for activating third-party public modules](../UserGuide/module-versioning.md#requirements-for-modules "../UserGuide/module-versioning.md#requirements-for-modules") in the
 *AWS CloudFormation User Guide*.


## Contents





**OriginalTypeName** 


The type name of the public extension.


If you specified a `TypeNameAlias` when enabling the extension in this account
 and Region, CloudFormation treats that alias as the extension's type name within the account and
 Region, not the type name of the public extension. For more information, see [Use
 aliases to refer to extensions](../UserGuide/registry-public.md#registry-public-enable-alias "../UserGuide/registry-public.md#registry-public-enable-alias") in the *AWS CloudFormation User Guide*.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: No




**PublisherId** 


The publisher ID of the extension publisher.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 40.


Pattern: `[0-9a-zA-Z]{12,40}`



Required: No




**SupportedMajorVersions.member.N** 


A list of the major versions of the extension type that the macro supports.


Type: Array of integers


Valid Range: Minimum value of 1. Maximum value of 65535.


Required: No




**TypeNameAlias** 


An alias assigned to the public extension, in this account and Region. If you specify an
 alias for the extension, CloudFormation treats the alias as the extension type name within this
 account and Region. You must use the alias to refer to the extension in your templates, API
 calls, and CloudFormation console.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RequiredActivatedType "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RequiredActivatedType")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RequiredActivatedType "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RequiredActivatedType")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RequiredActivatedType "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RequiredActivatedType")
