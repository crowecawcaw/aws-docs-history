# DescribeFilter

Describes a filter's properties.

## Request Syntax

```
{
   "filterArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[filterArn](#API_DescribeFilter_RequestSyntax "#API_DescribeFilter_RequestSyntax")**

The ARN of the filter to describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "filter": {
      "creationDateTime": ***number***,
      "datasetGroupArn": "***string***",
      "failureReason": "***string***",
      "filterArn": "***string***",
      "filterExpression": "***string***",
      "lastUpdatedDateTime": ***number***,
      "name": "***string***",
      "status": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[filter](#API_DescribeFilter_ResponseSyntax "#API_DescribeFilter_ResponseSyntax")**

The filter's details.

Type: [Filter](API_Filter.md "API_Filter.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeFilter.md "../../../goto/cli2/personalize-2018-05-22/DescribeFilter.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeFilter.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeFilter.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeFilter.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeFilter.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeFilter.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeFilter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeFilter.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeFilter.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeFilter.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeFilter.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeFilter.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeFilter.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeFilter.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeFilter.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeFilter.md "../../../goto/boto3/personalize-2018-05-22/DescribeFilter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeFilter.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeFilter.md")
