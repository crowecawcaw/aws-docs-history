# GetDashboard


Returns the specified dashboard.



## Request Syntax



```
{
   "DashboardId": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[DashboardId](#API_GetDashboard_RequestSyntax "#API_GetDashboard_RequestSyntax")**



The name or ARN for the dashboard.



Type: String


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: Yes




## Response Syntax



```
{
   "CreatedTimestamp": ***number***,
   "DashboardArn": "***string***",
   "LastRefreshFailureReason": "***string***",
   "LastRefreshId": "***string***",
   "RefreshSchedule": { 
      "Frequency": { 
         "Unit": "***string***",
         "Value": ***number***
      },
      "Status": "***string***",
      "TimeOfDay": "***string***"
   },
   "Status": "***string***",
   "TerminationProtectionEnabled": ***boolean***,
   "Type": "***string***",
   "UpdatedTimestamp": ***number***,
   "Widgets": [ 
      { 
         "QueryAlias": "***string***",
         "QueryParameters": [ "***string***" ],
         "QueryStatement": "***string***",
         "ViewProperties": { 
            "***string***" : "***string***" 
         }
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[CreatedTimestamp](#API_GetDashboard_ResponseSyntax "#API_GetDashboard_ResponseSyntax")**



 The timestamp that shows when the dashboard was created.



Type: Timestamp




**[DashboardArn](#API_GetDashboard_ResponseSyntax "#API_GetDashboard_ResponseSyntax")**



 The ARN for the dashboard.



Type: String


Pattern: `^[a-zA-Z0-9._/\-:]+$`





**[LastRefreshFailureReason](#API_GetDashboard_ResponseSyntax "#API_GetDashboard_ResponseSyntax")**



Provides information about failures for the last scheduled refresh.



Type: String


Length Constraints: Minimum length of 4. Maximum length of 1000.


Pattern: `.*`





**[LastRefreshId](#API_GetDashboard_ResponseSyntax "#API_GetDashboard_ResponseSyntax")**



The ID of the last dashboard refresh.



Type: String


Length Constraints: Minimum length of 10. Maximum length of 20.


Pattern: `\d+`





**[RefreshSchedule](#API_GetDashboard_ResponseSyntax "#API_GetDashboard_ResponseSyntax")**



The refresh schedule for the dashboard, if configured.



Type: [RefreshSchedule](API_RefreshSchedule.md "API_RefreshSchedule.md") object




**[Status](#API_GetDashboard_ResponseSyntax "#API_GetDashboard_ResponseSyntax")**



The status of the dashboard.



Type: String


Valid Values: `CREATING | CREATED | UPDATING | UPDATED | DELETING`





**[TerminationProtectionEnabled](#API_GetDashboard_ResponseSyntax "#API_GetDashboard_ResponseSyntax")**



Indicates whether termination protection is enabled for the dashboard.



Type: Boolean




**[Type](#API_GetDashboard_ResponseSyntax "#API_GetDashboard_ResponseSyntax")**



The type of dashboard.



Type: String


Valid Values: `MANAGED | CUSTOM`





**[UpdatedTimestamp](#API_GetDashboard_ResponseSyntax "#API_GetDashboard_ResponseSyntax")**



 The timestamp that shows when the dashboard was last updated.



Type: Timestamp




**[Widgets](#API_GetDashboard_ResponseSyntax "#API_GetDashboard_ResponseSyntax")**



An array of widgets for the dashboard.



Type: Array of [Widget](API_Widget.md "API_Widget.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ResourceNotFoundException** 


This exception is thrown when the specified resource is not found.


HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/GetDashboard "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/GetDashboard")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/GetDashboard "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/GetDashboard")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/GetDashboard")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/GetDashboard")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/GetDashboard")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/GetDashboard")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/GetDashboard")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/GetDashboard")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/GetDashboard "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/GetDashboard")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/GetDashboard")
