# DeleteProvisioningArtifact

Deletes the specified provisioning artifact (also known as a version) for the specified product.

You cannot delete a provisioning artifact associated with a product that was shared with you.
You cannot delete the last provisioning artifact for a product, because a product must have at
least one provisioning artifact.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "ProductId": "`string`",
   "ProvisioningArtifactId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DeleteProvisioningArtifact_RequestSyntax "#API_DeleteProvisioningArtifact_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[ProductId](#API_DeleteProvisioningArtifact_RequestSyntax "#API_DeleteProvisioningArtifact_RequestSyntax")**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[ProvisioningArtifactId](#API_DeleteProvisioningArtifact_RequestSyntax "#API_DeleteProvisioningArtifact_RequestSyntax")**

The identifier of the provisioning artifact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceInUseException**

A resource that is currently in use. Ensure that the resource is not in use and retry the operation.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md "../../../goto/cli2/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md "../../../goto/boto3/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DeleteProvisioningArtifact.md")
