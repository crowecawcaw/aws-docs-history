# SearchProvisionedProducts

Gets information about the provisioned products that meet the specified criteria.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "AccessLevelFilter": {
      "Key": "`string`",
      "Value": "`string`"
   },
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

**[AcceptLanguage](#API_SearchProvisionedProducts_RequestSyntax "#API_SearchProvisionedProducts_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[AccessLevelFilter](#API_SearchProvisionedProducts_RequestSyntax "#API_SearchProvisionedProducts_RequestSyntax")**

The access level to use to obtain results. The default is
`Account`.

Type: [AccessLevelFilter](API_AccessLevelFilter.md "API_AccessLevelFilter.md") object

Required: No

**[Filters](#API_SearchProvisionedProducts_RequestSyntax "#API_SearchProvisionedProducts_RequestSyntax")**

The search filters.

When the key is `SearchQuery`, the searchable fields are `arn`,
`createdTime`, `id`, `lastRecordId`,
`idempotencyToken`, `name`, `physicalId`, `productId`,
`provisioningArtifactId`, `type`, `status`,
`tags`, `userArn`, `userArnSession`, `lastProvisioningRecordId`, `lastSuccessfulProvisioningRecordId`,
`productName`, and `provisioningArtifactName`.

Example: `"SearchQuery":["status:AVAILABLE"]`

Type: String to array of strings map

Valid Keys: `SearchQuery`

Required: No

**[PageSize](#API_SearchProvisionedProducts_RequestSyntax "#API_SearchProvisionedProducts_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**[PageToken](#API_SearchProvisionedProducts_RequestSyntax "#API_SearchProvisionedProducts_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[SortBy](#API_SearchProvisionedProducts_RequestSyntax "#API_SearchProvisionedProducts_RequestSyntax")**

The sort field. If no value is specified, the results are not sorted. The valid values are `arn`, `id`, `name`,
and `lastRecordId`.

Type: String

Required: No

**[SortOrder](#API_SearchProvisionedProducts_RequestSyntax "#API_SearchProvisionedProducts_RequestSyntax")**

The sort order. If no value is specified, the results are not sorted.

Type: String

Valid Values: `ASCENDING | DESCENDING`

Required: No

## Response Syntax

```
{
   "NextPageToken": "***string***",
   "ProvisionedProducts": [
      {
         "Arn": "***string***",
         "CreatedTime": ***number***,
         "Id": "***string***",
         "IdempotencyToken": "***string***",
         "LastProvisioningRecordId": "***string***",
         "LastRecordId": "***string***",
         "LastSuccessfulProvisioningRecordId": "***string***",
         "LaunchRoleArn": "***string***",
         "Name": "***string***",
         "PhysicalId": "***string***",
         "ProductId": "***string***",
         "ProductName": "***string***",
         "ProvisioningArtifactId": "***string***",
         "ProvisioningArtifactName": "***string***",
         "Status": "***string***",
         "StatusMessage": "***string***",
         "Tags": [
            {
               "Key": "***string***",
               "Value": "***string***"
            }
         ],
         "Type": "***string***",
         "UserArn": "***string***",
         "UserArnSession": "***string***"
      }
   ],
   "TotalResultsCount": ***number***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextPageToken](#API_SearchProvisionedProducts_ResponseSyntax "#API_SearchProvisionedProducts_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[ProvisionedProducts](#API_SearchProvisionedProducts_ResponseSyntax "#API_SearchProvisionedProducts_ResponseSyntax")**

Information about the provisioned products.

Type: Array of [ProvisionedProductAttribute](API_ProvisionedProductAttribute.md "API_ProvisionedProductAttribute.md") objects

**[TotalResultsCount](#API_SearchProvisionedProducts_ResponseSyntax "#API_SearchProvisionedProducts_ResponseSyntax")**

The number of provisioned products found.

Type: Integer

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/SearchProvisionedProducts.md "../../../goto/cli2/servicecatalog-2015-12-10/SearchProvisionedProducts.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/SearchProvisionedProducts.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/SearchProvisionedProducts.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/SearchProvisionedProducts.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/SearchProvisionedProducts.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/SearchProvisionedProducts.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/SearchProvisionedProducts.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/SearchProvisionedProducts.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/SearchProvisionedProducts.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/SearchProvisionedProducts.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/SearchProvisionedProducts.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/SearchProvisionedProducts.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/SearchProvisionedProducts.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/SearchProvisionedProducts.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/SearchProvisionedProducts.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/SearchProvisionedProducts.md "../../../goto/boto3/servicecatalog-2015-12-10/SearchProvisionedProducts.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/SearchProvisionedProducts.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/SearchProvisionedProducts.md")
