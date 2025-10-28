# SourceConnection

A top level `ProductViewDetail` response containing details about the product’s connection.
AWS Service Catalog returns this field for the `CreateProduct`, `UpdateProduct`,
`DescribeProductAsAdmin`, and `SearchProductAsAdmin` APIs.
This response contains the same fields as the `ConnectionParameters` request, with the
addition of the `LastSync` response.

## Contents

**ConnectionParameters**

The connection details based on the connection `Type`.

Type: [SourceConnectionParameters](API_SourceConnectionParameters.md "API_SourceConnectionParameters.md") object

Required: Yes

**Type**

The only supported `SourceConnection` type is Codestar.

Type: String

Valid Values: `CODESTAR`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/SourceConnection.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/SourceConnection.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/SourceConnection.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/SourceConnection.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/SourceConnection.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/SourceConnection.md")
