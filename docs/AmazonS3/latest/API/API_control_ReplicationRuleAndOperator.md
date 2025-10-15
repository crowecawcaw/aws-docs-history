# ReplicationRuleAndOperator

A container for specifying rule filters. The filters determine the subset of objects to
 which the rule applies. This element is required only if you specify more than one filter. 

For example:


* If you specify both a `Prefix` and a `Tag` filter, wrap
 these filters in an `And` element.
* If you specify a filter based on multiple tags, wrap the `Tag` elements
 in an `And` element.

## Contents





**Prefix** 


An object key name prefix that identifies the subset of objects that the rule applies
 to.


Type: String


Required: No




**Tags** 


An array of tags that contain key and value pairs.


Type: Array of [S3Tag](API_control_S3Tag.md "API_control_S3Tag.md") data types


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ReplicationRuleAndOperator "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ReplicationRuleAndOperator")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ReplicationRuleAndOperator "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ReplicationRuleAndOperator")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ReplicationRuleAndOperator "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ReplicationRuleAndOperator")
