# IntelligentTieringAndOperator

A container for specifying S3 Intelligent-Tiering filters. The filters determine the subset of
 objects to which the rule applies.


## Contents





**Prefix** 


An object key name prefix that identifies the subset of objects to which the configuration
 applies.


Type: String


Required: No




**Tags** 


All of these tags must exist in the object's tag set in order for the configuration to apply.


Type: Array of [Tag](API_Tag.md "API_Tag.md") data types


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/IntelligentTieringAndOperator "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/IntelligentTieringAndOperator")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/IntelligentTieringAndOperator "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/IntelligentTieringAndOperator")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/IntelligentTieringAndOperator "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/IntelligentTieringAndOperator")
