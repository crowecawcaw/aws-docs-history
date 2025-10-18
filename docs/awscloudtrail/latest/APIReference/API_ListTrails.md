# ListTrails

Lists trails that are in the current account.


## Request Syntax



```
{
   "NextToken": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[NextToken](#API_ListTrails_RequestSyntax "#API_ListTrails_RequestSyntax")**


The token to use to get the next page of results after a previous API call. This token
 must be passed in with the same parameters that were specified in the original call. For
 example, if the original call specified an AttributeKey of 'Username' with a value of
 'root', the call with NextToken should include those same parameters.


Type: String


Required: No




## Response Syntax



```
{
   "NextToken": "***string***",
   "Trails": [ 
      { 
         "HomeRegion": "***string***",
         "Name": "***string***",
         "TrailARN": "***string***"
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[NextToken](#API_ListTrails_ResponseSyntax "#API_ListTrails_ResponseSyntax")**


The token to use to get the next page of results after a previous API call. If the token
 does not appear, there are no more results to return. The token must be passed in with the
 same parameters as the previous call. For example, if the original call specified an
 AttributeKey of 'Username' with a value of 'root', the call with NextToken should include
 those same parameters.


Type: String




**[Trails](#API_ListTrails_ResponseSyntax "#API_ListTrails_ResponseSyntax")**


Returns the name, ARN, and home Region of trails in the current account.


Type: Array of [TrailInfo](API_TrailInfo.md "API_TrailInfo.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**OperationNotPermittedException** 


This exception is thrown when the requested operation is not permitted.


HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListTrails "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListTrails")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/ListTrails "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/ListTrails")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListTrails "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListTrails")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListTrails "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListTrails")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListTrails "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListTrails")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListTrails "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListTrails")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListTrails "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListTrails")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListTrails "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListTrails")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListTrails "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListTrails")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListTrails "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListTrails")
