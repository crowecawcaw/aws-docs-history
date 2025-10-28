# Tag

Metadata assigned to a directory consisting of a key-value pair.

## Contents

**Key**

Required name of the tag. The string value can be Unicode characters and cannot be
prefixed with "aws:". The string can contain only the set of Unicode letters, digits,
white-space, '\_', '.', '/', '=', '+', '-', ':', '@'(Java regex:
"^([\\p{L}\\p{Z}\\p{N}\_.:/=+\\-]\*)$").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: Yes

**Value**

The optional value of the tag. The string value can be Unicode characters. The string
can contain only the set of Unicode letters, digits, white-space, '\_', '.', '/', '=', '+', '-', ':', '@'
(Java regex: "^([\\p{L}\\p{Z}\\p{N}\_.:/=+\\-]\*)$").

Type: String

Length Constraints: Minimum length of 0. Maximum length of 256.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/Tag.md "../../../goto/SdkForCpp/ds-2015-04-16/Tag.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/Tag.md "../../../goto/SdkForJavaV2/ds-2015-04-16/Tag.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/Tag.md "../../../goto/SdkForRubyV3/ds-2015-04-16/Tag.md")
