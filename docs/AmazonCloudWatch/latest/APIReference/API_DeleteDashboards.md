# DeleteDashboards

Deletes all dashboards that you specify. You can specify up to 100 dashboards to
 delete. If there is an error during this call, no dashboards are deleted.


## Request Parameters





**DashboardNames** 


The dashboards to be deleted. This parameter is required.


Type: Array of strings


Required: Yes




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ConflictException** 


This operation attempted to create a resource that already exists.


HTTP Status Code: 409




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DeleteDashboards "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DeleteDashboards")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DeleteDashboards "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DeleteDashboards")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DeleteDashboards "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DeleteDashboards")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DeleteDashboards "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DeleteDashboards")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteDashboards "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteDashboards")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DeleteDashboards "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DeleteDashboards")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DeleteDashboards "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DeleteDashboards")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DeleteDashboards "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DeleteDashboards")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteDashboards "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteDashboards")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteDashboards "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteDashboards")
