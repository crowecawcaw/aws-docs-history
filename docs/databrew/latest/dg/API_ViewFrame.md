# ViewFrame

Represents the data being transformed during an action.

## Contents

###### Note

In the following list, the required parameters are described first.

**StartColumnIndex**

The starting index for the range of columns to return in the view frame.

Type: Integer

Valid Range: Minimum value of 0.

Required: Yes

**Analytics**

Controls if analytics computation is enabled or disabled. Enabled by default.

Type: String

Valid Values: `ENABLE | DISABLE`

Required: No

**ColumnRange**

The number of columns to include in the view frame, beginning with the
`StartColumnIndex` value and ignoring any columns in the
`HiddenColumns` list.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 20.

Required: No

**HiddenColumns**

A list of columns to hide in the view frame.

Type: Array of strings

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: No

**RowRange**

The number of rows to include in the view frame, beginning with the
`StartRowIndex` value.

Type: Integer

Required: No

**StartRowIndex**

The starting index for the range of rows to return in the view frame.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/ViewFrame.md "../../../goto/SdkForCpp/databrew-2017-07-25/ViewFrame.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/ViewFrame.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/ViewFrame.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/ViewFrame.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/ViewFrame.md")
