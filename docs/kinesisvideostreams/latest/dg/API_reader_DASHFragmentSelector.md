# DASHFragmentSelector

Contains the range of timestamps for the requested media, and the source of the
timestamps.

## Contents

**FragmentSelectorType**

The source of the timestamps for the requested media.

When `FragmentSelectorType` is set to `PRODUCER_TIMESTAMP` and
[GetDASHStreamingSessionURL:PlaybackMode](API_reader_GetDASHStreamingSessionURL.md#KinesisVideo-reader_GetDASHStreamingSessionURL-request-PlaybackMode "API_reader_GetDASHStreamingSessionURL.md#KinesisVideo-reader_GetDASHStreamingSessionURL-request-PlaybackMode") is
`ON_DEMAND` or `LIVE_REPLAY`, the first fragment ingested with
a producer timestamp within the specified [FragmentSelector:TimestampRange](API_reader_FragmentSelector.md#KinesisVideo-Type-reader_FragmentSelector-TimestampRange "API_reader_FragmentSelector.md#KinesisVideo-Type-reader_FragmentSelector-TimestampRange") is included in the media playlist. In
addition, the fragments with producer timestamps within the `TimestampRange`
ingested immediately following the first fragment (up to the [GetDASHStreamingSessionURL:MaxManifestFragmentResults](API_reader_GetDASHStreamingSessionURL.md#KinesisVideo-reader_GetDASHStreamingSessionURL-request-MaxManifestFragmentResults "API_reader_GetDASHStreamingSessionURL.md#KinesisVideo-reader_GetDASHStreamingSessionURL-request-MaxManifestFragmentResults") value) are
included.

Fragments that have duplicate producer timestamps are deduplicated. This means that if
producers are producing a stream of fragments with producer timestamps that are
approximately equal to the true clock time, the MPEG-DASH manifest will contain all of
the fragments within the requested timestamp range. If some fragments are ingested
within the same time range and very different points in time, only the oldest ingested
collection of fragments are returned.

When `FragmentSelectorType` is set to `PRODUCER_TIMESTAMP` and
[GetDASHStreamingSessionURL:PlaybackMode](API_reader_GetDASHStreamingSessionURL.md#KinesisVideo-reader_GetDASHStreamingSessionURL-request-PlaybackMode "API_reader_GetDASHStreamingSessionURL.md#KinesisVideo-reader_GetDASHStreamingSessionURL-request-PlaybackMode") is `LIVE`,
the producer timestamps are used in the MP4 fragments and for deduplication. But the
most recently ingested fragments based on server timestamps are included in the
MPEG-DASH manifest. This means that even if fragments ingested in the past have producer
timestamps with values now, they are not included in the HLS media playlist.

The default is `SERVER_TIMESTAMP`.

Type: String

Valid Values: `PRODUCER_TIMESTAMP | SERVER_TIMESTAMP`

Required: No

**TimestampRange**

The start and end of the timestamp range for the requested media.

This value should not be present if `PlaybackType` is
`LIVE`.

Type: [DASHTimestampRange](API_reader_DASHTimestampRange.md "API_reader_DASHTimestampRange.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/DASHFragmentSelector.md "../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/DASHFragmentSelector.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/DASHFragmentSelector.md "../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/DASHFragmentSelector.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/DASHFragmentSelector.md "../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/DASHFragmentSelector.md")
