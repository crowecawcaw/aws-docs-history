# ListPrincipalsForPortfolio

Lists all `PrincipalARN`s and corresponding `PrincipalType`s associated with the specified portfolio.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "PageSize": `number`,
   "PageToken": "`string`",
   "PortfolioId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_ListPrincipalsForPortfolio_RequestSyntax "#API_ListPrincipalsForPortfolio_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[PageSize](#API_ListPrincipalsForPortfolio_RequestSyntax "#API_ListPrincipalsForPortfolio_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 20.

Required: No

**[PageToken](#API_ListPrincipalsForPortfolio_RequestSyntax "#API_ListPrincipalsForPortfolio_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[PortfolioId](#API_ListPrincipalsForPortfolio_RequestSyntax "#API_ListPrincipalsForPortfolio_RequestSyntax")**

The portfolio identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "NextPageToken": "***string***",
   "Principals": [
      {
         "PrincipalARN": "***string***",
         "PrincipalType": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextPageToken](#API_ListPrincipalsForPortfolio_ResponseSyntax "#API_ListPrincipalsForPortfolio_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[Principals](#API_ListPrincipalsForPortfolio_ResponseSyntax "#API_ListPrincipalsForPortfolio_ResponseSyntax")**

The `PrincipalARN`s and corresponding `PrincipalType`s associated with the portfolio.

Type: Array of [Principal](API_Principal.md "API_Principal.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md "../../../goto/cli2/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md "../../../goto/boto3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio.md")
