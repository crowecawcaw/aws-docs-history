# StartScanJob

Starts scanning jobs for specific resources.

## Request Syntax

```
PUT /scan/job HTTP/1.1
Content-type: application/json

{
   "BackupVaultName": "`string`",
   "IamRoleArn": "`string`",
   "IdempotencyToken": "`string`",
   "MalwareScanner": "`string`",
   "RecoveryPointArn": "`string`",
   "ScanBaseRecoveryPointArn": "`string`",
   "ScanMode": "`string`",
   "ScannerRoleArn": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[BackupVaultName](#API_StartScanJob_RequestSyntax "#API_StartScanJob_RequestSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified by names that
are unique to the account used to create them and the AWS Region where they are created.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Type: String

Required: Yes

**[IamRoleArn](#API_StartScanJob_RequestSyntax "#API_StartScanJob_RequestSyntax")**

Specifies the IAM role ARN used to create the target recovery point; for example,
`arn:aws:iam::123456789012:role/S3Access`.

Type: String

Required: Yes

**[IdempotencyToken](#API_StartScanJob_RequestSyntax "#API_StartScanJob_RequestSyntax")**

A customer-chosen string that you can use to distinguish between otherwise identical
calls to `StartScanJob`. Retrying a successful request with the same idempotency
token results in a success message with no action taken.

Type: String

Required: No

**[MalwareScanner](#API_StartScanJob_RequestSyntax "#API_StartScanJob_RequestSyntax")**

Specifies the malware scanner used during the scan job. Currently only supports `GUARDDUTY`.

Type: String

Valid Values: `GUARDDUTY`

Required: Yes

**[RecoveryPointArn](#API_StartScanJob_RequestSyntax "#API_StartScanJob_RequestSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a recovery point. This is your target recovery point for a full scan.
If you are running an incremental scan, this will be your a recovery point which has been created after your base recovery point selection.

Type: String

Required: Yes

**[ScanBaseRecoveryPointArn](#API_StartScanJob_RequestSyntax "#API_StartScanJob_RequestSyntax")**

An ARN that uniquely identifies the base recovery point to be used for incremental scanning.

Type: String

Required: No

**[ScanMode](#API_StartScanJob_RequestSyntax "#API_StartScanJob_RequestSyntax")**

Specifies the scan type use for the scan job.

Includes:

- `FULL_SCAN` will scan the entire data lineage within the backup.
- `INCREMENTAL_SCAN` will scan the data difference between the target recovery point and base recovery point ARN.

Type: String

Valid Values: `FULL_SCAN | INCREMENTAL_SCAN`

Required: Yes

**[ScannerRoleArn](#API_StartScanJob_RequestSyntax "#API_StartScanJob_RequestSyntax")**

Specified the IAM scanner role ARN.

Type: String

Required: Yes

## Response Syntax

```
HTTP/1.1 201
Content-type: application/json

{
   "CreationDate": ***number***,
   "ScanJobId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

**[CreationDate](#API_StartScanJob_ResponseSyntax "#API_StartScanJob_ResponseSyntax")**

The date and time that a backup job is created, in Unix format and Coordinated Universal
Time (UTC). The value of `CreationDate` is accurate to milliseconds. For
example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[ScanJobId](#API_StartScanJob_ResponseSyntax "#API_StartScanJob_ResponseSyntax")**

Uniquely identifies a request to AWS Backup to back up a resource.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/StartScanJob.md "../../../goto/cli2/backup-2018-11-15/StartScanJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/StartScanJob.md "../../../goto/DotNetSDKV3/backup-2018-11-15/StartScanJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/StartScanJob.md "../../../goto/SdkForCpp/backup-2018-11-15/StartScanJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/StartScanJob.md "../../../goto/SdkForGoV2/backup-2018-11-15/StartScanJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/StartScanJob.md "../../../goto/SdkForJavaV2/backup-2018-11-15/StartScanJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/StartScanJob.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/StartScanJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/StartScanJob.md "../../../goto/SdkForKotlin/backup-2018-11-15/StartScanJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/StartScanJob.md "../../../goto/SdkForPHPV3/backup-2018-11-15/StartScanJob.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/StartScanJob.md "../../../goto/boto3/backup-2018-11-15/StartScanJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/StartScanJob.md "../../../goto/SdkForRubyV3/backup-2018-11-15/StartScanJob.md")
