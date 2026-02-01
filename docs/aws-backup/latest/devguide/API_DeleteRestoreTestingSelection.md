# DeleteRestoreTestingSelection

Input the Restore Testing Plan name and Restore Testing Selection
name.

All testing selections associated with a restore testing plan must
be deleted before the restore testing plan can be deleted.

## Request Syntax

```
DELETE /restore-testing/plans/`RestoreTestingPlanName`/selections/`RestoreTestingSelectionName` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[RestoreTestingPlanName](#API_DeleteRestoreTestingSelection_RequestSyntax "#API_DeleteRestoreTestingSelection_RequestSyntax")**

Required unique name of the restore testing plan that contains the
restore testing selection you wish to delete.

Required: Yes

**[RestoreTestingSelectionName](#API_DeleteRestoreTestingSelection_RequestSyntax "#API_DeleteRestoreTestingSelection_RequestSyntax")**

Required unique name of the restore testing selection you
wish to delete.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 204

```

## Response Elements

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DeleteRestoreTestingSelection.md "../../../goto/cli2/backup-2018-11-15/DeleteRestoreTestingSelection.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/DeleteRestoreTestingSelection.md "../../../goto/DotNetSDKV4/backup-2018-11-15/DeleteRestoreTestingSelection.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DeleteRestoreTestingSelection.md "../../../goto/SdkForCpp/backup-2018-11-15/DeleteRestoreTestingSelection.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DeleteRestoreTestingSelection.md "../../../goto/SdkForGoV2/backup-2018-11-15/DeleteRestoreTestingSelection.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DeleteRestoreTestingSelection.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DeleteRestoreTestingSelection.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteRestoreTestingSelection.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteRestoreTestingSelection.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DeleteRestoreTestingSelection.md "../../../goto/SdkForKotlin/backup-2018-11-15/DeleteRestoreTestingSelection.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DeleteRestoreTestingSelection.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DeleteRestoreTestingSelection.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DeleteRestoreTestingSelection.md "../../../goto/boto3/backup-2018-11-15/DeleteRestoreTestingSelection.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DeleteRestoreTestingSelection.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DeleteRestoreTestingSelection.md")
