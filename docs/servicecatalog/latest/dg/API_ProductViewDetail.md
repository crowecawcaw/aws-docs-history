# ProductViewDetail

Information about a product view.

## Contents

**CreatedTime**

The UTC time stamp of the creation time.

Type: Timestamp

Required: No

**ProductARN**

The ARN of the product.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 150.

Required: No

**ProductViewSummary**

Summary information about the product view.

Type: [ProductViewSummary](API_ProductViewSummary.md "API_ProductViewSummary.md") object

Required: No

**SourceConnection**

A top level `ProductViewDetail` response containing details about the product’s connection.
AWS Service Catalog returns this field for the `CreateProduct`, `UpdateProduct`,
`DescribeProductAsAdmin`, and `SearchProductAsAdmin` APIs.
This response contains the same fields as the `ConnectionParameters` request, with the
addition of the `LastSync` response.

Type: [SourceConnectionDetail](API_SourceConnectionDetail.md "API_SourceConnectionDetail.md") object

Required: No

**Status**

The status of the product.

- `AVAILABLE` - The product is ready for use.
- `CREATING` - Product creation has started; the product is not ready for use.
- `FAILED` - An action failed.

Type: String

Valid Values: `AVAILABLE | CREATING | FAILED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProductViewDetail.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProductViewDetail.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProductViewDetail.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProductViewDetail.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProductViewDetail.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProductViewDetail.md")
