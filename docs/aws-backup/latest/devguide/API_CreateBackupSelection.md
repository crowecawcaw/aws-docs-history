# CreateBackupSelection

Creates a JSON document that specifies a set of resources to assign to a backup plan.
For examples, see [Assigning resources programmatically](assigning-resources.md#assigning-resources-json "assigning-resources.md#assigning-resources-json").

## Request Syntax

```
PUT /backup/plans/`backupPlanId`/selections/ HTTP/1.1
Content-type: application/json

{
   "BackupSelection": {
      "Conditions": {
         "StringEquals": [
            {
               "ConditionKey": "`string`",
               "ConditionValue": "`string`"
            }
         ],
         "StringLike": [
            {
               "ConditionKey": "`string`",
               "ConditionValue": "`string`"
            }
         ],
         "StringNotEquals": [
            {
               "ConditionKey": "`string`",
               "ConditionValue": "`string`"
            }
         ],
         "StringNotLike": [
            {
               "ConditionKey": "`string`",
               "ConditionValue": "`string`"
            }
         ]
      },
      "IamRoleArn": "`string`",
      "ListOfTags": [
         {
            "ConditionKey": "`string`",
            "ConditionType": "`string`",
            "ConditionValue": "`string`"
         }
      ],
      "NotResources": [ "`string`" ],
      "Resources": [ "`string`" ],
      "SelectionName": "`string`"
   },
   "CreatorRequestId": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[backupPlanId](#API_CreateBackupSelection_RequestSyntax "#API_CreateBackupSelection_RequestSyntax")**

The ID of the backup plan.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[BackupSelection](#API_CreateBackupSelection_RequestSyntax "#API_CreateBackupSelection_RequestSyntax")**

The body of a request to assign a set of resources to a backup plan.

Type: [BackupSelection](API_BackupSelection.md "API_BackupSelection.md") object

Required: Yes

**[CreatorRequestId](#API_CreateBackupSelection_RequestSyntax "#API_CreateBackupSelection_RequestSyntax")**

A unique string that identifies the request and allows failed requests to be retried
without the risk of running the operation twice. This parameter is optional.

If used, this parameter must contain 1 to 50 alphanumeric or '-\_.' characters.

Type: String

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupPlanId": "***string***",
   "CreationDate": ***number***,
   "SelectionId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupPlanId](#API_CreateBackupSelection_ResponseSyntax "#API_CreateBackupSelection_ResponseSyntax")**

The ID of the backup plan.

Type: String

**[CreationDate](#API_CreateBackupSelection_ResponseSyntax "#API_CreateBackupSelection_ResponseSyntax")**

The date and time a backup selection is created, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[SelectionId](#API_CreateBackupSelection_ResponseSyntax "#API_CreateBackupSelection_ResponseSyntax")**

Uniquely identifies the body of a request to assign a set of resources to a backup
plan.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AlreadyExistsException**

The required resource already exists.

**Arn**

**Context**

**CreatorRequestId**

**Type**

HTTP Status Code: 400

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

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

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/CreateBackupSelection.md "../../../goto/cli2/backup-2018-11-15/CreateBackupSelection.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/CreateBackupSelection.md "../../../goto/DotNetSDKV3/backup-2018-11-15/CreateBackupSelection.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/CreateBackupSelection.md "../../../goto/SdkForCpp/backup-2018-11-15/CreateBackupSelection.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/CreateBackupSelection.md "../../../goto/SdkForGoV2/backup-2018-11-15/CreateBackupSelection.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/CreateBackupSelection.md "../../../goto/SdkForJavaV2/backup-2018-11-15/CreateBackupSelection.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateBackupSelection.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateBackupSelection.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/CreateBackupSelection.md "../../../goto/SdkForKotlin/backup-2018-11-15/CreateBackupSelection.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/CreateBackupSelection.md "../../../goto/SdkForPHPV3/backup-2018-11-15/CreateBackupSelection.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/CreateBackupSelection.md "../../../goto/boto3/backup-2018-11-15/CreateBackupSelection.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/CreateBackupSelection.md "../../../goto/SdkForRubyV3/backup-2018-11-15/CreateBackupSelection.md")
