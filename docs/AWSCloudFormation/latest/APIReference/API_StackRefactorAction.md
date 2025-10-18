# StackRefactorAction

Describes the stack and the action that CloudFormation will perform on it if you execute the
 stack refactor.


## Contents





**Action** 


The action that CloudFormation takes on the stack.


Type: String


Valid Values: `MOVE | CREATE`



Required: No




**Description** 


A description to help you identify the refactor.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**Detection** 


The detection type is one of the following:



* Auto: CloudFormation figured out the mapping on its own.
* Manual: The customer provided the mapping in the `ResourceMapping`
 parameter.

Type: String


Valid Values: `AUTO | MANUAL`



Required: No




**DetectionReason** 


The description of the detection type.


Type: String


Required: No




**Entity** 


The type that will be evaluated in the `StackRefactorAction`. The following are
 potential `Entity` types:



* `Stack`
* `Resource`

Type: String


Valid Values: `RESOURCE | STACK`



Required: No




**PhysicalResourceId** 


The name or unique identifier associated with the physical instance of the resource.


Type: String


Required: No




**ResourceIdentifier** 


A key-value pair that identifies the target resource. The key is an identifier property (for
 example, `BucketName` for `AWS::S3::Bucket` resources) and the value is the
 actual property value (for example, `MyS3Bucket`).


Type: String


Required: No




**ResourceMapping** 


The mapping for the stack resource `Source` and stack resource
 `Destination`.


Type: [ResourceMapping](API_ResourceMapping.md "API_ResourceMapping.md") object


Required: No




**TagResources.member.N** 


Assigns one or more tags to specified resources.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




**UntagResources.member.N** 


Removes one or more tags to specified resources.


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 128.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackRefactorAction "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackRefactorAction")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackRefactorAction "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackRefactorAction")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackRefactorAction "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackRefactorAction")
