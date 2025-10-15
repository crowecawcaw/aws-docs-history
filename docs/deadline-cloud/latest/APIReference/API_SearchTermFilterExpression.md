# SearchTermFilterExpression

Searches for a particular search term.


## Contents





**searchTerm** 


The term to search for.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: Yes




**matchType** 


Specifies how Deadline Cloud matches your search term in the results. If you don't
 specify a `matchType` the default is `FUZZY_MATCH`.



* `FUZZY_MATCH` - Matches if a portion of the search term is found in the
 result.
* `CONTAINS` - Matches if the exact search term is contained in the
 result.

Type: String


Valid Values: `FUZZY_MATCH | CONTAINS`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchTermFilterExpression "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchTermFilterExpression")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchTermFilterExpression "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchTermFilterExpression")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchTermFilterExpression "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchTermFilterExpression")
