# CreateLegalHold

Creates a legal hold on a recovery point (backup). A legal hold is a restraint on
altering or deleting a backup until an authorized user cancels the legal hold. Any actions
to delete or disassociate a recovery point will fail with an error if one or more active
legal holds are on the recovery point.

## Request Syntax

```
POST /legal-holds/ HTTP/1.1
Content-type: application/json

{
   "Description": "`string`",
   "IdempotencyToken": "`string`",
   "RecoveryPointSelection": {
      "DateRange": {
         "FromDate": `number`,
         "ToDate": `number`
      },
      "ResourceIdentifiers": [ "`string`" ],
      "VaultNames": [ "`string`" ]
   },
   "Tags": {
      "`string`" : "`string`"
   },
   "Title": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[Description](#API_CreateLegalHold_RequestSyntax "#API_CreateLegalHold_RequestSyntax")**

The description of the legal hold.

Type: String

Required: Yes

**[IdempotencyToken](#API_CreateLegalHold_RequestSyntax "#API_CreateLegalHold_RequestSyntax")**

This is a user-chosen string used to distinguish between otherwise identical
calls. Retrying a successful request with the
same idempotency token results in a success message with no action taken.

Type: String

Required: No

**[RecoveryPointSelection](#API_CreateLegalHold_RequestSyntax "#API_CreateLegalHold_RequestSyntax")**

The criteria to assign a set of resources, such as resource types or backup vaults.

Type: [RecoveryPointSelection](API_RecoveryPointSelection.md "API_RecoveryPointSelection.md") object

Required: No

**[Tags](#API_CreateLegalHold_RequestSyntax "#API_CreateLegalHold_RequestSyntax")**

Optional tags to include. A tag is a key-value pair you can use to manage,
filter, and search for your resources. Allowed characters include UTF-8 letters,
numbers, spaces, and the following characters: + - = . \_ : /.

Type: String to string map

Required: No

**[Title](#API_CreateLegalHold_RequestSyntax "#API_CreateLegalHold_RequestSyntax")**

The title of the legal hold.

Type: String

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
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
   "Status": "***string***",
   "Title": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationDate](#API_CreateLegalHold_ResponseSyntax "#API_CreateLegalHold_ResponseSyntax")**

The time when the legal hold was created.

Type: Timestamp

**[Description](#API_CreateLegalHold_ResponseSyntax "#API_CreateLegalHold_ResponseSyntax")**

The description of the legal hold.

Type: String

**[LegalHoldArn](#API_CreateLegalHold_ResponseSyntax "#API_CreateLegalHold_ResponseSyntax")**

The Amazon Resource Name (ARN) of the legal hold.

Type: String

**[LegalHoldId](#API_CreateLegalHold_ResponseSyntax "#API_CreateLegalHold_ResponseSyntax")**

The ID of the legal hold.

Type: String

**[RecoveryPointSelection](#API_CreateLegalHold_ResponseSyntax "#API_CreateLegalHold_ResponseSyntax")**

The criteria to assign to a set of resources, such as resource types or backup vaults.

Type: [RecoveryPointSelection](API_RecoveryPointSelection.md "API_RecoveryPointSelection.md") object

**[Status](#API_CreateLegalHold_ResponseSyntax "#API_CreateLegalHold_ResponseSyntax")**

The status of the legal hold.

Type: String

Valid Values: `CREATING | ACTIVE | CANCELING | CANCELED`

**[Title](#API_CreateLegalHold_ResponseSyntax "#API_CreateLegalHold_ResponseSyntax")**

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/CreateLegalHold.md "../../../goto/cli2/backup-2018-11-15/CreateLegalHold.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/CreateLegalHold.md "../../../goto/DotNetSDKV3/backup-2018-11-15/CreateLegalHold.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/CreateLegalHold.md "../../../goto/SdkForCpp/backup-2018-11-15/CreateLegalHold.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/CreateLegalHold.md "../../../goto/SdkForGoV2/backup-2018-11-15/CreateLegalHold.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/CreateLegalHold.md "../../../goto/SdkForJavaV2/backup-2018-11-15/CreateLegalHold.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateLegalHold.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateLegalHold.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/CreateLegalHold.md "../../../goto/SdkForKotlin/backup-2018-11-15/CreateLegalHold.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/CreateLegalHold.md "../../../goto/SdkForPHPV3/backup-2018-11-15/CreateLegalHold.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/CreateLegalHold.md "../../../goto/boto3/backup-2018-11-15/CreateLegalHold.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/CreateLegalHold.md "../../../goto/SdkForRubyV3/backup-2018-11-15/CreateLegalHold.md")
