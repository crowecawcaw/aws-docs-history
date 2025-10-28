# UpdateRestoreTestingPlan

This request will send changes to your specified restore testing
plan. `RestoreTestingPlanName`
cannot be updated after it is created.

`RecoveryPointSelection` can contain:

- `Algorithm`
- `ExcludeVaults`
- `IncludeVaults`
- `RecoveryPointTypes`
- `SelectionWindowDays`

## Request Syntax

```
PUT /restore-testing/plans/`RestoreTestingPlanName` HTTP/1.1
Content-type: application/json

{
   "RestoreTestingPlan": {
      "RecoveryPointSelection": {
         "Algorithm": "`string`",
         "ExcludeVaults": [ "`string`" ],
         "IncludeVaults": [ "`string`" ],
         "RecoveryPointTypes": [ "`string`" ],
         "SelectionWindowDays": `number`
      },
      "ScheduleExpression": "`string`",
      "ScheduleExpressionTimezone": "`string`",
      "StartWindowHours": `number`
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[RestoreTestingPlanName](#API_UpdateRestoreTestingPlan_RequestSyntax "#API_UpdateRestoreTestingPlan_RequestSyntax")**

The name of the restore testing plan name.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[RestoreTestingPlan](#API_UpdateRestoreTestingPlan_RequestSyntax "#API_UpdateRestoreTestingPlan_RequestSyntax")**

Specifies the body of a restore testing plan.

Type: [RestoreTestingPlanForUpdate](API_RestoreTestingPlanForUpdate.md "API_RestoreTestingPlanForUpdate.md") object

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": ***number***,
   "RestoreTestingPlanArn": "***string***",
   "RestoreTestingPlanName": "***string***",
   "UpdateTime": ***number***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_UpdateRestoreTestingPlan_ResponseSyntax "#API_UpdateRestoreTestingPlan_ResponseSyntax")**

The time the resource testing plan was
created.

Type: Timestamp

**[RestoreTestingPlanArn](#API_UpdateRestoreTestingPlan_ResponseSyntax "#API_UpdateRestoreTestingPlan_ResponseSyntax")**

Unique ARN (Amazon Resource Name) of the restore testing plan.

Type: String

**[RestoreTestingPlanName](#API_UpdateRestoreTestingPlan_ResponseSyntax "#API_UpdateRestoreTestingPlan_ResponseSyntax")**

The name cannot be changed after creation. The name consists of
only alphanumeric characters and underscores. Maximum length is 50.

Type: String

**[UpdateTime](#API_UpdateRestoreTestingPlan_ResponseSyntax "#API_UpdateRestoreTestingPlan_ResponseSyntax")**

The time the update completed for the restore
testing plan.

Type: Timestamp

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ConflictException**

AWS Backup can't perform the action that you requested until it finishes
performing a previous action. Try again later.

**Context**

**Type**

HTTP Status Code: 400

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/UpdateRestoreTestingPlan.md "../../../goto/cli2/backup-2018-11-15/UpdateRestoreTestingPlan.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/UpdateRestoreTestingPlan.md "../../../goto/DotNetSDKV3/backup-2018-11-15/UpdateRestoreTestingPlan.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/UpdateRestoreTestingPlan.md "../../../goto/SdkForCpp/backup-2018-11-15/UpdateRestoreTestingPlan.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/UpdateRestoreTestingPlan.md "../../../goto/SdkForGoV2/backup-2018-11-15/UpdateRestoreTestingPlan.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateRestoreTestingPlan.md "../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateRestoreTestingPlan.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateRestoreTestingPlan.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateRestoreTestingPlan.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/UpdateRestoreTestingPlan.md "../../../goto/SdkForKotlin/backup-2018-11-15/UpdateRestoreTestingPlan.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateRestoreTestingPlan.md "../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateRestoreTestingPlan.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/UpdateRestoreTestingPlan.md "../../../goto/boto3/backup-2018-11-15/UpdateRestoreTestingPlan.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateRestoreTestingPlan.md "../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateRestoreTestingPlan.md")
