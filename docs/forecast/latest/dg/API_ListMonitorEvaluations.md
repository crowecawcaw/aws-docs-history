Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# ListMonitorEvaluations

Returns a list of the monitoring evaluation results and predictor events collected by
the monitor resource during different windows of time.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

For information about monitoring see [Predictor Monitoring](predictor-monitoring.md "predictor-monitoring.md"). For
more information about retrieving monitoring results see [Viewing Monitoring Results](predictor-monitoring-results.md "predictor-monitoring-results.md").

## Request Syntax

```
{
   "Filters": [
      {
         "Condition": "`string`",
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "MaxResults": `number`,
   "MonitorArn": "`string`",
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Filters](#API_ListMonitorEvaluations_RequestSyntax "#API_ListMonitorEvaluations_RequestSyntax")**

An array of filters. For each filter, provide a condition and a match statement. The
condition is either `IS` or `IS_NOT`, which specifies whether to
include or exclude the resources that match the statement from the list. The match
statement consists of a key and a value.

**Filter properties**

- `Condition` - The condition to apply. Valid values are
  `IS` and `IS_NOT`.
- `Key` - The name of the parameter to filter on. The only valid value is
  `EvaluationState`.
- `Value` - The value to match. Valid values are only `SUCCESS` or `FAILURE`.

For example, to list only successful monitor evaluations, you would specify:

`"Filters": [ { "Condition": "IS", "Key": "EvaluationState", "Value": "SUCCESS" } ]`

Type: Array of [Filter](API_Filter.md "API_Filter.md") objects

Required: No

**[MaxResults](#API_ListMonitorEvaluations_RequestSyntax "#API_ListMonitorEvaluations_RequestSyntax")**

The maximum number of monitoring results to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[MonitorArn](#API_ListMonitorEvaluations_RequestSyntax "#API_ListMonitorEvaluations_RequestSyntax")**

The Amazon Resource Name (ARN) of the monitor resource to get results from.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

**[NextToken](#API_ListMonitorEvaluations_RequestSyntax "#API_ListMonitorEvaluations_RequestSyntax")**

If the result of the previous request was truncated, the response includes a
`NextToken`. To retrieve the next set of results, use the token in the next
request. Tokens expire after 24 hours.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 3000.

Pattern: `.+`

Required: No

## Response Syntax

```
{
   "NextToken": "***string***",
   "PredictorMonitorEvaluations": [
      {
         "EvaluationState": "***string***",
         "EvaluationTime": ***number***,
         "Message": "***string***",
         "MetricResults": [
            {
               "MetricName": "***string***",
               "MetricValue": ***number***
            }
         ],
         "MonitorArn": "***string***",
         "MonitorDataSource": {
            "DatasetImportJobArn": "***string***",
            "ForecastArn": "***string***",
            "PredictorArn": "***string***"
         },
         "NumItemsEvaluated": ***number***,
         "PredictorEvent": {
            "Datetime": ***number***,
            "Detail": "***string***"
         },
         "ResourceArn": "***string***",
         "WindowEndDatetime": ***number***,
         "WindowStartDatetime": ***number***
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListMonitorEvaluations_ResponseSyntax "#API_ListMonitorEvaluations_ResponseSyntax")**

If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of
results, use the token in the next request. Tokens expire after 24 hours.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 3000.

Pattern: `.+`

**[PredictorMonitorEvaluations](#API_ListMonitorEvaluations_ResponseSyntax "#API_ListMonitorEvaluations_ResponseSyntax")**

The monitoring results and predictor events collected by the monitor resource during different windows of time.

For information about monitoring see [Viewing Monitoring Results](predictor-monitoring-results.md "predictor-monitoring-results.md"). For more information about retrieving monitoring results see [Viewing Monitoring Results](predictor-monitoring-results.md "predictor-monitoring-results.md").

Type: Array of [PredictorMonitorEvaluation](API_PredictorMonitorEvaluation.md "API_PredictorMonitorEvaluation.md") objects

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid. Tokens expire after 24 hours.

HTTP Status Code: 400

**ResourceNotFoundException**

We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try
again.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/ListMonitorEvaluations.md "../../../goto/cli2/forecast-2018-06-26/ListMonitorEvaluations.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/ListMonitorEvaluations.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/ListMonitorEvaluations.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/ListMonitorEvaluations.md "../../../goto/SdkForCpp/forecast-2018-06-26/ListMonitorEvaluations.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/ListMonitorEvaluations.md "../../../goto/SdkForGoV2/forecast-2018-06-26/ListMonitorEvaluations.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/ListMonitorEvaluations.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/ListMonitorEvaluations.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/ListMonitorEvaluations.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/ListMonitorEvaluations.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/ListMonitorEvaluations.md "../../../goto/SdkForKotlin/forecast-2018-06-26/ListMonitorEvaluations.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/ListMonitorEvaluations.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/ListMonitorEvaluations.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/ListMonitorEvaluations.md "../../../goto/boto3/forecast-2018-06-26/ListMonitorEvaluations.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/ListMonitorEvaluations.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/ListMonitorEvaluations.md")
