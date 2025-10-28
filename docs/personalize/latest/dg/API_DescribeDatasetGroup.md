# DescribeDatasetGroup

Describes the given dataset group. For more information on dataset
groups, see [CreateDatasetGroup](API_CreateDatasetGroup.md "API_CreateDatasetGroup.md").

## Request Syntax

```
{
   "datasetGroupArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetGroupArn](#API_DescribeDatasetGroup_RequestSyntax "#API_DescribeDatasetGroup_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset group to
describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "datasetGroup": {
      "creationDateTime": ***number***,
      "datasetGroupArn": "***string***",
      "domain": "***string***",
      "failureReason": "***string***",
      "kmsKeyArn": "***string***",
      "lastUpdatedDateTime": ***number***,
      "name": "***string***",
      "roleArn": "***string***",
      "status": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[datasetGroup](#API_DescribeDatasetGroup_ResponseSyntax "#API_DescribeDatasetGroup_ResponseSyntax")**

A listing of the dataset group's properties.

Type: [DatasetGroup](API_DatasetGroup.md "API_DatasetGroup.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeDatasetGroup.md "../../../goto/cli2/personalize-2018-05-22/DescribeDatasetGroup.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeDatasetGroup.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeDatasetGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeDatasetGroup.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeDatasetGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeDatasetGroup.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeDatasetGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeDatasetGroup.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeDatasetGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeDatasetGroup.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeDatasetGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeDatasetGroup.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeDatasetGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeDatasetGroup.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeDatasetGroup.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeDatasetGroup.md "../../../goto/boto3/personalize-2018-05-22/DescribeDatasetGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeDatasetGroup.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeDatasetGroup.md")
