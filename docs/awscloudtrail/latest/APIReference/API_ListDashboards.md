# ListDashboards


 Returns information about all dashboards in the account, in the current Region.



## Request Syntax



```
{
   "MaxResults": `number`,
   "NamePrefix": "`string`",
   "NextToken": "`string`",
   "Type": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[MaxResults](#API_ListDashboards_RequestSyntax "#API_ListDashboards_RequestSyntax")**



 The maximum number of dashboards to display on a single page.



Type: Integer


Valid Range: Minimum value of 1. Maximum value of 1000.


Required: No




**[NamePrefix](#API_ListDashboards_RequestSyntax "#API_ListDashboards_RequestSyntax")**



Specify a name prefix to filter on.



Type: String


Length Constraints: Minimum length of 3. Maximum length of 128.


Pattern: `^[a-zA-Z0-9_\-]+$`



Required: No




**[NextToken](#API_ListDashboards_RequestSyntax "#API_ListDashboards_RequestSyntax")**



 A token you can use to get the next page of dashboard results.



Type: String


Length Constraints: Minimum length of 4. Maximum length of 1000.


Pattern: `.*`



Required: No




**[Type](#API_ListDashboards_RequestSyntax "#API_ListDashboards_RequestSyntax")**



Specify a dashboard type to filter on: `CUSTOM` or `MANAGED`.



Type: String


Valid Values: `MANAGED | CUSTOM`



Required: No




## Response Syntax



```
{
   "Dashboards": [ 
      { 
         "DashboardArn": "***string***",
         "Type": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Dashboards](#API_ListDashboards_ResponseSyntax "#API_ListDashboards_ResponseSyntax")**



 Contains information about dashboards in the account, in the current Region that match the applied filters.



Type: Array of [DashboardDetail](API_DashboardDetail.md "API_DashboardDetail.md") objects




**[NextToken](#API_ListDashboards_ResponseSyntax "#API_ListDashboards_ResponseSyntax")**



 A token you can use to get the next page of dashboard results.



Type: String


Length Constraints: Minimum length of 4. Maximum length of 1000.


Pattern: `.*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListDashboards "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListDashboards")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/ListDashboards "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/ListDashboards")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListDashboards "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListDashboards")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListDashboards "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListDashboards")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListDashboards "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListDashboards")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListDashboards "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListDashboards")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListDashboards "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListDashboards")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListDashboards "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListDashboards")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListDashboards "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListDashboards")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListDashboards "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListDashboards")
