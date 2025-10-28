# DisassociatePrincipalFromPortfolio

Disassociates a previously associated principal ARN from a specified
portfolio.

The `PrincipalType` and `PrincipalARN` must match the
`AssociatePrincipalWithPortfolio` call request details. For example,
to disassociate an association created with a `PrincipalARN` of `PrincipalType`
IAM you must use the `PrincipalType` IAM when calling `DisassociatePrincipalFromPortfolio`.

For portfolios that have been shared with principal name sharing enabled: after disassociating a principal,
share recipient accounts will no longer be able to provision products in this portfolio using a role matching the name
of the associated principal.

For more information, review [associate-principal-with-portfolio](../../../cli/latest/reference/servicecatalog/associate-principal-with-portfolio.md#options "../../../cli/latest/reference/servicecatalog/associate-principal-with-portfolio.md#options")
in the AWS CLI Command Reference.

###### Note

If you disassociate a principal from a portfolio, with PrincipalType as `IAM`, the same principal will
still have access to the portfolio if it matches one of the associated principals of type `IAM_PATTERN`.
To fully remove access for a principal, verify all the associated Principals of type `IAM_PATTERN`,
and then ensure you disassociate any `IAM_PATTERN` principals that match the principal
whose access you are removing.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "PortfolioId": "`string`",
   "PrincipalARN": "`string`",
   "PrincipalType": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DisassociatePrincipalFromPortfolio_RequestSyntax "#API_DisassociatePrincipalFromPortfolio_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[PortfolioId](#API_DisassociatePrincipalFromPortfolio_RequestSyntax "#API_DisassociatePrincipalFromPortfolio_RequestSyntax")**

The portfolio identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[PrincipalARN](#API_DisassociatePrincipalFromPortfolio_RequestSyntax "#API_DisassociatePrincipalFromPortfolio_RequestSyntax")**

The ARN of the principal (user, role, or group). This field allows an ARN with no `accountID` with or without wildcard characters if
`PrincipalType` is `IAM_PATTERN`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1000.

Required: Yes

**[PrincipalType](#API_DisassociatePrincipalFromPortfolio_RequestSyntax "#API_DisassociatePrincipalFromPortfolio_RequestSyntax")**

The supported value is `IAM` if you use a fully defined ARN, or `IAM_PATTERN`
if you specify an `IAM` ARN with no AccountId, with or without wildcard characters.

Type: String

Valid Values: `IAM | IAM_PATTERN`

Required: No

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

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md "../../../goto/cli2/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md "../../../goto/boto3/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio.md")
