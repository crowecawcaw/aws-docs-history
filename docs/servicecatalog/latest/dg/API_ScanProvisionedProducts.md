# ScanProvisionedProducts

Lists the provisioned products that are available (not terminated).

To use additional filtering, see [SearchProvisionedProducts](API_SearchProvisionedProducts.md "API_SearchProvisionedProducts.md").

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "AccessLevelFilter": {
      "Key": "`string`",
      "Value": "`string`"
   },
   "PageSize": `number`,
   "PageToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_ScanProvisionedProducts_RequestSyntax "#API_ScanProvisionedProducts_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[AccessLevelFilter](#API_ScanProvisionedProducts_RequestSyntax "#API_ScanProvisionedProducts_RequestSyntax")**

The access level to use to obtain results. The default is `User`.

Type: [AccessLevelFilter](API_AccessLevelFilter.md "API_AccessLevelFilter.md") object

Required: No

**[PageSize](#API_ScanProvisionedProducts_RequestSyntax "#API_ScanProvisionedProducts_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 20.

Required: No

**[PageToken](#API_ScanProvisionedProducts_RequestSyntax "#API_ScanProvisionedProducts_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

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
         "ProductId": "***string***",
         "ProvisioningArtifactId": "***string***",
         "Status": "***string***",
         "StatusMessage": "***string***",
         "Type": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextPageToken](#API_ScanProvisionedProducts_ResponseSyntax "#API_ScanProvisionedProducts_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[ProvisionedProducts](#API_ScanProvisionedProducts_ResponseSyntax "#API_ScanProvisionedProducts_ResponseSyntax")**

Information about the provisioned products.

Type: Array of [ProvisionedProductDetail](API_ProvisionedProductDetail.md "API_ProvisionedProductDetail.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ScanProvisionedProducts.md "../../../goto/cli2/servicecatalog-2015-12-10/ScanProvisionedProducts.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ScanProvisionedProducts.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ScanProvisionedProducts.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ScanProvisionedProducts.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ScanProvisionedProducts.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ScanProvisionedProducts.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ScanProvisionedProducts.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ScanProvisionedProducts.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ScanProvisionedProducts.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ScanProvisionedProducts.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ScanProvisionedProducts.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ScanProvisionedProducts.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ScanProvisionedProducts.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ScanProvisionedProducts.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ScanProvisionedProducts.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ScanProvisionedProducts.md "../../../goto/boto3/servicecatalog-2015-12-10/ScanProvisionedProducts.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ScanProvisionedProducts.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ScanProvisionedProducts.md")
