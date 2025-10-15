# LifecycleRuleFilter

The `Filter` is used to identify objects that a Lifecycle Rule applies to. A
 `Filter` can have exactly one of `Prefix`, `Tag`,
 `ObjectSizeGreaterThan`, `ObjectSizeLessThan`, or `And` specified. If
 the `Filter` element is left empty, the Lifecycle Rule applies to all objects in the
 bucket.


## Contents





**And** 


This is used in a Lifecycle Rule Filter to apply a logical AND to two or more predicates. The
 Lifecycle Rule will apply to any object matching all of the predicates configured inside the And
 operator.


Type: [LifecycleRuleAndOperator](API_LifecycleRuleAndOperator.md "API_LifecycleRuleAndOperator.md") data type


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

Replacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").


Type: String


Required: No




**Tag** 


This tag must exist in the object's tag set in order for the rule to apply.


###### Note

This parameter applies to general purpose buckets only. It is not supported for directory bucket
 lifecycle configurations.


Type: [Tag](API_Tag.md "API_Tag.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/LifecycleRuleFilter "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/LifecycleRuleFilter")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/LifecycleRuleFilter "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/LifecycleRuleFilter")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/LifecycleRuleFilter "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/LifecycleRuleFilter")
