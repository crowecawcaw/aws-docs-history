# SearchProducts

Gets information about the products to which the caller has access.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "Filters": {
      "`string`" : [ "`string`" ]
   },
   "PageSize": `number`,
   "PageToken": "`string`",
   "SortBy": "`string`",
   "SortOrder": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_SearchProducts_RequestSyntax "#API_SearchProducts_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Filters](#API_SearchProducts_RequestSyntax "#API_SearchProducts_RequestSyntax")**

The search filters. If no search filters are specified, the output includes
all products to which the caller has access.

Type: String to array of strings map

Valid Keys: `FullTextSearch | Owner | ProductType | SourceProductId`

Required: No

**[PageSize](#API_SearchProducts_RequestSyntax "#API_SearchProducts_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**[PageToken](#API_SearchProducts_RequestSyntax "#API_SearchProducts_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[SortBy](#API_SearchProducts_RequestSyntax "#API_SearchProducts_RequestSyntax")**

The sort field. If no value is specified, the results are not sorted.

Type: String

Valid Values: `Title | VersionCount | CreationDate`

Required: No

**[SortOrder](#API_SearchProducts_RequestSyntax "#API_SearchProducts_RequestSyntax")**

The sort order. If no value is specified, the results are not sorted.

Type: String

Valid Values: `ASCENDING | DESCENDING`

Required: No

## Response Syntax

```
{
   "NextPageToken": "***string***",
   "ProductViewAggregations": {
      "***string***" : [
         {
            "ApproximateCount": ***number***,
            "Value": "***string***"
         }
      ]
   },
   "ProductViewSummaries": [
      {
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
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextPageToken](#API_SearchProducts_ResponseSyntax "#API_SearchProducts_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[ProductViewAggregations](#API_SearchProducts_ResponseSyntax "#API_SearchProducts_ResponseSyntax")**

The product view aggregations.

Type: String to array of [ProductViewAggregationValue](API_ProductViewAggregationValue.md "API_ProductViewAggregationValue.md") objects map

**[ProductViewSummaries](#API_SearchProducts_ResponseSyntax "#API_SearchProducts_ResponseSyntax")**

Information about the product views.

Type: Array of [ProductViewSummary](API_ProductViewSummary.md "API_ProductViewSummary.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

## Examples

### Search for all available products

The following JSON example retrieves all products available to the current
user.

#### Sample Request

```
POST
/
content-type:application/x-amz-json-1.1
host:servicecatalog.us-west-2.amazonaws.com
user-agent:aws-cli/1.10.19 Python/2.7.10 Darwin/15.5.0 botocore/1.4.10
x-amz-date:20160607T224008Z
x-amz-target:AWS242ServiceCatalogService.SearchProducts
```

#### Sample Response

```
{
   "ProductViewAggregations":
   {
      "Owner":
      [
         {
            "ApproximateCount":4,
            "Value":"387896429941"
         }
      ],
      "ProductType":
      [
         {
            "ApproximateCount":4,
            "Value":"ServiceCatalog"
         }
      ],
      "Vendor":
      [
         {
            "ApproximateCount":1,
            "Value":""
         },
         {
            "ApproximateCount":1,
            "Value":"me"
         }
      ]
   },
   "ProductViewSummaries":
   [
      {
         "HasDefaultPath":false,
         "Id":"prodview-w35uhtf6nrqqy",
         "Name":"RDS template",
         "Owner":"AWS",
         "ProductId":"prod-3tsertlc2g7pw",
         "ShortDescription":"Test 2",
         "Type":"Base"
      },
      {
         "HasDefaultPath":false,
         "Id":"prodview-r2tzjgsao7mc4",
         "Name":"Devo enviro 2",
         "Owner":"asda",
         "ProductId":"prod-enx2jvf33gi52",
         "ShortDescription":"asd",
         "Type":"Base"
      },
      {
         "Distributor":"",
         "HasDefaultPath":false,
         "Id":"prodview-e64tf73gp3gl4",
         "Name":"Devo environment",
         "Owner":"test",
         "ProductId":"prod-3p2k2ejvcsdvi",
         "ShortDescription":"test",
         "Type":"Base"
      },
      {
         "Distributor":"Me",
         "HasDefaultPath":false,
         "Id":"prodview-3fmrw464floam",
         "Name":"Testtemplate",
         "Owner":"MSP XYZ",
         "ProductId":"prod-eqeqzgemstiea",
         "ShortDescription":"asdas",
         "Type":"Base"
      }
   ]
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/SearchProducts.md "../../../goto/cli2/servicecatalog-2015-12-10/SearchProducts.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/SearchProducts.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/SearchProducts.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/SearchProducts.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/SearchProducts.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/SearchProducts.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/SearchProducts.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/SearchProducts.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/SearchProducts.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/SearchProducts.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/SearchProducts.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/SearchProducts.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/SearchProducts.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/SearchProducts.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/SearchProducts.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/SearchProducts.md "../../../goto/boto3/servicecatalog-2015-12-10/SearchProducts.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/SearchProducts.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/SearchProducts.md")
