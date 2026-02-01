# PutRestoreValidationResult

This request allows you to send your independent self-run
restore test validation results.
`RestoreJobId` and `ValidationStatus`
are required. Optionally, you can input a
`ValidationStatusMessage`.

## Request Syntax

```
PUT /restore-jobs/`restoreJobId`/validations HTTP/1.1
Content-type: application/json

{
   "ValidationStatus": "`string`",
   "ValidationStatusMessage": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[restoreJobId](#API_PutRestoreValidationResult_RequestSyntax "#API_PutRestoreValidationResult_RequestSyntax")**

This is a unique identifier of a restore job within AWS Backup.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[ValidationStatus](#API_PutRestoreValidationResult_RequestSyntax "#API_PutRestoreValidationResult_RequestSyntax")**

The status of your restore validation.

Type: String

Valid Values: `FAILED | SUCCESSFUL | TIMED_OUT | VALIDATING`

Required: Yes

**[ValidationStatusMessage](#API_PutRestoreValidationResult_RequestSyntax "#API_PutRestoreValidationResult_RequestSyntax")**

This is an optional message string you can input to
describe the validation status for the restore test validation.

Type: String

Required: No

## Response Syntax

```
HTTP/1.1 204

```

## Response Elements

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**InvalidRequestException**

Indicates that something is wrong with the input to the request. For example, a
parameter is of the wrong type.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/PutRestoreValidationResult.md "../../../goto/cli2/backup-2018-11-15/PutRestoreValidationResult.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/PutRestoreValidationResult.md "../../../goto/DotNetSDKV4/backup-2018-11-15/PutRestoreValidationResult.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/PutRestoreValidationResult.md "../../../goto/SdkForCpp/backup-2018-11-15/PutRestoreValidationResult.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/PutRestoreValidationResult.md "../../../goto/SdkForGoV2/backup-2018-11-15/PutRestoreValidationResult.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/PutRestoreValidationResult.md "../../../goto/SdkForJavaV2/backup-2018-11-15/PutRestoreValidationResult.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/PutRestoreValidationResult.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/PutRestoreValidationResult.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/PutRestoreValidationResult.md "../../../goto/SdkForKotlin/backup-2018-11-15/PutRestoreValidationResult.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/PutRestoreValidationResult.md "../../../goto/SdkForPHPV3/backup-2018-11-15/PutRestoreValidationResult.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/PutRestoreValidationResult.md "../../../goto/boto3/backup-2018-11-15/PutRestoreValidationResult.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/PutRestoreValidationResult.md "../../../goto/SdkForRubyV3/backup-2018-11-15/PutRestoreValidationResult.md")
