# GetSolutionMetrics

Gets the metrics for the specified solution version.

## Request Syntax

```
{
   "solutionVersionArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[solutionVersionArn](#API_GetSolutionMetrics_RequestSyntax "#API_GetSolutionMetrics_RequestSyntax")**

The Amazon Resource Name (ARN) of the solution version for which to get metrics.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "metrics": {
      "***string***" : ***number***
   },
   "solutionVersionArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[metrics](#API_GetSolutionMetrics_ResponseSyntax "#API_GetSolutionMetrics_ResponseSyntax")**

The metrics for the solution version. For more information, see
[Evaluating a solution version with metrics](working-with-training-metrics.md "working-with-training-metrics.md") .

Type: String to double map

Map Entries: Maximum number of 100 items.

Key Length Constraints: Maximum length of 256.

**[solutionVersionArn](#API_GetSolutionMetrics_ResponseSyntax "#API_GetSolutionMetrics_ResponseSyntax")**

The same solution version ARN as specified in the request.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/GetSolutionMetrics.md "../../../goto/cli2/personalize-2018-05-22/GetSolutionMetrics.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/GetSolutionMetrics.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/GetSolutionMetrics.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/GetSolutionMetrics.md "../../../goto/SdkForCpp/personalize-2018-05-22/GetSolutionMetrics.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/GetSolutionMetrics.md "../../../goto/SdkForGoV2/personalize-2018-05-22/GetSolutionMetrics.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/GetSolutionMetrics.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/GetSolutionMetrics.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/GetSolutionMetrics.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/GetSolutionMetrics.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/GetSolutionMetrics.md "../../../goto/SdkForKotlin/personalize-2018-05-22/GetSolutionMetrics.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/GetSolutionMetrics.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/GetSolutionMetrics.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/GetSolutionMetrics.md "../../../goto/boto3/personalize-2018-05-22/GetSolutionMetrics.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/GetSolutionMetrics.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/GetSolutionMetrics.md")
