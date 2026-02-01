# DisassociateServiceActionFromProvisioningArtifact

Disassociates the specified self-service action association from the specified provisioning artifact.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "IdempotencyToken": "`string`",
   "ProductId": "`string`",
   "ProvisioningArtifactId": "`string`",
   "ServiceActionId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax "#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[IdempotencyToken](#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax "#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax")**

A unique identifier that you provide to ensure idempotency. If multiple requests from the same AWS account use the same idempotency token, the same response is returned for each repeated request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: No

**[ProductId](#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax "#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax")**

The product identifier. For example, `prod-abcdzk7xy33qa`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[ProvisioningArtifactId](#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax "#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax")**

The identifier of the provisioning artifact. For example, `pa-4abcdjnxjj6ne`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[ServiceActionId](#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax "#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax")**

The self-service action identifier. For example, `act-fs7abcd89wxyz`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md "../../../goto/cli2/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md "../../../goto/boto3/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact.md")
