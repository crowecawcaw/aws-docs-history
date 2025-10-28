# AllowedStatistics

Configuration of statistics that are allowed to be run on columns that
contain detected entities. When undefined, no statistics will be computed
on columns that contain detected entities.

## Contents

###### Note

In the following list, the required parameters are described first.

**Statistics**

One or more column statistics to allow for columns that contain detected entities.

Type: Array of strings

Array Members: Minimum number of 1 item.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^[A-Z\_]+$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/AllowedStatistics.md "../../../goto/SdkForCpp/databrew-2017-07-25/AllowedStatistics.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/AllowedStatistics.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/AllowedStatistics.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/AllowedStatistics.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/AllowedStatistics.md")
