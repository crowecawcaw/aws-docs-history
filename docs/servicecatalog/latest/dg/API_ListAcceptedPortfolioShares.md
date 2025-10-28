# ListAcceptedPortfolioShares

Lists all imported portfolios for which account-to-account shares were accepted by
this account. By specifying the `PortfolioShareType`, you can list portfolios for which
organizational shares were accepted by this account.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "PageSize": `number`,
   "PageToken": "`string`",
   "PortfolioShareType": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_ListAcceptedPortfolioShares_RequestSyntax "#API_ListAcceptedPortfolioShares_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[PageSize](#API_ListAcceptedPortfolioShares_RequestSyntax "#API_ListAcceptedPortfolioShares_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**[PageToken](#API_ListAcceptedPortfolioShares_RequestSyntax "#API_ListAcceptedPortfolioShares_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[PortfolioShareType](#API_ListAcceptedPortfolioShares_RequestSyntax "#API_ListAcceptedPortfolioShares_RequestSyntax")**

The type of shared portfolios to list. The default is to list imported portfolios.

- `AWS_ORGANIZATIONS` - List portfolios accepted and shared via organizational sharing by the management account or delegated administrator of your organization.
- `AWS_SERVICECATALOG` - Deprecated type.
- `IMPORTED` - List imported portfolios that have been accepted and
  shared through account-to-account sharing.

Type: String

Valid Values: `IMPORTED | AWS_SERVICECATALOG | AWS_ORGANIZATIONS`

Required: No

## Response Syntax

```
{
   "NextPageToken": "***string***",
   "PortfolioDetails": [
      {
         "ARN": "***string***",
         "CreatedTime": ***number***,
         "Description": "***string***",
         "DisplayName": "***string***",
         "Id": "***string***",
         "ProviderName": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextPageToken](#API_ListAcceptedPortfolioShares_ResponseSyntax "#API_ListAcceptedPortfolioShares_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[PortfolioDetails](#API_ListAcceptedPortfolioShares_ResponseSyntax "#API_ListAcceptedPortfolioShares_ResponseSyntax")**

Information about the portfolios.

Type: Array of [PortfolioDetail](API_PortfolioDetail.md "API_PortfolioDetail.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**OperationNotSupportedException**

The operation is not supported.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md "../../../goto/cli2/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md "../../../goto/boto3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares.md")
