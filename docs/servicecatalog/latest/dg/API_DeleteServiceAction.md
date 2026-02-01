# DeleteServiceAction

Deletes a self-service action.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "Id": "`string`",
   "IdempotencyToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DeleteServiceAction_RequestSyntax "#API_DeleteServiceAction_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Id](#API_DeleteServiceAction_RequestSyntax "#API_DeleteServiceAction_RequestSyntax")**

The self-service action identifier. For example, `act-fs7abcd89wxyz`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[IdempotencyToken](#API_DeleteServiceAction_RequestSyntax "#API_DeleteServiceAction_RequestSyntax")**

A unique identifier that you provide to ensure idempotency. If multiple requests from the same AWS account use the same idempotency token, the same response is returned for each repeated request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: No

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**ResourceInUseException**

A resource that is currently in use. Ensure that the resource is not in use and retry the operation.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DeleteServiceAction.md "../../../goto/cli2/servicecatalog-2015-12-10/DeleteServiceAction.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DeleteServiceAction.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DeleteServiceAction.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DeleteServiceAction.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DeleteServiceAction.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DeleteServiceAction.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DeleteServiceAction.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DeleteServiceAction.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DeleteServiceAction.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DeleteServiceAction.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DeleteServiceAction.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DeleteServiceAction.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DeleteServiceAction.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DeleteServiceAction.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DeleteServiceAction.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DeleteServiceAction.md "../../../goto/boto3/servicecatalog-2015-12-10/DeleteServiceAction.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DeleteServiceAction.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DeleteServiceAction.md")
