# InsightSelector

A JSON string that contains a list of Insights types that are logged on a trail or event data store.


## Contents





**InsightType** 


The type of Insights events to log on a trail or event data store. `ApiCallRateInsight` and
 `ApiErrorRateInsight` are valid Insight types.


The `ApiCallRateInsight` Insights type analyzes write-only
 management API calls that are aggregated per minute against a baseline API call volume.


The `ApiErrorRateInsight` Insights type analyzes management
 API calls that result in error codes. The error is shown if the API call is
 unsuccessful.


Type: String


Valid Values: `ApiCallRateInsight | ApiErrorRateInsight`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/InsightSelector "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/InsightSelector")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/InsightSelector "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/InsightSelector")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/InsightSelector "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/InsightSelector")
