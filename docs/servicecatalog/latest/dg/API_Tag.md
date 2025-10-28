# Tag

Information about a tag. A tag is a key-value pair. Tags are propagated
to the resources created when provisioning a product.

## Contents

**Key**

The tag key.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: Yes

**Value**

The value for this key.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/Tag.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/Tag.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/Tag.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/Tag.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/Tag.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/Tag.md")
