# CancelLegalHold

Removes the specified legal hold on a recovery point. This action can only be performed
by a user with sufficient permissions.

## Request Syntax

```
DELETE /legal-holds/`legalHoldId`?cancelDescription=`CancelDescription`&retainRecordInDays=`RetainRecordInDays` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[CancelDescription](#API_CancelLegalHold_RequestSyntax "#API_CancelLegalHold_RequestSyntax")**

A string the describes the reason for removing the legal hold.

Required: Yes

**[legalHoldId](#API_CancelLegalHold_RequestSyntax "#API_CancelLegalHold_RequestSyntax")**

The ID of the legal hold.

Required: Yes

**[RetainRecordInDays](#API_CancelLegalHold_RequestSyntax "#API_CancelLegalHold_RequestSyntax")**

The integer amount, in days, after which to remove legal hold.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 201

```

## Response Elements

If the action is successful, the service sends back an HTTP 201 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**InvalidResourceStateException**

AWS Backup is already performing an action on this recovery point. It can't
perform the action you requested until the first action finishes. Try again later.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/CancelLegalHold.md "../../../goto/cli2/backup-2018-11-15/CancelLegalHold.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/CancelLegalHold.md "../../../goto/DotNetSDKV4/backup-2018-11-15/CancelLegalHold.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/CancelLegalHold.md "../../../goto/SdkForCpp/backup-2018-11-15/CancelLegalHold.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/CancelLegalHold.md "../../../goto/SdkForGoV2/backup-2018-11-15/CancelLegalHold.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/CancelLegalHold.md "../../../goto/SdkForJavaV2/backup-2018-11-15/CancelLegalHold.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CancelLegalHold.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CancelLegalHold.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/CancelLegalHold.md "../../../goto/SdkForKotlin/backup-2018-11-15/CancelLegalHold.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/CancelLegalHold.md "../../../goto/SdkForPHPV3/backup-2018-11-15/CancelLegalHold.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/CancelLegalHold.md "../../../goto/boto3/backup-2018-11-15/CancelLegalHold.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/CancelLegalHold.md "../../../goto/SdkForRubyV3/backup-2018-11-15/CancelLegalHold.md")
