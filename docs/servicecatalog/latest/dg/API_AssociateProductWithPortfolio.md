# AssociateProductWithPortfolio

Associates the specified product with the specified portfolio.

A delegated admin is authorized to invoke this command.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "PortfolioId": "`string`",
   "ProductId": "`string`",
   "SourcePortfolioId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_AssociateProductWithPortfolio_RequestSyntax "#API_AssociateProductWithPortfolio_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[PortfolioId](#API_AssociateProductWithPortfolio_RequestSyntax "#API_AssociateProductWithPortfolio_RequestSyntax")**

The portfolio identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[ProductId](#API_AssociateProductWithPortfolio_RequestSyntax "#API_AssociateProductWithPortfolio_RequestSyntax")**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[SourcePortfolioId](#API_AssociateProductWithPortfolio_RequestSyntax "#API_AssociateProductWithPortfolio_RequestSyntax")**

The identifier of the source portfolio.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**LimitExceededException**

The current limits of the service would have been exceeded by this operation. Decrease your
resource use or increase your service limits and retry the operation.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md "../../../goto/cli2/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md "../../../goto/boto3/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/AssociateProductWithPortfolio.md")
