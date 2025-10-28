# Step 4: Create a Channel with Optional

Recording

An Amazon IVS channel stores configuration information related to your live stream.
You first create a channel and then contribute video to it using the channel’s stream
key to start your live stream.

As part of channel creation, the following items are assigned:

- An _ingest server_ identifies a specific
  Amazon IVS component that receives the stream, along with an ingestion protocol
  (RTMPS or RTMP).
- Amazon IVS assigns a _stream key_ when you
  create a channel and uses it to authorize streaming. **_Treat the stream key like a secret, since it
  allows anyone to stream to the channel_**.
- A _playback URL_ identifies the endpoint to
  start playback for a specific channel. This endpoint can be used globally. It
  automatically selects the best location from the Amazon IVS global content
  delivery network for a viewer to stream the video. (Note that Amazon IVS does
  not support custom domains for playback. _Do not proxy
  the playback URL with your own domain; that does not work and will cause
  issues._)
  You can create a channel — with or without recording — through the Amazon IVS console
  or the AWS CLI. Channel creation and recording are discussed below.
