# DescribeProductAsAdmin

Gets information about the specified product. This operation is run with administrator access.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "Id": "`string`",
   "Name": "`string`",
   "SourcePortfolioId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DescribeProductAsAdmin_RequestSyntax "#API_DescribeProductAsAdmin_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Id](#API_DescribeProductAsAdmin_RequestSyntax "#API_DescribeProductAsAdmin_RequestSyntax")**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[Name](#API_DescribeProductAsAdmin_RequestSyntax "#API_DescribeProductAsAdmin_RequestSyntax")**

The product name.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**[SourcePortfolioId](#API_DescribeProductAsAdmin_RequestSyntax "#API_DescribeProductAsAdmin_RequestSyntax")**

The unique identifier of the shared portfolio that the specified product is associated
with.

You can provide this parameter to retrieve the shared TagOptions associated with the
product. If this parameter is provided and if TagOptions sharing is enabled in the
portfolio share, the API returns both local and shared TagOptions associated with the
product. Otherwise only local TagOptions will be returned.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

## Response Syntax

```
{
   "Budgets": [
      {
         "BudgetName": "***string***"
      }
   ],
   "ProductViewDetail": {
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
   },
   "ProvisioningArtifactSummaries": [
      {
         "CreatedTime": ***number***,
         "Description": "***string***",
         "Id": "***string***",
         "Name": "***string***",
         "ProvisioningArtifactMetadata": {
            "***string***" : "***string***"
         }
      }
   ],
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

**[Budgets](#API_DescribeProductAsAdmin_ResponseSyntax "#API_DescribeProductAsAdmin_ResponseSyntax")**

Information about the associated budgets.

Type: Array of [BudgetDetail](API_BudgetDetail.md "API_BudgetDetail.md") objects

**[ProductViewDetail](#API_DescribeProductAsAdmin_ResponseSyntax "#API_DescribeProductAsAdmin_ResponseSyntax")**

Information about the product view.

Type: [ProductViewDetail](API_ProductViewDetail.md "API_ProductViewDetail.md") object

**[ProvisioningArtifactSummaries](#API_DescribeProductAsAdmin_ResponseSyntax "#API_DescribeProductAsAdmin_ResponseSyntax")**

Information about the provisioning artifacts (also known as versions) for the specified product.

Type: Array of [ProvisioningArtifactSummary](API_ProvisioningArtifactSummary.md "API_ProvisioningArtifactSummary.md") objects

**[TagOptions](#API_DescribeProductAsAdmin_ResponseSyntax "#API_DescribeProductAsAdmin_ResponseSyntax")**

Information about the TagOptions associated with the product.

Type: Array of [TagOptionDetail](API_TagOptionDetail.md "API_TagOptionDetail.md") objects

**[Tags](#API_DescribeProductAsAdmin_ResponseSyntax "#API_DescribeProductAsAdmin_ResponseSyntax")**

Information about the tags associated with the product.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Maximum number of 50 items.

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DescribeProductAsAdmin.md "../../../goto/cli2/servicecatalog-2015-12-10/DescribeProductAsAdmin.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/DescribeProductAsAdmin.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/DescribeProductAsAdmin.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProductAsAdmin.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProductAsAdmin.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProductAsAdmin.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProductAsAdmin.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProductAsAdmin.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProductAsAdmin.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProductAsAdmin.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProductAsAdmin.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProductAsAdmin.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProductAsAdmin.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProductAsAdmin.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProductAsAdmin.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DescribeProductAsAdmin.md "../../../goto/boto3/servicecatalog-2015-12-10/DescribeProductAsAdmin.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProductAsAdmin.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProductAsAdmin.md")
