# AttributeGroupDetails

The details related to a specific AttributeGroup.

## Contents

**arn**

The Amazon resource name (ARN) that specifies the attribute group.

Type: String

Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+`

Required: No

**createdBy**

The service principal that created the attribute group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^(?!-)([a-z0-9-]+\.)+(aws\.internal|amazonaws\.com(\.cn)?)$`

Required: No

**id**

The unique identifier of the attribute group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[-.\w]+`

Required: No

**name**

###### Important

This field is no longer supported.
We recommend
you don't use the field when using `ListAttributeGroupsForApplication`.

The name of the attribute group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[-.\w]+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AttributeGroupDetails.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AttributeGroupDetails.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AttributeGroupDetails.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AttributeGroupDetails.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AttributeGroupDetails.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AttributeGroupDetails.md")
