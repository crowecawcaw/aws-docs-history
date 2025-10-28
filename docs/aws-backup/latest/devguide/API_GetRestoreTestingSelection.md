# GetRestoreTestingSelection

Returns RestoreTestingSelection, which displays resources
and elements of the restore testing plan.

## Request Syntax

```
GET /restore-testing/plans/`RestoreTestingPlanName`/selections/`RestoreTestingSelectionName` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[RestoreTestingPlanName](#API_GetRestoreTestingSelection_RequestSyntax "#API_GetRestoreTestingSelection_RequestSyntax")**

Required unique name of the restore testing plan.

Required: Yes

**[RestoreTestingSelectionName](#API_GetRestoreTestingSelection_RequestSyntax "#API_GetRestoreTestingSelection_RequestSyntax")**

Required unique name of the restore testing selection.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "RestoreTestingSelection": {
      "CreationTime": ***number***,
      "CreatorRequestId": "***string***",
      "IamRoleArn": "***string***",
      "ProtectedResourceArns": [ "***string***" ],
      "ProtectedResourceConditions": {
         "StringEquals": [
            {
               "Key": "***string***",
               "Value": "***string***"
            }
         ],
         "StringNotEquals": [
            {
               "Key": "***string***",
               "Value": "***string***"
            }
         ]
      },
      "ProtectedResourceType": "***string***",
      "RestoreMetadataOverrides": {
         "***string***" : "***string***"
      },
      "RestoreTestingPlanName": "***string***",
      "RestoreTestingSelectionName": "***string***",
      "ValidationWindowHours": ***number***
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[RestoreTestingSelection](#API_GetRestoreTestingSelection_ResponseSyntax "#API_GetRestoreTestingSelection_ResponseSyntax")**

Unique name of the restore testing selection.

Type: [RestoreTestingSelectionForGet](API_RestoreTestingSelectionForGet.md "API_RestoreTestingSelectionForGet.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/GetRestoreTestingSelection.md "../../../goto/cli2/backup-2018-11-15/GetRestoreTestingSelection.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/GetRestoreTestingSelection.md "../../../goto/DotNetSDKV3/backup-2018-11-15/GetRestoreTestingSelection.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/GetRestoreTestingSelection.md "../../../goto/SdkForCpp/backup-2018-11-15/GetRestoreTestingSelection.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/GetRestoreTestingSelection.md "../../../goto/SdkForGoV2/backup-2018-11-15/GetRestoreTestingSelection.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/GetRestoreTestingSelection.md "../../../goto/SdkForJavaV2/backup-2018-11-15/GetRestoreTestingSelection.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetRestoreTestingSelection.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetRestoreTestingSelection.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/GetRestoreTestingSelection.md "../../../goto/SdkForKotlin/backup-2018-11-15/GetRestoreTestingSelection.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/GetRestoreTestingSelection.md "../../../goto/SdkForPHPV3/backup-2018-11-15/GetRestoreTestingSelection.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/GetRestoreTestingSelection.md "../../../goto/boto3/backup-2018-11-15/GetRestoreTestingSelection.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/GetRestoreTestingSelection.md "../../../goto/SdkForRubyV3/backup-2018-11-15/GetRestoreTestingSelection.md")
