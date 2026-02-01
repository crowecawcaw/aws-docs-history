# DeleteBackupPlan

Deletes a backup plan. A backup plan can only be deleted after all associated selections
of resources have been deleted. Deleting a backup plan deletes the current version of a
backup plan. Previous versions, if any, will still exist.

## Request Syntax

```
DELETE /backup/plans/`backupPlanId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[backupPlanId](#API_DeleteBackupPlan_RequestSyntax "#API_DeleteBackupPlan_RequestSyntax")**

Uniquely identifies a backup plan.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupPlanArn": "***string***",
   "BackupPlanId": "***string***",
   "DeletionDate": ***number***,
   "VersionId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupPlanArn](#API_DeleteBackupPlan_ResponseSyntax "#API_DeleteBackupPlan_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example,
`arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`.

Type: String

**[BackupPlanId](#API_DeleteBackupPlan_ResponseSyntax "#API_DeleteBackupPlan_ResponseSyntax")**

Uniquely identifies a backup plan.

Type: String

**[DeletionDate](#API_DeleteBackupPlan_ResponseSyntax "#API_DeleteBackupPlan_ResponseSyntax")**

The date and time a backup plan is deleted, in Unix format and Coordinated Universal
Time (UTC). The value of `DeletionDate` is accurate to milliseconds. For
example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[VersionId](#API_DeleteBackupPlan_ResponseSyntax "#API_DeleteBackupPlan_ResponseSyntax")**

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

**InvalidRequestException**

Indicates that something is wrong with the input to the request. For example, a
parameter is of the wrong type.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DeleteBackupPlan.md "../../../goto/cli2/backup-2018-11-15/DeleteBackupPlan.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/DeleteBackupPlan.md "../../../goto/DotNetSDKV4/backup-2018-11-15/DeleteBackupPlan.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DeleteBackupPlan.md "../../../goto/SdkForCpp/backup-2018-11-15/DeleteBackupPlan.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DeleteBackupPlan.md "../../../goto/SdkForGoV2/backup-2018-11-15/DeleteBackupPlan.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DeleteBackupPlan.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DeleteBackupPlan.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteBackupPlan.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteBackupPlan.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DeleteBackupPlan.md "../../../goto/SdkForKotlin/backup-2018-11-15/DeleteBackupPlan.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DeleteBackupPlan.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DeleteBackupPlan.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DeleteBackupPlan.md "../../../goto/boto3/backup-2018-11-15/DeleteBackupPlan.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DeleteBackupPlan.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DeleteBackupPlan.md")
