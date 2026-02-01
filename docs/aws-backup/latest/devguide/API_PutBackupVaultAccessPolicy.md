# PutBackupVaultAccessPolicy

Sets a resource-based policy that is used to manage access permissions on the target
backup vault. Requires a backup vault name and an access policy document in JSON
format.

## Request Syntax

```
PUT /backup-vaults/`backupVaultName`/access-policy HTTP/1.1
Content-type: application/json

{
   "Policy": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[backupVaultName](#API_PutBackupVaultAccessPolicy_RequestSyntax "#API_PutBackupVaultAccessPolicy_RequestSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the AWS
Region where they are created.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[Policy](#API_PutBackupVaultAccessPolicy_RequestSyntax "#API_PutBackupVaultAccessPolicy_RequestSyntax")**

The backup vault access policy document in JSON format.

Type: String

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/PutBackupVaultAccessPolicy.md "../../../goto/cli2/backup-2018-11-15/PutBackupVaultAccessPolicy.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/PutBackupVaultAccessPolicy.md "../../../goto/DotNetSDKV4/backup-2018-11-15/PutBackupVaultAccessPolicy.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/PutBackupVaultAccessPolicy.md "../../../goto/SdkForCpp/backup-2018-11-15/PutBackupVaultAccessPolicy.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/PutBackupVaultAccessPolicy.md "../../../goto/SdkForGoV2/backup-2018-11-15/PutBackupVaultAccessPolicy.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/PutBackupVaultAccessPolicy.md "../../../goto/SdkForJavaV2/backup-2018-11-15/PutBackupVaultAccessPolicy.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/PutBackupVaultAccessPolicy.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/PutBackupVaultAccessPolicy.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/PutBackupVaultAccessPolicy.md "../../../goto/SdkForKotlin/backup-2018-11-15/PutBackupVaultAccessPolicy.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/PutBackupVaultAccessPolicy.md "../../../goto/SdkForPHPV3/backup-2018-11-15/PutBackupVaultAccessPolicy.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/PutBackupVaultAccessPolicy.md "../../../goto/boto3/backup-2018-11-15/PutBackupVaultAccessPolicy.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/PutBackupVaultAccessPolicy.md "../../../goto/SdkForRubyV3/backup-2018-11-15/PutBackupVaultAccessPolicy.md")
