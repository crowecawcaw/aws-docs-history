# LaunchPathSummary

Summary information about a product path for a user.

## Contents

**ConstraintSummaries**

The constraints on the portfolio-product relationship.

Type: Array of [ConstraintSummary](API_ConstraintSummary.md "API_ConstraintSummary.md") objects

Required: No

**Id**

The identifier of the product path.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**Name**

The name of the portfolio that contains the product.

Type: String

Required: No

**Tags**

The tags associated with this product path.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Maximum number of 50 items.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/LaunchPathSummary.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/LaunchPathSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/LaunchPathSummary.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/LaunchPathSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/LaunchPathSummary.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/LaunchPathSummary.md")
