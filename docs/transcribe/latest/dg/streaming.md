

# Transcribing streaming audio
<a name="streaming"></a>

Using Amazon Transcribe streaming, you can produce real-time transcriptions for your media content. Unlike batch transcriptions, which involve uploading media files, streaming media is delivered to Amazon Transcribe in real time. Amazon Transcribe then returns a transcript, also in real time.

Streaming can include pre-recorded media (movies, music, and podcasts) and real-time media (live news broadcasts). Common streaming use cases for Amazon Transcribe include live closed captioning for sporting events and real-time monitoring of call center audio.

Streaming content is delivered as a series of sequential data packets, or 'chunks,' that Amazon Transcribe transcribes instantaneously. The advantages of using streaming over batch include real-time speech-to-text capabilities in your applications and faster transcription times. However, this increased speed may have accuracy limitations in some cases.

Amazon Transcribe offers the following options for streaming:
+ [SDKs](getting-started-sdk.md) (preferred)
+ [HTTP/2](streaming-setting-up.md#streaming-http2)
+ [WebSockets](streaming-setting-up.md#streaming-websocket)
+ [AWS Management Console](https://console.aws.amazon.com/transcribe/)

To transcribe streaming audio in the AWS Management Console, speak into your computer microphone.

**Tip**  
For SDK code examples, refer to the [AWS Samples repository](https://github.com/orgs/aws-samples/repositories?language=&q=transcribe&sort=&type=all) on GitHub.

Audio formats supported for streaming transcriptions are:
+ FLAC
+ OPUS-encoded audio in an Ogg container
+ PCM (only signed 16-bit little-endian audio formats, which does **not** include WAV)

Lossless formats (FLAC or PCM) are recommended.

**Note**  
Streaming transcriptions are not supported with all languages. Refer to the 'Data input' column in the [supported languages table](supported-languages.md) for details.

To view the Amazon Transcribe Region availability for streaming transcriptions, see: [Amazon Transcribe Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#transcribe_region).

## Best practices
<a name="best-practices"></a>

The following recommendations improve streaming transcription efficiency:
+ If possible, use PCM-encoded audio.
+ Ensure that your stream is as close to real-time as possible.
+ Latency depends on the size of your audio chunks. If you're able to specify chunk size with your audio type (such as with PCM), set each chunk to between 50 ms and 200 ms. You can calculate the audio chunk size by the following formula: 

  ```
  chunk_size_in_bytes = chunk_duration_in_millisecond / 1000 * audio_sample_rate * 2
  ```
+ Use a uniform chunk size.
+ Make sure you correctly specify the number of audio channels.
+ With single-channel PCM audio, each sample consists of two bytes, so each chunk should consist of an even number of bytes.
+ With dual-channel PCM audio, each sample consists of four bytes, so each chunk should be a multiple of 4 bytes.
+ When your audio stream contains no speech, encode and send the same amount of silence. For example, silence for PCM is a stream of zero bytes.
+ Make sure you specify the correct sampling rate for your audio. If possible, record at a sampling rate of 16,000 Hz; this provides the best compromise between quality and data volume sent over the network. Note that most high-end microphones record at 44,100 Hz or 48,000 Hz.

## Handling LimitExceededException errors
<a name="streaming-limit-exceeded"></a>

As with any distributed system, Amazon Transcribe has protection mechanisms that detect resource over-consumption and react accordingly. `LimitExceededException` errors can occur when one of these mechanisms is triggered. There are three distinct causes for this error:

**Concurrent stream service quota exceeded**  
This is the most common cause. It occurs when you exceed your concurrent stream service quota. To resolve this error, retry with exponential backoff. If you consistently hit this limit, request a service quota increase through the [Service Quotas console](https://console.aws.amazon.com/servicequotas/). You can also contact the [AWS Support Center](https://console.aws.amazon.com/support/home) for assistance. For more information about retry strategies, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools Reference Guide*.

**Maximum session duration exceeded**  
This error occurs when a stream exceeds the maximum allowed session duration. This is a hard limit that cannot be increased. To continue transcribing, start a new streaming session.

**Number of concurrent streams increased too quickly**  
This is a rare cause. It can occur if you increase your number of concurrent streams too quickly, for example during load tests. This is a system-level protection mechanism with no adjustable quota. To resolve this error, retry with exponential backoff and gradually increase your number of concurrent streams. For more information about retry strategies, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools Reference Guide*. You can also visit [AWS re:Post](https://repost.aws/) or contact [AWS Premium Support](https://aws.amazon.com/premiumsupport/).