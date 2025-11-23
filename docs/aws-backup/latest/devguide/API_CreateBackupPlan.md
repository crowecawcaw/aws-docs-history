# CreateBackupPlan

Creates a backup plan using a backup plan name and backup rules. A backup plan is a
document that contains information that AWS Backup uses to schedule tasks that
create recovery points for resources.

If you call `CreateBackupPlan` with a plan that already exists, you receive
an `AlreadyExistsException` exception.

## Request Syntax

```
PUT /backup/plans/ HTTP/1.1
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
                     "DeleteAfterEvent": "`string`",
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
               "DeleteAfterEvent": "`string`",
               "MoveToColdStorageAfterDays": `number`,
               "OptInToArchiveForSupportedResources": `boolean`
            },
            "RecoveryPointTags": {
               "`string`" : "`string`"
            },
            "RuleName": "`string`",
            "ScanActions": [
               {
                  "MalwareScanner": "`string`",
                  "ScanMode": "`string`"
               }
            ],
            "ScheduleExpression": "`string`",
            "ScheduleExpressionTimezone": "`string`",
            "StartWindowMinutes": `number`,
            "TargetBackupVaultName": "`string`",
            "TargetLogicallyAirGappedBackupVaultArn": "`string`"
         }
      ],
      "ScanSettings": [
         {
            "MalwareScanner": "`string`",
            "ResourceTypes": [ "`string`" ],
            "ScannerRoleArn": "`string`"
         }
      ]
   },
   "BackupPlanTags": {
      "`string`" : "`string`"
   },
   "CreatorRequestId": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[BackupPlan](#API_CreateBackupPlan_RequestSyntax "#API_CreateBackupPlan_RequestSyntax")**

The body of a backup plan. Includes a `BackupPlanName` and one or
more sets of `Rules`.

Type: [BackupPlanInput](API_BackupPlanInput.md "API_BackupPlanInput.md") object

Required: Yes

**[BackupPlanTags](#API_CreateBackupPlan_RequestSyntax "#API_CreateBackupPlan_RequestSyntax")**

The tags to assign to the backup plan.

Type: String to string map

Required: No

**[CreatorRequestId](#API_CreateBackupPlan_RequestSyntax "#API_CreateBackupPlan_RequestSyntax")**

Identifies the request and allows failed requests to be retried without the risk of
running the operation twice. If the request includes a `CreatorRequestId` that
matches an existing backup plan, that plan is returned. This parameter is optional.

If used, this parameter must contain 1 to 50 alphanumeric or '-\_.' characters.

Type: String

Required: No

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

**[AdvancedBackupSettings](#API_CreateBackupPlan_ResponseSyntax "#API_CreateBackupPlan_ResponseSyntax")**

The settings for a resource type. This option is only
available for Windows Volume Shadow Copy Service (VSS) backup jobs.

Type: Array of [AdvancedBackupSetting](API_AdvancedBackupSetting.md "API_AdvancedBackupSetting.md") objects

**[BackupPlanArn](#API_CreateBackupPlan_ResponseSyntax "#API_CreateBackupPlan_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
`arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`.

Type: String

**[BackupPlanId](#API_CreateBackupPlan_ResponseSyntax "#API_CreateBackupPlan_ResponseSyntax")**

The ID of the backup plan.

Type: String

**[CreationDate](#API_CreateBackupPlan_ResponseSyntax "#API_CreateBackupPlan_ResponseSyntax")**

The date and time that a backup plan is created, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[VersionId](#API_CreateBackupPlan_ResponseSyntax "#API_CreateBackupPlan_ResponseSyntax")**

Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes
long. They cannot be edited.

Type: String

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/CreateBackupPlan.md "../../../goto/cli2/backup-2018-11-15/CreateBackupPlan.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/CreateBackupPlan.md "../../../goto/DotNetSDKV3/backup-2018-11-15/CreateBackupPlan.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/CreateBackupPlan.md "../../../goto/SdkForCpp/backup-2018-11-15/CreateBackupPlan.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/CreateBackupPlan.md "../../../goto/SdkForGoV2/backup-2018-11-15/CreateBackupPlan.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/CreateBackupPlan.md "../../../goto/SdkForJavaV2/backup-2018-11-15/CreateBackupPlan.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateBackupPlan.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateBackupPlan.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/CreateBackupPlan.md "../../../goto/SdkForKotlin/backup-2018-11-15/CreateBackupPlan.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/CreateBackupPlan.md "../../../goto/SdkForPHPV3/backup-2018-11-15/CreateBackupPlan.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/CreateBackupPlan.md "../../../goto/boto3/backup-2018-11-15/CreateBackupPlan.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/CreateBackupPlan.md "../../../goto/SdkForRubyV3/backup-2018-11-15/CreateBackupPlan.md")
