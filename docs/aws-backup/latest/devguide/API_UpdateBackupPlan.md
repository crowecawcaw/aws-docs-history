# UpdateBackupPlan

Updates the specified backup plan. The new version is uniquely identified by its ID.

## Request Syntax

```
POST /backup/plans/`backupPlanId` HTTP/1.1
Content-type: application/json

{
   "BackupPlan": {
      "AdvancedBackupSettings": [
         {
            "BackupOptions": {
               "`string`" : "`string`"
            },
            "ResourceType": "`string`"
         }
      ],
      "BackupPlanName": "`string`",
      "Rules": [
         {
            "CompletionWindowMinutes": `number`,
            "CopyActions": [
               {
                  "DestinationBackupVaultArn": "`string`",
                  "Lifecycle": {
                     "DeleteAfterDays": `number`,
                     "MoveToColdStorageAfterDays": `number`,
                     "OptInToArchiveForSupportedResources": `boolean`
                  }
               }
            ],
            "EnableContinuousBackup": `boolean`,
            "IndexActions": [
               {
                  "ResourceTypes": [ "`string`" ]
               }
            ],
            "Lifecycle": {
               "DeleteAfterDays": `number`,
               "MoveToColdStorageAfterDays": `number`,
               "OptInToArchiveForSupportedResources": `boolean`
            },
            "RecoveryPointTags": {
               "`string`" : "`string`"
            },
            "RuleName": "`string`",
            "ScheduleExpression": "`string`",
            "ScheduleExpressionTimezone": "`string`",
            "StartWindowMinutes": `number`,
            "TargetBackupVaultName": "`string`"
         }
      ]
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[backupPlanId](#API_UpdateBackupPlan_RequestSyntax "#API_UpdateBackupPlan_RequestSyntax")**

The ID of the backup plan.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[BackupPlan](#API_UpdateBackupPlan_RequestSyntax "#API_UpdateBackupPlan_RequestSyntax")**

The body of a backup plan. Includes a `BackupPlanName` and one or
more sets of `Rules`.

Type: [BackupPlanInput](API_BackupPlanInput.md "API_BackupPlanInput.md") object

Required: Yes

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
   "BackupPlanArn": "***string***",
   "BackupPlanId": "***string***",
   "CreationDate": ***number***,
   "VersionId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AdvancedBackupSettings](#API_UpdateBackupPlan_ResponseSyntax "#API_UpdateBackupPlan_ResponseSyntax")**

Contains a list of `BackupOptions` for each resource type.

Type: Array of [AdvancedBackupSetting](API_AdvancedBackupSetting.md "API_AdvancedBackupSetting.md") objects

**[BackupPlanArn](#API_UpdateBackupPlan_ResponseSyntax "#API_UpdateBackupPlan_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
`arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`.

Type: String

**[BackupPlanId](#API_UpdateBackupPlan_ResponseSyntax "#API_UpdateBackupPlan_ResponseSyntax")**

Uniquely identifies a backup plan.

Type: String

**[CreationDate](#API_UpdateBackupPlan_ResponseSyntax "#API_UpdateBackupPlan_ResponseSyntax")**

The date and time a backup plan is created, in Unix format and Coordinated Universal
Time (UTC). The value of `CreationDate` is accurate to milliseconds. For
example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[VersionId](#API_UpdateBackupPlan_ResponseSyntax "#API_UpdateBackupPlan_ResponseSyntax")**

Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes
long. Version Ids cannot be edited.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/UpdateBackupPlan.md "../../../goto/cli2/backup-2018-11-15/UpdateBackupPlan.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/UpdateBackupPlan.md "../../../goto/DotNetSDKV3/backup-2018-11-15/UpdateBackupPlan.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/UpdateBackupPlan.md "../../../goto/SdkForCpp/backup-2018-11-15/UpdateBackupPlan.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/UpdateBackupPlan.md "../../../goto/SdkForGoV2/backup-2018-11-15/UpdateBackupPlan.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateBackupPlan.md "../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateBackupPlan.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateBackupPlan.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateBackupPlan.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/UpdateBackupPlan.md "../../../goto/SdkForKotlin/backup-2018-11-15/UpdateBackupPlan.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateBackupPlan.md "../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateBackupPlan.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/UpdateBackupPlan.md "../../../goto/boto3/backup-2018-11-15/UpdateBackupPlan.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateBackupPlan.md "../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateBackupPlan.md")
