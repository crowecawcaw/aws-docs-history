# SearchSampleQueries


 Searches sample queries and returns a list of sample queries that are sorted by relevance. 
 To search for sample queries, provide a natural language `SearchPhrase` in English.
 


## Request Syntax



```
{
   "MaxResults": `number`,
   "NextToken": "`string`",
   "SearchPhrase": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[MaxResults](#API_SearchSampleQueries_RequestSyntax "#API_SearchSampleQueries_RequestSyntax")**



 The maximum number of results to return on a single page. The default value is 10.
 


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 50.


Required: No




**[NextToken](#API_SearchSampleQueries_RequestSyntax "#API_SearchSampleQueries_RequestSyntax")**



 A token you can use to get the next page of results. The length constraint is in characters, not words.
 


Type: String


Length Constraints: Minimum length of 4. Maximum length of 1000.


Pattern: `.*`



Required: No




**[SearchPhrase](#API_SearchSampleQueries_RequestSyntax "#API_SearchSampleQueries_RequestSyntax")**



 The natural language phrase to use for the semantic search. The phrase must be in English. The length constraint is in characters, not words.


Type: String


Length Constraints: Minimum length of 2. Maximum length of 1000.


Pattern: `^[ -~\n]*$`



Required: Yes




## Response Syntax



```
{
   "NextToken": "***string***",
   "SearchResults": [ 
      { 
         "Description": "***string***",
         "Name": "***string***",
         "Relevance": ***number***,
         "SQL": "***string***"
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[NextToken](#API_SearchSampleQueries_ResponseSyntax "#API_SearchSampleQueries_ResponseSyntax")**



 A token you can use to get the next page of results.


Type: String


Length Constraints: Minimum length of 4. Maximum length of 1000.


Pattern: `.*`





**[SearchResults](#API_SearchSampleQueries_ResponseSyntax "#API_SearchSampleQueries_ResponseSyntax")**



 A list of objects containing the search results ordered from most relevant to least relevant.
 


Type: Array of [SearchSampleQueriesSearchResult](API_SearchSampleQueriesSearchResult.md "API_SearchSampleQueriesSearchResult.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidParameterException** 


The request includes a parameter that is not valid.


HTTP Status Code: 400




**OperationNotPermittedException** 


This exception is thrown when the requested operation is not permitted.


HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/SearchSampleQueries "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/SearchSampleQueries")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/SearchSampleQueries "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/SearchSampleQueries")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/SearchSampleQueries "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/SearchSampleQueries")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/SearchSampleQueries "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/SearchSampleQueries")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/SearchSampleQueries "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/SearchSampleQueries")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/SearchSampleQueries "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/SearchSampleQueries")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/SearchSampleQueries "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/SearchSampleQueries")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/SearchSampleQueries "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/SearchSampleQueries")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/SearchSampleQueries "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/SearchSampleQueries")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/SearchSampleQueries "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/SearchSampleQueries")
