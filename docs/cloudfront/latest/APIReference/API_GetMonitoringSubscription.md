# GetMonitoringSubscription

Gets information about whether additional CloudWatch metrics are enabled for the
 specified CloudFront distribution.


## Request Syntax



```
GET /2020-05-31/distributions/`DistributionId`/monitoring-subscription HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[DistributionId](#API_GetMonitoringSubscription_RequestSyntax "#API_GetMonitoringSubscription_RequestSyntax")**


The ID of the distribution that you are getting metrics information for.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<MonitoringSubscription>
   <RealtimeMetricsSubscriptionConfig>
      <RealtimeMetricsSubscriptionStatus>***string***</RealtimeMetricsSubscriptionStatus>
   </RealtimeMetricsSubscriptionConfig>
</MonitoringSubscription>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[MonitoringSubscription](#API_GetMonitoringSubscription_ResponseSyntax "#API_GetMonitoringSubscription_ResponseSyntax")**


Root level tag for the MonitoringSubscription parameters.


Required: Yes




**[RealtimeMetricsSubscriptionConfig](#API_GetMonitoringSubscription_ResponseSyntax "#API_GetMonitoringSubscription_ResponseSyntax")**


A subscription configuration for additional CloudWatch metrics.


Type: [RealtimeMetricsSubscriptionConfig](API_RealtimeMetricsSubscriptionConfig.md "API_RealtimeMetricsSubscriptionConfig.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**NoSuchDistribution** 


The specified distribution does not exist.


HTTP Status Code: 404




**NoSuchMonitoringSubscription** 


A monitoring subscription does not exist for the specified distribution.


HTTP Status Code: 404




**UnsupportedOperation** 


This operation is not supported in this AWS Region.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetMonitoringSubscription "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetMonitoringSubscription")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetMonitoringSubscription "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetMonitoringSubscription")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetMonitoringSubscription")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetMonitoringSubscription")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetMonitoringSubscription")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetMonitoringSubscription")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetMonitoringSubscription")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetMonitoringSubscription")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetMonitoringSubscription "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetMonitoringSubscription")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetMonitoringSubscription")
