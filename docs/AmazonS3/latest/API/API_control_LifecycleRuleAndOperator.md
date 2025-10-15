# LifecycleRuleAndOperator

The container for the Outposts bucket lifecycle rule and operator.


## Contents





**ObjectSizeGreaterThan** 


The non-inclusive minimum object size for the lifecycle rule. Setting this property to 7
 means the rule applies to objects with a size that is greater than 7. 


Type: Long


Required: No




**ObjectSizeLessThan** 


The non-inclusive maximum object size for the lifecycle rule. Setting this property to
 77 means the rule applies to objects with a size that is less than 77. 


Type: Long


Required: No




**Prefix** 


Prefix identifying one or more objects to which the rule applies.


Type: String


Required: No




**Tags** 


All of these tags must exist in the object's tag set in order for the rule to
 apply.


Type: Array of [S3Tag](API_control_S3Tag.md "API_control_S3Tag.md") data types


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/LifecycleRuleAndOperator "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/LifecycleRuleAndOperator")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/LifecycleRuleAndOperator "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/LifecycleRuleAndOperator")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/LifecycleRuleAndOperator "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/LifecycleRuleAndOperator")
