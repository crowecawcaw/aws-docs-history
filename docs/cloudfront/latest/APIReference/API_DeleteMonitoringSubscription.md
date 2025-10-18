# DeleteMonitoringSubscription

Disables additional CloudWatch metrics for the specified CloudFront distribution.


## Request Syntax



```
DELETE /2020-05-31/distributions/`DistributionId`/monitoring-subscription HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[DistributionId](#API_DeleteMonitoringSubscription_RequestSyntax "#API_DeleteMonitoringSubscription_RequestSyntax")**


The ID of the distribution that you are disabling metrics for.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteMonitoringSubscription "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteMonitoringSubscription")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DeleteMonitoringSubscription "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DeleteMonitoringSubscription")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteMonitoringSubscription")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteMonitoringSubscription")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteMonitoringSubscription")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteMonitoringSubscription")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteMonitoringSubscription")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteMonitoringSubscription")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteMonitoringSubscription "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteMonitoringSubscription")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteMonitoringSubscription "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteMonitoringSubscription")
