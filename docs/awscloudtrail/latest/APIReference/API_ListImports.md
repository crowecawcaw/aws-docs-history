# ListImports

 Returns information on all imports, or a select set of imports by
 `ImportStatus` or `Destination`. 


## Request Syntax



```
{
   "Destination": "`string`",
   "ImportStatus": "`string`",
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[Destination](#API_ListImports_RequestSyntax "#API_ListImports_RequestSyntax")**


 The ARN of the destination event data store. 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: No




**[ImportStatus](#API_ListImports_RequestSyntax "#API_ListImports_RequestSyntax")**


 The status of the import. 


Type: String


Valid Values: `INITIALIZING | IN_PROGRESS | FAILED | STOPPED | COMPLETED`



Required: No




**[MaxResults](#API_ListImports_RequestSyntax "#API_ListImports_RequestSyntax")**


 The maximum number of imports to display on a single page. 


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 1000.


Required: No




**[NextToken](#API_ListImports_RequestSyntax "#API_ListImports_RequestSyntax")**


 A token you can use to get the next page of import results. 


Type: String


Length Constraints: Minimum length of 4. Maximum length of 1000.


Pattern: `.*`



Required: No




## Response Syntax



```
{
   "Imports": [ 
      { 
         "CreatedTimestamp": ***number***,
         "Destinations": [ "***string***" ],
         "ImportId": "***string***",
         "ImportStatus": "***string***",
         "UpdatedTimestamp": ***number***
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Imports](#API_ListImports_ResponseSyntax "#API_ListImports_ResponseSyntax")**


 The list of returned imports. 


Type: Array of [ImportsListItem](API_ImportsListItem.md "API_ImportsListItem.md") objects




**[NextToken](#API_ListImports_ResponseSyntax "#API_ListImports_ResponseSyntax")**


 A token you can use to get the next page of import results. 


Type: String


Length Constraints: Minimum length of 4. Maximum length of 1000.


Pattern: `.*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**EventDataStoreARNInvalidException** 


The specified event data store ARN is not valid or does not map to an event data store
 in your account.


HTTP Status Code: 400




**InvalidNextTokenException** 


A token that is not valid, or a token that was previously used in a request with
 different parameters. This exception is thrown if the token is not valid.


HTTP Status Code: 400




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListImports "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListImports")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/ListImports "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/ListImports")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListImports "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListImports")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListImports "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListImports")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListImports "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListImports")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListImports "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListImports")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListImports "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListImports")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListImports "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListImports")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListImports "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListImports")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListImports "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListImports")
