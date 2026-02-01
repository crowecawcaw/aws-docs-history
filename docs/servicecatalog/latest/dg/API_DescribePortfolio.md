# DescribePortfolio

Gets information about the specified portfolio.

A delegated admin is authorized to invoke this command.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "Id": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DescribePortfolio_RequestSyntax "#API_DescribePortfolio_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Id](#API_DescribePortfolio_RequestSyntax "#API_DescribePortfolio_RequestSyntax")**

The portfolio identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "Budgets": [
      {
         "BudgetName": "***string***"
      }
   ],
   "PortfolioDetail": {
      "ARN": "***string***",
      "CreatedTime": ***number***,
      "Description": "***string***",
      "DisplayName": "***string***",
      "Id": "***string***",
      "ProviderName": "***string***"
   },
   "TagOptions": [
      {
         "Active": ***boolean***,
         "Id": "***string***",
         "Key": "***string***",
         "Owner": "***string***",
         "Value": "***string***"
      }
   ],
   "Tags": [
      {
         "Key": "***string***",
         "Value": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Budgets](#API_DescribePortfolio_ResponseSyntax "#API_DescribePortfolio_ResponseSyntax")**

Information about the associated budgets.

Type: Array of [BudgetDetail](API_BudgetDetail.md "API_BudgetDetail.md") objects

**[PortfolioDetail](#API_DescribePortfolio_ResponseSyntax "#API_DescribePortfolio_ResponseSyntax")**

Information about the portfolio.

Type: [PortfolioDetail](API_PortfolioDetail.md "API_PortfolioDetail.md") object

**[TagOptions](#API_DescribePortfolio_ResponseSyntax "#API_DescribePortfolio_ResponseSyntax")**

Information about the TagOptions associated with the portfolio.

Type: Array of [TagOptionDetail](API_TagOptionDetail.md "API_TagOptionDetail.md") objects

**[Tags](#API_DescribePortfolio_ResponseSyntax "#API_DescribePortfolio_ResponseSyntax")**

Information about the tags associated with the portfolio.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Maximum number of 50 items.

## Errors

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DescribePortfolio.md "../../../goto/cli2/servicecatalog-2015-12-10/DescribePortfolio.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribePortfolio.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribePortfolio.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribePortfolio.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribePortfolio.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribePortfolio.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribePortfolio.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribePortfolio.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribePortfolio.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribePortfolio.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribePortfolio.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribePortfolio.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribePortfolio.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribePortfolio.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribePortfolio.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DescribePortfolio.md "../../../goto/boto3/servicecatalog-2015-12-10/DescribePortfolio.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribePortfolio.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribePortfolio.md")
