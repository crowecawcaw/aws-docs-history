# UpdatePortfolio

Updates the specified portfolio.

You cannot update a product that was shared with you.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "AddTags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "Description": "`string`",
   "DisplayName": "`string`",
   "Id": "`string`",
   "ProviderName": "`string`",
   "RemoveTags": [ "`string`" ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_UpdatePortfolio_RequestSyntax "#API_UpdatePortfolio_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[AddTags](#API_UpdatePortfolio_RequestSyntax "#API_UpdatePortfolio_RequestSyntax")**

The tags to add.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Maximum number of 20 items.

Required: No

**[Description](#API_UpdatePortfolio_RequestSyntax "#API_UpdatePortfolio_RequestSyntax")**

The updated description of the portfolio.

Type: String

Length Constraints: Maximum length of 2000.

Required: No

**[DisplayName](#API_UpdatePortfolio_RequestSyntax "#API_UpdatePortfolio_RequestSyntax")**

The name to use for display purposes.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: No

**[Id](#API_UpdatePortfolio_RequestSyntax "#API_UpdatePortfolio_RequestSyntax")**

The portfolio identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[ProviderName](#API_UpdatePortfolio_RequestSyntax "#API_UpdatePortfolio_RequestSyntax")**

The updated name of the portfolio provider.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: No

**[RemoveTags](#API_UpdatePortfolio_RequestSyntax "#API_UpdatePortfolio_RequestSyntax")**

The tags to remove.

Type: Array of strings

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: No

## Response Syntax

```
{
   "PortfolioDetail": {
      "ARN": "***string***",
      "CreatedTime": ***number***,
      "Description": "***string***",
      "DisplayName": "***string***",
      "Id": "***string***",
      "ProviderName": "***string***"
   },
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

**[PortfolioDetail](#API_UpdatePortfolio_ResponseSyntax "#API_UpdatePortfolio_ResponseSyntax")**

Information about the portfolio.

Type: [PortfolioDetail](API_PortfolioDetail.md "API_PortfolioDetail.md") object

**[Tags](#API_UpdatePortfolio_ResponseSyntax "#API_UpdatePortfolio_ResponseSyntax")**

Information about the tags associated with the portfolio.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Maximum number of 50 items.

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

**TagOptionNotMigratedException**

An operation requiring TagOptions failed because the TagOptions migration process has
not been performed for this account. Use the AWS Management Console to perform the migration
process before retrying the operation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/UpdatePortfolio.md "../../../goto/cli2/servicecatalog-2015-12-10/UpdatePortfolio.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/UpdatePortfolio.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/UpdatePortfolio.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdatePortfolio.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdatePortfolio.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdatePortfolio.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdatePortfolio.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdatePortfolio.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdatePortfolio.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdatePortfolio.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdatePortfolio.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdatePortfolio.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdatePortfolio.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdatePortfolio.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdatePortfolio.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/UpdatePortfolio.md "../../../goto/boto3/servicecatalog-2015-12-10/UpdatePortfolio.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdatePortfolio.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdatePortfolio.md")
