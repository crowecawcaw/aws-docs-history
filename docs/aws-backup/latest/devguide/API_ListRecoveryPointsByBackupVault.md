# ListRecoveryPointsByBackupVault

Returns detailed information about the recovery points stored in a backup vault.

## Request Syntax

```
GET /backup-vaults/`backupVaultName`/recovery-points/?backupPlanId=`ByBackupPlanId`&backupVaultAccountId=`BackupVaultAccountId`&createdAfter=`ByCreatedAfter`&createdBefore=`ByCreatedBefore`&maxResults=`MaxResults`&nextToken=`NextToken`&parentRecoveryPointArn=`ByParentRecoveryPointArn`&resourceArn=`ByResourceArn`&resourceType=`ByResourceType` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[BackupVaultAccountId](#API_ListRecoveryPointsByBackupVault_RequestSyntax "#API_ListRecoveryPointsByBackupVault_RequestSyntax")**

This parameter will sort the list of recovery points by account ID.

Pattern: `^[0-9]{12}$`

**[backupVaultName](#API_ListRecoveryPointsByBackupVault_RequestSyntax "#API_ListRecoveryPointsByBackupVault_RequestSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the AWS
Region where they are created.

###### Note

Backup vault name might not be available when a supported service creates the
backup.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

**[ByBackupPlanId](#API_ListRecoveryPointsByBackupVault_RequestSyntax "#API_ListRecoveryPointsByBackupVault_RequestSyntax")**

Returns only recovery points that match the specified backup plan ID.

**[ByCreatedAfter](#API_ListRecoveryPointsByBackupVault_RequestSyntax "#API_ListRecoveryPointsByBackupVault_RequestSyntax")**

Returns only recovery points that were created after the specified timestamp.

**[ByCreatedBefore](#API_ListRecoveryPointsByBackupVault_RequestSyntax "#API_ListRecoveryPointsByBackupVault_RequestSyntax")**

Returns only recovery points that were created before the specified timestamp.

**[ByParentRecoveryPointArn](#API_ListRecoveryPointsByBackupVault_RequestSyntax "#API_ListRecoveryPointsByBackupVault_RequestSyntax")**

This returns only recovery points that match the specified parent (composite)
recovery point Amazon Resource Name (ARN).

**[ByResourceArn](#API_ListRecoveryPointsByBackupVault_RequestSyntax "#API_ListRecoveryPointsByBackupVault_RequestSyntax")**

Returns only recovery points that match the specified resource Amazon Resource Name
(ARN).

**[ByResourceType](#API_ListRecoveryPointsByBackupVault_RequestSyntax "#API_ListRecoveryPointsByBackupVault_RequestSyntax")**

Returns only recovery points that match the specified resource type(s):

- `Aurora` for Amazon Aurora
- `CloudFormation` for AWS CloudFormation
- `DocumentDB` for Amazon DocumentDB (with MongoDB compatibility)
- `DynamoDB` for Amazon DynamoDB
- `EBS` for Amazon Elastic Block Store
- `EC2` for Amazon Elastic Compute Cloud
- `EFS` for Amazon Elastic File System
- `FSx` for Amazon FSx
- `Neptune` for Amazon Neptune
- `RDS` for Amazon Relational Database Service
- `Redshift` for Amazon Redshift
- `S3` for Amazon Simple Storage Service (Amazon S3)
- `SAP HANA on Amazon EC2` for SAP HANA databases
  on Amazon Elastic Compute Cloud instances
- `Storage Gateway` for AWS Storage Gateway
- `Timestream` for Amazon Timestream
- `VirtualMachine` for VMware virtual machines

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

**[MaxResults](#API_ListRecoveryPointsByBackupVault_RequestSyntax "#API_ListRecoveryPointsByBackupVault_RequestSyntax")**

The maximum number of items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListRecoveryPointsByBackupVault_RequestSyntax "#API_ListRecoveryPointsByBackupVault_RequestSyntax")**

The next item following a partial list of returned items. For example, if a request is
made to return `MaxResults` number of items, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "RecoveryPoints": [
      {
         "BackupSizeInBytes": ***number***,
         "BackupVaultArn": "***string***",
         "BackupVaultName": "***string***",
         "CalculatedLifecycle": {
            "DeleteAt": ***number***,
            "MoveToColdStorageAt": ***number***
         },
         "CompletionDate": ***number***,
         "CompositeMemberIdentifier": "***string***",
         "CreatedBy": {
            "BackupPlanArn": "***string***",
            "BackupPlanId": "***string***",
            "BackupPlanName": "***string***",
            "BackupPlanVersion": "***string***",
            "BackupRuleCron": "***string***",
            "BackupRuleId": "***string***",
            "BackupRuleName": "***string***",
            "BackupRuleTimezone": "***string***"
         },
         "CreationDate": ***number***,
         "EncryptionKeyArn": "***string***",
         "IamRoleArn": "***string***",
         "IndexStatus": "***string***",
         "IndexStatusMessage": "***string***",
         "InitiationDate": ***number***,
         "IsEncrypted": ***boolean***,
         "IsParent": ***boolean***,
         "LastRestoreTime": ***number***,
         "Lifecycle": {
            "DeleteAfterDays": ***number***,
            "MoveToColdStorageAfterDays": ***number***,
            "OptInToArchiveForSupportedResources": ***boolean***
         },
         "ParentRecoveryPointArn": "***string***",
         "RecoveryPointArn": "***string***",
         "ResourceArn": "***string***",
         "ResourceName": "***string***",
         "ResourceType": "***string***",
         "SourceBackupVaultArn": "***string***",
         "Status": "***string***",
         "StatusMessage": "***string***",
         "VaultType": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListRecoveryPointsByBackupVault_ResponseSyntax "#API_ListRecoveryPointsByBackupVault_ResponseSyntax")**

The next item following a partial list of returned items. For example, if a request is
made to return `MaxResults` number of items, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

Type: String

**[RecoveryPoints](#API_ListRecoveryPointsByBackupVault_ResponseSyntax "#API_ListRecoveryPointsByBackupVault_ResponseSyntax")**

An array of objects that contain detailed information about recovery points saved in a
backup vault.

Type: Array of [RecoveryPointByBackupVault](API_RecoveryPointByBackupVault.md "API_RecoveryPointByBackupVault.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListRecoveryPointsByBackupVault.md "../../../goto/cli2/backup-2018-11-15/ListRecoveryPointsByBackupVault.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListRecoveryPointsByBackupVault.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListRecoveryPointsByBackupVault.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListRecoveryPointsByBackupVault.md "../../../goto/SdkForCpp/backup-2018-11-15/ListRecoveryPointsByBackupVault.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListRecoveryPointsByBackupVault.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListRecoveryPointsByBackupVault.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListRecoveryPointsByBackupVault.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListRecoveryPointsByBackupVault.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRecoveryPointsByBackupVault.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRecoveryPointsByBackupVault.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListRecoveryPointsByBackupVault.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListRecoveryPointsByBackupVault.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListRecoveryPointsByBackupVault.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListRecoveryPointsByBackupVault.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListRecoveryPointsByBackupVault.md "../../../goto/boto3/backup-2018-11-15/ListRecoveryPointsByBackupVault.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListRecoveryPointsByBackupVault.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListRecoveryPointsByBackupVault.md")
