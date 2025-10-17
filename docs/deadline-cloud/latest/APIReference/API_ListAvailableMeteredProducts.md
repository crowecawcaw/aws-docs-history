# ListAvailableMeteredProducts

A list of the available metered products.


## Request Syntax



```
GET /2023-10-12/metered-products?maxResults=`maxResults`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[maxResults](#API_ListAvailableMeteredProducts_RequestSyntax "#API_ListAvailableMeteredProducts_RequestSyntax")**


The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.


Valid Range: Minimum value of 1. Maximum value of 100.




**[nextToken](#API_ListAvailableMeteredProducts_RequestSyntax "#API_ListAvailableMeteredProducts_RequestSyntax")**


The token for the next set of results, or `null` to start from the beginning.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "meteredProducts": [ 
      { 
         "family": "***string***",
         "port": ***number***,
         "productId": "***string***",
         "vendor": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[meteredProducts](#API_ListAvailableMeteredProducts_ResponseSyntax "#API_ListAvailableMeteredProducts_ResponseSyntax")**


The metered products.


Type: Array of [MeteredProductSummary](API_MeteredProductSummary.md "API_MeteredProductSummary.md") objects




**[nextToken](#API_ListAvailableMeteredProducts_ResponseSyntax "#API_ListAvailableMeteredProducts_ResponseSyntax")**


If Deadline Cloud returns `nextToken`, then there are more results available. The value of `nextToken` is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then `nextToken` is set to `null`. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 `ValidationException` error.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InternalServerErrorException** 


Deadline Cloud can't process your request right now. Try again later.





**retryAfterSeconds** 


The number of seconds a client should wait before retrying the request.




HTTP Status Code: 500




**ThrottlingException** 


Your request exceeded a request rate quota.





**context** 


Information about the resources in use when the exception was thrown.




**quotaCode** 


Identifies the quota that is being throttled.




**retryAfterSeconds** 


The number of seconds a client should wait before retrying the request.




**serviceCode** 


Identifies the service that is being throttled.




HTTP Status Code: 429




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/ListAvailableMeteredProducts "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/ListAvailableMeteredProducts")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/ListAvailableMeteredProducts "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/ListAvailableMeteredProducts")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ListAvailableMeteredProducts "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ListAvailableMeteredProducts")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/ListAvailableMeteredProducts "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/ListAvailableMeteredProducts")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ListAvailableMeteredProducts "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ListAvailableMeteredProducts")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/ListAvailableMeteredProducts "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/ListAvailableMeteredProducts")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/ListAvailableMeteredProducts "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/ListAvailableMeteredProducts")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/ListAvailableMeteredProducts "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/ListAvailableMeteredProducts")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/ListAvailableMeteredProducts "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/ListAvailableMeteredProducts")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ListAvailableMeteredProducts "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ListAvailableMeteredProducts")
