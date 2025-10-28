# Handling encode sharing

Read this section if you plan to use the per-output option to insert overlays in MediaLive
outputs, and you have already set up output groups to use video encode sharing. Video encode
sharing involves creating one video encode, and then sharing it among two or more outputs in
the same channel. For example, you might use the same video encode in the outputs in an ABR
stack in an HLS output group and in an ABR stack in a Microsoft Smooth output group.

Video encode sharing isn't compatible with per-output image insertion. To undo sharing,
follow this procedure:

1. Identify the encodes that you have set up for sharing:
   - In the **Create channel** or **Edit channel**
     page for the channel, find one of the output groups where you plan to insert
     per-output images. Select the first video output, then in **Stream
     settings**, select the video encode. If this video encode is shared, a note
     appears listing the other outputs.

   - Repeat for every output group in the channel. Make a list of the encodes and how
     they are shared.

2. If you plan different images for these outputs, you must stop sharing them:
   - Stop sharing the video encode in one of the outputs, for example in output group
     A. For instructions, see [To stop sharing an encode](create-video-share.md#create-video-stop-sharing "create-video-share.md#create-video-stop-sharing"). The video encode
     is now used only in output group B.

   - In output group B, clone the video encode that was previously shared. Keep in mind
     that cloning isn't the same as sharing. For more information, see [Creating a video encode by cloning](create-video-clone.md "create-video-clone.md").
