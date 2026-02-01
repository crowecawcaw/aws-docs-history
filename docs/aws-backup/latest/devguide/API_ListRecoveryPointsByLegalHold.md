# ListRecoveryPointsByLegalHold

This action returns recovery point ARNs (Amazon Resource Names) of the
specified legal hold.

## Request Syntax

```
GET /legal-holds/`legalHoldId`/recovery-points?maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[legalHoldId](#API_ListRecoveryPointsByLegalHold_RequestSyntax "#API_ListRecoveryPointsByLegalHold_RequestSyntax")**

The ID of the legal hold.

Required: Yes

**[MaxResults](#API_ListRecoveryPointsByLegalHold_RequestSyntax "#API_ListRecoveryPointsByLegalHold_RequestSyntax")**

The maximum number of resource list items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListRecoveryPointsByLegalHold_RequestSyntax "#API_ListRecoveryPointsByLegalHold_RequestSyntax")**

The next item following a partial list of returned resources. For example, if a request
is made to return `MaxResults` number of resources, `NextToken`
allows you to return more items in your list starting at the location pointed to by the
next token.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "RecoveryPoints": [
      {
         "BackupVaultName": "***string***",
         "RecoveryPointArn": "***string***",
         "ResourceArn": "***string***",
         "ResourceType": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListRecoveryPointsByLegalHold_ResponseSyntax "#API_ListRecoveryPointsByLegalHold_ResponseSyntax")**

The next item following a partial list of returned resources.

Type: String

**[RecoveryPoints](#API_ListRecoveryPointsByLegalHold_ResponseSyntax "#API_ListRecoveryPointsByLegalHold_ResponseSyntax")**

The recovery points.

Type: Array of [RecoveryPointMember](API_RecoveryPointMember.md "API_RecoveryPointMember.md") objects

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

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListRecoveryPointsByLegalHold.md "../../../goto/cli2/backup-2018-11-15/ListRecoveryPointsByLegalHold.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/ListRecoveryPointsByLegalHold.md "../../../goto/DotNetSDKV4/backup-2018-11-15/ListRecoveryPointsByLegalHold.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListRecoveryPointsByLegalHold.md "../../../goto/SdkForCpp/backup-2018-11-15/ListRecoveryPointsByLegalHold.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListRecoveryPointsByLegalHold.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListRecoveryPointsByLegalHold.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListRecoveryPointsByLegalHold.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListRecoveryPointsByLegalHold.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRecoveryPointsByLegalHold.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRecoveryPointsByLegalHold.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListRecoveryPointsByLegalHold.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListRecoveryPointsByLegalHold.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListRecoveryPointsByLegalHold.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListRecoveryPointsByLegalHold.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListRecoveryPointsByLegalHold.md "../../../goto/boto3/backup-2018-11-15/ListRecoveryPointsByLegalHold.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListRecoveryPointsByLegalHold.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListRecoveryPointsByLegalHold.md")
