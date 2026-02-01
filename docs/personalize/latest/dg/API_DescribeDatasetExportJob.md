# DescribeDatasetExportJob

Describes the dataset export job created by [CreateDatasetExportJob](API_CreateDatasetExportJob.md "API_CreateDatasetExportJob.md"), including the export job status.

## Request Syntax

```
{
   "datasetExportJobArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetExportJobArn](#API_DescribeDatasetExportJob_RequestSyntax "#API_DescribeDatasetExportJob_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset export job to
describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "datasetExportJob": {
      "creationDateTime": ***number***,
      "datasetArn": "***string***",
      "datasetExportJobArn": "***string***",
      "failureReason": "***string***",
      "ingestionMode": "***string***",
      "jobName": "***string***",
      "jobOutput": {
         "s3DataDestination": {
            "kmsKeyArn": "***string***",
            "path": "***string***"
         }
      },
      "lastUpdatedDateTime": ***number***,
      "roleArn": "***string***",
      "status": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[datasetExportJob](#API_DescribeDatasetExportJob_ResponseSyntax "#API_DescribeDatasetExportJob_ResponseSyntax")**

Information about the dataset export job, including the status.

The status is one of the following values:

- CREATE PENDING
- CREATE IN_PROGRESS
- ACTIVE
- CREATE FAILED

Type: [DatasetExportJob](API_DatasetExportJob.md "API_DatasetExportJob.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeDatasetExportJob.md "../../../goto/cli2/personalize-2018-05-22/DescribeDatasetExportJob.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeDatasetExportJob.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeDatasetExportJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeDatasetExportJob.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeDatasetExportJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeDatasetExportJob.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeDatasetExportJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeDatasetExportJob.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeDatasetExportJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeDatasetExportJob.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeDatasetExportJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeDatasetExportJob.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeDatasetExportJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeDatasetExportJob.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeDatasetExportJob.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeDatasetExportJob.md "../../../goto/boto3/personalize-2018-05-22/DescribeDatasetExportJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeDatasetExportJob.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeDatasetExportJob.md")
