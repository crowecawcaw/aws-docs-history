# DeleteDashboard


Deletes the specified dashboard. You cannot delete a dashboard that has termination protection enabled.



## Request Syntax



```
{
   "DashboardId": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[DashboardId](#API_DeleteDashboard_RequestSyntax "#API_DeleteDashboard_RequestSyntax")**



The name or ARN for the dashboard.



Type: String


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: Yes




## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ConflictException** 


This exception is thrown when the specified resource is not ready for an operation. This
 can occur when you try to run an operation on a resource before CloudTrail has time
 to fully load the resource, or because another operation is modifying the resource. If this exception occurs, wait a few minutes, and then try the
 operation again.


HTTP Status Code: 400




**ResourceNotFoundException** 


This exception is thrown when the specified resource is not found.


HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DeleteDashboard "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DeleteDashboard")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/DeleteDashboard "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/DeleteDashboard")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DeleteDashboard "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DeleteDashboard")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DeleteDashboard "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DeleteDashboard")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DeleteDashboard "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DeleteDashboard")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DeleteDashboard "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DeleteDashboard")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DeleteDashboard "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DeleteDashboard")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DeleteDashboard "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DeleteDashboard")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DeleteDashboard "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DeleteDashboard")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DeleteDashboard "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DeleteDashboard")
