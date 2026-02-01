# GetRestoreTestingInferredMetadata

This request returns the minimal required set of metadata needed to
start a restore job with secure default settings. `BackupVaultName`
and `RecoveryPointArn` are required parameters.
`BackupVaultAccountId` is an optional parameter.

## Request Syntax

```
GET /restore-testing/inferred-metadata?BackupVaultAccountId=`BackupVaultAccountId`&BackupVaultName=`BackupVaultName`&RecoveryPointArn=`RecoveryPointArn` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[BackupVaultAccountId](#API_GetRestoreTestingInferredMetadata_RequestSyntax "#API_GetRestoreTestingInferredMetadata_RequestSyntax")**

The account ID of the specified backup vault.

**[BackupVaultName](#API_GetRestoreTestingInferredMetadata_RequestSyntax "#API_GetRestoreTestingInferredMetadata_RequestSyntax")**

The name of a logical container where backups are stored. Backup
vaults are identified by names that are unique to the account used to
create them and the AWSRegion where they are created.
They consist of letters, numbers, and hyphens.

Required: Yes

**[RecoveryPointArn](#API_GetRestoreTestingInferredMetadata_RequestSyntax "#API_GetRestoreTestingInferredMetadata_RequestSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a recovery
point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "InferredMetadata": {
      "***string***" : "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[InferredMetadata](#API_GetRestoreTestingInferredMetadata_ResponseSyntax "#API_GetRestoreTestingInferredMetadata_ResponseSyntax")**

This is a string map of the metadata inferred from the request.

Type: String to string map

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/GetRestoreTestingInferredMetadata.md "../../../goto/cli2/backup-2018-11-15/GetRestoreTestingInferredMetadata.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/GetRestoreTestingInferredMetadata.md "../../../goto/DotNetSDKV4/backup-2018-11-15/GetRestoreTestingInferredMetadata.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/GetRestoreTestingInferredMetadata.md "../../../goto/SdkForCpp/backup-2018-11-15/GetRestoreTestingInferredMetadata.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/GetRestoreTestingInferredMetadata.md "../../../goto/SdkForGoV2/backup-2018-11-15/GetRestoreTestingInferredMetadata.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/GetRestoreTestingInferredMetadata.md "../../../goto/SdkForJavaV2/backup-2018-11-15/GetRestoreTestingInferredMetadata.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetRestoreTestingInferredMetadata.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetRestoreTestingInferredMetadata.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/GetRestoreTestingInferredMetadata.md "../../../goto/SdkForKotlin/backup-2018-11-15/GetRestoreTestingInferredMetadata.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/GetRestoreTestingInferredMetadata.md "../../../goto/SdkForPHPV3/backup-2018-11-15/GetRestoreTestingInferredMetadata.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/GetRestoreTestingInferredMetadata.md "../../../goto/boto3/backup-2018-11-15/GetRestoreTestingInferredMetadata.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/GetRestoreTestingInferredMetadata.md "../../../goto/SdkForRubyV3/backup-2018-11-15/GetRestoreTestingInferredMetadata.md")
