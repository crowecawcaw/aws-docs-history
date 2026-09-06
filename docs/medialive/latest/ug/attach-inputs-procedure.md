

# The procedure to attach inputs
<a name="attach-inputs-procedure"></a>

**To attach one MediaLive input**

1. On the **Create channel** page, for **Input attachments**, choose **Add**. The **Attach input** section appears.

1. In **Input**, choose an existing input. As soon as you choose the input, information about the input appears. To review this information, see the following sections:
   + [Channel input—CDI VPC push input](input-cdi.md)

     [Channel input—Elemental Link push input](input-elink.md)
   + [Channel input—HLS pull input](input-hls-pull.md)
   + [Channel input—MediaConnect push input](input-mediaconnect-push.md)
   + [Channel input—MediaConnect Router input](input-mediaconnect-router.md)
   + [Channel input—MP4 pull input](input-mp4-pull.md)
   + [Channel input—RTMP push input](input-rtmp-push.md)
   +  [Channel input—RTMP pull input](input-rtmp-pull.md) 
   + [Channel input—RTP push input](input-rtp-push.md)
   + [Channel input—SMPTE 2110 input](input-s2110-pull.md) 
   + [Channel input—SRT caller input](input-srt-pull.md) 
   + [Channel input—SRT listener input](input-srt-push.md) 

1. Complete the **Logical interface names** fields. These fields appear only if you set up the channel to [run in a MediaLive Anywhere cluster](creating-a-channel-step1.md) and the input is a SMPTE 2110 input. 
   + You must specify the logical interface for the incoming content for the input.
   + If the channel implements SMPTE 2022-7 seamless protection switching, you must also specify the logical interface for that content. Slide the selector beside **Use 2022-7 **to enable the feature. Then select the logical interface to use.

   If you were involved in [designing the MediaLive Anywhere clusters](emla-deploy-design-cluster.md) in your organization, you should know which logical interface or interfaces to select. If you weren't involved in this design, you must obtain this information from the video engineer who was involved. 

1. Enter a name for the attachment. The default name is the name of the input itself.

1. Choose **Confirm**. The **Input attachment** section closes, and the **General input settings** section appears.

1. For information about completing the fields in the **General input settings** section, go to the [next step](creating-a-channel-step2a.md).