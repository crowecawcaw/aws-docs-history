# Burning the timecode into output

You can set up any video encode in a MediaLive channel to burn in the output timecode. The
time code will become part of the video.

Note that the timecode burnin feature is independent of the timecode metadata feature.
You don't have to enable timecode metadata in order to burn in the timecode.

###### To burn the timecode into the video output

1. On the **Create Channel** page, in the **Output
   groups** section, choose an output group, then choose an
   output.
2. Display the **Stream settings** section, and then choose the
   **Video** section. In **Codec settings**,
   choose the codec for this video encode. More fields appear.
3. Choose **Timecode**, then in **Timecode burn-in
   settings**, choose **Timecode burnin**. More
   fields appear.
4. Set the style and position of the timecode in the video frame. In the optional
   **Prefix** field, enter any descriptor. For example,
   `UTC-1`.
