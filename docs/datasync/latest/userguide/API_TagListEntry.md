# TagListEntry

A key-value pair representing a single tag that's been applied to an AWS
resource.

## Contents

**Key**

The key for an AWS resource tag.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^[a-zA-Z0-9\s+=._:/-]+$`

Required: Yes

**Value**

The value for an AWS resource tag.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 256.

Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/TagListEntry.md "../../../goto/SdkForCpp/datasync-2018-11-09/TagListEntry.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/TagListEntry.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/TagListEntry.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/TagListEntry.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/TagListEntry.md")
