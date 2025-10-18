# ChangeSetHook

Specifies the resource, the Hook, and the Hook version to be
 invoked.


## Contents





**FailureMode** 


Specify the Hook failure mode for non-compliant resources in the followings
 ways.



* `FAIL` Stops provisioning resources.
* `WARN` Allows provisioning to continue with a warning message.

Type: String


Valid Values: `FAIL | WARN`



Required: No




**InvocationPoint** 


The specific point in the provisioning process where the Hook is invoked.


Type: String


Valid Values: `PRE_PROVISION`



Required: No




**TargetDetails** 


Specifies details about the target that the Hook will run against.


Type: [ChangeSetHookTargetDetails](API_ChangeSetHookTargetDetails.md "API_ChangeSetHookTargetDetails.md") object


Required: No




**TypeConfigurationVersionId** 


The version ID of the type configuration.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[A-Za-z0-9-]+`



Required: No




**TypeName** 


The unique name for your Hook. Specifies a three-part namespace for your
 Hook, with a recommended pattern of `Organization::Service::Hook`.


###### Note

The following organization namespaces are reserved and can't be used in your Hook
 type names:


* `Alexa`
* `AMZN`
* `Amazon`
* `ASK`
* `AWS`
* `Custom`
* `Dev`

Type: String


Length Constraints: Minimum length of 10. Maximum length of 196.


Required: No




**TypeVersionId** 


The version ID of the type specified.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[A-Za-z0-9-]+`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ChangeSetHook "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ChangeSetHook")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ChangeSetHook "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ChangeSetHook")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ChangeSetHook "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ChangeSetHook")
