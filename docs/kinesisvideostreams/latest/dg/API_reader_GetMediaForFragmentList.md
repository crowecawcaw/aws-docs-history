# GetMediaForFragmentList

Gets media for a list of fragments (specified by fragment number) from the archived
data in an Amazon Kinesis video stream.

###### Note

You must first call the `GetDataEndpoint` API to get an endpoint.
Then send the `GetMediaForFragmentList` requests to this endpoint using
the [--endpoint-url
parameter](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

For limits, see [Kinesis Video Streams quotas](limits.md "limits.md").

###### Important

If an error is thrown after invoking a Kinesis Video Streams archived media API,
in addition to the HTTP status code and the response body, it includes the following
pieces of information:

- `x-amz-ErrorType` HTTP header – contains a more specific error
  type in addition to what the HTTP status code provides.
- `x-amz-RequestId` HTTP header – if you want to report an issue to
  AWS, the support team can better diagnose the problem if given the Request
  Id.
  Both the HTTP status code and the ErrorType header can be utilized to make
  programmatic decisions about whether errors are retry-able and under what
  conditions, as well as provide information on what actions the client programmer
  might need to take in order to successfully try again.

For more information, see the **Errors** section at
the bottom of this topic, as well as [Common Errors](CommonErrors.md "CommonErrors.md").

## Request Syntax

```
POST /getMediaForFragmentList HTTP/1.1
Content-type: application/json

{
   "Fragments": [ "`string`" ],
   "StreamARN": "`string`",
   "StreamName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[Fragments](#API_reader_GetMediaForFragmentList_RequestSyntax "#API_reader_GetMediaForFragmentList_RequestSyntax")**

A list of the numbers of fragments for which to retrieve media. You retrieve these
values with [ListFragments](API_reader_ListFragments.md "API_reader_ListFragments.md").

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 1000 items.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^[0-9]+$`

Required: Yes

**[StreamARN](#API_reader_GetMediaForFragmentList_RequestSyntax "#API_reader_GetMediaForFragmentList_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream from which to retrieve fragment media. Specify either this parameter or the `StreamName` parameter.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_reader_GetMediaForFragmentList_RequestSyntax "#API_reader_GetMediaForFragmentList_RequestSyntax")**

The name of the stream from which to retrieve fragment media. Specify either this parameter or the `StreamARN` parameter.

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

**[ContentType](#API_reader_GetMediaForFragmentList_ResponseSyntax "#API_reader_GetMediaForFragmentList_ResponseSyntax")**

The content type of the requested media.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^[a-zA-Z0-9_\.\-]+$`

The response returns the following as the HTTP body.

**[Payload](#API_reader_GetMediaForFragmentList_ResponseSyntax "#API_reader_GetMediaForFragmentList_ResponseSyntax")**

The payload that Kinesis Video Streams returns is a sequence of chunks from the
specified stream. For information about the chunks, see [PutMedia](API_dataplane_PutMedia.md "API_dataplane_PutMedia.md"). The chunks that Kinesis Video Streams returns in the
`GetMediaForFragmentList` call also include the following additional
Matroska (MKV) tags:

- AWS_KINESISVIDEO_FRAGMENT_NUMBER - Fragment number returned in the
  chunk.
- AWS_KINESISVIDEO_SERVER_SIDE_TIMESTAMP - Server-side timestamp of the
  fragment.
- AWS_KINESISVIDEO_PRODUCER_SIDE_TIMESTAMP - Producer-side timestamp of the
  fragment.

The following tags will be included if an exception occurs:

- AWS_KINESISVIDEO_FRAGMENT_NUMBER - The number of the fragment that threw the exception.
- AWS_KINESISVIDEO_EXCEPTION_ERROR_CODE - The integer code of the error.
- AWS_KINESISVIDEO_EXCEPTION_MESSAGE - A text description of the exception.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded a limit. Try making the call later. For information about limits, see [Kinesis Video Streams quotas](limits.md "limits.md").

HTTP Status Code: 400

**InvalidArgumentException**

A specified parameter exceeds its restrictions, is not supported, or can't be
used.

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md "../../../goto/cli2/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md "../../../goto/DotNetSDKV3/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md "../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md "../../../goto/SdkForGoV2/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md "../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md "../../../goto/SdkForJavaScriptV3/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md "../../../goto/SdkForKotlin/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md "../../../goto/SdkForPHPV3/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md")
- [AWS SDK for Python](../../../goto/boto3/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md "../../../goto/boto3/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md "../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/GetMediaForFragmentList.md")
