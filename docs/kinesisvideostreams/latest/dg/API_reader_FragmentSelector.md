# FragmentSelector

Describes the timestamp range and timestamp origin of a range of fragments.

Only fragments with a start timestamp greater than or equal to the given start time
and less than or equal to the end time are returned. For example, if a stream contains
fragments with the following start timestamps:

- 00:00:00
- 00:00:02
- 00:00:04
- 00:00:06
  A fragment selector range with a start time of 00:00:01 and end time of 00:00:04
  would return the fragments with start times of 00:00:02 and 00:00:04.

## Contents

**FragmentSelectorType**

The origin of the timestamps to use (Server or Producer).

Type: String

Valid Values: `PRODUCER_TIMESTAMP | SERVER_TIMESTAMP`

Required: Yes

**TimestampRange**

The range of timestamps to return.

Type: [TimestampRange](API_reader_TimestampRange.md "API_reader_TimestampRange.md") object

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/FragmentSelector.md "../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/FragmentSelector.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/FragmentSelector.md "../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/FragmentSelector.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/FragmentSelector.md "../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/FragmentSelector.md")
