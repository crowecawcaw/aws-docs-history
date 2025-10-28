# DescribeDatasetImportJob

Describes the dataset import job created by [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md"), including the import job status.

## Request Syntax

```
{
   "datasetImportJobArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetImportJobArn](#API_DescribeDatasetImportJob_RequestSyntax "#API_DescribeDatasetImportJob_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset import job to
describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "datasetImportJob": {
      "creationDateTime": ***number***,
      "datasetArn": "***string***",
      "datasetImportJobArn": "***string***",
      "dataSource": {
         "dataLocation": "***string***"
      },
      "failureReason": "***string***",
      "importMode": "***string***",
      "jobName": "***string***",
      "lastUpdatedDateTime": ***number***,
      "publishAttributionMetricsToS3": ***boolean***,
      "roleArn": "***string***",
      "status": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[datasetImportJob](#API_DescribeDatasetImportJob_ResponseSyntax "#API_DescribeDatasetImportJob_ResponseSyntax")**

Information about the dataset import job, including the status.

The status is one of the following values:

- CREATE PENDING
- CREATE IN_PROGRESS
- ACTIVE
- CREATE FAILED

Type: [DatasetImportJob](API_DatasetImportJob.md "API_DatasetImportJob.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeDatasetImportJob.md "../../../goto/cli2/personalize-2018-05-22/DescribeDatasetImportJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeDatasetImportJob.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeDatasetImportJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeDatasetImportJob.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeDatasetImportJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeDatasetImportJob.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeDatasetImportJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeDatasetImportJob.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeDatasetImportJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeDatasetImportJob.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeDatasetImportJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeDatasetImportJob.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeDatasetImportJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeDatasetImportJob.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeDatasetImportJob.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeDatasetImportJob.md "../../../goto/boto3/personalize-2018-05-22/DescribeDatasetImportJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeDatasetImportJob.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeDatasetImportJob.md")
