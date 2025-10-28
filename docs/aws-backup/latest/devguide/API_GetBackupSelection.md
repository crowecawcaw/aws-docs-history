# GetBackupSelection

Returns selection metadata and a document in JSON format that specifies a list of
resources that are associated with a backup plan.

## Request Syntax

```
GET /backup/plans/`backupPlanId`/selections/`selectionId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[backupPlanId](#API_GetBackupSelection_RequestSyntax "#API_GetBackupSelection_RequestSyntax")**

Uniquely identifies a backup plan.

Required: Yes

**[selectionId](#API_GetBackupSelection_RequestSyntax "#API_GetBackupSelection_RequestSyntax")**

Uniquely identifies the body of a request to assign a set of resources to a backup
plan.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupPlanId": "***string***",
   "BackupSelection": {
      "Conditions": {
         "StringEquals": [
            {
               "ConditionKey": "***string***",
               "ConditionValue": "***string***"
            }
         ],
         "StringLike": [
            {
               "ConditionKey": "***string***",
               "ConditionValue": "***string***"
            }
         ],
         "StringNotEquals": [
            {
               "ConditionKey": "***string***",
               "ConditionValue": "***string***"
            }
         ],
         "StringNotLike": [
            {
               "ConditionKey": "***string***",
               "ConditionValue": "***string***"
            }
         ]
      },
      "IamRoleArn": "***string***",
      "ListOfTags": [
         {
            "ConditionKey": "***string***",
            "ConditionType": "***string***",
            "ConditionValue": "***string***"
         }
      ],
      "NotResources": [ "***string***" ],
      "Resources": [ "***string***" ],
      "SelectionName": "***string***"
   },
   "CreationDate": ***number***,
   "CreatorRequestId": "***string***",
   "SelectionId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupPlanId](#API_GetBackupSelection_ResponseSyntax "#API_GetBackupSelection_ResponseSyntax")**

Uniquely identifies a backup plan.

Type: String

**[BackupSelection](#API_GetBackupSelection_ResponseSyntax "#API_GetBackupSelection_ResponseSyntax")**

Specifies the body of a request to assign a set of resources to a backup plan.

Type: [BackupSelection](API_BackupSelection.md "API_BackupSelection.md") object

**[CreationDate](#API_GetBackupSelection_ResponseSyntax "#API_GetBackupSelection_ResponseSyntax")**

The date and time a backup selection is created, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[CreatorRequestId](#API_GetBackupSelection_ResponseSyntax "#API_GetBackupSelection_ResponseSyntax")**

A unique string that identifies the request and allows failed requests to be retried
without the risk of running the operation twice.

Type: String

**[SelectionId](#API_GetBackupSelection_ResponseSyntax "#API_GetBackupSelection_ResponseSyntax")**

Uniquely identifies the body of a request to assign a set of resources to a backup
plan.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/GetBackupSelection.md "../../../goto/cli2/backup-2018-11-15/GetBackupSelection.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/GetBackupSelection.md "../../../goto/DotNetSDKV3/backup-2018-11-15/GetBackupSelection.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/GetBackupSelection.md "../../../goto/SdkForCpp/backup-2018-11-15/GetBackupSelection.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/GetBackupSelection.md "../../../goto/SdkForGoV2/backup-2018-11-15/GetBackupSelection.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/GetBackupSelection.md "../../../goto/SdkForJavaV2/backup-2018-11-15/GetBackupSelection.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetBackupSelection.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetBackupSelection.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/GetBackupSelection.md "../../../goto/SdkForKotlin/backup-2018-11-15/GetBackupSelection.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/GetBackupSelection.md "../../../goto/SdkForPHPV3/backup-2018-11-15/GetBackupSelection.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/GetBackupSelection.md "../../../goto/boto3/backup-2018-11-15/GetBackupSelection.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/GetBackupSelection.md "../../../goto/SdkForRubyV3/backup-2018-11-15/GetBackupSelection.md")
