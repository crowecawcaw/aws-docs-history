# DescribeReportPlan

Returns a list of all report plans for an AWS account and AWS Region.

## Request Syntax

```
GET /audit/report-plans/`reportPlanName` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[reportPlanName](#API_DescribeReportPlan_RequestSyntax "#API_DescribeReportPlan_RequestSyntax")**

The unique name of a report plan.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ReportPlan": {
      "CreationTime": ***number***,
      "DeploymentStatus": "***string***",
      "LastAttemptedExecutionTime": ***number***,
      "LastSuccessfulExecutionTime": ***number***,
      "ReportDeliveryChannel": {
         "Formats": [ "***string***" ],
         "S3BucketName": "***string***",
         "S3KeyPrefix": "***string***"
      },
      "ReportPlanArn": "***string***",
      "ReportPlanDescription": "***string***",
      "ReportPlanName": "***string***",
      "ReportSetting": {
         "Accounts": [ "***string***" ],
         "FrameworkArns": [ "***string***" ],
         "NumberOfFrameworks": ***number***,
         "OrganizationUnits": [ "***string***" ],
         "Regions": [ "***string***" ],
         "ReportTemplate": "***string***"
      }
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ReportPlan](#API_DescribeReportPlan_ResponseSyntax "#API_DescribeReportPlan_ResponseSyntax")**

Returns details about the report plan that is specified by its name. These details
include the report plan's Amazon Resource Name (ARN), description, settings, delivery
channel, deployment status, creation time, and last attempted and successful run
times.

Type: [ReportPlan](API_ReportPlan.md "API_ReportPlan.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DescribeReportPlan.md "../../../goto/cli2/backup-2018-11-15/DescribeReportPlan.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/DescribeReportPlan.md "../../../goto/DotNetSDKV3/backup-2018-11-15/DescribeReportPlan.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DescribeReportPlan.md "../../../goto/SdkForCpp/backup-2018-11-15/DescribeReportPlan.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DescribeReportPlan.md "../../../goto/SdkForGoV2/backup-2018-11-15/DescribeReportPlan.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeReportPlan.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeReportPlan.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeReportPlan.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeReportPlan.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DescribeReportPlan.md "../../../goto/SdkForKotlin/backup-2018-11-15/DescribeReportPlan.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeReportPlan.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeReportPlan.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DescribeReportPlan.md "../../../goto/boto3/backup-2018-11-15/DescribeReportPlan.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeReportPlan.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeReportPlan.md")
