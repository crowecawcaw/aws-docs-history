# SearchFilterExpression

The type of search filter to apply.


## Contents


###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.





**dateTimeFilter** 


Filters based on date and time.


Type: [DateTimeFilterExpression](API_DateTimeFilterExpression.md "API_DateTimeFilterExpression.md") object


Required: No




**groupFilter** 


Filters by group.


Type: [SearchGroupedFilterExpressions](API_SearchGroupedFilterExpressions.md "API_SearchGroupedFilterExpressions.md") object


Required: No




**parameterFilter** 


Filters by parameter.


Type: [ParameterFilterExpression](API_ParameterFilterExpression.md "API_ParameterFilterExpression.md") object


Required: No




**searchTermFilter** 


Filters by a specified search term.


Type: [SearchTermFilterExpression](API_SearchTermFilterExpression.md "API_SearchTermFilterExpression.md") object


Required: No




**stringFilter** 


Filters by a string.


Type: [StringFilterExpression](API_StringFilterExpression.md "API_StringFilterExpression.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchFilterExpression "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchFilterExpression")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchFilterExpression "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchFilterExpression")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchFilterExpression "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchFilterExpression")
