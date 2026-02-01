# ListScanJobs

Returns a list of existing scan jobs for an authenticated account for the last 30 days.

## Request Syntax

```
GET /scan/jobs?ByAccountId=`ByAccountId`&ByBackupVaultName=`ByBackupVaultName`&ByCompleteAfter=`ByCompleteAfter`&ByCompleteBefore=`ByCompleteBefore`&ByMalwareScanner=`ByMalwareScanner`&ByRecoveryPointArn=`ByRecoveryPointArn`&ByResourceArn=`ByResourceArn`&ByResourceType=`ByResourceType`&ByScanResultStatus=`ByScanResultStatus`&ByState=`ByState`&MaxResults=`MaxResults`&NextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[ByAccountId](#API_ListScanJobs_RequestSyntax "#API_ListScanJobs_RequestSyntax")**

The account ID to list the jobs from. Returns only backup jobs associated with the specified account ID.

If used from an AWS Organizations management account, passing `*` returns all jobs across the organization.

Pattern: `^[0-9]{12}$`

**[ByBackupVaultName](#API_ListScanJobs_RequestSyntax "#API_ListScanJobs_RequestSyntax")**

Returns only scan jobs that will be stored in the specified backup vault.
Backup vaults are identified by names that are unique to the account
used to create them and the AWS Region where they are created.

Pattern: `^[a-zA-Z0-9\-\_\.]{2,50}$`

**[ByCompleteAfter](#API_ListScanJobs_RequestSyntax "#API_ListScanJobs_RequestSyntax")**

Returns only scan jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).

**[ByCompleteBefore](#API_ListScanJobs_RequestSyntax "#API_ListScanJobs_RequestSyntax")**

Returns only backup jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).

**[ByMalwareScanner](#API_ListScanJobs_RequestSyntax "#API_ListScanJobs_RequestSyntax")**

Returns only the scan jobs for the specified malware scanner. Currently only supports `GUARDDUTY`.

Valid Values: `GUARDDUTY`

**[ByRecoveryPointArn](#API_ListScanJobs_RequestSyntax "#API_ListScanJobs_RequestSyntax")**

Returns only the scan jobs that are ran against the specified recovery point.

**[ByResourceArn](#API_ListScanJobs_RequestSyntax "#API_ListScanJobs_RequestSyntax")**

Returns only scan jobs that match the specified resource Amazon Resource Name (ARN).

**[ByResourceType](#API_ListScanJobs_RequestSyntax "#API_ListScanJobs_RequestSyntax")**

Returns restore testing selections by the specified restore testing
plan name.

- `EBS`for Amazon Elastic Block Store
- `EC2`for Amazon Elastic Compute Cloud
- `S3`for Amazon Simple Storage Service (Amazon S3)

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Valid Values: `EBS | EC2 | S3`

**[ByScanResultStatus](#API_ListScanJobs_RequestSyntax "#API_ListScanJobs_RequestSyntax")**

Returns only the scan jobs for the specified scan results:

- `THREATS_FOUND`
- `NO_THREATS_FOUND`

Valid Values: `NO_THREATS_FOUND | THREATS_FOUND`

**[ByState](#API_ListScanJobs_RequestSyntax "#API_ListScanJobs_RequestSyntax")**

Returns only the scan jobs for the specified scanning job state.

Valid Values: `CANCELED | COMPLETED | COMPLETED_WITH_ISSUES | CREATED | FAILED | RUNNING`

**[MaxResults](#API_ListScanJobs_RequestSyntax "#API_ListScanJobs_RequestSyntax")**

The maximum number of items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListScanJobs_RequestSyntax "#API_ListScanJobs_RequestSyntax")**

The next item following a partial list of returned items. For example, if a request is made to
return `MaxResults` number of items, `NextToken` allows you to return more items
in your list starting at the location pointed to by the next token.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "ScanJobs": [
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
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListScanJobs_ResponseSyntax "#API_ListScanJobs_ResponseSyntax")**

The next item following a partial list of returned items. For example, if a request is made to
return `MaxResults` number of items, `NextToken` allows you to return more items
in your list starting at the location pointed to by the next token.

Type: String

**[ScanJobs](#API_ListScanJobs_ResponseSyntax "#API_ListScanJobs_ResponseSyntax")**

An array of structures containing metadata about your scan jobs returned in JSON format.

Type: Array of [ScanJob](API_ScanJob.md "API_ScanJob.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListScanJobs.md "../../../goto/cli2/backup-2018-11-15/ListScanJobs.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/ListScanJobs.md "../../../goto/DotNetSDKV4/backup-2018-11-15/ListScanJobs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListScanJobs.md "../../../goto/SdkForCpp/backup-2018-11-15/ListScanJobs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListScanJobs.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListScanJobs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListScanJobs.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListScanJobs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListScanJobs.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListScanJobs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListScanJobs.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListScanJobs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListScanJobs.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListScanJobs.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListScanJobs.md "../../../goto/boto3/backup-2018-11-15/ListScanJobs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListScanJobs.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListScanJobs.md")
