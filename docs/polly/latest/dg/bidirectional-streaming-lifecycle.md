# Sending text and receiving audio

A bidirectional streaming session involves opening a connection, sending text
and receiving audio concurrently, then closing the stream when input is complete.
The following sections describe each phase in detail.

## Open the stream

Your application calls the
[StartSpeechSynthesisStream](API_StartSpeechSynthesisStream.md "API_StartSpeechSynthesisStream.md")
operation through the SDK, specifying synthesis parameters
(`Engine`, `VoiceId`, `OutputFormat`, and
optionally `LanguageCode`, `LexiconNames`,
`SampleRate`). The SDK establishes an HTTP/2 connection and the
bidirectional stream is ready to accept input events.

## Send text

The client sends one or more
[TextEvent](API_TextEvent.md "API_TextEvent.md") messages on the
input stream. Each event can be sent as soon as text is available, without waiting
for the full input to be ready. Text events do not need to align with sentence or
punctuation boundaries. Amazon Polly reassembles the text internally and produces
natural-sounding speech regardless of how the input is split across events.

###### Note

When using [SSML](ssml.md "ssml.md"), each SSML
document must be self-contained within a single `TextEvent`. You
cannot split SSML tags across multiple events. However, you can mix plain
text events and SSML events within the same stream.

The stream is subject to the following time limits:

- **Maximum stream duration**: 10 minutes.
  Amazon Polly closes the stream after 10 minutes regardless of activity. If your
  content requires more time, open a new stream for the remaining
  text.
- **Idle timeout between consecutive events**:
  5 seconds. If no input event is sent for 5 seconds, Amazon Polly closes the
  stream. If your text source has pauses longer than 5 seconds, send a
  keep-alive `TextEvent` with an empty or whitespace string to
  prevent the timeout.

### Forcing synthesis of buffered text with flushing

By default, Amazon Polly decides when to synthesize buffered text based on natural
language boundaries. This produces the best audio quality but means audio may
not be returned immediately after you send a
`TextEvent`.

Flushing gives you control over when synthesis happens. When you flush,
Amazon Polly immediately synthesizes all text it has buffered so far, regardless of
whether the text ends at a natural boundary. This is useful when your text
source pauses between logical sections and you want to deliver audio for
what has been sent so far.

To flush, set the
[FlushStreamConfiguration](API_FlushStreamConfiguration.md "API_FlushStreamConfiguration.md").`Force`
parameter to `true` on a
`TextEvent`. You can
also send an empty `TextEvent` with the flush flag set to trigger
synthesis without adding new content.

Flushing is a tradeoff. Setting `Force` to `true`
mid-sentence may affect pronunciation and intonation because the synthesizer
lacks context about what follows. For best results, allow Amazon Polly to buffer to
natural boundaries whenever possible and only force synthesis when latency
requirements demand it.

## Receive audio

As Amazon Polly synthesizes text, it returns
[AudioEvent](API_AudioEvent.md "API_AudioEvent.md") messages on
the output stream. Each event contains a chunk of audio data. Your application must
accumulate these chunks (for example, by writing them sequentially to a file or
audio buffer) to produce the complete audio output. Audio events can arrive while
you are still sending text events.

## Close the stream

When all input text has been sent, the client sends a
[CloseStreamEvent](API_CloseStreamEvent.md "API_CloseStreamEvent.md").
Amazon Polly finishes processing any remaining buffered text, sends final audio events,
and returns a
[StreamClosedEvent](API_StreamClosedEvent.md "API_StreamClosedEvent.md")
that contains the total number of characters synthesized. Always send a
`CloseStreamEvent` rather than relying on flushing to end the stream.
Closing ensures that all buffered text is synthesized and returned.

For full details on request parameters, event types, and errors, see the
[StartSpeechSynthesisStream
API reference](API_StartSpeechSynthesisStream.md "API_StartSpeechSynthesisStream.md").
