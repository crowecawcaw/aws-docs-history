# Step 8: Set up the output and

encodes

Now that you have defined one output group in the channel, you can
set up an output ins that output group, and specify how you want to
encode the video output and the audio output.

###### To set up the output

1. In the **Output groups** section, choose
   **Output 1**. MediaLive automatically added this
   output when you created the output group. In addition, MediaLive
   automatically set up the output with one video and one audio, as
   shown in the **Stream settings** section.
2. In **Stream settings**, choose
   **Video**.
3. For **Video description name**, change the
   default name to `H264 video`.
4. For **Codec settings**, choose
   **H264**.

Leave the remaining fields with the default values.
Specifically, keep **Width** and
**Height** empty to use the same width as the
input. 5. In **Stream settings**, choose **Audio
1**. 6. For **Audio description name**, change the
default name to `AAC audio`. 7. For **Audio selector name**, enter
`My audio source`, which is the audio
selector that you created in[Step 6: Set up
input video, audio, captions](getting-started-step4a-input-selectors.md "getting-started-step4a-input-selectors.md"). 8. For **Codec settings**, choose
**AAC**. 9. Leave the remaining fields with the default values.
