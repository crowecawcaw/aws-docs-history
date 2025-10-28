# PortfolioShareDetail

Information about the portfolio share.

## Contents

**Accepted**

Indicates whether the shared portfolio is imported by the recipient account. If the recipient is in an organization node, the share is automatically imported, and the field is always set to true.

Type: Boolean

Required: No

**PrincipalARN**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1000.

Required: No

**PrincipalId**

The identifier of the recipient entity that received the portfolio share.
The recipient entity can be one of the following:

1. An external account.

2. An organziation member account.

3. An organzational unit (OU).

4. The organization itself. (This shares with every account in the organization).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**SharePrincipals**

Indicates if `Principal` sharing is enabled or disabled for the portfolio share.

Type: Boolean

Required: No

**ShareTagOptions**

Indicates whether TagOptions sharing is enabled or disabled for the portfolio share.

Type: Boolean

Required: No

**Status**

Type: String

Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | ERROR`

Required: No

**Type**

The type of the portfolio share.

Type: String

Valid Values: `ACCOUNT | ORGANIZATION | ORGANIZATIONAL_UNIT | ORGANIZATION_MEMBER_ACCOUNT`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/PortfolioShareDetail.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/PortfolioShareDetail.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/PortfolioShareDetail.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/PortfolioShareDetail.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/PortfolioShareDetail.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/PortfolioShareDetail.md")
