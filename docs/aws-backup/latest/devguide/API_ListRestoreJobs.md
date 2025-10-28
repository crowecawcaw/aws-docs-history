# ListRestoreJobs

Returns a list of jobs that AWS Backup initiated to restore a saved resource,
including details about the recovery process.

## Request Syntax

```
GET /restore-jobs/?accountId=`ByAccountId`&completeAfter=`ByCompleteAfter`&completeBefore=`ByCompleteBefore`&createdAfter=`ByCreatedAfter`&createdBefore=`ByCreatedBefore`&maxResults=`MaxResults`&nextToken=`NextToken`&resourceType=`ByResourceType`&restoreTestingPlanArn=`ByRestoreTestingPlanArn`&status=`ByStatus` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[ByAccountId](#API_ListRestoreJobs_RequestSyntax "#API_ListRestoreJobs_RequestSyntax")**

The account ID to list the jobs from. Returns only restore jobs associated with the
specified account ID.

Pattern: `^[0-9]{12}$`

**[ByCompleteAfter](#API_ListRestoreJobs_RequestSyntax "#API_ListRestoreJobs_RequestSyntax")**

Returns only copy jobs completed after a date expressed in Unix format and Coordinated
Universal Time (UTC).

**[ByCompleteBefore](#API_ListRestoreJobs_RequestSyntax "#API_ListRestoreJobs_RequestSyntax")**

Returns only copy jobs completed before a date expressed in Unix format and Coordinated
Universal Time (UTC).

**[ByCreatedAfter](#API_ListRestoreJobs_RequestSyntax "#API_ListRestoreJobs_RequestSyntax")**

Returns only restore jobs that were created after the specified date.

**[ByCreatedBefore](#API_ListRestoreJobs_RequestSyntax "#API_ListRestoreJobs_RequestSyntax")**

Returns only restore jobs that were created before the specified date.

**[ByResourceType](#API_ListRestoreJobs_RequestSyntax "#API_ListRestoreJobs_RequestSyntax")**

Include this parameter to return only restore jobs for the specified resources:

- `Aurora` for Amazon Aurora
- `CloudFormation` for AWS CloudFormation
- `DocumentDB` for Amazon DocumentDB (with MongoDB compatibility)
- `DynamoDB` for Amazon DynamoDB
- `EBS` for Amazon Elastic Block Store
- `EC2` for Amazon Elastic Compute Cloud
- `EFS` for Amazon Elastic File System
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

**[ByRestoreTestingPlanArn](#API_ListRestoreJobs_RequestSyntax "#API_ListRestoreJobs_RequestSyntax")**

This returns only restore testing jobs that match the
specified resource Amazon Resource Name (ARN).

**[ByStatus](#API_ListRestoreJobs_RequestSyntax "#API_ListRestoreJobs_RequestSyntax")**

Returns only restore jobs associated with the specified job status.

Valid Values: `PENDING | RUNNING | COMPLETED | ABORTED | FAILED`

**[MaxResults](#API_ListRestoreJobs_RequestSyntax "#API_ListRestoreJobs_RequestSyntax")**

The maximum number of items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListRestoreJobs_RequestSyntax "#API_ListRestoreJobs_RequestSyntax")**

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
   "NextToken": "***string***",
   "RestoreJobs": [
      {
         "AccountId": "***string***",
         "BackupSizeInBytes": ***number***,
         "BackupVaultArn": "***string***",
         "CompletionDate": ***number***,
         "CreatedBy": {
            "RestoreTestingPlanArn": "***string***"
         },
         "CreatedResourceArn": "***string***",
         "CreationDate": ***number***,
         "DeletionStatus": "***string***",
         "DeletionStatusMessage": "***string***",
         "ExpectedCompletionTimeMinutes": ***number***,
         "IamRoleArn": "***string***",
         "PercentDone": "***string***",
         "RecoveryPointArn": "***string***",
         "RecoveryPointCreationDate": ***number***,
         "ResourceType": "***string***",
         "RestoreJobId": "***string***",
         "SourceResourceArn": "***string***",
         "Status": "***string***",
         "StatusMessage": "***string***",
         "ValidationStatus": "***string***",
         "ValidationStatusMessage": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListRestoreJobs_ResponseSyntax "#API_ListRestoreJobs_ResponseSyntax")**

The next item following a partial list of returned items. For example, if a request is
made to return `MaxResults` number of items, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

Type: String

**[RestoreJobs](#API_ListRestoreJobs_ResponseSyntax "#API_ListRestoreJobs_ResponseSyntax")**

An array of objects that contain detailed information about jobs to restore saved
resources.

Type: Array of [RestoreJobsListMember](API_RestoreJobsListMember.md "API_RestoreJobsListMember.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListRestoreJobs.md "../../../goto/cli2/backup-2018-11-15/ListRestoreJobs.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListRestoreJobs.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListRestoreJobs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListRestoreJobs.md "../../../goto/SdkForCpp/backup-2018-11-15/ListRestoreJobs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListRestoreJobs.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListRestoreJobs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListRestoreJobs.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListRestoreJobs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRestoreJobs.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRestoreJobs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListRestoreJobs.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListRestoreJobs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListRestoreJobs.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListRestoreJobs.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListRestoreJobs.md "../../../goto/boto3/backup-2018-11-15/ListRestoreJobs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListRestoreJobs.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListRestoreJobs.md")
