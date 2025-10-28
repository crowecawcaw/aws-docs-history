# JobSample

A sample configuration for profile jobs only, which determines the number of rows on which the
profile job is run. If a `JobSample` value isn't provided, the
default is used. The default value is CUSTOM_ROWS for the mode parameter and
20,000 for the size parameter.

## Contents

###### Note

In the following list, the required parameters are described first.

**Mode**

A value that determines whether the profile job is run on the entire dataset or a
specified number of rows. This value must be one of the following:

- FULL_DATASET - The profile job is run on the entire dataset.
- CUSTOM_ROWS - The profile job is run on the number of rows specified in the
  `Size` parameter.

Type: String

Valid Values: `FULL_DATASET | CUSTOM_ROWS`

Required: No

**Size**

The `Size` parameter is only required when the mode is CUSTOM_ROWS. The
profile job is run on the specified number of rows. The maximum value for size is
Long.MAX_VALUE.

Long.MAX_VALUE = 9223372036854775807

Type: Long

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/JobSample.md "../../../goto/SdkForCpp/databrew-2017-07-25/JobSample.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/JobSample.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/JobSample.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/JobSample.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/JobSample.md")
