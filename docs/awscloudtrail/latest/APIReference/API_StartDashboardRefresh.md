# StartDashboardRefresh


Starts a refresh of the specified dashboard.



 Each time a dashboard is refreshed, CloudTrail runs queries to populate the dashboard's widgets. CloudTrail must be granted permissions to run the `StartQuery` operation on your behalf. To provide permissions, run the `PutResourcePolicy` operation to attach a resource-based policy to each event data store. For more information, 
 see [Example: Allow CloudTrail to run queries to populate a dashboard](../userguide/security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard "../userguide/security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard") in the *AWS CloudTrail User Guide*.



## Request Syntax



```
{
   "DashboardId": "`string`",
   "QueryParameterValues": { 
      "`string`" : "`string`" 
   }
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[DashboardId](#API_StartDashboardRefresh_RequestSyntax "#API_StartDashboardRefresh_RequestSyntax")**



The name or ARN of the dashboard.



Type: String


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: Yes




**[QueryParameterValues](#API_StartDashboardRefresh_RequestSyntax "#API_StartDashboardRefresh_RequestSyntax")**



 The query parameter values for the dashboard



For custom dashboards, the following query parameters are valid: `$StartTime$`, `$EndTime$`, and `$Period$`.


For managed dashboards, the following query parameters are valid: `$StartTime$`,
 `$EndTime$`, `$Period$`, and `$EventDataStoreId$`. The
 `$EventDataStoreId$` query parameter is required.


Type: String to string map


Key Length Constraints: Minimum length of 3. Maximum length of 128.


Key Pattern: `^[a-zA-Z0-9._/\-:$]+$`



Value Length Constraints: Minimum length of 1. Maximum length of 128.


Value Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: No




## Response Syntax



```
{
   "RefreshId": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[RefreshId](#API_StartDashboardRefresh_ResponseSyntax "#API_StartDashboardRefresh_ResponseSyntax")**



The refresh ID for the dashboard.



Type: String


Length Constraints: Minimum length of 10. Maximum length of 20.


Pattern: `\d+`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**EventDataStoreNotFoundException** 


The specified event data store was not found.


HTTP Status Code: 400




**InactiveEventDataStoreException** 


The event data store is inactive.


HTTP Status Code: 400




**ResourceNotFoundException** 


This exception is thrown when the specified resource is not found.


HTTP Status Code: 400




**ServiceQuotaExceededException** 



 This exception is thrown when the quota is exceeded. For information about CloudTrail quotas, see [Service quotas](https://docs.aws.amazon.com/general/latest/gr/ct.html#limits_cloudtrail "https://docs.aws.amazon.com/general/latest/gr/ct.html#limits_cloudtrail") 
 in the *AWS General Reference*.



HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## Examples


### Example


The following example refreshes a managed dashboard. Because managed dashboards are configured by CloudTrail, 
 the refresh request needs to include the ID of the event data store that the queries will run on.



```
{
  "DashboardId": "AWSCloudTrail-Overview",
  "QueryParameterValues": {
      "$StartTime$": "2024-11-13T08:00:00.00Z",
      "$EndTime$": "2024-11-13T12:00:00.00Z",
      "$Period$": "minute",
      "$EventDataStoreId$": "<eds-id>"
  }
}
```

### Example


The following example refreshes a custom dashboard named `AccountActivityDashboard`.



```
{
  "DashboardId": "AccountActivityDashboard",
  "QueryParameterValues": {
      "$StartTime$": "2024-11-13T08:00:00.00Z",
      "$EndTime$": "2024-11-13T12:00:00.00Z",
      "$Period$": "minute"
  }
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/StartDashboardRefresh "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/StartDashboardRefresh")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/StartDashboardRefresh "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/StartDashboardRefresh")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/StartDashboardRefresh "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/StartDashboardRefresh")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/StartDashboardRefresh "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/StartDashboardRefresh")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/StartDashboardRefresh "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/StartDashboardRefresh")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/StartDashboardRefresh "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/StartDashboardRefresh")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/StartDashboardRefresh "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/StartDashboardRefresh")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/StartDashboardRefresh "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/StartDashboardRefresh")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/StartDashboardRefresh "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/StartDashboardRefresh")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/StartDashboardRefresh "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/StartDashboardRefresh")
