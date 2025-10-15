# ReplicationRuleFilter

A filter that identifies the subset of objects to which the replication rule applies. A
 `Filter` element must specify exactly one `Prefix`,
 `Tag`, or `And` child element.


## Contents





**And** 


A container for specifying rule filters. The filters determine the subset of objects
 that the rule applies to. This element is required only if you specify more than one
 filter. For example: 



* If you specify both a `Prefix` and a `Tag` filter, wrap
 these filters in an `And` element.
* If you specify a filter based on multiple tags, wrap the `Tag` elements
 in an `And` element.

Type: [ReplicationRuleAndOperator](API_control_ReplicationRuleAndOperator.md "API_control_ReplicationRuleAndOperator.md") data type


Required: No




**Prefix** 


An object key name prefix that identifies the subset of objects that the rule applies
 to.


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



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ReplicationRuleFilter "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ReplicationRuleFilter")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ReplicationRuleFilter "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ReplicationRuleFilter")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ReplicationRuleFilter "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ReplicationRuleFilter")
