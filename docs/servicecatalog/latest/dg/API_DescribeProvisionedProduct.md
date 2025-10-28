# DescribeProvisionedProduct

Gets information about the specified provisioned product.

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

**[AcceptLanguage](#API_DescribeProvisionedProduct_RequestSyntax "#API_DescribeProvisionedProduct_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Id](#API_DescribeProvisionedProduct_RequestSyntax "#API_DescribeProvisionedProduct_RequestSyntax")**

The provisioned product identifier. You must provide the name or ID, but not both.

If you do not provide a name or ID, or you provide both name and ID, an `InvalidParametersException` will occur.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[Name](#API_DescribeProvisionedProduct_RequestSyntax "#API_DescribeProvisionedProduct_RequestSyntax")**

The name of the provisioned product. You must provide the name or ID, but not both.

If you do not provide a name or ID, or you provide both name and ID, an `InvalidParametersException` will occur.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`

Required: No

## Response Syntax

```
{
   "CloudWatchDashboards": [
      {
         "Name": "***string***"
      }
   ],
   "ProvisionedProductDetail": {
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
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CloudWatchDashboards](#API_DescribeProvisionedProduct_ResponseSyntax "#API_DescribeProvisionedProduct_ResponseSyntax")**

Any CloudWatch dashboards that were created when provisioning the product.

Type: Array of [CloudWatchDashboard](API_CloudWatchDashboard.md "API_CloudWatchDashboard.md") objects

**[ProvisionedProductDetail](#API_DescribeProvisionedProduct_ResponseSyntax "#API_DescribeProvisionedProduct_ResponseSyntax")**

Information about the provisioned product.

Type: [ProvisionedProductDetail](API_ProvisionedProductDetail.md "API_ProvisionedProductDetail.md") object

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DescribeProvisionedProduct.md "../../../goto/cli2/servicecatalog-2015-12-10/DescribeProvisionedProduct.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/DescribeProvisionedProduct.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/DescribeProvisionedProduct.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProvisionedProduct.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProvisionedProduct.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProvisionedProduct.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProvisionedProduct.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProvisionedProduct.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProvisionedProduct.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProvisionedProduct.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProvisionedProduct.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProvisionedProduct.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProvisionedProduct.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProvisionedProduct.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProvisionedProduct.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DescribeProvisionedProduct.md "../../../goto/boto3/servicecatalog-2015-12-10/DescribeProvisionedProduct.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProvisionedProduct.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProvisionedProduct.md")
