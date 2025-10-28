# NotifyUpdateProvisionedProductEngineWorkflowResult

Notifies the result
of the update engine execution.

## Request Syntax

```
{
   "FailureReason": "`string`",
   "IdempotencyToken": "`string`",
   "Outputs": [
      {
         "Description": "`string`",
         "OutputKey": "`string`",
         "OutputValue": "`string`"
      }
   ],
   "RecordId": "`string`",
   "Status": "`string`",
   "WorkflowToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[FailureReason](#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax "#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax")**

The reason
why the update engine execution failed.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[IdempotencyToken](#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax "#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax")**

The idempotency token
that identifies the update engine execution.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: Yes

**[Outputs](#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax "#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax")**

The output
of the update engine execution.

Type: Array of [RecordOutput](API_RecordOutput.md "API_RecordOutput.md") objects

Required: No

**[RecordId](#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax "#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax")**

The identifier
of the record.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[Status](#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax "#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax")**

The status
of the update engine execution.

Type: String

Valid Values: `SUCCEEDED | FAILED`

Required: Yes

**[WorkflowToken](#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax "#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax")**

The encrypted contents
of the update engine execution payload
that Service Catalog sends
after the Terraform product update workflow starts.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 20000.

Pattern: `[0-9A-Za-z+\/\-=]+`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md "../../../goto/cli2/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md "../../../goto/boto3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult.md")
