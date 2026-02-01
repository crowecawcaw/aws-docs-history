# DescribeProduct

Gets information about the specified product.

###### Note

Running this operation
with administrator access
results
in a failure.
[DescribeProductAsAdmin](API_DescribeProductAsAdmin.md "API_DescribeProductAsAdmin.md") should be used instead.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "Id": "`string`",
   "Name": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DescribeProduct_RequestSyntax "#API_DescribeProduct_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Id](#API_DescribeProduct_RequestSyntax "#API_DescribeProduct_RequestSyntax")**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[Name](#API_DescribeProduct_RequestSyntax "#API_DescribeProduct_RequestSyntax")**

The product name.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

## Response Syntax

```
{
   "Budgets": [
      {
         "BudgetName": "***string***"
      }
   ],
   "LaunchPaths": [
      {
         "Id": "***string***",
         "Name": "***string***"
      }
   ],
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
   "ProvisioningArtifacts": [
      {
         "CreatedTime": ***number***,
         "Description": "***string***",
         "Guidance": "***string***",
         "Id": "***string***",
         "Name": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Budgets](#API_DescribeProduct_ResponseSyntax "#API_DescribeProduct_ResponseSyntax")**

Information about the associated budgets.

Type: Array of [BudgetDetail](API_BudgetDetail.md "API_BudgetDetail.md") objects

**[LaunchPaths](#API_DescribeProduct_ResponseSyntax "#API_DescribeProduct_ResponseSyntax")**

Information about the associated launch paths.

Type: Array of [LaunchPath](API_LaunchPath.md "API_LaunchPath.md") objects

**[ProductViewSummary](#API_DescribeProduct_ResponseSyntax "#API_DescribeProduct_ResponseSyntax")**

Summary information about the product view.

Type: [ProductViewSummary](API_ProductViewSummary.md "API_ProductViewSummary.md") object

**[ProvisioningArtifacts](#API_DescribeProduct_ResponseSyntax "#API_DescribeProduct_ResponseSyntax")**

Information about the provisioning artifacts for the specified product.

Type: Array of [ProvisioningArtifact](API_ProvisioningArtifact.md "API_ProvisioningArtifact.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DescribeProduct.md "../../../goto/cli2/servicecatalog-2015-12-10/DescribeProduct.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeProduct.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeProduct.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProduct.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProduct.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProduct.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProduct.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProduct.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProduct.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProduct.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProduct.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProduct.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProduct.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProduct.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProduct.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DescribeProduct.md "../../../goto/boto3/servicecatalog-2015-12-10/DescribeProduct.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProduct.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProduct.md")
