# OrganizationNode

Information about the organization node.

## Contents

**Type**

The organization node type.

Type: String

Valid Values: `ORGANIZATION | ORGANIZATIONAL_UNIT | ACCOUNT`

Required: No

**Value**

The identifier of the organization node.

Type: String

Pattern: `(^[0-9]{12}$)|(^arn:aws:organizations::\d{12}:organization\/o-[a-z0-9]{10,32})|(^o-[a-z0-9]{10,32}$)|(^arn:aws:organizations::\d{12}:ou\/o-[a-z0-9]{10,32}\/ou-[0-9a-z]{4,32}-[0-9a-z]{8,32}$)|(^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/OrganizationNode.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/OrganizationNode.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/OrganizationNode.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/OrganizationNode.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/OrganizationNode.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/OrganizationNode.md")
