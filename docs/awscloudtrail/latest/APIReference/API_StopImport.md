# StopImport

 Stops a specified import. 


## Request Syntax



```
{
   "ImportId": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[ImportId](#API_StopImport_RequestSyntax "#API_StopImport_RequestSyntax")**


 The ID of the import. 


Type: String


Length Constraints: Fixed length of 36.


Pattern: `^[a-f0-9\-]+$`



Required: Yes




## Response Syntax



```
{
   "CreatedTimestamp": ***number***,
   "Destinations": [ "***string***" ],
   "EndEventTime": ***number***,
   "ImportId": "***string***",
   "ImportSource": { 
      "S3": { 
         "S3BucketAccessRoleArn": "***string***",
         "S3BucketRegion": "***string***",
         "S3LocationUri": "***string***"
      }
   },
   "ImportStatistics": { 
      "EventsCompleted": ***number***,
      "FailedEntries": ***number***,
      "FilesCompleted": ***number***,
      "PrefixesCompleted": ***number***,
      "PrefixesFound": ***number***
   },
   "ImportStatus": "***string***",
   "StartEventTime": ***number***,
   "UpdatedTimestamp": ***number***
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[CreatedTimestamp](#API_StopImport_ResponseSyntax "#API_StopImport_ResponseSyntax")**


 The timestamp of the import's creation. 


Type: Timestamp




**[Destinations](#API_StopImport_ResponseSyntax "#API_StopImport_ResponseSyntax")**


 The ARN of the destination event data store. 


Type: Array of strings


Array Members: Fixed number of 1 item.


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`





**[EndEventTime](#API_StopImport_ResponseSyntax "#API_StopImport_ResponseSyntax")**


 Used with `StartEventTime` to bound a `StartImport` request, and
 limit imported trail events to only those events logged within a specified time period.
 


Type: Timestamp




**[ImportId](#API_StopImport_ResponseSyntax "#API_StopImport_ResponseSyntax")**


 The ID for the import. 


Type: String


Length Constraints: Fixed length of 36.


Pattern: `^[a-f0-9\-]+$`





**[ImportSource](#API_StopImport_ResponseSyntax "#API_StopImport_ResponseSyntax")**


 The source S3 bucket for the import. 


Type: [ImportSource](API_ImportSource.md "API_ImportSource.md") object




**[ImportStatistics](#API_StopImport_ResponseSyntax "#API_StopImport_ResponseSyntax")**


 Returns information on the stopped import. 


Type: [ImportStatistics](API_ImportStatistics.md "API_ImportStatistics.md") object




**[ImportStatus](#API_StopImport_ResponseSyntax "#API_StopImport_ResponseSyntax")**


 The status of the import. 


Type: String


Valid Values: `INITIALIZING | IN_PROGRESS | FAILED | STOPPED | COMPLETED`





**[StartEventTime](#API_StopImport_ResponseSyntax "#API_StopImport_ResponseSyntax")**


 Used with `EndEventTime` to bound a `StartImport` request, and
 limit imported trail events to only those events logged within a specified time period.
 


Type: Timestamp




**[UpdatedTimestamp](#API_StopImport_ResponseSyntax "#API_StopImport_ResponseSyntax")**


 The timestamp of the import's last update. 


Type: Timestamp




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ImportNotFoundException** 


 The specified import was not found. 


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/StopImport "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/StopImport")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/StopImport "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/StopImport")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/StopImport "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/StopImport")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/StopImport "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/StopImport")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/StopImport "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/StopImport")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/StopImport "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/StopImport")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/StopImport "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/StopImport")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/StopImport "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/StopImport")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/StopImport "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/StopImport")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/StopImport "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/StopImport")
