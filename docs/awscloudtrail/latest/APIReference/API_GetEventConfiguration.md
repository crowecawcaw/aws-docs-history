# GetEventConfiguration

Retrieves the current event configuration settings for the specified event data store, including details 
 about maximum event size and context key selectors configured for the event data store.


## Request Syntax



```
{
   "EventDataStore": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[EventDataStore](#API_GetEventConfiguration_RequestSyntax "#API_GetEventConfiguration_RequestSyntax")**


The Amazon Resource Name (ARN) or ID suffix of the ARN of the event data store for which you want to retrieve event configuration settings.


Type: String


Required: No




## Response Syntax



```
{
   "ContextKeySelectors": [ 
      { 
         "Equals": [ "***string***" ],
         "Type": "***string***"
      }
   ],
   "EventDataStoreArn": "***string***",
   "MaxEventSize": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[ContextKeySelectors](#API_GetEventConfiguration_ResponseSyntax "#API_GetEventConfiguration_ResponseSyntax")**


The list of context key selectors that are configured for the event data store.


Type: Array of [ContextKeySelector](API_ContextKeySelector.md "API_ContextKeySelector.md") objects


Array Members: Maximum number of 2 items.




**[EventDataStoreArn](#API_GetEventConfiguration_ResponseSyntax "#API_GetEventConfiguration_ResponseSyntax")**


The Amazon Resource Name (ARN) or ID suffix of the ARN of the event data store for which the event configuration settings are returned.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`





**[MaxEventSize](#API_GetEventConfiguration_ResponseSyntax "#API_GetEventConfiguration_ResponseSyntax")**


The maximum allowed size for events stored in the specified event data store.


Type: String


Valid Values: `Standard | Large`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CloudTrailARNInvalidException** 


This exception is thrown when an operation is called with an ARN that is not valid.


The following is the format of a trail ARN: `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`



The following is the format of an event data store ARN:
 `arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`



The following is the format of a dashboard ARN: `arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash`



The following is the format of a channel ARN:
 `arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890`



HTTP Status Code: 400




**EventDataStoreARNInvalidException** 


The specified event data store ARN is not valid or does not map to an event data store
 in your account.


HTTP Status Code: 400




**EventDataStoreNotFoundException** 


The specified event data store was not found.


HTTP Status Code: 400




**InvalidEventDataStoreCategoryException** 


This exception is thrown when event categories of specified event data stores are not
 valid.


HTTP Status Code: 400




**InvalidEventDataStoreStatusException** 


The event data store is not in a status that supports the operation.


HTTP Status Code: 400




**InvalidParameterCombinationException** 


This exception is thrown when the combination of parameters provided is not
 valid.


HTTP Status Code: 400




**InvalidParameterException** 


The request includes a parameter that is not valid.


HTTP Status Code: 400




**NoManagementAccountSLRExistsException** 


 This exception is thrown when the management account does not have a service-linked
 role. 


HTTP Status Code: 400




**OperationNotPermittedException** 


This exception is thrown when the requested operation is not permitted.


HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/GetEventConfiguration "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/GetEventConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/GetEventConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/GetEventConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/GetEventConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/GetEventConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/GetEventConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/GetEventConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/GetEventConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/GetEventConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/GetEventConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/GetEventConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/GetEventConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/GetEventConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/GetEventConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/GetEventConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/GetEventConfiguration "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/GetEventConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/GetEventConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/GetEventConfiguration")
