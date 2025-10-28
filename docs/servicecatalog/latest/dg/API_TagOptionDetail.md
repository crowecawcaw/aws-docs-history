# TagOptionDetail

Information about a TagOption.

## Contents

**Active**

The TagOption active state.

Type: Boolean

Required: No

**Id**

The TagOption identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: No

**Key**

The TagOption key.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: No

**Owner**

The AWS account Id of the owner account that created the TagOption.

Type: String

Required: No

**Value**

The TagOption value.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/TagOptionDetail.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/TagOptionDetail.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/TagOptionDetail.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/TagOptionDetail.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/TagOptionDetail.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/TagOptionDetail.md")
