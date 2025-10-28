# AttributeGroup

Represents a AWS Service Catalog AppRegistry attribute group that is rich metadata which describes an application and its components.

## Contents

**arn**

The Amazon resource name (ARN) that specifies the attribute group across services.

Type: String

Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+`

Required: No

**creationTime**

The ISO-8601 formatted timestamp of the moment the attribute group was created.

Type: Timestamp

Required: No

**description**

The description of the attribute group that the user provides.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**id**

The globally unique attribute group identifier of the attribute group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[-.\w]+`

Required: No

**lastUpdateTime**

The ISO-8601 formatted timestamp of the moment the attribute group was last updated. This time is the same as the creationTime for a newly created attribute group.

Type: Timestamp

Required: No

**name**

The name of the attribute group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[-.\w]+`

Required: No

**tags**

Key-value pairs you can use to associate with the attribute group.

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`

Value Length Constraints: Maximum length of 256.

Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AttributeGroup.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AttributeGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AttributeGroup.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AttributeGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AttributeGroup.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AttributeGroup.md")
