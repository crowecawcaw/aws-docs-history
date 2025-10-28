Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# ListDatasets

Returns a list of datasets created using the [CreateDataset](API_CreateDataset.md "API_CreateDataset.md") operation. For each
dataset, a summary of its properties, including its Amazon Resource Name (ARN), is returned.
To retrieve the complete set of properties, use the ARN with the [DescribeDataset](API_DescribeDataset.md "API_DescribeDataset.md") operation.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Request Syntax

```
{
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[MaxResults](#API_ListDatasets_RequestSyntax "#API_ListDatasets_RequestSyntax")**

The number of items to return in the response.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[NextToken](#API_ListDatasets_RequestSyntax "#API_ListDatasets_RequestSyntax")**

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
   "Datasets": [
      {
         "CreationTime": ***number***,
         "DatasetArn": "***string***",
         "DatasetName": "***string***",
         "DatasetType": "***string***",
         "Domain": "***string***",
         "LastModificationTime": ***number***
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Datasets](#API_ListDatasets_ResponseSyntax "#API_ListDatasets_ResponseSyntax")**

An array of objects that summarize each dataset's properties.

Type: Array of [DatasetSummary](API_DatasetSummary.md "API_DatasetSummary.md") objects

**[NextToken](#API_ListDatasets_ResponseSyntax "#API_ListDatasets_ResponseSyntax")**

If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of
results, use the token in the next request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 3000.

Pattern: `.+`

## Errors

**InvalidNextTokenException**

The token is not valid. Tokens expire after 24 hours.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/ListDatasets.md "../../../goto/cli2/forecast-2018-06-26/ListDatasets.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/forecast-2018-06-26/ListDatasets.md "../../../goto/DotNetSDKV3/forecast-2018-06-26/ListDatasets.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/ListDatasets.md "../../../goto/SdkForCpp/forecast-2018-06-26/ListDatasets.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/ListDatasets.md "../../../goto/SdkForGoV2/forecast-2018-06-26/ListDatasets.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/ListDatasets.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/ListDatasets.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/ListDatasets.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/ListDatasets.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/ListDatasets.md "../../../goto/SdkForKotlin/forecast-2018-06-26/ListDatasets.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/ListDatasets.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/ListDatasets.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/ListDatasets.md "../../../goto/boto3/forecast-2018-06-26/ListDatasets.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/ListDatasets.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/ListDatasets.md")
