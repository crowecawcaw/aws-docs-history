# IntelligentTieringFilter

The `Filter` is used to identify objects that the S3 Intelligent-Tiering configuration
 applies to.


## Contents





**And** 


A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The
 operator must have at least two predicates, and an object must match all of the predicates in order for
 the filter to apply.


Type: [IntelligentTieringAndOperator](API_IntelligentTieringAndOperator.md "API_IntelligentTieringAndOperator.md") data type


Required: No




**Prefix** 


An object key name prefix that identifies the subset of objects to which the rule applies.


###### Important

Replacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").


Type: String


Required: No




**Tag** 


A container of a key value name pair.


Type: [Tag](API_Tag.md "API_Tag.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/IntelligentTieringFilter "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/IntelligentTieringFilter")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/IntelligentTieringFilter "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/IntelligentTieringFilter")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/IntelligentTieringFilter "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/IntelligentTieringFilter")
