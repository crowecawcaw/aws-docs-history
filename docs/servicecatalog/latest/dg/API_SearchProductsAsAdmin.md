# SearchProductsAsAdmin

Gets information about the products for the specified portfolio or all products.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "Filters": {
      "`string`" : [ "`string`" ]
   },
   "PageSize": `number`,
   "PageToken": "`string`",
   "PortfolioId": "`string`",
   "ProductSource": "`string`",
   "SortBy": "`string`",
   "SortOrder": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_SearchProductsAsAdmin_RequestSyntax "#API_SearchProductsAsAdmin_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Filters](#API_SearchProductsAsAdmin_RequestSyntax "#API_SearchProductsAsAdmin_RequestSyntax")**

The search filters. If no search filters are specified, the output includes all products
to which the administrator has access.

Type: String to array of strings map

Valid Keys: `FullTextSearch | Owner | ProductType | SourceProductId`

Required: No

**[PageSize](#API_SearchProductsAsAdmin_RequestSyntax "#API_SearchProductsAsAdmin_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**[PageToken](#API_SearchProductsAsAdmin_RequestSyntax "#API_SearchProductsAsAdmin_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[PortfolioId](#API_SearchProductsAsAdmin_RequestSyntax "#API_SearchProductsAsAdmin_RequestSyntax")**

The portfolio identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[ProductSource](#API_SearchProductsAsAdmin_RequestSyntax "#API_SearchProductsAsAdmin_RequestSyntax")**

Access level of the source of the product.

Type: String

Valid Values: `ACCOUNT`

Required: No

**[SortBy](#API_SearchProductsAsAdmin_RequestSyntax "#API_SearchProductsAsAdmin_RequestSyntax")**

The sort field. If no value is specified, the results are not sorted.

Type: String

Valid Values: `Title | VersionCount | CreationDate`

Required: No

**[SortOrder](#API_SearchProductsAsAdmin_RequestSyntax "#API_SearchProductsAsAdmin_RequestSyntax")**

The sort order. If no value is specified, the results are not sorted.

Type: String

Valid Values: `ASCENDING | DESCENDING`

Required: No

## Response Syntax

```
{
   "NextPageToken": "***string***",
   "ProductViewDetails": [
      {
         "CreatedTime": ***number***,
         "ProductARN": "***string***",
         "ProductViewSummary": {
            "Distributor": "***string***",
            "HasDefaultPath": ***boolean***,
            "Id": "***string***",
            "Name": "***string***",
            "Owner": "***string***",
            "ProductId": "***string***",
            "ShortDescription": "***string***",
            "SupportDescription": "***string***",
            "SupportEmail": "***string***",
            "SupportUrl": "***string***",
            "Type": "***string***"
         },
         "SourceConnection": {
            "ConnectionParameters": {
               "CodeStar": {
                  "ArtifactPath": "***string***",
                  "Branch": "***string***",
                  "ConnectionArn": "***string***",
                  "Repository": "***string***"
               }
            },
            "LastSync": {
               "LastSuccessfulSyncProvisioningArtifactId": "***string***",
               "LastSuccessfulSyncTime": ***number***,
               "LastSyncStatus": "***string***",
               "LastSyncStatusMessage": "***string***",
               "LastSyncTime": ***number***
            },
            "Type": "***string***"
         },
         "Status": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextPageToken](#API_SearchProductsAsAdmin_ResponseSyntax "#API_SearchProductsAsAdmin_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[ProductViewDetails](#API_SearchProductsAsAdmin_ResponseSyntax "#API_SearchProductsAsAdmin_ResponseSyntax")**

Information about the product views.

Type: Array of [ProductViewDetail](API_ProductViewDetail.md "API_ProductViewDetail.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/SearchProductsAsAdmin.md "../../../goto/cli2/servicecatalog-2015-12-10/SearchProductsAsAdmin.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/SearchProductsAsAdmin.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/SearchProductsAsAdmin.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/SearchProductsAsAdmin.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/SearchProductsAsAdmin.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/SearchProductsAsAdmin.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/SearchProductsAsAdmin.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/SearchProductsAsAdmin.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/SearchProductsAsAdmin.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/SearchProductsAsAdmin.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/SearchProductsAsAdmin.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/SearchProductsAsAdmin.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/SearchProductsAsAdmin.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/SearchProductsAsAdmin.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/SearchProductsAsAdmin.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/SearchProductsAsAdmin.md "../../../goto/boto3/servicecatalog-2015-12-10/SearchProductsAsAdmin.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/SearchProductsAsAdmin.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/SearchProductsAsAdmin.md")
