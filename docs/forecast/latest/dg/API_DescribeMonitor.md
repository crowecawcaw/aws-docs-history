Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DescribeMonitor

Describes a monitor resource. In addition to listing the properties provided in the [CreateMonitor](API_CreateMonitor.md "API_CreateMonitor.md") request, this operation lists the following properties:

- `Baseline`
- `CreationTime`
- `LastEvaluationTime`
- `LastEvaluationState`
- `LastModificationTime`
- `Message`
- `Status`

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Request Syntax

```
{
   "MonitorArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[MonitorArn](#API_DescribeMonitor_RequestSyntax "#API_DescribeMonitor_RequestSyntax")**

The Amazon Resource Name (ARN) of the monitor resource to describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "Baseline": {
      "PredictorBaseline": {
         "BaselineMetrics": [
            {
               "Name": "***string***",
               "Value": ***number***
            }
         ]
      }
   },
   "CreationTime": ***number***,
   "EstimatedEvaluationTimeRemainingInMinutes": ***number***,
   "LastEvaluationState": "***string***",
   "LastEvaluationTime": ***number***,
   "LastModificationTime": ***number***,
   "Message": "***string***",
   "MonitorArn": "***string***",
   "MonitorName": "***string***",
   "ResourceArn": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Baseline](#API_DescribeMonitor_ResponseSyntax "#API_DescribeMonitor_ResponseSyntax")**

Metrics you can use as a baseline for comparison purposes. Use these values you interpret monitoring results for an auto predictor.

Type: [Baseline](API_Baseline.md "API_Baseline.md") object

**[CreationTime](#API_DescribeMonitor_ResponseSyntax "#API_DescribeMonitor_ResponseSyntax")**

The timestamp for when the monitor resource was created.

Type: Timestamp

**[EstimatedEvaluationTimeRemainingInMinutes](#API_DescribeMonitor_ResponseSyntax "#API_DescribeMonitor_ResponseSyntax")**

The estimated number of minutes remaining before the monitor resource finishes its current evaluation.

Type: Long

**[LastEvaluationState](#API_DescribeMonitor_ResponseSyntax "#API_DescribeMonitor_ResponseSyntax")**

The state of the monitor's latest evaluation.

Type: String

Length Constraints: Maximum length of 256.

**[LastEvaluationTime](#API_DescribeMonitor_ResponseSyntax "#API_DescribeMonitor_ResponseSyntax")**

The timestamp of the latest evaluation completed by the monitor.

Type: Timestamp

**[LastModificationTime](#API_DescribeMonitor_ResponseSyntax "#API_DescribeMonitor_ResponseSyntax")**

The timestamp of the latest modification to the monitor.

Type: Timestamp

**[Message](#API_DescribeMonitor_ResponseSyntax "#API_DescribeMonitor_ResponseSyntax")**

An error message, if any, for the monitor.

Type: String

**[MonitorArn](#API_DescribeMonitor_ResponseSyntax "#API_DescribeMonitor_ResponseSyntax")**

The Amazon Resource Name (ARN) of the monitor resource described.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[MonitorName](#API_DescribeMonitor_ResponseSyntax "#API_DescribeMonitor_ResponseSyntax")**

The name of the monitor.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

**[ResourceArn](#API_DescribeMonitor_ResponseSyntax "#API_DescribeMonitor_ResponseSyntax")**

The Amazon Resource Name (ARN) of the auto predictor being monitored.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[Status](#API_DescribeMonitor_ResponseSyntax "#API_DescribeMonitor_ResponseSyntax")**

The status of the monitor resource.

Type: String

Length Constraints: Maximum length of 256.

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

HTTP Status Code: 400

**ResourceNotFoundException**

We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try
again.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DescribeMonitor.md "../../../goto/cli2/forecast-2018-06-26/DescribeMonitor.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/DescribeMonitor.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/DescribeMonitor.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DescribeMonitor.md "../../../goto/SdkForCpp/forecast-2018-06-26/DescribeMonitor.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeMonitor.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeMonitor.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeMonitor.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeMonitor.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeMonitor.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeMonitor.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeMonitor.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeMonitor.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeMonitor.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeMonitor.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DescribeMonitor.md "../../../goto/boto3/forecast-2018-06-26/DescribeMonitor.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeMonitor.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeMonitor.md")
