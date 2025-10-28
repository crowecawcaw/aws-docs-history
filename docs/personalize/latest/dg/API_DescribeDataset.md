# DescribeDataset

Describes the given dataset. For more information on datasets, see
[CreateDataset](API_CreateDataset.md "API_CreateDataset.md").

## Request Syntax

```
{
   "datasetArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetArn](#API_DescribeDataset_RequestSyntax "#API_DescribeDataset_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset to describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "dataset": {
      "creationDateTime": ***number***,
      "datasetArn": "***string***",
      "datasetGroupArn": "***string***",
      "datasetType": "***string***",
      "lastUpdatedDateTime": ***number***,
      "latestDatasetUpdate": {
         "creationDateTime": ***number***,
         "failureReason": "***string***",
         "lastUpdatedDateTime": ***number***,
         "schemaArn": "***string***",
         "status": "***string***"
      },
      "name": "***string***",
      "schemaArn": "***string***",
      "status": "***string***",
      "trackingId": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[dataset](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

A listing of the dataset's properties.

Type: [Dataset](API_Dataset.md "API_Dataset.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeDataset.md "../../../goto/cli2/personalize-2018-05-22/DescribeDataset.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeDataset.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeDataset.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeDataset.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeDataset.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeDataset.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeDataset.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeDataset.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeDataset.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeDataset.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeDataset.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeDataset.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeDataset.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeDataset.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeDataset.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeDataset.md "../../../goto/boto3/personalize-2018-05-22/DescribeDataset.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeDataset.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeDataset.md")
