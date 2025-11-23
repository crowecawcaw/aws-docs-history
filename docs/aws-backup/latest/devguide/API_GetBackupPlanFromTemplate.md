# GetBackupPlanFromTemplate

Returns the template specified by its `templateId` as a backup plan.

## Request Syntax

```
GET /backup/template/plans/`templateId`/toPlan HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[templateId](#API_GetBackupPlanFromTemplate_RequestSyntax "#API_GetBackupPlanFromTemplate_RequestSyntax")**

Uniquely identifies a stored backup plan template.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupPlanDocument": {
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
                     "DeleteAfterEvent": "***string***",
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
               "DeleteAfterEvent": "***string***",
               "MoveToColdStorageAfterDays": ***number***,
               "OptInToArchiveForSupportedResources": ***boolean***
            },
            "RecoveryPointTags": {
               "***string***" : "***string***"
            },
            "RuleId": "***string***",
            "RuleName": "***string***",
            "ScanActions": [
               {
                  "MalwareScanner": "***string***",
                  "ScanMode": "***string***"
               }
            ],
            "ScheduleExpression": "***string***",
            "ScheduleExpressionTimezone": "***string***",
            "StartWindowMinutes": ***number***,
            "TargetBackupVaultName": "***string***",
            "TargetLogicallyAirGappedBackupVaultArn": "***string***"
         }
      ],
      "ScanSettings": [
         {
            "MalwareScanner": "***string***",
            "ResourceTypes": [ "***string***" ],
            "ScannerRoleArn": "***string***"
         }
      ]
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupPlanDocument](#API_GetBackupPlanFromTemplate_ResponseSyntax "#API_GetBackupPlanFromTemplate_ResponseSyntax")**

Returns the body of a backup plan based on the target template, including the name,
rules, and backup vault of the plan.

Type: [BackupPlan](API_BackupPlan.md "API_BackupPlan.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/GetBackupPlanFromTemplate.md "../../../goto/cli2/backup-2018-11-15/GetBackupPlanFromTemplate.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/GetBackupPlanFromTemplate.md "../../../goto/DotNetSDKV3/backup-2018-11-15/GetBackupPlanFromTemplate.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/GetBackupPlanFromTemplate.md "../../../goto/SdkForCpp/backup-2018-11-15/GetBackupPlanFromTemplate.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/GetBackupPlanFromTemplate.md "../../../goto/SdkForGoV2/backup-2018-11-15/GetBackupPlanFromTemplate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/GetBackupPlanFromTemplate.md "../../../goto/SdkForJavaV2/backup-2018-11-15/GetBackupPlanFromTemplate.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetBackupPlanFromTemplate.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetBackupPlanFromTemplate.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/GetBackupPlanFromTemplate.md "../../../goto/SdkForKotlin/backup-2018-11-15/GetBackupPlanFromTemplate.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/GetBackupPlanFromTemplate.md "../../../goto/SdkForPHPV3/backup-2018-11-15/GetBackupPlanFromTemplate.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/GetBackupPlanFromTemplate.md "../../../goto/boto3/backup-2018-11-15/GetBackupPlanFromTemplate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/GetBackupPlanFromTemplate.md "../../../goto/SdkForRubyV3/backup-2018-11-15/GetBackupPlanFromTemplate.md")
