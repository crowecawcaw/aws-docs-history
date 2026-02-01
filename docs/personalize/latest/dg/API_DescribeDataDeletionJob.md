# DescribeDataDeletionJob

Describes the data deletion job created by [CreateDataDeletionJob](API_CreateDataDeletionJob.md "API_CreateDataDeletionJob.md"), including the job status.

## Request Syntax

```
{
   "dataDeletionJobArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[dataDeletionJobArn](#API_DescribeDataDeletionJob_RequestSyntax "#API_DescribeDataDeletionJob_RequestSyntax")**

The Amazon Resource Name (ARN) of the data deletion job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "dataDeletionJob": {
      "creationDateTime": ***number***,
      "dataDeletionJobArn": "***string***",
      "datasetGroupArn": "***string***",
      "dataSource": {
         "dataLocation": "***string***"
      },
      "failureReason": "***string***",
      "jobName": "***string***",
      "lastUpdatedDateTime": ***number***,
      "numDeleted": ***number***,
      "roleArn": "***string***",
      "status": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[dataDeletionJob](#API_DescribeDataDeletionJob_ResponseSyntax "#API_DescribeDataDeletionJob_ResponseSyntax")**

Information about the data deletion job, including the status.

The status is one of the following values:

- PENDING
- IN_PROGRESS
- COMPLETED
- FAILED

Type: [DataDeletionJob](API_DataDeletionJob.md "API_DataDeletionJob.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeDataDeletionJob.md "../../../goto/cli2/personalize-2018-05-22/DescribeDataDeletionJob.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeDataDeletionJob.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeDataDeletionJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeDataDeletionJob.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeDataDeletionJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeDataDeletionJob.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeDataDeletionJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeDataDeletionJob.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeDataDeletionJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeDataDeletionJob.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeDataDeletionJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeDataDeletionJob.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeDataDeletionJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeDataDeletionJob.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeDataDeletionJob.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeDataDeletionJob.md "../../../goto/boto3/personalize-2018-05-22/DescribeDataDeletionJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeDataDeletionJob.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeDataDeletionJob.md")
