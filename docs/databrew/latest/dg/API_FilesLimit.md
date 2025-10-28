# FilesLimit

Represents a limit imposed on number of Amazon S3 files that should be selected for a
dataset from a connected Amazon S3 path.

## Contents

###### Note

In the following list, the required parameters are described first.

**MaxFiles**

The number of Amazon S3 files to select.

Type: Integer

Valid Range: Minimum value of 1.

Required: Yes

**Order**

A criteria to use for Amazon S3 files sorting before their selection. By
default uses DESCENDING order, i.e. most recent files are selected first. Another
possible value is ASCENDING.

Type: String

Valid Values: `DESCENDING | ASCENDING`

Required: No

**OrderedBy**

A criteria to use for Amazon S3 files sorting before their selection. By default uses LAST_MODIFIED_DATE as
a sorting criteria. Currently it's the only allowed value.

Type: String

Valid Values: `LAST_MODIFIED_DATE`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/FilesLimit.md "../../../goto/SdkForCpp/databrew-2017-07-25/FilesLimit.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/FilesLimit.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/FilesLimit.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/FilesLimit.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/FilesLimit.md")
