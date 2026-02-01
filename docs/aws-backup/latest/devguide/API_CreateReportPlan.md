# CreateReportPlan

Creates a report plan. A report plan is a document that contains information about the
contents of the report and where AWS Backup will deliver it.

If you call `CreateReportPlan` with a plan that already exists, you receive
an `AlreadyExistsException` exception.

## Request Syntax

```
POST /audit/report-plans HTTP/1.1
Content-type: application/json

{
   "IdempotencyToken": "`string`",
   "ReportDeliveryChannel": {
      "Formats": [ "`string`" ],
      "S3BucketName": "`string`",
      "S3KeyPrefix": "`string`"
   },
   "ReportPlanDescription": "`string`",
   "ReportPlanName": "`string`",
   "ReportPlanTags": {
      "`string`" : "`string`"
   },
   "ReportSetting": {
      "Accounts": [ "`string`" ],
      "FrameworkArns": [ "`string`" ],
      "NumberOfFrameworks": `number`,
      "OrganizationUnits": [ "`string`" ],
      "Regions": [ "`string`" ],
      "ReportTemplate": "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[IdempotencyToken](#API_CreateReportPlan_RequestSyntax "#API_CreateReportPlan_RequestSyntax")**

A customer-chosen string that you can use to distinguish between otherwise identical
calls to `CreateReportPlanInput`. Retrying a successful request with the same
idempotency token results in a success message with no action taken.

Type: String

Required: No

**[ReportDeliveryChannel](#API_CreateReportPlan_RequestSyntax "#API_CreateReportPlan_RequestSyntax")**

A structure that contains information about where and how to deliver your reports,
specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your
reports.

Type: [ReportDeliveryChannel](API_ReportDeliveryChannel.md "API_ReportDeliveryChannel.md") object

Required: Yes

**[ReportPlanDescription](#API_CreateReportPlan_RequestSyntax "#API_CreateReportPlan_RequestSyntax")**

An optional description of the report plan with a maximum of 1,024 characters.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `.*\S.*`

Required: No

**[ReportPlanName](#API_CreateReportPlan_RequestSyntax "#API_CreateReportPlan_RequestSyntax")**

The unique name of the report plan. The name must be between 1 and 256 characters,
starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and
underscores (\_).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

Required: Yes

**[ReportPlanTags](#API_CreateReportPlan_RequestSyntax "#API_CreateReportPlan_RequestSyntax")**

The tags to assign to the report plan.

Type: String to string map

Required: No

**[ReportSetting](#API_CreateReportPlan_RequestSyntax "#API_CreateReportPlan_RequestSyntax")**

Identifies the report template for the report. Reports are built using a report
template. The report templates are:

`RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT |
 COPY_JOB_REPORT | RESTORE_JOB_REPORT | SCAN_JOB_REPORT`

If the report template is `RESOURCE_COMPLIANCE_REPORT` or
`CONTROL_COMPLIANCE_REPORT`, this API resource also describes the report
coverage by AWS Regions and frameworks.

Type: [ReportSetting](API_ReportSetting.md "API_ReportSetting.md") object

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": ***number***,
   "ReportPlanArn": "***string***",
   "ReportPlanName": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_CreateReportPlan_ResponseSyntax "#API_CreateReportPlan_ResponseSyntax")**

The date and time a backup vault is created, in Unix format and Coordinated Universal
Time (UTC). The value of `CreationTime` is accurate to milliseconds. For
example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[ReportPlanArn](#API_CreateReportPlan_ResponseSyntax "#API_CreateReportPlan_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
depends on the resource type.

Type: String

**[ReportPlanName](#API_CreateReportPlan_ResponseSyntax "#API_CreateReportPlan_ResponseSyntax")**

The unique name of the report plan.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AlreadyExistsException**

The required resource already exists.

**Arn**

**Context**

**CreatorRequestId**

**Type**

HTTP Status Code: 400

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**LimitExceededException**

A limit in the request has been exceeded; for example, a maximum number of items allowed
in a request.

**Context**

**Type**

HTTP Status Code: 400

**MissingParameterValueException**

Indicates that a required parameter is missing.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/CreateReportPlan.md "../../../goto/cli2/backup-2018-11-15/CreateReportPlan.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/CreateReportPlan.md "../../../goto/DotNetSDKV4/backup-2018-11-15/CreateReportPlan.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/CreateReportPlan.md "../../../goto/SdkForCpp/backup-2018-11-15/CreateReportPlan.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/CreateReportPlan.md "../../../goto/SdkForGoV2/backup-2018-11-15/CreateReportPlan.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/CreateReportPlan.md "../../../goto/SdkForJavaV2/backup-2018-11-15/CreateReportPlan.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateReportPlan.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateReportPlan.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/CreateReportPlan.md "../../../goto/SdkForKotlin/backup-2018-11-15/CreateReportPlan.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/CreateReportPlan.md "../../../goto/SdkForPHPV3/backup-2018-11-15/CreateReportPlan.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/CreateReportPlan.md "../../../goto/boto3/backup-2018-11-15/CreateReportPlan.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/CreateReportPlan.md "../../../goto/SdkForRubyV3/backup-2018-11-15/CreateReportPlan.md")
