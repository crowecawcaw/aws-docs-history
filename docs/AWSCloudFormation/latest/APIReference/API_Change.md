# Change

The `Change` structure describes the changes CloudFormation will perform if you
 execute the change set.


## Contents





**HookInvocationCount** 


Is either `null`, if no Hooks invoke for the resource, or contains the number
 of Hooks that will invoke for the resource.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 100.


Required: No




**ResourceChange** 


A `ResourceChange` structure that describes the resource and action that
 CloudFormation will perform.


Type: [ResourceChange](API_ResourceChange.md "API_ResourceChange.md") object


Required: No




**Type** 


The type of entity that CloudFormation changes.



* `Resource` This change is for a resource.

Type: String


Valid Values: `Resource`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/Change "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/Change")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/Change "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/Change")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/Change "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/Change")
