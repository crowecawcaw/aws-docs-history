# RejectPortfolioShare

Rejects an offer to share the specified portfolio.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "PortfolioId": "`string`",
   "PortfolioShareType": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_RejectPortfolioShare_RequestSyntax "#API_RejectPortfolioShare_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[PortfolioId](#API_RejectPortfolioShare_RequestSyntax "#API_RejectPortfolioShare_RequestSyntax")**

The portfolio identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[PortfolioShareType](#API_RejectPortfolioShare_RequestSyntax "#API_RejectPortfolioShare_RequestSyntax")**

The type of shared portfolios to reject. The default is to reject imported portfolios.

- `AWS_ORGANIZATIONS` - Reject portfolios shared by the management account of your
  organization.
- `IMPORTED` - Reject imported portfolios.
- `AWS_SERVICECATALOG` - Not supported. (Throws ResourceNotFoundException.)

For example, `aws servicecatalog reject-portfolio-share --portfolio-id "port-2qwzkwxt3y5fk" --portfolio-share-type AWS_ORGANIZATIONS`

Type: String

Valid Values: `IMPORTED | AWS_SERVICECATALOG | AWS_ORGANIZATIONS`

Required: No

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/RejectPortfolioShare.md "../../../goto/cli2/servicecatalog-2015-12-10/RejectPortfolioShare.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/RejectPortfolioShare.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/RejectPortfolioShare.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/RejectPortfolioShare.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/RejectPortfolioShare.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/RejectPortfolioShare.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/RejectPortfolioShare.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/RejectPortfolioShare.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/RejectPortfolioShare.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/RejectPortfolioShare.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/RejectPortfolioShare.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/RejectPortfolioShare.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/RejectPortfolioShare.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/RejectPortfolioShare.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/RejectPortfolioShare.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/RejectPortfolioShare.md "../../../goto/boto3/servicecatalog-2015-12-10/RejectPortfolioShare.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/RejectPortfolioShare.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/RejectPortfolioShare.md")
