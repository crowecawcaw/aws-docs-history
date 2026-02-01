# TerminateProvisionedProduct

Terminates the specified provisioned product.

This operation does not delete any records associated with the provisioned product.

You can check the status of this request using [DescribeRecord](API_DescribeRecord.md "API_DescribeRecord.md").

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "IgnoreErrors": `boolean`,
   "ProvisionedProductId": "`string`",
   "ProvisionedProductName": "`string`",
   "RetainPhysicalResources": `boolean`,
   "TerminateToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_TerminateProvisionedProduct_RequestSyntax "#API_TerminateProvisionedProduct_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[IgnoreErrors](#API_TerminateProvisionedProduct_RequestSyntax "#API_TerminateProvisionedProduct_RequestSyntax")**

If set to true, AWS Service Catalog stops managing the specified provisioned product even
if it cannot delete the underlying resources.

Type: Boolean

Required: No

**[ProvisionedProductId](#API_TerminateProvisionedProduct_RequestSyntax "#API_TerminateProvisionedProduct_RequestSyntax")**

The identifier of the provisioned product. You cannot specify both
`ProvisionedProductName` and `ProvisionedProductId`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[ProvisionedProductName](#API_TerminateProvisionedProduct_RequestSyntax "#API_TerminateProvisionedProduct_RequestSyntax")**

The name of the provisioned product. You cannot specify both
`ProvisionedProductName` and `ProvisionedProductId`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1224.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]{0,127}|arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

Required: No

**[RetainPhysicalResources](#API_TerminateProvisionedProduct_RequestSyntax "#API_TerminateProvisionedProduct_RequestSyntax")**

When this boolean parameter is set to true, the `TerminateProvisionedProduct` API deletes
the AWS Service Catalog provisioned product. However, it does not remove the AWS CloudFormation
stack, stack set, or the underlying resources of the deleted provisioned product. The
default value is false.

Type: Boolean

Required: No

**[TerminateToken](#API_TerminateProvisionedProduct_RequestSyntax "#API_TerminateProvisionedProduct_RequestSyntax")**

An idempotency token that uniquely identifies the termination request. This token is
only valid during the termination process. After the provisioned product is terminated,
subsequent requests to terminate the same provisioned product always return
**ResourceNotFound**.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: Yes

## Response Syntax

```
{
   "RecordDetail": {
      "CreatedTime": ***number***,
      "LaunchRoleArn": "***string***",
      "PathId": "***string***",
      "ProductId": "***string***",
      "ProvisionedProductId": "***string***",
      "ProvisionedProductName": "***string***",
      "ProvisionedProductType": "***string***",
      "ProvisioningArtifactId": "***string***",
      "RecordErrors": [
         {
            "Code": "***string***",
            "Description": "***string***"
         }
      ],
      "RecordId": "***string***",
      "RecordTags": [
         {
            "Key": "***string***",
            "Value": "***string***"
         }
      ],
      "RecordType": "***string***",
      "Status": "***string***",
      "UpdatedTime": ***number***
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[RecordDetail](#API_TerminateProvisionedProduct_ResponseSyntax "#API_TerminateProvisionedProduct_ResponseSyntax")**

Information about the result of this request.

Type: [RecordDetail](API_RecordDetail.md "API_RecordDetail.md") object

## Errors

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/TerminateProvisionedProduct.md "../../../goto/cli2/servicecatalog-2015-12-10/TerminateProvisionedProduct.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/TerminateProvisionedProduct.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/TerminateProvisionedProduct.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/TerminateProvisionedProduct.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/TerminateProvisionedProduct.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/TerminateProvisionedProduct.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/TerminateProvisionedProduct.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/TerminateProvisionedProduct.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/TerminateProvisionedProduct.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/TerminateProvisionedProduct.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/TerminateProvisionedProduct.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/TerminateProvisionedProduct.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/TerminateProvisionedProduct.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/TerminateProvisionedProduct.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/TerminateProvisionedProduct.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/TerminateProvisionedProduct.md "../../../goto/boto3/servicecatalog-2015-12-10/TerminateProvisionedProduct.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/TerminateProvisionedProduct.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/TerminateProvisionedProduct.md")
