# ListImportFailures

 Returns a list of failures for the specified import. 


## Request Syntax



```
{
   "ImportId": "`string`",
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[ImportId](#API_ListImportFailures_RequestSyntax "#API_ListImportFailures_RequestSyntax")**


 The ID of the import. 


Type: String


Length Constraints: Fixed length of 36.


Pattern: `^[a-f0-9\-]+$`



Required: Yes




**[MaxResults](#API_ListImportFailures_RequestSyntax "#API_ListImportFailures_RequestSyntax")**


 The maximum number of failures to display on a single page. 


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 1000.


Required: No




**[NextToken](#API_ListImportFailures_RequestSyntax "#API_ListImportFailures_RequestSyntax")**


 A token you can use to get the next page of import failures. 


Type: String


Length Constraints: Minimum length of 4. Maximum length of 1000.


Pattern: `.*`



Required: No




## Response Syntax



```
{
   "Failures": [ 
      { 
         "ErrorMessage": "***string***",
         "ErrorType": "***string***",
         "LastUpdatedTime": ***number***,
         "Location": "***string***",
         "Status": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Failures](#API_ListImportFailures_ResponseSyntax "#API_ListImportFailures_ResponseSyntax")**


 Contains information about the import failures. 


Type: Array of [ImportFailureListItem](API_ImportFailureListItem.md "API_ImportFailureListItem.md") objects




**[NextToken](#API_ListImportFailures_ResponseSyntax "#API_ListImportFailures_ResponseSyntax")**


 A token you can use to get the next page of results. 


Type: String


Length Constraints: Minimum length of 4. Maximum length of 1000.


Pattern: `.*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListImportFailures "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListImportFailures")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/ListImportFailures "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/ListImportFailures")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListImportFailures "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListImportFailures")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListImportFailures "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListImportFailures")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListImportFailures "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListImportFailures")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListImportFailures "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListImportFailures")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListImportFailures "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListImportFailures")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListImportFailures "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListImportFailures")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListImportFailures "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListImportFailures")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListImportFailures "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListImportFailures")
