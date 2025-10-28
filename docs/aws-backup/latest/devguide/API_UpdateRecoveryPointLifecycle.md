# UpdateRecoveryPointLifecycle

Sets the transition lifecycle of a recovery point.

The lifecycle defines when a protected resource is transitioned to cold storage and when
it expires. AWS Backup transitions and expires backups automatically according to
the lifecycle that you define.

Resource types that can transition to cold storage are listed in the [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table. AWS Backup ignores this expression for
other resource types.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
days. Therefore, the “retention” setting must be 90 days greater than the “transition to
cold after days” setting. The “transition to cold after days” setting cannot be changed
after a backup has been transitioned to cold.

###### Important

If your lifecycle currently uses the parameters `DeleteAfterDays` and
`MoveToColdStorageAfterDays`, include these parameters and their values when you call
this operation. Not including them may result in your plan updating with null values.

This operation does not support continuous backups.

## Request Syntax

```
POST /backup-vaults/`backupVaultName`/recovery-points/`recoveryPointArn` HTTP/1.1
Content-type: application/json

{
   "Lifecycle": {
      "DeleteAfterDays": `number`,
      "MoveToColdStorageAfterDays": `number`,
      "OptInToArchiveForSupportedResources": `boolean`
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[backupVaultName](#API_UpdateRecoveryPointLifecycle_RequestSyntax "#API_UpdateRecoveryPointLifecycle_RequestSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the AWS
Region where they are created.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

**[recoveryPointArn](#API_UpdateRecoveryPointLifecycle_RequestSyntax "#API_UpdateRecoveryPointLifecycle_RequestSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[Lifecycle](#API_UpdateRecoveryPointLifecycle_RequestSyntax "#API_UpdateRecoveryPointLifecycle_RequestSyntax")**

The lifecycle defines when a protected resource is transitioned to cold storage and when
it expires. AWS Backup transitions and expires backups automatically according to
the lifecycle that you define.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
days. Therefore, the “retention” setting must be 90 days greater than the “transition to
cold after days” setting. The “transition to cold after days” setting cannot be changed
after a backup has been transitioned to cold.

Type: [Lifecycle](API_Lifecycle.md "API_Lifecycle.md") object

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupVaultArn": "***string***",
   "CalculatedLifecycle": {
      "DeleteAt": ***number***,
      "MoveToColdStorageAt": ***number***
   },
   "Lifecycle": {
      "DeleteAfterDays": ***number***,
      "MoveToColdStorageAfterDays": ***number***,
      "OptInToArchiveForSupportedResources": ***boolean***
   },
   "RecoveryPointArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupVaultArn](#API_UpdateRecoveryPointLifecycle_ResponseSyntax "#API_UpdateRecoveryPointLifecycle_ResponseSyntax")**

An ARN that uniquely identifies a backup vault; for example,
`arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.

Type: String

**[CalculatedLifecycle](#API_UpdateRecoveryPointLifecycle_ResponseSyntax "#API_UpdateRecoveryPointLifecycle_ResponseSyntax")**

A `CalculatedLifecycle` object containing `DeleteAt` and
`MoveToColdStorageAt` timestamps.

Type: [CalculatedLifecycle](API_CalculatedLifecycle.md "API_CalculatedLifecycle.md") object

**[Lifecycle](#API_UpdateRecoveryPointLifecycle_ResponseSyntax "#API_UpdateRecoveryPointLifecycle_ResponseSyntax")**

The lifecycle defines when a protected resource is transitioned to cold storage and when
it expires. AWS Backup transitions and expires backups automatically according to
the lifecycle that you define.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
days. Therefore, the “retention” setting must be 90 days greater than the “transition to
cold after days” setting. The “transition to cold after days” setting cannot be changed
after a backup has been transitioned to cold.

Resource types that can transition to cold storage are listed in the [Feature availability
by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table. AWS Backup ignores this expression for other resource types.

Type: [Lifecycle](API_Lifecycle.md "API_Lifecycle.md") object

**[RecoveryPointArn](#API_UpdateRecoveryPointLifecycle_ResponseSyntax "#API_UpdateRecoveryPointLifecycle_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/UpdateRecoveryPointLifecycle.md "../../../goto/cli2/backup-2018-11-15/UpdateRecoveryPointLifecycle.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/UpdateRecoveryPointLifecycle.md "../../../goto/DotNetSDKV3/backup-2018-11-15/UpdateRecoveryPointLifecycle.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/UpdateRecoveryPointLifecycle.md "../../../goto/SdkForCpp/backup-2018-11-15/UpdateRecoveryPointLifecycle.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/UpdateRecoveryPointLifecycle.md "../../../goto/SdkForGoV2/backup-2018-11-15/UpdateRecoveryPointLifecycle.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateRecoveryPointLifecycle.md "../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateRecoveryPointLifecycle.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateRecoveryPointLifecycle.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateRecoveryPointLifecycle.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/UpdateRecoveryPointLifecycle.md "../../../goto/SdkForKotlin/backup-2018-11-15/UpdateRecoveryPointLifecycle.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateRecoveryPointLifecycle.md "../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateRecoveryPointLifecycle.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/UpdateRecoveryPointLifecycle.md "../../../goto/boto3/backup-2018-11-15/UpdateRecoveryPointLifecycle.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateRecoveryPointLifecycle.md "../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateRecoveryPointLifecycle.md")
