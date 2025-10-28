# Setting

Contains information about the configurable settings for a directory.

## Contents

**Name**

The name of the directory setting. For example:

`TLS_1_0`

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^[a-zA-Z0-9-/. _]*$`

Required: Yes

**Value**

The value of the directory setting for which to retrieve information. For example, for
`TLS_1_0`, the valid values are: `Enable` and
`Disable`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^[a-zA-Z0-9_]*$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/Setting.md "../../../goto/SdkForCpp/ds-2015-04-16/Setting.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/Setting.md "../../../goto/SdkForJavaV2/ds-2015-04-16/Setting.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/Setting.md "../../../goto/SdkForRubyV3/ds-2015-04-16/Setting.md")
