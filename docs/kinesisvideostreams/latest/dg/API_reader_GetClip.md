# GetClip

Downloads an MP4 file (clip) containing the archived, on-demand media from the
specified video stream over the specified time range.

Both the StreamName and the StreamARN parameters are optional, but you must specify
either the StreamName or the StreamARN when invoking this API operation.

###### Note

You must first call the `GetDataEndpoint` API to get an endpoint. Then
send the `GetClip` requests to this endpoint using the [--endpoint-url
parameter](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

An Amazon Kinesis video stream has the following requirements for providing data
through MP4:

- [Video
  playback track requirements](video-playback-requirements.md "video-playback-requirements.md").
- Data retention must be greater than 0.
- The video track of each fragment must contain codec private data in the
  Advanced Video Coding (AVC) for H.264 format and HEVC for H.265 format. For more
  information, see [MPEG-4
  specification ISO/IEC 14496-15](https://www.iso.org/standard/55980.html "https://www.iso.org/standard/55980.html"). For information about adapting
  stream data to a given format, see [NAL
  Adaptation Flags](producer-reference-nal.md "producer-reference-nal.md").
- The audio track (if present) of each fragment must contain codec private data
  in the AAC format ([AAC
  specification ISO/IEC 13818-7](https://www.iso.org/standard/43345.html "https://www.iso.org/standard/43345.html")) or the [MS
  Wave format](https://www.mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html "https://www.mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html").
  You can monitor the amount of outgoing data by monitoring the
  `GetClip.OutgoingBytes` Amazon CloudWatch metric. For information about
  using CloudWatch to monitor Kinesis Video Streams, see [Monitoring Kinesis Video Streams](monitoring.md "monitoring.md"). For pricing information, see [Amazon Kinesis Video
  Streams Pricing](https://aws.amazon.com/kinesis/video-streams/pricing/ "https://aws.amazon.com/kinesis/video-streams/pricing/") and [AWS
  Pricing](https://aws.amazon.com/pricing/ "https://aws.amazon.com/pricing/"). Charges for outgoing AWS data apply.

###### Important

The codec private data (CPD) contained in each fragment contains codec-specific
initialization information, such as frame rate, resolution, and encoding profile,
which are necessary to properly decode the fragment. CPD changes aren't
supported between the target fragments of the resulting clip. The CPD must remain
consistent through the queried media, otherwise an error will be returned.

###### Important

Track changes aren't supported. Tracks must remain consistent throughout the
queried media. An error is returned if the fragments in the stream change from
having only video to having both audio and video, or if an AAC audio track is
changed to an A-Law audio track.

## Request Syntax

```
POST /getClip HTTP/1.1
Content-type: application/json

{
   "ClipFragmentSelector": {
      "FragmentSelectorType": "`string`",
      "TimestampRange": {
         "EndTimestamp": `number`,
         "StartTimestamp": `number`
      }
   },
   "StreamARN": "`string`",
   "StreamName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[ClipFragmentSelector](#API_reader_GetClip_RequestSyntax "#API_reader_GetClip_RequestSyntax")**

The time range of the requested clip and the source of the timestamps.

Type: [ClipFragmentSelector](API_reader_ClipFragmentSelector.md "API_reader_ClipFragmentSelector.md") object

Required: Yes

**[StreamARN](#API_reader_GetClip_RequestSyntax "#API_reader_GetClip_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream for which to retrieve the media clip.

You must specify either the StreamName or the StreamARN.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_reader_GetClip_RequestSyntax "#API_reader_GetClip_RequestSyntax")**

The name of the stream for which to retrieve the media clip.

You must specify either the StreamName or the StreamARN.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-Type: `ContentType`

`Payload`
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

**[ContentType](#API_reader_GetClip_ResponseSyntax "#API_reader_GetClip_ResponseSyntax")**

The content type of the media in the requested clip.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^[a-zA-Z0-9_\.\-]+$`

The response returns the following as the HTTP body.

**[Payload](#API_reader_GetClip_ResponseSyntax "#API_reader_GetClip_ResponseSyntax")**

Traditional MP4 file that contains the media clip from the specified video stream. The
output will contain the first 100 MB or the first 200 fragments from the specified start
timestamp. For more information, see [Kinesis
Video Streams quotas](limits.md "limits.md").

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded a limit. Try making the call later. For information about limits, see [Kinesis Video Streams quotas](limits.md "limits.md").

HTTP Status Code: 400

**InvalidArgumentException**

A specified parameter exceeds its restrictions, is not supported, or can't be
used.

HTTP Status Code: 400

**InvalidCodecPrivateDataException**

The codec private data in at least one of the tracks of the video stream is not valid
for this operation.

HTTP Status Code: 400

**InvalidMediaFrameException**

One or more frames in the requested clip could not be parsed based on the specified
codec.

HTTP Status Code: 400

**MissingCodecPrivateDataException**

No codec private data was found in at least one of tracks of the video stream.

HTTP Status Code: 400

**NoDataRetentionException**

`GetImages` was requested for a stream that does not retain data (that is, has
a `DataRetentionInHours` of 0).

HTTP Status Code: 400

**NotAuthorizedException**

Status Code: 403, The caller is not authorized to perform an operation on the given
stream, or the token has expired.

HTTP Status Code: 401

**ResourceNotFoundException**

`GetImages` will throw this error when Kinesis Video Streams can't find the stream
that you specified.

`GetHLSStreamingSessionURL` and `GetDASHStreamingSessionURL` throw
this error if a session with a `PlaybackMode` of `ON_DEMAND` or
`LIVE_REPLAY` is requested for a stream that has no fragments within the
requested time range, or if a session with a `PlaybackMode` of
`LIVE` is requested for a stream that has no fragments within the last 30
seconds.

HTTP Status Code: 404

**UnsupportedStreamMediaTypeException**

The type of the media (for example, h.264 or h.265 video or AAC or G.711 audio) could
not be determined from the codec IDs of the tracks in the first fragment for a playback
session. The codec ID for track 1 should be `V_MPEG/ISO/AVC` and, optionally,
the codec ID for track 2 should be `A_AAC`.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesis-video-reader-data-2017-09-30/GetClip.md "../../../goto/cli2/kinesis-video-reader-data-2017-09-30/GetClip.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesis-video-reader-data-2017-09-30/GetClip.md "../../../goto/DotNetSDKV3/kinesis-video-reader-data-2017-09-30/GetClip.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/GetClip.md "../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/GetClip.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesis-video-reader-data-2017-09-30/GetClip.md "../../../goto/SdkForGoV2/kinesis-video-reader-data-2017-09-30/GetClip.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/GetClip.md "../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/GetClip.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesis-video-reader-data-2017-09-30/GetClip.md "../../../goto/SdkForJavaScriptV3/kinesis-video-reader-data-2017-09-30/GetClip.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesis-video-reader-data-2017-09-30/GetClip.md "../../../goto/SdkForKotlin/kinesis-video-reader-data-2017-09-30/GetClip.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesis-video-reader-data-2017-09-30/GetClip.md "../../../goto/SdkForPHPV3/kinesis-video-reader-data-2017-09-30/GetClip.md")
- [AWS SDK for Python](../../../goto/boto3/kinesis-video-reader-data-2017-09-30/GetClip.md "../../../goto/boto3/kinesis-video-reader-data-2017-09-30/GetClip.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/GetClip.md "../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/GetClip.md")
