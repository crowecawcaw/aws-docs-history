# Setting up enhanced VQ mode

Enhanced VQ is an optional mode that affects the video quality of MediaLive outputs. It affects the
video encode where both of the following apply:

- The encode uses H.264 (AVC).
- The encode uses QVBR or CBR [rate control
  mode](video-encode-ratecontrol.md "video-encode-ratecontrol.md").
  Enhanced VQ applies as follows:

- It doesn't apply to Frame capture output groups.
- It does apply to Multiplex output groups. For this type of output group, you _must_ enable the mode.
- It does apply to the other types of output groups. For these types, you can _optionally_ enable the mode.

- It is required if you want to convert an HDR color space to an SDR color space in an
  output that uses H.264. Even if the encode uses VBR, you must enable the mode to obtain this
  color space conversion. For more information, see [Step 1: Configure enhanced VQ
  mode](color-space-simplified-output-handling.md#color-space-simplified-output-config-vq "color-space-simplified-output-handling.md#color-space-simplified-output-config-vq").

###### Note

If the rate control mode is VBR, there is no benefit to setting up enhanced VQ mode. But
the channel would still incur the costs for enhanced VQ.

For more information about the benefits of enhanced VQ mode, see [Benefits of enhanced VQ](#vq_benefits "#vq_benefits").

For information on charges for using this mode, see [the MediaLive price list](https://aws.amazon.com/medialive/pricing/ "https://aws.amazon.com/medialive/pricing/").

###### Note

This section assumes that you are familiar with creating or editing a channel, as
described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

The fields in the console for setting this mode are in the **Codec
settings** section of the video **Stream settings** in each
output. To review the step where you complete these fields, see [Set up the video encode](creating-a-channel-step6.md "creating-a-channel-step6.md").

###### To enable enhanced VQ

You can enable enhanced VQ in any video encode that uses H.264 (AVC) as the codec.

1.  In the **Output groups** section of the **Create
    channel** page of the MediaLive console, in the **Stream settings**
    pane, choose **Video**.
2.  In the **Codec settings** section, expand the **Additional
    encoding settings** section. Complete the fields as follows:

        * **Quality level**: Choose **ENHANCED\_QUALITY**.
        * **Filter settings**: Choose **Temporal filter**.
         Or to omit the filter, choose **Don't include**. For information about
         the benefits of filters, see [Benefits of the temporal filter](#temporal_benefits "#temporal_benefits").


        If you choose **Temporal**, optionally change the default strength,
         and optionally enable sharpening. For details about a field on the MediaLive console, choose the **Info** link next to the field.

    **Benefits of
    enhanced VQ**

When enhanced VQ is enabled, MediaLive can produce slightly better video quality without an
increase in the bitrate (the bitrate fields in the **Rate control** section
under **Codec settings**).

You can therefore use enhanced VQ in one of two ways:

- You can choose to take advantage of the improved video quality. Typically, the main
  improvement is to smooth out complex transitions in high-motion video content.
- You can choose to lower the bitrate (by perhaps 5%) and maintain the original target
  video quality. Doing so lowers the bandwidth requirements for the output.

      + To change the bitrate when the rate control mode is QVBR, change the **Max
       bitrate**.
      + To change the bitrate when the rate control mode is CBR, change the
       **Bitrate**.

  **Benefits of the temporal filter**

The temporal filter is useful for both source content that is noisy (when it has excessive
digital artifacts) and source content that is clean.

When the content is noisy, the filter cleans up the source content before the encoding
phase, with these two effects:

- It improves the output video quality because the content has been cleaned up.
- It decreases the bandwidth because MediaLive doesn't waste bits on encoding noise.
  When the content is reasonably clean, the filter tends to decrease the bitrate, especially
  when the rate control mode is QVBR.
