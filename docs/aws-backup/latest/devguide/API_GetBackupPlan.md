# GetBackupPlan

Returns `BackupPlan` details for the specified `BackupPlanId`. The
details are the body of a backup plan in JSON format, in addition to plan metadata.

## Request Syntax

```
GET /backup/plans/`backupPlanId`/?MaxScheduledRunsPreview=`MaxScheduledRunsPreview`&versionId=`VersionId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[backupPlanId](#API_GetBackupPlan_RequestSyntax "#API_GetBackupPlan_RequestSyntax")**

Uniquely identifies a backup plan.

Required: Yes

**[MaxScheduledRunsPreview](#API_GetBackupPlan_RequestSyntax "#API_GetBackupPlan_RequestSyntax")**

Number of future scheduled backup runs to preview. When set to 0 (default), no scheduled runs preview is included in the response. Valid range is 0-10.

Valid Range: Minimum value of 0. Maximum value of 10.

**[VersionId](#API_GetBackupPlan_RequestSyntax "#API_GetBackupPlan_RequestSyntax")**

Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes
long. Version IDs cannot be edited.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "AdvancedBackupSettings": [
      {
         "BackupOptions": {
            "***string***" : "***string***"
         },
         "ResourceType": "***string***"
      }
   ],
   "BackupPlan": {
      "AdvancedBackupSettings": [
         {
            "BackupOptions": {
               "***string***" : "***string***"
            },
            "ResourceType": "***string***"
         }
      ],
      "BackupPlanName": "***string***",
      "Rules": [
         {
            "CompletionWindowMinutes": ***number***,
            "CopyActions": [
               {
                  "DestinationBackupVaultArn": "***string***",
                  "Lifecycle": {
                     "DeleteAfterDays": ***number***,
                     "MoveToColdStorageAfterDays": ***number***,
                     "OptInToArchiveForSupportedResources": ***boolean***
                  }
               }
            ],
            "EnableContinuousBackup": ***boolean***,
            "IndexActions": [
               {
                  "ResourceTypes": [ "***string***" ]
               }
            ],
            "Lifecycle": {
               "DeleteAfterDays": ***number***,
               "MoveToColdStorageAfterDays": ***number***,
               "OptInToArchiveForSupportedResources": ***boolean***
            },
            "RecoveryPointTags": {
               "***string***" : "***string***"
            },
            "RuleId": "***string***",
            "RuleName": "***string***",
            "ScheduleExpression": "***string***",
            "ScheduleExpressionTimezone": "***string***",
            "StartWindowMinutes": ***number***,
            "TargetBackupVaultName": "***string***"
         }
      ]
   },
   "BackupPlanArn": "***string***",
   "BackupPlanId": "***string***",
   "CreationDate": ***number***,
   "CreatorRequestId": "***string***",
   "DeletionDate": ***number***,
   "LastExecutionDate": ***number***,
   "ScheduledRunsPreview": [
      {
         "ExecutionTime": ***number***,
         "RuleExecutionType": "***string***",
         "RuleId": "***string***"
      }
   ],
   "VersionId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AdvancedBackupSettings](#API_GetBackupPlan_ResponseSyntax "#API_GetBackupPlan_ResponseSyntax")**

Contains a list of `BackupOptions` for each resource type. The list is
populated only if the advanced option is set for the backup plan.

Type: Array of [AdvancedBackupSetting](API_AdvancedBackupSetting.md "API_AdvancedBackupSetting.md") objects

**[BackupPlan](#API_GetBackupPlan_ResponseSyntax "#API_GetBackupPlan_ResponseSyntax")**

Specifies the body of a backup plan. Includes a `BackupPlanName` and one or
more sets of `Rules`.

Type: [BackupPlan](API_BackupPlan.md "API_BackupPlan.md") object

**[BackupPlanArn](#API_GetBackupPlan_ResponseSyntax "#API_GetBackupPlan_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
`arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`.

Type: String

**[BackupPlanId](#API_GetBackupPlan_ResponseSyntax "#API_GetBackupPlan_ResponseSyntax")**

Uniquely identifies a backup plan.

Type: String

**[CreationDate](#API_GetBackupPlan_ResponseSyntax "#API_GetBackupPlan_ResponseSyntax")**

The date and time that a backup plan is created, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[CreatorRequestId](#API_GetBackupPlan_ResponseSyntax "#API_GetBackupPlan_ResponseSyntax")**

A unique string that identifies the request and allows failed requests to be retried
without the risk of running the operation twice.

Type: String

**[DeletionDate](#API_GetBackupPlan_ResponseSyntax "#API_GetBackupPlan_ResponseSyntax")**

The date and time that a backup plan is deleted, in Unix format and Coordinated
Universal Time (UTC). The value of `DeletionDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[LastExecutionDate](#API_GetBackupPlan_ResponseSyntax "#API_GetBackupPlan_ResponseSyntax")**

The last time this backup plan was run. A date and time,
in Unix format and Coordinated Universal Time (UTC). The value of
`LastExecutionDate` is accurate to milliseconds. For example, the value
1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Type: Timestamp

**[ScheduledRunsPreview](#API_GetBackupPlan_ResponseSyntax "#API_GetBackupPlan_ResponseSyntax")**

List of upcoming scheduled backup runs. Only included when `MaxScheduledRunsPreview` parameter is greater than 0. Contains up to 10 future backup executions with their scheduled times, execution types, and associated rule IDs.

Type: Array of [ScheduledPlanExecutionMember](API_ScheduledPlanExecutionMember.md "API_ScheduledPlanExecutionMember.md") objects

**[VersionId](#API_GetBackupPlan_ResponseSyntax "#API_GetBackupPlan_ResponseSyntax")**

Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes
long. Version IDs cannot be edited.

Type: String

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/GetBackupPlan.md "../../../goto/cli2/backup-2018-11-15/GetBackupPlan.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/GetBackupPlan.md "../../../goto/DotNetSDKV3/backup-2018-11-15/GetBackupPlan.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/GetBackupPlan.md "../../../goto/SdkForCpp/backup-2018-11-15/GetBackupPlan.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/GetBackupPlan.md "../../../goto/SdkForGoV2/backup-2018-11-15/GetBackupPlan.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/GetBackupPlan.md "../../../goto/SdkForJavaV2/backup-2018-11-15/GetBackupPlan.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetBackupPlan.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetBackupPlan.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/GetBackupPlan.md "../../../goto/SdkForKotlin/backup-2018-11-15/GetBackupPlan.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/GetBackupPlan.md "../../../goto/SdkForPHPV3/backup-2018-11-15/GetBackupPlan.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/GetBackupPlan.md "../../../goto/boto3/backup-2018-11-15/GetBackupPlan.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/GetBackupPlan.md "../../../goto/SdkForRubyV3/backup-2018-11-15/GetBackupPlan.md")
