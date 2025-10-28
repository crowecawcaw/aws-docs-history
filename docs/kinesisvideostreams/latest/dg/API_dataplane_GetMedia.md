# GetMedia

Use this API to retrieve media content from a Kinesis video stream. In the request, you
identify the stream name or stream Amazon Resource Name (ARN), and the starting chunk. Kinesis
Video Streams then returns a stream of chunks in order by fragment number.

###### Note

You must first call the `GetDataEndpoint` API to get an endpoint. Then send
the `GetMedia` requests to this endpoint using the [--endpoint-url parameter](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

When you put media data (fragments) on a stream, Kinesis Video Streams stores each incoming fragment and
related metadata in what is called a "chunk." For more information, see [PutMedia](API_dataplane_PutMedia.md "API_dataplane_PutMedia.md"). The `GetMedia` API returns a stream of these chunks starting
from the chunk that you specify in the request.

The `GetMedia` API is designed to operate as a streaming API over a
long-running connection. It is not intended for use in a traditional RESTful manner, where a
new HTTP connection is established and closed for each fragment. When you invoke the
`GetMedia` API, Kinesis Video Streams delivers fragments continuously through a persistent
long-running connection using HTTP chunked transfer encoding.

The following limits apply when using the `GetMedia` API:

- A client can call `GetMedia` up to five times per second per stream.
- Kinesis Video Streams sends media data at a rate of up to 25 megabytes per second (or 200 megabits
  per second) during a `GetMedia` session.

###### Note

Use `GetMedia` as a streaming long-running connection to retrieve multiple fragments in
a single persistent connection. Don't use the `GetMedia` API in a traditional RESTful manner
where you establish and close a new HTTP connection for each fragment. If you attempt more
than three concurrent `GetMedia` connections, Kinesis Video Streams throttles the latest
connections with a `ConnectionLimitExceededException` error.

###### Note

The `GetMedia` HTTP response status code will be returned immediately, but
the reading of the HTTP response payload will timeout after 3 seconds if there are no
ingested fragments available for playback.

###### Note

If an error is thrown after invoking a Kinesis Video Streams media API, in addition to the HTTP status
code and the response body, it includes the following pieces of information:

- `x-amz-ErrorType` HTTP header – contains a more specific error type in
  addition to what the HTTP status code provides.
- `x-amz-RequestId` HTTP header – if you want to report an issue to AWS, the support team can better diagnose the problem if given the Request
  Id.
  Both the HTTP status code and the ErrorType header can be utilized to make programmatic
  decisions about whether errors are retry-able and under what conditions, as well as provide
  information on what actions the client programmer might need to take in order to
  successfully try again.

For more information, see the **Errors** section at the
bottom of this topic, as well as [Common Errors](CommonErrors.md "CommonErrors.md").

## Request Syntax

```
POST /getMedia HTTP/1.1
Content-type: application/json

{
   "StartSelector": {
      "AfterFragmentNumber": "`string`",
      "ContinuationToken": "`string`",
      "StartSelectorType": "`string`",
      "StartTimestamp": `number`
   },
   "StreamARN": "`string`",
   "StreamName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[StartSelector](#API_dataplane_GetMedia_RequestSyntax "#API_dataplane_GetMedia_RequestSyntax")**

Identifies the starting chunk to get from the specified stream.

Type: [StartSelector](API_dataplane_StartSelector.md "API_dataplane_StartSelector.md") object

Required: Yes

**[StreamARN](#API_dataplane_GetMedia_RequestSyntax "#API_dataplane_GetMedia_RequestSyntax")**

The ARN of the stream from where you want to get the media content. If you don't specify
the `streamARN`, you must specify the `streamName`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_dataplane_GetMedia_RequestSyntax "#API_dataplane_GetMedia_RequestSyntax")**

The Kinesis video stream name from where you want to get the media content. If you don't
specify the `streamName`, you must specify the `streamARN`.

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

**[ContentType](#API_dataplane_GetMedia_ResponseSyntax "#API_dataplane_GetMedia_ResponseSyntax")**

The content type of the requested media.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^[a-zA-Z0-9_\.\-]+$`

The response returns the following as the HTTP body.

**[Payload](#API_dataplane_GetMedia_ResponseSyntax "#API_dataplane_GetMedia_ResponseSyntax")**

The payload Kinesis Video Streams returns is a sequence of chunks from the specified stream. For more
information about the chunks, see [PutMedia](API_dataplane_PutMedia.md "API_dataplane_PutMedia.md"). The
chunks that Kinesis Video Streams returns in the `GetMedia` call also include the following
additional Matroska (MKV) tags:

- AWS_KINESISVIDEO_CONTINUATION_TOKEN (UTF-8 string) - In the event your
  `GetMedia` call terminates, you can use this continuation token in your next
  request to get the next chunk where the last request terminated.
- AWS_KINESISVIDEO_MILLIS_BEHIND_NOW (UTF-8 string) - Client applications can use this
  tag value to determine how far behind the chunk returned in the response is from the
  latest chunk on the stream.
- AWS_KINESISVIDEO_FRAGMENT_NUMBER - Fragment number returned in the chunk.
- AWS_KINESISVIDEO_SERVER_TIMESTAMP - Server timestamp of the fragment.
- AWS_KINESISVIDEO_PRODUCER_TIMESTAMP - Producer timestamp of the fragment.

The following tags will be present if an error occurs:

- AWS_KINESISVIDEO_ERROR_CODE - String description of an error that caused GetMedia to
  stop.
- AWS_KINESISVIDEO_ERROR_ID: Integer code of the error.

The error codes are as follows:

- 3002 - Error writing to the stream
- 4000 - Requested fragment is not found
- 4500 - Access denied for the stream's KMS key
- 4501 - Stream's KMS key is disabled
- 4502 - Validation error on the stream's KMS key
- 4503 - KMS key specified in the stream is unavailable
- 4504 - Invalid usage of the KMS key specified in the stream
- 4505 - Invalid state of the KMS key specified in the stream
- 4506 - Unable to find the KMS key specified in the stream
- 5000 - Internal error

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client
calls. Try making the call later.

HTTP Status Code: 400

**ConnectionLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client
connections.

HTTP Status Code: 400

**InvalidArgumentException**

The value for this input parameter is invalid.

HTTP Status Code: 400

**InvalidEndpointException**

Caller used wrong endpoint to write data to a stream. On receiving such an exception, the
user must call `GetDataEndpoint` with `APIName` set to
`PUT_MEDIA` and use the endpoint from response to invoke the next
`PutMedia` call.

HTTP Status Code: 400

**NotAuthorizedException**

The caller is not authorized to perform an operation on the given stream, or the token has
expired.

HTTP Status Code: 401

**ResourceNotFoundException**

Status Code: 404, The stream with the given name does not exist.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesis-video-data-2017-09-30/GetMedia.md "../../../goto/cli2/kinesis-video-data-2017-09-30/GetMedia.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesis-video-data-2017-09-30/GetMedia.md "../../../goto/DotNetSDKV3/kinesis-video-data-2017-09-30/GetMedia.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesis-video-data-2017-09-30/GetMedia.md "../../../goto/SdkForCpp/kinesis-video-data-2017-09-30/GetMedia.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesis-video-data-2017-09-30/GetMedia.md "../../../goto/SdkForGoV2/kinesis-video-data-2017-09-30/GetMedia.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesis-video-data-2017-09-30/GetMedia.md "../../../goto/SdkForJavaV2/kinesis-video-data-2017-09-30/GetMedia.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesis-video-data-2017-09-30/GetMedia.md "../../../goto/SdkForJavaScriptV3/kinesis-video-data-2017-09-30/GetMedia.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesis-video-data-2017-09-30/GetMedia.md "../../../goto/SdkForKotlin/kinesis-video-data-2017-09-30/GetMedia.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesis-video-data-2017-09-30/GetMedia.md "../../../goto/SdkForPHPV3/kinesis-video-data-2017-09-30/GetMedia.md")
- [AWS SDK for Python](../../../goto/boto3/kinesis-video-data-2017-09-30/GetMedia.md "../../../goto/boto3/kinesis-video-data-2017-09-30/GetMedia.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesis-video-data-2017-09-30/GetMedia.md "../../../goto/SdkForRubyV3/kinesis-video-data-2017-09-30/GetMedia.md")
