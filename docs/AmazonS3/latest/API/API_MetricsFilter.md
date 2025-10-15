# MetricsFilter

Specifies a metrics configuration filter. The metrics configuration only includes objects that meet
 the filter's criteria. A filter must be a prefix, an object tag, an access point ARN, or a conjunction
 (MetricsAndOperator). For more information, see [PutBucketMetricsConfiguration](API_PutBucketMetricsConfiguration.md "API_PutBucketMetricsConfiguration.md").


## Contents





**AccessPointArn** 


The access point ARN used when evaluating a metrics filter.


Type: String


Required: No




**And** 


A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The
 operator must have at least two predicates, and an object must match all of the predicates in order for
 the filter to apply.


Type: [MetricsAndOperator](API_MetricsAndOperator.md "API_MetricsAndOperator.md") data type


Required: No




**Prefix** 


The prefix used when evaluating a metrics filter.


Type: String


Required: No




**Tag** 


The tag used when evaluating a metrics filter.


Type: [Tag](API_Tag.md "API_Tag.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/MetricsFilter "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/MetricsFilter")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/MetricsFilter "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/MetricsFilter")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/MetricsFilter "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/MetricsFilter")
