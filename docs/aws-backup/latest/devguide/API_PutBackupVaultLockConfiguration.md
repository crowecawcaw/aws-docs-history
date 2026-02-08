# PutBackupVaultLockConfiguration

Applies AWS Backup Vault Lock to a backup vault, preventing attempts to delete
any recovery point stored in or created in a backup vault. Vault Lock also prevents
attempts to update the lifecycle policy that controls the retention period of any recovery
point currently stored in a backup vault. If specified, Vault Lock enforces a minimum and
maximum retention period for future backup and copy jobs that target a backup vault.

###### Note

AWS Backup Vault Lock has been assessed by Cohasset Associates for use in environments
that are subject to SEC 17a-4, CFTC, and FINRA regulations. For more information about
how AWS Backup Vault Lock relates to these regulations, see the
[Cohasset Associates
Compliance Assessment.](samples/cohassetreport.md "samples/cohassetreport.md")

For more information, see [AWS Backup Vault Lock](vault-lock.md "vault-lock.md").

## Request Syntax

```
PUT /backup-vaults/`backupVaultName`/vault-lock HTTP/1.1
Content-type: application/json

{
   "ChangeableForDays": `number`,
   "MaxRetentionDays": `number`,
   "MinRetentionDays": `number`
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[backupVaultName](#API_PutBackupVaultLockConfiguration_RequestSyntax "#API_PutBackupVaultLockConfiguration_RequestSyntax")**

The AWS Backup Vault Lock configuration that specifies the name of the backup
vault it protects.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[ChangeableForDays](#API_PutBackupVaultLockConfiguration_RequestSyntax "#API_PutBackupVaultLockConfiguration_RequestSyntax")**

The AWS Backup Vault Lock configuration that specifies the number of days before
the lock date. For example, setting `ChangeableForDays` to 30 on Jan. 1, 2022 at
8pm UTC will set the lock date to Jan. 31, 2022 at 8pm UTC.

AWS Backup enforces a 72-hour cooling-off period before Vault Lock takes effect
and becomes immutable. Therefore, you must set `ChangeableForDays` to 3 or
greater.

The maximum value you can specify is 36,500 days (approximately 100 years).

Before the lock date, you can delete Vault Lock from the vault using
`DeleteBackupVaultLockConfiguration` or change the Vault Lock configuration
using `PutBackupVaultLockConfiguration`. On and after the lock date, the Vault
Lock becomes immutable and cannot be changed or deleted.

If this parameter is not specified, you can delete Vault Lock from the vault using
`DeleteBackupVaultLockConfiguration` or change the Vault Lock configuration
using `PutBackupVaultLockConfiguration` at any time.

Type: Long

Required: No

**[MaxRetentionDays](#API_PutBackupVaultLockConfiguration_RequestSyntax "#API_PutBackupVaultLockConfiguration_RequestSyntax")**

The AWS Backup Vault Lock configuration that specifies the maximum retention
period that the vault retains its recovery points. This setting can be useful if, for
example, your organization's policies require you to destroy certain data after retaining
it for four years (1460 days).

If this parameter is not included, Vault Lock does not enforce a maximum retention
period on the recovery points in the vault. If this parameter is included without a value,
Vault Lock will not enforce a maximum retention period.

If this parameter is specified, any backup or copy job to the vault must have a
lifecycle policy with a retention period equal to or shorter than the maximum retention
period. If the job's retention period is longer than that maximum retention period, then
the vault fails the backup or copy job, and you should either modify your lifecycle
settings or use a different vault. The longest maximum retention period
you can specify is 36500 days (approximately 100 years).
Recovery points already saved in the vault prior to
Vault Lock are not affected.

Type: Long

Required: No

**[MinRetentionDays](#API_PutBackupVaultLockConfiguration_RequestSyntax "#API_PutBackupVaultLockConfiguration_RequestSyntax")**

The AWS Backup Vault Lock configuration that specifies the minimum retention
period that the vault retains its recovery points. This setting can be useful if, for
example, your organization's policies require you to retain certain data for at least seven
years (2555 days).

This parameter is required when a vault lock is created through AWS CloudFormation;
otherwise, this parameter is optional. If this parameter is not specified, Vault Lock will
not enforce a minimum retention period.

If this parameter is specified, any backup or copy job to the vault must have a
lifecycle policy with a retention period equal to or longer than the minimum retention
period. If the job's retention period is shorter than that minimum retention period, then
the vault fails that backup or copy job, and you should either modify your lifecycle
settings or use a different vault. The shortest minimum retention period
you can specify is 1 day. Recovery points already saved in the vault prior to
Vault Lock are not affected.

Type: Long

Required: No

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/PutBackupVaultLockConfiguration.md "../../../goto/cli2/backup-2018-11-15/PutBackupVaultLockConfiguration.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/PutBackupVaultLockConfiguration.md "../../../goto/DotNetSDKV4/backup-2018-11-15/PutBackupVaultLockConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/PutBackupVaultLockConfiguration.md "../../../goto/SdkForCpp/backup-2018-11-15/PutBackupVaultLockConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/PutBackupVaultLockConfiguration.md "../../../goto/SdkForGoV2/backup-2018-11-15/PutBackupVaultLockConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/PutBackupVaultLockConfiguration.md "../../../goto/SdkForJavaV2/backup-2018-11-15/PutBackupVaultLockConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/PutBackupVaultLockConfiguration.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/PutBackupVaultLockConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/PutBackupVaultLockConfiguration.md "../../../goto/SdkForKotlin/backup-2018-11-15/PutBackupVaultLockConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/PutBackupVaultLockConfiguration.md "../../../goto/SdkForPHPV3/backup-2018-11-15/PutBackupVaultLockConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/PutBackupVaultLockConfiguration.md "../../../goto/boto3/backup-2018-11-15/PutBackupVaultLockConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/PutBackupVaultLockConfiguration.md "../../../goto/SdkForRubyV3/backup-2018-11-15/PutBackupVaultLockConfiguration.md")
