# NotifyTerminateProvisionedProductEngineWorkflowResult

Notifies the result
of the terminate engine execution.

## Request Syntax

```
{
   "FailureReason": "`string`",
   "IdempotencyToken": "`string`",
   "RecordId": "`string`",
   "Status": "`string`",
   "WorkflowToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[FailureReason](#API_NotifyTerminateProvisionedProductEngineWorkflowResult_RequestSyntax "#API_NotifyTerminateProvisionedProductEngineWorkflowResult_RequestSyntax")**

The reason
why the terminate engine execution failed.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[IdempotencyToken](#API_NotifyTerminateProvisionedProductEngineWorkflowResult_RequestSyntax "#API_NotifyTerminateProvisionedProductEngineWorkflowResult_RequestSyntax")**

The idempotency token
that identifies the terminate engine execution.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: Yes

**[RecordId](#API_NotifyTerminateProvisionedProductEngineWorkflowResult_RequestSyntax "#API_NotifyTerminateProvisionedProductEngineWorkflowResult_RequestSyntax")**

The identifier
of the record.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[Status](#API_NotifyTerminateProvisionedProductEngineWorkflowResult_RequestSyntax "#API_NotifyTerminateProvisionedProductEngineWorkflowResult_RequestSyntax")**

The status
of the terminate engine execution.

Type: String

Valid Values: `SUCCEEDED | FAILED`

Required: Yes

**[WorkflowToken](#API_NotifyTerminateProvisionedProductEngineWorkflowResult_RequestSyntax "#API_NotifyTerminateProvisionedProductEngineWorkflowResult_RequestSyntax")**

The encrypted contents
of the terminate engine execution payload
that Service Catalog sends
after the Terraform product terminate workflow starts.

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

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md "../../../goto/cli2/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md "../../../goto/boto3/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/NotifyTerminateProvisionedProductEngineWorkflowResult.md")
