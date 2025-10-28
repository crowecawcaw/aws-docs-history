# Setting up on the input side

To set up an audio-only output in a MediaLive channel, you must verify that the source
inputs meet the requirements, then you must set up the audio selectors in the usual
way.

## Requirements for the channel and audio

sources

The channel can have a single input or multiples inputs. All the output groups
(both those that are audio-only and those that are video-and-audio) always ingest
the same inputs.

Each source must be one of these categories of source.

- A source that contains _only audio_.
  In this case, the source must be one of the following:
  - A transport stream in a MediaConnect input
  - A transport stream in an RTP input

- Input that contains _both audio and
  video_ (and optionally captions). In this case, the input
  can be any input type that MediaLive supports.

## Setting up the inputs in the

channel

1. Create the inputs in the usual way. Then in the channel, set up the input
   attachments.
2. In each input attachment, create as many audio selectors as you require.
   For example, create a selector for each language to extract. Or create a
   selector for each audio quality or codec that is available.

Keep in mind that in a channel with both audio-only and audio-and-video
output groups, you don't have to create special audio selectors for the sole
use of the audio-only output. The same audio selector can be used by both
audio-only and audio-and-video output groups.
