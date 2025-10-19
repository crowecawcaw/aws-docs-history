# GetDashboard

Displays the details of the dashboard that you specify.

To copy an existing dashboard, use `GetDashboard`, and then use the data
 returned within `DashboardBody` as the template for the new dashboard when
 you call `PutDashboard` to create the copy.


## Request Parameters





**DashboardName** 


The name of the dashboard to be described.


Type: String


Required: Yes




## Response Elements


The following elements are returned by the service.





**DashboardArn** 


The Amazon Resource Name (ARN) of the dashboard.


Type: String




**DashboardBody** 


The detailed information about the dashboard, including what widgets are included
 and their location on the dashboard. For more information about the
 `DashboardBody` syntax, see [Dashboard Body Structure and Syntax](CloudWatch-Dashboard-Body-Structure.md "CloudWatch-Dashboard-Body-Structure.md"). 


Type: String




**DashboardName** 


The name of the dashboard.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InternalServiceError** 


Request processing has failed due to some unknown error, exception, or
 failure.





**Message** 





HTTP Status Code: 500




**InvalidParameterValue** 


The value of an input parameter is bad or out-of-range.





**message** 





HTTP Status Code: 400




**ResourceNotFound** 


The specified dashboard does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetDashboard "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetDashboard")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/GetDashboard "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/GetDashboard")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetDashboard")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetDashboard")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetDashboard")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetDashboard")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetDashboard")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetDashboard")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetDashboard "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetDashboard")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetDashboard "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetDashboard")
