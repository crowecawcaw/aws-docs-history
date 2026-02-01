# DescribeReportJob

Returns the details associated with creating a report as specified by its
`ReportJobId`.

## Request Syntax

```
GET /audit/report-jobs/`reportJobId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[reportJobId](#API_DescribeReportJob_RequestSyntax "#API_DescribeReportJob_RequestSyntax")**

The identifier of the report job. A unique, randomly generated, Unicode, UTF-8 encoded
string that is at most 1,024 bytes long. The report job ID cannot be edited.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ReportJob": {
      "CompletionTime": ***number***,
      "CreationTime": ***number***,
      "ReportDestination": {
         "S3BucketName": "***string***",
         "S3Keys": [ "***string***" ]
      },
      "ReportJobId": "***string***",
      "ReportPlanArn": "***string***",
      "ReportTemplate": "***string***",
      "Status": "***string***",
      "StatusMessage": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ReportJob](#API_DescribeReportJob_ResponseSyntax "#API_DescribeReportJob_ResponseSyntax")**

The information about a report job, including its completion and creation times,
report destination, unique report job ID, Amazon Resource Name (ARN), report template,
status, and status message.

Type: [ReportJob](API_ReportJob.md "API_ReportJob.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**MissingParameterValueException**

Indicates that a required parameter is missing.

**Context**

**Type**

HTTP Status Code: 400

**ResourceNotFoundException**

A resource that is required for the action doesn't exist.

**Context**

**Type**

HTTP Status Code: 400

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DescribeReportJob.md "../../../goto/cli2/backup-2018-11-15/DescribeReportJob.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/DescribeReportJob.md "../../../goto/DotNetSDKV4/backup-2018-11-15/DescribeReportJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DescribeReportJob.md "../../../goto/SdkForCpp/backup-2018-11-15/DescribeReportJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DescribeReportJob.md "../../../goto/SdkForGoV2/backup-2018-11-15/DescribeReportJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeReportJob.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeReportJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeReportJob.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeReportJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DescribeReportJob.md "../../../goto/SdkForKotlin/backup-2018-11-15/DescribeReportJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeReportJob.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeReportJob.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DescribeReportJob.md "../../../goto/boto3/backup-2018-11-15/DescribeReportJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeReportJob.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeReportJob.md")
