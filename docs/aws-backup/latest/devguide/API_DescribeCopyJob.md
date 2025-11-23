# DescribeCopyJob

Returns metadata associated with creating a copy of a resource.

## Request Syntax

```
GET /copy-jobs/`copyJobId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[copyJobId](#API_DescribeCopyJob_RequestSyntax "#API_DescribeCopyJob_RequestSyntax")**

Uniquely identifies a copy job.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CopyJob": {
      "AccountId": "***string***",
      "BackupSizeInBytes": ***number***,
      "ChildJobsInState": {
         "***string***" : ***number***
      },
      "CompletionDate": ***number***,
      "CompositeMemberIdentifier": "***string***",
      "CopyJobId": "***string***",
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
      "CreatedByBackupJobId": "***string***",
      "CreationDate": ***number***,
      "DestinationBackupVaultArn": "***string***",
      "DestinationEncryptionKeyArn": "***string***",
      "DestinationRecoveryPointArn": "***string***",
      "DestinationRecoveryPointLifecycle": {
         "DeleteAfterDays": ***number***,
         "DeleteAfterEvent": "***string***",
         "MoveToColdStorageAfterDays": ***number***,
         "OptInToArchiveForSupportedResources": ***boolean***
      },
      "DestinationVaultLockState": "***string***",
      "DestinationVaultType": "***string***",
      "IamRoleArn": "***string***",
      "IsParent": ***boolean***,
      "MessageCategory": "***string***",
      "NumberOfChildJobs": ***number***,
      "ParentJobId": "***string***",
      "ResourceArn": "***string***",
      "ResourceName": "***string***",
      "ResourceType": "***string***",
      "SourceBackupVaultArn": "***string***",
      "SourceRecoveryPointArn": "***string***",
      "State": "***string***",
      "StatusMessage": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CopyJob](#API_DescribeCopyJob_ResponseSyntax "#API_DescribeCopyJob_ResponseSyntax")**

Contains detailed information about a copy job.

Type: [CopyJob](API_CopyJob.md "API_CopyJob.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DescribeCopyJob.md "../../../goto/cli2/backup-2018-11-15/DescribeCopyJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/DescribeCopyJob.md "../../../goto/DotNetSDKV3/backup-2018-11-15/DescribeCopyJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DescribeCopyJob.md "../../../goto/SdkForCpp/backup-2018-11-15/DescribeCopyJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DescribeCopyJob.md "../../../goto/SdkForGoV2/backup-2018-11-15/DescribeCopyJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeCopyJob.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeCopyJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeCopyJob.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeCopyJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DescribeCopyJob.md "../../../goto/SdkForKotlin/backup-2018-11-15/DescribeCopyJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeCopyJob.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeCopyJob.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DescribeCopyJob.md "../../../goto/boto3/backup-2018-11-15/DescribeCopyJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeCopyJob.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeCopyJob.md")
