# Fragment

Represents a segment of video or other time-delimited data.

## Contents

**FragmentLengthInMilliseconds**

The playback duration or other time value associated with the fragment.

Type: Long

Required: No

**FragmentNumber**

The unique identifier of the fragment. This value monotonically increases based on the
ingestion order.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^[0-9]+$`

Required: No

**FragmentSizeInBytes**

The total fragment size, including information about the fragment and contained media
data.

Type: Long

Required: No

**ProducerTimestamp**

The timestamp from the producer corresponding to the fragment, in milliseconds.

Type: Timestamp

Required: No

**ServerTimestamp**

The timestamp from the AWS server corresponding to the fragment, in milliseconds.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/Fragment.md "../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/Fragment.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/Fragment.md "../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/Fragment.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/Fragment.md "../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/Fragment.md")
