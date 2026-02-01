# CopyProduct

Copies the specified source product to the specified target product or a new
product.

You can copy a product to the same account or another account. You can copy a product
to the same Region or another Region. If you copy a product to another account, you must
first share the product in a portfolio using [CreatePortfolioShare](API_CreatePortfolioShare.md "API_CreatePortfolioShare.md").

This operation is performed asynchronously. To track the progress of the
operation, use [DescribeCopyProductStatus](API_DescribeCopyProductStatus.md "API_DescribeCopyProductStatus.md").

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "CopyOptions": [ "`string`" ],
   "IdempotencyToken": "`string`",
   "SourceProductArn": "`string`",
   "SourceProvisioningArtifactIdentifiers": [
      {
         "`string`" : "`string`"
      }
   ],
   "TargetProductId": "`string`",
   "TargetProductName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_CopyProduct_RequestSyntax "#API_CopyProduct_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[CopyOptions](#API_CopyProduct_RequestSyntax "#API_CopyProduct_RequestSyntax")**

The copy options. If the value is `CopyTags`, the tags from the source
product are copied to the target product.

Type: Array of strings

Valid Values: `CopyTags`

Required: No

**[IdempotencyToken](#API_CopyProduct_RequestSyntax "#API_CopyProduct_RequestSyntax")**

A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token,
the same response is returned for each repeated request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: Yes

**[SourceProductArn](#API_CopyProduct_RequestSyntax "#API_CopyProduct_RequestSyntax")**

The Amazon Resource Name (ARN) of the source product.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1224.

Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

Required: Yes

**[SourceProvisioningArtifactIdentifiers](#API_CopyProduct_RequestSyntax "#API_CopyProduct_RequestSyntax")**

The identifiers of the provisioning artifacts (also known as versions) of the product to copy.
By default, all provisioning artifacts are copied.

Type: Array of string to string maps

Valid Keys: `Id`

Required: No

**[TargetProductId](#API_CopyProduct_RequestSyntax "#API_CopyProduct_RequestSyntax")**

The identifier of the target product. By default, a new product is created.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[TargetProductName](#API_CopyProduct_RequestSyntax "#API_CopyProduct_RequestSyntax")**

A name for the target product. The default is the name of the source product.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

## Response Syntax

```
{
   "CopyProductToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CopyProductToken](#API_CopyProduct_ResponseSyntax "#API_CopyProduct_ResponseSyntax")**

The token to use to track the progress of the operation.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/CopyProduct.md "../../../goto/cli2/servicecatalog-2015-12-10/CopyProduct.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/CopyProduct.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/CopyProduct.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/CopyProduct.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/CopyProduct.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/CopyProduct.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/CopyProduct.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/CopyProduct.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/CopyProduct.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CopyProduct.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CopyProduct.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/CopyProduct.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/CopyProduct.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/CopyProduct.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/CopyProduct.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/CopyProduct.md "../../../goto/boto3/servicecatalog-2015-12-10/CopyProduct.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/CopyProduct.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/CopyProduct.md")
