# Transcribing with HTTP or WebSockets

Amazon Transcribe supports HTTP for both batch (HTTP/1.1) and streaming (HTTP/2)
transcriptions. WebSockets are supported for streaming transcriptions.

If you're transcribing a media file located in an Amazon S3 bucket, you're
performing a batch transcription. If you're transcribing a real-time stream of audio data,
you're performing a streaming transcription.

Both HTTP and WebSockets require you to authenticate your request using AWS
Signature Version 4 headers. Refer to [Signing AWS API requests](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md")
for more information.

You can make a batch HTTP request using the following headers:

- host
- x-amz-target
- content-type
- x-amz-content-sha256
- x-amz-date
- authorization
  Here's an example of a `StartTranscriptionJob` request:

```
POST /transcribe HTTP/1.1
host: transcribe.`us-west-2`.amazonaws.com
x-amz-target: com.amazonaws.transcribe.Transcribe.`StartTranscriptionJob`
content-type: application/x-amz-json-1.1
x-amz-content-sha256: `string`
x-amz-date: `YYYYMMDD`T`HHMMSS`Z
authorization: AWS4-HMAC-SHA256 Credential=`access-key`/`YYYYMMSS`/`us-west-2`/transcribe/aws4_request, SignedHeaders=content-type;host;x-amz-content-sha256;x-amz-date;x-amz-target;x-amz-security-token, Signature=`string`

{
    "TranscriptionJobName": "`my-first-transcription-job`",
    "LanguageCode": "`en-US`",
    "Media": {
        "MediaFileUri": "s3://`amzn-s3-demo-bucket`/`my-input-files`/`my-media-file`.`flac`"
    },
    "OutputBucketName": "`amzn-s3-demo-bucket`",
    "OutputKey": "`my-output-files`/"
}
```

Additional operations and parameters are listed in the [API Reference](../APIReference/API_Reference.md "../APIReference/API_Reference.md"); parameters common to
all AWS API operations are listed in the [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md")
section. Other signature elements are detailed in [Elements of an AWS Signature
Version 4 request](../../../general/latest/gr/sigv4_elements.md "../../../general/latest/gr/sigv4_elements.md").

Streaming transcriptions using HTTP/2 and WebSockets are more involved than using
SDKs. We recommend reviewing the [Setting up a streaming transcription](streaming-setting-up.md "streaming-setting-up.md") section before setting up your first
stream.

For more information on these methods, refer to [Setting up an HTTP/2 stream](streaming-setting-up.md#streaming-http2 "streaming-setting-up.md#streaming-http2") or [Setting up a WebSocket stream](streaming-setting-up.md#streaming-websocket "streaming-setting-up.md#streaming-websocket").

###### Note

We strongly recommend using an SDK for streaming transcriptions. For a list of supported SDKs,
refer to [Supported programming languages](supported-languages.md#supported-sdks "supported-languages.md#supported-sdks").
