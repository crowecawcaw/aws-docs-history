Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# ListPredictors

Returns a list of predictors created using the [CreateAutoPredictor](API_CreateAutoPredictor.md "API_CreateAutoPredictor.md") or
[CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") operations. For each predictor, this operation returns a
summary of its properties, including its Amazon Resource Name (ARN).

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

You can retrieve the complete set of properties by using the ARN with the [DescribeAutoPredictor](API_DescribeAutoPredictor.md "API_DescribeAutoPredictor.md") and [DescribePredictor](API_DescribePredictor.md "API_DescribePredictor.md") operations. You
can filter the list using an array of [Filter](API_Filter.md "API_Filter.md") objects.

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
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Filters](#API_ListPredictors_RequestSyntax "#API_ListPredictors_RequestSyntax")**

An array of filters. For each filter, you provide a condition and a match statement. The
condition is either `IS` or `IS_NOT`, which specifies whether to include
or exclude the predictors that match the statement from the list, respectively. The match
statement consists of a key and a value.

**Filter properties**

- `Condition` - The condition to apply. Valid values are `IS` and
  `IS_NOT`. To include the predictors that match the statement, specify
  `IS`. To exclude matching predictors, specify `IS_NOT`.
- `Key` - The name of the parameter to filter on. Valid values are
  `DatasetGroupArn` and `Status`.
- `Value` - The value to match.

For example, to list all predictors whose status is ACTIVE, you would specify:

`"Filters": [ { "Condition": "IS", "Key": "Status", "Value": "ACTIVE" }
 ]`

Type: Array of [Filter](API_Filter.md "API_Filter.md") objects

Required: No

**[MaxResults](#API_ListPredictors_RequestSyntax "#API_ListPredictors_RequestSyntax")**

The number of items to return in the response.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[NextToken](#API_ListPredictors_RequestSyntax "#API_ListPredictors_RequestSyntax")**

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
   "Predictors": [
      {
         "CreationTime": ***number***,
         "DatasetGroupArn": "***string***",
         "IsAutoPredictor": ***boolean***,
         "LastModificationTime": ***number***,
         "Message": "***string***",
         "PredictorArn": "***string***",
         "PredictorName": "***string***",
         "ReferencePredictorSummary": {
            "Arn": "***string***",
            "State": "***string***"
         },
         "Status": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListPredictors_ResponseSyntax "#API_ListPredictors_ResponseSyntax")**

If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of
results, use the token in the next request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 3000.

Pattern: `.+`

**[Predictors](#API_ListPredictors_ResponseSyntax "#API_ListPredictors_ResponseSyntax")**

An array of objects that summarize each predictor's properties.

Type: Array of [PredictorSummary](API_PredictorSummary.md "API_PredictorSummary.md") objects

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid. Tokens expire after 24 hours.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/ListPredictors.md "../../../goto/cli2/forecast-2018-06-26/ListPredictors.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/ListPredictors.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/ListPredictors.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/ListPredictors.md "../../../goto/SdkForCpp/forecast-2018-06-26/ListPredictors.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/ListPredictors.md "../../../goto/SdkForGoV2/forecast-2018-06-26/ListPredictors.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/ListPredictors.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/ListPredictors.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/ListPredictors.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/ListPredictors.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/ListPredictors.md "../../../goto/SdkForKotlin/forecast-2018-06-26/ListPredictors.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/ListPredictors.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/ListPredictors.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/ListPredictors.md "../../../goto/boto3/forecast-2018-06-26/ListPredictors.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/ListPredictors.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/ListPredictors.md")
