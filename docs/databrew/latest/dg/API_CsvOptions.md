# CsvOptions

Represents a set of options that define how DataBrew will read a
comma-separated value (CSV) file when creating a dataset from that file.

## Contents

###### Note

In the following list, the required parameters are described first.

**Delimiter**

A single character that specifies the delimiter being used in the CSV file.

Type: String

Length Constraints: Fixed length of 1.

Required: No

**HeaderRow**

A variable that specifies whether the first row in the file is parsed as the
header. If this value is false, column names are auto-generated.

Type: Boolean

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/CsvOptions.md "../../../goto/SdkForCpp/databrew-2017-07-25/CsvOptions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/CsvOptions.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/CsvOptions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/CsvOptions.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/CsvOptions.md")
