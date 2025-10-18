# GenerateQuery


 Generates a query from a natural language prompt. This operation uses generative artificial intelligence
 (generative AI) to produce a ready-to-use SQL query from the prompt.
 

The prompt can be a question or a statement about the event data
 in your event data store. For example, you can enter prompts like "What are my
 top errors in the past month?" and “Give me a list of users that used SNS.”

The prompt must be in English. For information about limitations, permissions, and supported Regions, see 
 [Create CloudTrail Lake queries from natural language prompts](../userguide/lake-query-generator.md "../userguide/lake-query-generator.md") 
 in the *AWS CloudTrail*  user guide.

###### Note

Do not include any personally identifying, confidential, or sensitive information
 in your prompts.

This feature uses generative AI large language models (LLMs); we recommend double-checking the
 LLM response.


## Request Syntax



```
{
   "EventDataStores": [ "`string`" ],
   "Prompt": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[EventDataStores](#API_GenerateQuery_RequestSyntax "#API_GenerateQuery_RequestSyntax")**



 The ARN (or ID suffix of the ARN) of the event data store
 that you want to query. You can only specify one event data store.
 


Type: Array of strings


Array Members: Fixed number of 1 item.


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: Yes




**[Prompt](#API_GenerateQuery_RequestSyntax "#API_GenerateQuery_RequestSyntax")**



 The prompt that you want to use to generate the query. The prompt must be in English. For example prompts, see 
 [Example prompts](../userguide/lake-query-generator.md#lake-query-generator-examples "../userguide/lake-query-generator.md#lake-query-generator-examples") 
 in the *AWS CloudTrail*  user guide.
 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 500.


Pattern: `^[ -~\n]*$`



Required: Yes




## Response Syntax



```
{
   "EventDataStoreOwnerAccountId": "***string***",
   "QueryAlias": "***string***",
   "QueryStatement": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[EventDataStoreOwnerAccountId](#API_GenerateQuery_ResponseSyntax "#API_GenerateQuery_ResponseSyntax")**



 The account ID of the event data store owner.



Type: String


Length Constraints: Minimum length of 12. Maximum length of 16.


Pattern: `\d+`





**[QueryAlias](#API_GenerateQuery_ResponseSyntax "#API_GenerateQuery_ResponseSyntax")**



 An alias that identifies the prompt. When you run the `StartQuery` operation, you can pass in either the `QueryAlias` or 
 `QueryStatement` parameter.
 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Pattern: `^[a-zA-Z][a-zA-Z0-9._\-]*$`





**[QueryStatement](#API_GenerateQuery_ResponseSyntax "#API_GenerateQuery_ResponseSyntax")**



 The SQL query statement generated from the prompt.
 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 10000.


Pattern: `(?s).*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**EventDataStoreARNInvalidException** 


The specified event data store ARN is not valid or does not map to an event data store
 in your account.


HTTP Status Code: 400




**EventDataStoreNotFoundException** 


The specified event data store was not found.


HTTP Status Code: 400




**GenerateResponseException** 



 This exception is thrown when a valid query could not be generated for the provided prompt. 
 


HTTP Status Code: 400




**InactiveEventDataStoreException** 


The event data store is inactive.


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




## Examples


### Example


The following example provides the prompt `"Show me all console login events for the past week"` to generate a query for the specified event data store.



```
{
   "EventDataStores": [ "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-ee54-4813-92d5-999aeEXAMPLE" ],
   "Prompt": "Show me all console login events for the past week"
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/GenerateQuery "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/GenerateQuery")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/GenerateQuery "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/GenerateQuery")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/GenerateQuery "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/GenerateQuery")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/GenerateQuery "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/GenerateQuery")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/GenerateQuery "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/GenerateQuery")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/GenerateQuery "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/GenerateQuery")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/GenerateQuery "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/GenerateQuery")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/GenerateQuery "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/GenerateQuery")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/GenerateQuery "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/GenerateQuery")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/GenerateQuery "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/GenerateQuery")
