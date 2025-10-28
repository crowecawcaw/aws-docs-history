# GetRestoreTestingPlan

Returns `RestoreTestingPlan` details for the specified
`RestoreTestingPlanName`. The details are the body of a restore testing plan
in JSON format, in addition to plan metadata.

## Request Syntax

```
GET /restore-testing/plans/`RestoreTestingPlanName` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[RestoreTestingPlanName](#API_GetRestoreTestingPlan_RequestSyntax "#API_GetRestoreTestingPlan_RequestSyntax")**

Required unique name of the restore testing plan.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "RestoreTestingPlan": {
      "CreationTime": ***number***,
      "CreatorRequestId": "***string***",
      "LastExecutionTime": ***number***,
      "LastUpdateTime": ***number***,
      "RecoveryPointSelection": {
         "Algorithm": "***string***",
         "ExcludeVaults": [ "***string***" ],
         "IncludeVaults": [ "***string***" ],
         "RecoveryPointTypes": [ "***string***" ],
         "SelectionWindowDays": ***number***
      },
      "RestoreTestingPlanArn": "***string***",
      "RestoreTestingPlanName": "***string***",
      "ScheduleExpression": "***string***",
      "ScheduleExpressionTimezone": "***string***",
      "StartWindowHours": ***number***
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[RestoreTestingPlan](#API_GetRestoreTestingPlan_ResponseSyntax "#API_GetRestoreTestingPlan_ResponseSyntax")**

Specifies the body of a restore testing plan. Includes
`RestoreTestingPlanName`.

Type: [RestoreTestingPlanForGet](API_RestoreTestingPlanForGet.md "API_RestoreTestingPlanForGet.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/GetRestoreTestingPlan.md "../../../goto/cli2/backup-2018-11-15/GetRestoreTestingPlan.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/GetRestoreTestingPlan.md "../../../goto/DotNetSDKV3/backup-2018-11-15/GetRestoreTestingPlan.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/GetRestoreTestingPlan.md "../../../goto/SdkForCpp/backup-2018-11-15/GetRestoreTestingPlan.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/GetRestoreTestingPlan.md "../../../goto/SdkForGoV2/backup-2018-11-15/GetRestoreTestingPlan.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/GetRestoreTestingPlan.md "../../../goto/SdkForJavaV2/backup-2018-11-15/GetRestoreTestingPlan.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetRestoreTestingPlan.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetRestoreTestingPlan.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/GetRestoreTestingPlan.md "../../../goto/SdkForKotlin/backup-2018-11-15/GetRestoreTestingPlan.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/GetRestoreTestingPlan.md "../../../goto/SdkForPHPV3/backup-2018-11-15/GetRestoreTestingPlan.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/GetRestoreTestingPlan.md "../../../goto/boto3/backup-2018-11-15/GetRestoreTestingPlan.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/GetRestoreTestingPlan.md "../../../goto/SdkForRubyV3/backup-2018-11-15/GetRestoreTestingPlan.md")
