# DeleteBackupVaultAccessPolicy

Deletes the policy document that manages permissions on a backup vault.

## Request Syntax

```
DELETE /backup-vaults/`backupVaultName`/access-policy HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[backupVaultName](#API_DeleteBackupVaultAccessPolicy_RequestSyntax "#API_DeleteBackupVaultAccessPolicy_RequestSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the AWS
Region where they are created. They consist of lowercase letters, numbers, and
hyphens.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

## Request Body

The request does not have a request body.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md "../../../goto/cli2/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md "../../../goto/DotNetSDKV4/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md "../../../goto/SdkForCpp/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md "../../../goto/SdkForGoV2/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md "../../../goto/SdkForKotlin/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md "../../../goto/boto3/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DeleteBackupVaultAccessPolicy.md")
