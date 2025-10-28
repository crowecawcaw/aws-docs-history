# Transcribing a medical conversation in

a real-time stream

You can transcribe an audio stream of a medical conversation using either the HTTP/2
or [WebSocket](https://tools.ietf.org/html/rfc6455 "https://tools.ietf.org/html/rfc6455") protocols. For
information on how to start a stream using the WebSocket protocol, see [Setting up a WebSocket stream](streaming-setting-up.md#streaming-websocket "streaming-setting-up.md#streaming-websocket"). To start an HTTP/2 stream,
use the [`StartMedicalStreamTranscription`](../APIReference/API_streaming_StartMedicalStreamTranscription.md "../APIReference/API_streaming_StartMedicalStreamTranscription.md") API.

You can transcribe streaming audio in the following medical specialties:

- Cardiology
- Neurology
- Oncology
- Primary Care
- Urology
  Each medical specialty includes many types of procedures and appointments. Clinicians
  therefore dictate many different types of notes. Use the following examples as guidance
  to help you specify the value of the `specialty` URI parameter of the
  WebSocket request, or the `Specialty` parameter of the
  [`StartMedicalStreamTranscription`](../APIReference/API_streaming_StartMedicalStreamTranscription.md "../APIReference/API_streaming_StartMedicalStreamTranscription.md") API:

- For electrophysiology or echocardiography consultations, choose
  `CARDIOLOGY`.
- For medical oncology, surgical oncology, or radiation oncology consultations,
  choose `ONCOLOGY`.
- For a physician providing a consultation to a patient who had a stroke, either
  a transient ischemic attack or a cerebrovascular attack, choose
  `NEUROLOGY`.
- For a consultation around urinary incontinence, choose
  `UROLOGY`.
- For yearly checkup or urgent care visits, choose
  `PRIMARYCARE`.
- For inpatient hospitalist visits, choose `PRIMARYCARE`.
- For consultations regarding fertility, tubal ligation, IUD insertion, or
  abortion, choose `PRIMARYCARE`.

###### To transcribe a streaming medical conversation (AWS Management Console)

To use the AWS Management Console to transcribe a clinician-patient dialogue in real-time
stream, choose the option to transcribe a medical conversation, start the
stream, and begin speaking into the microphone.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/transcribe/ "https://console.aws.amazon.com/transcribe/").
2. In the navigation pane, under Amazon Transcribe Medical, choose **Real-time
   transcription**.
3. Choose **Conversation**.
4. For **Medical specialty**, choose the clinician's
   specialty.
5. Choose **Start streaming**.
6. Speak into the microphone.
   The following is the syntax for the parameters of an HTTP/2 request.

To transcribe an HTTP/2 stream of a medical conversation, use the
[`StartMedicalStreamTranscription`](../APIReference/API_streaming_StartMedicalStreamTranscription.md "../APIReference/API_streaming_StartMedicalStreamTranscription.md") API
and specify the following:

- `LanguageCode` – The language code. The valid value
  is `en-US`
- `MediaEncoding` – The encoding used for the input
  audio. Valid values are `pcm`, `ogg-opus`, and
  `flac`.
- `Specialty` – The specialty of the medical
  professional.
- `Type` – `CONVERSATION`
  To improve transcription accuracy of specific terms in a real-time stream, use
  a custom vocabulary. To enable a custom vocabulary, set the value of
  `VocabularyName` parameter to the name of the custom vocabulary
  that you want to use. For more information, see [Improving transcription accuracy with medical custom
  vocabularies](vocabulary-med.md "vocabulary-med.md").

To label the speech from different speakers, set the
`ShowSpeakerLabel` parameter to `true`. For more
information, see [Enabling speaker partitioning](conversation-diarization-med.md "conversation-diarization-med.md").

For more information on setting up an HTTP/2 stream to transcribe a medical
conversation, see [Setting up an HTTP/2 stream](streaming-setting-up.md#streaming-http2 "streaming-setting-up.md#streaming-http2").

You can use a WebSocket request to transcribe a medical conversation. When you
make a WebSocket request, you create a presigned URI. This URI contains the
information needed to set up the audio stream between your application and
Amazon Transcribe Medical. For more information on creating WebSocket requests, see [Setting up a WebSocket stream](streaming-setting-up.md#streaming-websocket "streaming-setting-up.md#streaming-websocket").

Use the following template to create your presigned URI.

```
GET wss://transcribestreaming.`us-west-2`.amazonaws.com:8443/medical-stream-transcription-websocket
?language-code=`languageCode`
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=`AKIAIOSFODNN7EXAMPLE`%2F`20220208`%2F`us-west-2`%2F`transcribe`%2Faws4_request
&X-Amz-Date=`20220208T235959Z`
&X-Amz-Expires=`300`
&X-Amz-Security-Token=`security-token`
&X-Amz-Signature=`Signature Version 4 signature`
&X-Amz-SignedHeaders=host
&media-encoding=`flac`
&sample-rate=`16000`
&session-id=`sessionId`
&specialty=`medicalSpecialty`
&type=`CONVERSATION`
&vocabulary-name=`vocabularyName`
&show-speaker-label=`boolean`

```

To improve transcription accuracy of specific terms in a real-time stream, use
a custom vocabulary. To enable a custom vocabulary, set the value of
`vocabulary-name` to the name of the custom vocabulary that you
want to use. For more information, see [Improving transcription accuracy with medical custom
vocabularies](vocabulary-med.md "vocabulary-med.md").

To label the speech from different speakers, set the
`show-speaker-label` parameter in to `true`. For more
information, see [Enabling speaker partitioning](conversation-diarization-med.md "conversation-diarization-med.md").

For more information on creating pre-signed URIs, see [Setting up a WebSocket stream](streaming-setting-up.md#streaming-websocket "streaming-setting-up.md#streaming-websocket").
