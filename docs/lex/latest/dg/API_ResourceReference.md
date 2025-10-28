End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# ResourceReference

Describes the resource that refers to the resource that you are
attempting to delete. This object is returned as part of the
`ResourceInUseException` exception.

## Contents

**name**

The name of the resource that is using the resource that you are
trying to delete.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[a-zA-Z_]+`

Required: No

**version**

The version of the resource that is using the resource that you are
trying to delete.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/ResourceReference.md "../../../goto/SdkForCpp/lex-models-2017-04-19/ResourceReference.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/ResourceReference.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/ResourceReference.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/ResourceReference.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/ResourceReference.md")
