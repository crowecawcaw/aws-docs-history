# StartCopyJob

Starts a job to create a one-time copy of the specified resource.

Does not support continuous backups.

See [Copy
job retry](recov-point-create-a-copy.md#backup-copy-retry "recov-point-create-a-copy.md#backup-copy-retry") for information on how AWS Backup retries copy job
operations.

## Request Syntax

```
PUT /copy-jobs HTTP/1.1
Content-type: application/json

{
   "DestinationBackupVaultArn": "`string`",
   "IamRoleArn": "`string`",
   "IdempotencyToken": "`string`",
   "Lifecycle": {
      "DeleteAfterDays": `number`,
      "DeleteAfterEvent": "`string`",
      "MoveToColdStorageAfterDays": `number`,
      "OptInToArchiveForSupportedResources": `boolean`
   },
   "RecoveryPointArn": "`string`",
   "SourceBackupVaultName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[DestinationBackupVaultArn](#API_StartCopyJob_RequestSyntax "#API_StartCopyJob_RequestSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a destination backup vault to
copy to; for example,
`arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.

Type: String

Required: Yes

**[IamRoleArn](#API_StartCopyJob_RequestSyntax "#API_StartCopyJob_RequestSyntax")**

Specifies the IAM role ARN used to copy the target recovery point; for example,
`arn:aws:iam::123456789012:role/S3Access`.

Type: String

Required: Yes

**[IdempotencyToken](#API_StartCopyJob_RequestSyntax "#API_StartCopyJob_RequestSyntax")**

A customer-chosen string that you can use to distinguish between otherwise identical
calls to `StartCopyJob`. Retrying a successful request with the same idempotency
token results in a success message with no action taken.

Type: String

Required: No

**[Lifecycle](#API_StartCopyJob_RequestSyntax "#API_StartCopyJob_RequestSyntax")**

Specifies the time period, in days, before a recovery point transitions to cold storage
or is deleted.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90
days. Therefore, on the console, the retention setting must be 90 days greater than the
transition to cold after days setting. The transition to cold after days setting can't
be changed after a backup has been transitioned to cold.

Resource types that can transition to cold storage are listed in the [Feature
availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table. AWS Backup ignores this expression for
other resource types.

To remove the existing lifecycle and retention periods and keep your recovery points indefinitely,
specify -1 for `MoveToColdStorageAfterDays` and `DeleteAfterDays`.

Type: [Lifecycle](API_Lifecycle.md "API_Lifecycle.md") object

Required: No

**[RecoveryPointArn](#API_StartCopyJob_RequestSyntax "#API_StartCopyJob_RequestSyntax")**

An ARN that uniquely identifies a recovery point to use for the copy job; for example,
arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45.

Type: String

Required: Yes

**[SourceBackupVaultName](#API_StartCopyJob_RequestSyntax "#API_StartCopyJob_RequestSyntax")**

The name of a logical source container where backups are stored. Backup vaults are
identified by names that are unique to the account used to create them and the AWS Region where they are created.

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CopyJobId": "***string***",
   "CreationDate": ***number***,
   "IsParent": ***boolean***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CopyJobId](#API_StartCopyJob_ResponseSyntax "#API_StartCopyJob_ResponseSyntax")**

Uniquely identifies a copy job.

Type: String

**[CreationDate](#API_StartCopyJob_ResponseSyntax "#API_StartCopyJob_ResponseSyntax")**

The date and time that a copy job is created, in Unix format and Coordinated Universal
Time (UTC). The value of `CreationDate` is accurate to milliseconds. For
example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[IsParent](#API_StartCopyJob_ResponseSyntax "#API_StartCopyJob_ResponseSyntax")**

This is a returned boolean value indicating this is a parent (composite)
copy job.

Type: Boolean

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/StartCopyJob.md "../../../goto/cli2/backup-2018-11-15/StartCopyJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/StartCopyJob.md "../../../goto/DotNetSDKV3/backup-2018-11-15/StartCopyJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/StartCopyJob.md "../../../goto/SdkForCpp/backup-2018-11-15/StartCopyJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/StartCopyJob.md "../../../goto/SdkForGoV2/backup-2018-11-15/StartCopyJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/StartCopyJob.md "../../../goto/SdkForJavaV2/backup-2018-11-15/StartCopyJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/StartCopyJob.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/StartCopyJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/StartCopyJob.md "../../../goto/SdkForKotlin/backup-2018-11-15/StartCopyJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/StartCopyJob.md "../../../goto/SdkForPHPV3/backup-2018-11-15/StartCopyJob.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/StartCopyJob.md "../../../goto/boto3/backup-2018-11-15/StartCopyJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/StartCopyJob.md "../../../goto/SdkForRubyV3/backup-2018-11-15/StartCopyJob.md")
