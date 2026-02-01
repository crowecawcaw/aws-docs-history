# ListPortfolioAccess

Lists the account IDs that have access to the specified portfolio.

A delegated admin can list the accounts that have access to the shared portfolio. Note that if a delegated admin is de-registered, they can no longer perform this operation.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "OrganizationParentId": "`string`",
   "PageSize": `number`,
   "PageToken": "`string`",
   "PortfolioId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_ListPortfolioAccess_RequestSyntax "#API_ListPortfolioAccess_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[OrganizationParentId](#API_ListPortfolioAccess_RequestSyntax "#API_ListPortfolioAccess_RequestSyntax")**

The ID of an organization node the portfolio is shared with. All children of this node with an inherited portfolio share will be returned.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[PageSize](#API_ListPortfolioAccess_RequestSyntax "#API_ListPortfolioAccess_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**[PageToken](#API_ListPortfolioAccess_RequestSyntax "#API_ListPortfolioAccess_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[PortfolioId](#API_ListPortfolioAccess_RequestSyntax "#API_ListPortfolioAccess_RequestSyntax")**

The portfolio identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "AccountIds": [ "***string***" ],
   "NextPageToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AccountIds](#API_ListPortfolioAccess_ResponseSyntax "#API_ListPortfolioAccess_ResponseSyntax")**

Information about the AWS accounts with access to the portfolio.

Type: Array of strings

Pattern: `^[0-9]{12}$`

**[NextPageToken](#API_ListPortfolioAccess_ResponseSyntax "#API_ListPortfolioAccess_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ListPortfolioAccess.md "../../../goto/cli2/servicecatalog-2015-12-10/ListPortfolioAccess.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListPortfolioAccess.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListPortfolioAccess.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListPortfolioAccess.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListPortfolioAccess.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListPortfolioAccess.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListPortfolioAccess.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListPortfolioAccess.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListPortfolioAccess.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListPortfolioAccess.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListPortfolioAccess.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListPortfolioAccess.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListPortfolioAccess.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListPortfolioAccess.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListPortfolioAccess.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ListPortfolioAccess.md "../../../goto/boto3/servicecatalog-2015-12-10/ListPortfolioAccess.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListPortfolioAccess.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListPortfolioAccess.md")
