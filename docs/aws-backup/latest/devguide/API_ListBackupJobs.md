# ListBackupJobs

Returns a list of existing backup jobs for an authenticated account for the last 30
days. For a longer period of time, consider using these [monitoring tools](monitoring.md "monitoring.md").

## Request Syntax

```
GET /backup-jobs/?accountId=`ByAccountId`&backupVaultName=`ByBackupVaultName`&completeAfter=`ByCompleteAfter`&completeBefore=`ByCompleteBefore`&createdAfter=`ByCreatedAfter`&createdBefore=`ByCreatedBefore`&maxResults=`MaxResults`&messageCategory=`ByMessageCategory`&nextToken=`NextToken`&parentJobId=`ByParentJobId`&resourceArn=`ByResourceArn`&resourceType=`ByResourceType`&state=`ByState` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[ByAccountId](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

The account ID to list the jobs from. Returns only backup jobs associated with the
specified account ID.

If used from an AWS Organizations management account, passing `*` returns
all jobs across the organization.

Pattern: `^[0-9]{12}$`

**[ByBackupVaultName](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

Returns only backup jobs that will be stored in the specified backup vault. Backup
vaults are identified by names that are unique to the account used to create them and the
AWS Region where they are created.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

**[ByCompleteAfter](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

Returns only backup jobs completed after a date expressed in Unix format and Coordinated
Universal Time (UTC).

**[ByCompleteBefore](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

Returns only backup jobs completed before a date expressed in Unix format and
Coordinated Universal Time (UTC).

**[ByCreatedAfter](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

Returns only backup jobs that were created after the specified date.

**[ByCreatedBefore](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

Returns only backup jobs that were created before the specified date.

**[ByMessageCategory](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

This is an optional parameter that can be used to
filter out jobs with a MessageCategory which matches the
value you input.

Example strings may include `AccessDenied`,
`SUCCESS`, `AGGREGATE_ALL`, and
`InvalidParameters`.

View [Monitoring](monitoring.md "monitoring.md")

The wildcard () returns count of all message categories.

`AGGREGATE_ALL` aggregates job counts
for all message categories and returns the sum.

**[ByParentJobId](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

This is a filter to list child (nested) jobs based on parent job ID.

**[ByResourceArn](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

Returns only backup jobs that match the specified resource Amazon Resource Name
(ARN).

**[ByResourceType](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

Returns only backup jobs for the specified resources:

- `Aurora` for Amazon Aurora
- `CloudFormation` for AWS CloudFormation
- `DocumentDB` for Amazon DocumentDB (with MongoDB compatibility)
- `DynamoDB` for Amazon DynamoDB
- `EBS` for Amazon Elastic Block Store
- `EC2` for Amazon Elastic Compute Cloud
- `EFS` for Amazon Elastic File System
- `EKS` for Amazon Elastic Kubernetes Service
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

**[ByState](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

Returns only backup jobs that are in the specified state.

`Completed with issues` is a status found only in the AWS Backup
console. For API, this status refers to jobs with a state of `COMPLETED` and a
`MessageCategory` with a value other than `SUCCESS`; that is, the
status is completed but comes with a status message.

To obtain the job count for
`Completed with issues`, run two GET requests, and subtract the second,
smaller number:

GET /backup-jobs/?state=COMPLETED

GET /backup-jobs/?messageCategory=SUCCESS&state=COMPLETED

Valid Values: `CREATED | PENDING | RUNNING | ABORTING | ABORTED | COMPLETED | FAILED | EXPIRED | PARTIAL`

**[MaxResults](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

The maximum number of items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListBackupJobs_RequestSyntax "#API_ListBackupJobs_RequestSyntax")**

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
   "BackupJobs": [
      {
         "AccountId": "***string***",
         "BackupJobId": "***string***",
         "BackupOptions": {
            "***string***" : "***string***"
         },
         "BackupSizeInBytes": ***number***,
         "BackupType": "***string***",
         "BackupVaultArn": "***string***",
         "BackupVaultName": "***string***",
         "BytesTransferred": ***number***,
         "CompletionDate": ***number***,
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
         "ExpectedCompletionDate": ***number***,
         "IamRoleArn": "***string***",
         "InitiationDate": ***number***,
         "IsEncrypted": ***boolean***,
         "IsParent": ***boolean***,
         "MessageCategory": "***string***",
         "ParentJobId": "***string***",
         "PercentDone": "***string***",
         "RecoveryPointArn": "***string***",
         "RecoveryPointLifecycle": {
            "DeleteAfterDays": ***number***,
            "DeleteAfterEvent": "***string***",
            "MoveToColdStorageAfterDays": ***number***,
            "OptInToArchiveForSupportedResources": ***boolean***
         },
         "ResourceArn": "***string***",
         "ResourceName": "***string***",
         "ResourceType": "***string***",
         "StartBy": ***number***,
         "State": "***string***",
         "StatusMessage": "***string***",
         "VaultLockState": "***string***",
         "VaultType": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupJobs](#API_ListBackupJobs_ResponseSyntax "#API_ListBackupJobs_ResponseSyntax")**

An array of structures containing metadata about your backup jobs returned in JSON
format.

Type: Array of [BackupJob](API_BackupJob.md "API_BackupJob.md") objects

**[NextToken](#API_ListBackupJobs_ResponseSyntax "#API_ListBackupJobs_ResponseSyntax")**

The next item following a partial list of returned items. For example, if a request is
made to return `MaxResults` number of items, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

Type: String

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListBackupJobs.md "../../../goto/cli2/backup-2018-11-15/ListBackupJobs.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListBackupJobs.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListBackupJobs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListBackupJobs.md "../../../goto/SdkForCpp/backup-2018-11-15/ListBackupJobs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListBackupJobs.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListBackupJobs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListBackupJobs.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListBackupJobs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListBackupJobs.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListBackupJobs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListBackupJobs.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListBackupJobs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListBackupJobs.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListBackupJobs.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListBackupJobs.md "../../../goto/boto3/backup-2018-11-15/ListBackupJobs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListBackupJobs.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListBackupJobs.md")
