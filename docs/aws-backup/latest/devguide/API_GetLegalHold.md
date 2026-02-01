# GetLegalHold

This action returns details for a specified legal hold. The details are the
body of a legal hold in JSON format, in addition to metadata.

## Request Syntax

```
GET /legal-holds/`legalHoldId`/ HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[legalHoldId](#API_GetLegalHold_RequestSyntax "#API_GetLegalHold_RequestSyntax")**

The ID of the legal hold.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CancelDescription": "***string***",
   "CancellationDate": ***number***,
   "CreationDate": ***number***,
   "Description": "***string***",
   "LegalHoldArn": "***string***",
   "LegalHoldId": "***string***",
   "RecoveryPointSelection": {
      "DateRange": {
         "FromDate": ***number***,
         "ToDate": ***number***
      },
      "ResourceIdentifiers": [ "***string***" ],
      "VaultNames": [ "***string***" ]
   },
   "RetainRecordUntil": ***number***,
   "Status": "***string***",
   "Title": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CancelDescription](#API_GetLegalHold_ResponseSyntax "#API_GetLegalHold_ResponseSyntax")**

The reason for removing the legal hold.

Type: String

**[CancellationDate](#API_GetLegalHold_ResponseSyntax "#API_GetLegalHold_ResponseSyntax")**

The time when the legal hold was cancelled.

Type: Timestamp

**[CreationDate](#API_GetLegalHold_ResponseSyntax "#API_GetLegalHold_ResponseSyntax")**

The time when the legal hold was created.

Type: Timestamp

**[Description](#API_GetLegalHold_ResponseSyntax "#API_GetLegalHold_ResponseSyntax")**

The description of the legal hold.

Type: String

**[LegalHoldArn](#API_GetLegalHold_ResponseSyntax "#API_GetLegalHold_ResponseSyntax")**

The framework ARN for the specified legal hold. The format
of the ARN depends on the resource type.

Type: String

**[LegalHoldId](#API_GetLegalHold_ResponseSyntax "#API_GetLegalHold_ResponseSyntax")**

The ID of the legal hold.

Type: String

**[RecoveryPointSelection](#API_GetLegalHold_ResponseSyntax "#API_GetLegalHold_ResponseSyntax")**

The criteria to assign a set of resources, such as resource types or backup vaults.

Type: [RecoveryPointSelection](API_RecoveryPointSelection.md "API_RecoveryPointSelection.md") object

**[RetainRecordUntil](#API_GetLegalHold_ResponseSyntax "#API_GetLegalHold_ResponseSyntax")**

The date and time until which the legal hold record is retained.

Type: Timestamp

**[Status](#API_GetLegalHold_ResponseSyntax "#API_GetLegalHold_ResponseSyntax")**

The status of the legal hold.

Type: String

Valid Values: `CREATING | ACTIVE | CANCELING | CANCELED`

**[Title](#API_GetLegalHold_ResponseSyntax "#API_GetLegalHold_ResponseSyntax")**

The title of the legal hold.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/GetLegalHold.md "../../../goto/cli2/backup-2018-11-15/GetLegalHold.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/GetLegalHold.md "../../../goto/DotNetSDKV4/backup-2018-11-15/GetLegalHold.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/GetLegalHold.md "../../../goto/SdkForCpp/backup-2018-11-15/GetLegalHold.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/GetLegalHold.md "../../../goto/SdkForGoV2/backup-2018-11-15/GetLegalHold.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/GetLegalHold.md "../../../goto/SdkForJavaV2/backup-2018-11-15/GetLegalHold.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetLegalHold.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetLegalHold.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/GetLegalHold.md "../../../goto/SdkForKotlin/backup-2018-11-15/GetLegalHold.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/GetLegalHold.md "../../../goto/SdkForPHPV3/backup-2018-11-15/GetLegalHold.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/GetLegalHold.md "../../../goto/boto3/backup-2018-11-15/GetLegalHold.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/GetLegalHold.md "../../../goto/SdkForRubyV3/backup-2018-11-15/GetLegalHold.md")
