# ProductViewSummary

Summary information about a product view.

## Contents

**Distributor**

The distributor of the product. Contact the product administrator for the
significance of this value.

Type: String

Required: No

**HasDefaultPath**

Indicates whether the product has a default path.
If the product does not have a default path, call [ListLaunchPaths](API_ListLaunchPaths.md "API_ListLaunchPaths.md")
to disambiguate between paths. Otherwise, [ListLaunchPaths](API_ListLaunchPaths.md "API_ListLaunchPaths.md") is not
required, and the output of [ProductViewSummary](API_ProductViewSummary.md "API_ProductViewSummary.md") can be used directly with
[DescribeProvisioningParameters](API_DescribeProvisioningParameters.md "API_DescribeProvisioningParameters.md").

Type: Boolean

Required: No

**Id**

The product view identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**Name**

The name of the product.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**Owner**

The owner of the product. Contact the product administrator for the significance of
this value.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**ProductId**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**ShortDescription**

Short description of the product.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**SupportDescription**

The description of the support for this Product.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**SupportEmail**

The email contact information to obtain support for this Product.

Type: String

Length Constraints: Maximum length of 254.

Required: No

**SupportUrl**

The URL information to obtain support for this Product.

Type: String

Length Constraints: Maximum length of 2083.

Required: No

**Type**

The product type. Contact the product administrator for the significance of this
value. If this value is `MARKETPLACE`, the product was created by AWS Marketplace.

Type: String

Length Constraints: Maximum length of 8191.

Valid Values: `CLOUD_FORMATION_TEMPLATE | MARKETPLACE | TERRAFORM_OPEN_SOURCE | EXTERNAL | TERRAFORM_CLOUD`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProductViewSummary.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProductViewSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProductViewSummary.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProductViewSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProductViewSummary.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProductViewSummary.md")
