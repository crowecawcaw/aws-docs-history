# ExcelOptions

Represents a set of options that define how DataBrew will interpret a Microsoft Excel file when
creating a dataset from that file.

## Contents

###### Note

In the following list, the required parameters are described first.

**HeaderRow**

A variable that specifies whether the first row in the file is parsed as the
header. If this value is false, column names are auto-generated.

Type: Boolean

Required: No

**SheetIndexes**

One or more sheet numbers in the Excel file that will be included in the
dataset.

Type: Array of integers

Array Members: Fixed number of 1 item.

Valid Range: Minimum value of 0. Maximum value of 200.

Required: No

**SheetNames**

One or more named sheets in the Excel file that will be included in the dataset.

Type: Array of strings

Array Members: Fixed number of 1 item.

Length Constraints: Minimum length of 1. Maximum length of 31.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/ExcelOptions.md "../../../goto/SdkForCpp/databrew-2017-07-25/ExcelOptions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/ExcelOptions.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/ExcelOptions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/ExcelOptions.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/ExcelOptions.md")
