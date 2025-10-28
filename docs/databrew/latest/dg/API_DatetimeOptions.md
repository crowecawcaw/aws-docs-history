# DatetimeOptions

Represents additional options for correct interpretation of datetime parameters used in
the Amazon S3 path of a dataset.

## Contents

###### Note

In the following list, the required parameters are described first.

**Format**

Required option, that defines the datetime format used for a date parameter in the
Amazon S3 path. Should use only supported datetime specifiers and separation characters, all
literal a-z or A-Z characters should be escaped with single quotes. E.g. "MM.dd.yyyy-'at'-HH:mm".

Type: String

Length Constraints: Minimum length of 2. Maximum length of 100.

Required: Yes

**LocaleCode**

Optional value for a non-US locale code, needed for correct interpretation of some date formats.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 100.

Pattern: `^[A-Za-z0-9_\.#@\-]+$`

Required: No

**TimezoneOffset**

Optional value for a timezone offset of the datetime parameter value in the Amazon S3
path. Shouldn't be used if Format for this parameter includes timezone fields.
If no offset specified, UTC is assumed.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 6.

Pattern: `^(Z|[-+](\d|\d{2}|\d{2}:?\d{2}))$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/DatetimeOptions.md "../../../goto/SdkForCpp/databrew-2017-07-25/DatetimeOptions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/DatetimeOptions.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/DatetimeOptions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/DatetimeOptions.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/DatetimeOptions.md")
