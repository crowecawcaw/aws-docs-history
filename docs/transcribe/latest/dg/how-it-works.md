# How Amazon Transcribe works

Amazon Transcribe uses machine learning models to convert speech to text.

In addition to the transcribed text, transcripts contains data about the transcribed content, including
confidence scores and timestamps for each word or punctuation mark. To see an output example, refer to
the [Data input and output](how-input.md#how-output "how-input.md#how-output") section. For a complete list of features that
you can apply to your transcription, refer to the [feature
summary](feature-matrix.md "feature-matrix.md").

Transcription methods can be separated into two main categories:

- **Batch transcriptions**: Transcribe media files that have been uploaded
  into an Amazon S3 bucket. You can use the
  [AWS CLI](getting-started-cli.md "getting-started-cli.md"),
  [AWS Management Console](getting-started-console.md "getting-started-console.md"), and various
  [AWS SDKs](getting-started-sdk.md "getting-started-sdk.md") for batch transcriptions.
- **Streaming transcriptions**: Transcribe media streams in real time. You can
  use the [AWS Management Console](getting-started-console.md "getting-started-console.md"),
  [HTTP/2](streaming-setting-up.md#streaming-http2 "streaming-setting-up.md#streaming-http2"),
  [WebSockets](streaming-setting-up.md#streaming-websocket "streaming-setting-up.md#streaming-websocket"), and various
  [AWS SDKs](getting-started-sdk.md "getting-started-sdk.md") for streaming
  transcriptions.
  Note that feature and language support differs for batch and streaming transcriptions. For more
  information, refer to [Amazon Transcribe features](feature-matrix.md "feature-matrix.md") and
  [Supported languages](supported-languages.md "supported-languages.md").

###### Topics

- [Data input and output](how-input.md "how-input.md")
- [Transcribing numbers and punctuation](how-numbers.md "how-numbers.md")

###### API operations to get you started

Batch:
[`StartTranscriptionJob`](../APIReference/API_StartTranscriptionJob.md "../APIReference/API_StartTranscriptionJob.md")

Streaming:
[`StartStreamTranscription`](../APIReference/API_StartStreamTranscription.md "../APIReference/API_StartStreamTranscription.md"), StartStreamTranscriptionWebSocket
