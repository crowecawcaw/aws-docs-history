# ClipFragmentSelector

Describes the timestamp range and timestamp origin of a range of fragments.

Fragments that have duplicate producer timestamps are deduplicated. This means that if
producers are producing a stream of fragments with producer timestamps that are
approximately equal to the true clock time, the clip will contain all of the fragments
within the requested timestamp range. If some fragments are ingested within the same
time range and very different points in time, only the oldest ingested collection of
fragments are returned.

## Contents

**FragmentSelectorType**

The origin of the timestamps to use (Server or Producer).

Type: String

Valid Values: `PRODUCER_TIMESTAMP | SERVER_TIMESTAMP`

Required: Yes

**TimestampRange**

The range of timestamps to return.

Type: [ClipTimestampRange](API_reader_ClipTimestampRange.md "API_reader_ClipTimestampRange.md") object

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/ClipFragmentSelector.md "../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/ClipFragmentSelector.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/ClipFragmentSelector.md "../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/ClipFragmentSelector.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/ClipFragmentSelector.md "../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/ClipFragmentSelector.md")
