# LifecycleRuleFilter

The container for the filter of the lifecycle rule.


## Contents





**And** 


The container for the `AND` condition for the lifecycle rule.


Type: [LifecycleRuleAndOperator](API_control_LifecycleRuleAndOperator.md "API_control_LifecycleRuleAndOperator.md") data type


Required: No




**ObjectSizeGreaterThan** 


Minimum object size to which the rule applies.


Type: Long


Required: No




**ObjectSizeLessThan** 


Maximum object size to which the rule applies.


Type: Long


Required: No




**Prefix** 


Prefix identifying one or more objects to which the rule applies.


###### Important

When you're using XML requests, you must 
replace special characters (such as carriage returns) in object keys with their equivalent XML entity codes. 
For more information, see [XML-related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints") in the *Amazon S3 User Guide*.


Type: String


Required: No




**Tag** 


A container for a key-value name pair.


Type: [S3Tag](API_control_S3Tag.md "API_control_S3Tag.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/LifecycleRuleFilter "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/LifecycleRuleFilter")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/LifecycleRuleFilter "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/LifecycleRuleFilter")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/LifecycleRuleFilter "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/LifecycleRuleFilter")
