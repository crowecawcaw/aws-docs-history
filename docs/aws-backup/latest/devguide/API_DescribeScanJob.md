# DescribeScanJob

Returns scan job details for the specified ScanJobID.

## Request Syntax

```
GET /scan/jobs/`ScanJobId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[ScanJobId](#API_DescribeScanJob_RequestSyntax "#API_DescribeScanJob_RequestSyntax")**

Uniquely identifies a request to AWS Backup to scan a resource.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountId": "***string***",
   "BackupVaultArn": "***string***",
   "BackupVaultName": "***string***",
   "CompletionDate": ***number***,
   "CreatedBy": {
      "BackupPlanArn": "***string***",
      "BackupPlanId": "***string***",
      "BackupPlanVersion": "***string***",
      "BackupRuleId": "***string***"
   },
   "CreationDate": ***number***,
   "IamRoleArn": "***string***",
   "MalwareScanner": "***string***",
   "RecoveryPointArn": "***string***",
   "ResourceArn": "***string***",
   "ResourceName": "***string***",
   "ResourceType": "***string***",
   "ScanBaseRecoveryPointArn": "***string***",
   "ScanId": "***string***",
   "ScanJobId": "***string***",
   "ScanMode": "***string***",
   "ScannerRoleArn": "***string***",
   "ScanResult": {
      "ScanResultStatus": "***string***"
   },
   "State": "***string***",
   "StatusMessage": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AccountId](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

Returns the account ID that owns the scan job.

Pattern: `^[0-9]{12}$`

Type: String

**[BackupVaultArn](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
`arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`

Type: String

**[BackupVaultName](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified by names that are
unique to the account used to create them and the AWS Region where they are created.

Pattern: `^[a-zA-Z0-9\-\_\.]{2,50}$`

Type: String

**[CompletionDate](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

The date and time that a backup index finished creation, in Unix format and Coordinated
Universal Time (UTC). The value of `CompletionDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[CreatedBy](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

Contains identifying information about the creation of a scan job, including the backup plan and rule that initiated the scan.

Type: [ScanJobCreator](API_ScanJobCreator.md "API_ScanJobCreator.md") object

**[CreationDate](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

The date and time that a backup index finished creation, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[IamRoleArn](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
`arn:aws:iam::123456789012:role/S3Access`.

Type: String

**[MalwareScanner](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

The scanning engine used for the corresponding scan job. Currently only `GUARDUTY` is supported.

Type: String

Valid Values: `GUARDDUTY`

**[RecoveryPointArn](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

An ARN that uniquely identifies the target recovery point for scanning.; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Type: String

**[ResourceArn](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

An ARN that uniquely identifies the source resource of the corresponding recovery point ARN.

Type: String

**[ResourceName](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

The non-unique name of the resource that belongs to the specified backup.

Type: String

**[ResourceType](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

The type of AWS Resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume.

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Type: String

Valid Values: `EBS | EC2 | S3`

**[ScanBaseRecoveryPointArn](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

An ARN that uniquely identifies the base recovery point for scanning. This field will only be populated when an incremental scan job has taken place.

Type: String

**[ScanId](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

The scan ID generated by Amazon GuardDuty for the corresponding Scan Job ID request from AWS Backup.

Type: String

**[ScanJobId](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

The scan job ID that uniquely identified the request to AWS Backup.

Type: String

**[ScanMode](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

Specifies the scan type used for the scan job.

Type: String

Valid Values: `FULL_SCAN | INCREMENTAL_SCAN`

**[ScannerRoleArn](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

Specifies the scanner IAM role ARN used to for the scan job.

Type: String

**[ScanResult](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

Contains the `ScanResultsStatus` for the scanning job and returns `THREATS_FOUND` or `NO_THREATS_FOUND` for completed jobs.

Type: [ScanResultInfo](API_ScanResultInfo.md "API_ScanResultInfo.md") object

**[State](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

The current state of a scan job.

Type: String

Valid Values: `CANCELED | COMPLETED | COMPLETED_WITH_ISSUES | CREATED | FAILED | RUNNING`

**[StatusMessage](#API_DescribeScanJob_ResponseSyntax "#API_DescribeScanJob_ResponseSyntax")**

A detailed message explaining the status of the job to back up a resource.

Type: String

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DescribeScanJob.md "../../../goto/cli2/backup-2018-11-15/DescribeScanJob.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/DescribeScanJob.md "../../../goto/DotNetSDKV4/backup-2018-11-15/DescribeScanJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DescribeScanJob.md "../../../goto/SdkForCpp/backup-2018-11-15/DescribeScanJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DescribeScanJob.md "../../../goto/SdkForGoV2/backup-2018-11-15/DescribeScanJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeScanJob.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeScanJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeScanJob.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeScanJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DescribeScanJob.md "../../../goto/SdkForKotlin/backup-2018-11-15/DescribeScanJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeScanJob.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeScanJob.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DescribeScanJob.md "../../../goto/boto3/backup-2018-11-15/DescribeScanJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeScanJob.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeScanJob.md")
