# ConstraintDetail

Information about a constraint.

## Contents

**ConstraintId**

The identifier of the constraint.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**Description**

The description of the constraint.

Type: String

Length Constraints: Maximum length of 2000.

Required: No

**Owner**

The owner of the constraint.

Type: String

Pattern: `^[0-9]{12}$`

Required: No

**PortfolioId**

The identifier of the portfolio the product resides in. The constraint applies only to the instance of the product that lives within this portfolio.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**ProductId**

The identifier of the product the constraint applies to. Note that a constraint applies to a specific instance of a product within a certain portfolio.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**Type**

The type of constraint.

- `LAUNCH`
- `NOTIFICATION`
- STACKSET
- `TEMPLATE`

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ConstraintDetail.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ConstraintDetail.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ConstraintDetail.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ConstraintDetail.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ConstraintDetail.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ConstraintDetail.md")
