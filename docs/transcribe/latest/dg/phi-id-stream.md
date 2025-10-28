# Identifying PHI in a real-time stream

You can identify Personal Health Information (PHI) in either HTTP/2 or
WebSocket streams. When you activate PHI Identification, Amazon Transcribe Medical labels the PHI that it
identifies in the transcription results. For information about the PHI that Amazon Transcribe Medical can
identify, see [Identifying personal health information (PHI) in a
transcription](phi-id.md "phi-id.md").

To use the AWS Management Console to transcribe the speech picked up by your
microphone and identify any PHI, choose **Dictation** as the
audio input type, start the stream, and begin speaking into the microphone on
your computer.

###### To identify PHI in a dictation using the AWS Management Console

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/transcribe/ "https://console.aws.amazon.com/transcribe/").
2. In the navigation pane, choose **Real-time
   transcription**.
3. For **Audio input type**, choose
   **Dictation**.
4. For
   **Additional settings**, choose **PHI
   identification**.
5. Choose **Start streaming** and speak into the
   microphone.
6. Choose **Stop streaming** to end the
   dictation.
   To start an HTTP/2 stream with PHI Identification activated, use the
   [`StartMedicalStreamTranscription`](../APIReference/API_streaming_StartMedicalStreamTranscription.md "../APIReference/API_streaming_StartMedicalStreamTranscription.md") API
   and specify the following:

- For `LanguageCode`, specify the language code for the
  language spoken in the stream. For US English, specify
  `en-US`.
- For `MediaSampleHertz`, specify the sample rate of the
  audio.
- For `content-identification-type`, specify
  `PHI`.
  To a start a WebSocket stream with PHI Identification activated, use the
  following
  format to create a presigned
  URL.

```
GET wss://transcribestreaming.`us-west-2`.amazonaws.com:8443/medical-stream-transcription-websocket?
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=`AKIAIOSFODNN7EXAMPLE`%2F`20220208`%2F`us-west-2`%2F`transcribe`%2Faws4_request
&X-Amz-Date=`20220208T235959Z`
&X-Amz-Expires=`300`
&X-Amz-Security-Token=`security-token`
&X-Amz-Signature=`Signature Version 4 signature`
&X-Amz-SignedHeaders=host
&language-code=`en-US`
&media-encoding=`flac`
&sample-rate=`16000`
&specialty=`medical-specialty`
&content-identification-type=PHI
```

Parameter definitions can be found in the [API Reference](../APIReference/API_Reference.md "../APIReference/API_Reference.md"); parameters common to
all AWS API operations are listed in the [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md")
section.
