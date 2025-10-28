# FilterRule

Specifies which files, folders, and objects to include or exclude when transferring files
from source to destination.

## Contents

**FilterType**

The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN
rule type.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^[A-Z0-9_]+$`

Valid Values: `SIMPLE_PATTERN`

Required: No

**Value**

A single filter string that consists of the patterns to include or exclude. The patterns
are delimited by "|" (that is, a pipe), for example: `/folder1|/folder2`

Type: String

Length Constraints: Maximum length of 102400.

Pattern: `^[^\x00]+$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/FilterRule.md "../../../goto/SdkForCpp/datasync-2018-11-09/FilterRule.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/FilterRule.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/FilterRule.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/FilterRule.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/FilterRule.md")
