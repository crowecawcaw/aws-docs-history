# Setting up the encodes

This section describes the rules for setting up the audio-only encode in a MediaLive
channel.

1. Configure the streams in each output so that they are suitable for generating
   audio-only outputs.

**All outputs _except
UDP_**

In the **Streams settings** section for each output, set up
so that each output has one and only one audio encode:

    * Remove the video encode that MediaLive automatically adds.
    * Make sure that you don't add any captions encodes.

**UDP outputs**

In the **Streams settings** section for the single output,
set up so that each output contains only audio encodes:

    * Add as many audio encodes as you require.
    * Remove the video encode that MediaLive automatically adds.
    * Make sure that you don't add any captions encodes.

2. In each **Streams settings** section, in the
   **Audio** section, set up each encode as follows.
   - In **Audio selector name**, choose one of the audio
     sources that you set up when you configured the input attachment.
   - In **Codec settings**, choose any output audio codec
     that the output type supports.
