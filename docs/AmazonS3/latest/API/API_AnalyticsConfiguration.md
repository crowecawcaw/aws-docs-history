# AnalyticsConfiguration

Specifies the configuration and any analyses for the analytics filter of an Amazon S3 bucket.


## Contents





**Id** 


The ID that identifies the analytics configuration.


Type: String


Required: Yes




**StorageClassAnalysis** 


 Contains data related to access patterns to be collected and made available to analyze the
 tradeoffs between different storage classes. 


Type: [StorageClassAnalysis](API_StorageClassAnalysis.md "API_StorageClassAnalysis.md") data type


Required: Yes




**Filter** 


The filter used to describe a set of objects for analyses. A filter must have exactly one prefix,
 one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be
 considered in any analysis.


Type: [AnalyticsFilter](API_AnalyticsFilter.md "API_AnalyticsFilter.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AnalyticsConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AnalyticsConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AnalyticsConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AnalyticsConfiguration")
