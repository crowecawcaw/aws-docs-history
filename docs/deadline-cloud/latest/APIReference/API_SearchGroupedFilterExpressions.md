# SearchGroupedFilterExpressions

The filter expression, `AND` or `OR`, to use
when searching among a group of search strings in a resource.

You can use two groupings per search each within parenthesis `()`.


## Contents





**filters** 


The filters to use for the search.


Type: Array of [SearchFilterExpression](API_SearchFilterExpression.md "API_SearchFilterExpression.md") objects


Array Members: Minimum number of 1 item. Maximum number of 3 items.


Required: Yes




**operator** 


The operators to include in the search.


Type: String


Valid Values: `AND | OR`



Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchGroupedFilterExpressions "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchGroupedFilterExpressions")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchGroupedFilterExpressions "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchGroupedFilterExpressions")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchGroupedFilterExpressions "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchGroupedFilterExpressions")
