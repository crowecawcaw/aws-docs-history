

# Step 5: View Your Live Stream
<a name="getting-started-view-stream"></a>

You can view your live stream with:
+ The native [IVS player SDKs](#view-stream-player-sdks).
+ The [Amazon IVS console](#view-stream-console).

## Viewing with the Amazon IVS Player SDKs
<a name="view-stream-player-sdks"></a>

1. Set up the IVS Player. Start with the [IVS Player SDK overview](player.md), then read the appropriate platform-specific Player guide(s).

1. From the [Amazon IVS console](https://console.aws.amazon.com/ivs), get the **Playback URL** that was generated when you created your channel. (See [Final Channel Creation](create-channel-console.md#getting-started-create-channel-console-record-s3) earlier in this *Getting Started* guide.)

1. Call `player.load()` with the playback URL.

## Viewing with the Amazon IVS Console
<a name="view-stream-console"></a>

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs).

   (You can also access the Amazon IVS console through the [AWS Management Console](https://console.aws.amazon.com).) 

1. On the navigation pane, choose **Live channels**. (If the nav pane is collapsed, first open it by choosing the hamburger icon.)

1. Choose the channel whose stream you want to view, to go to a details page for that channel.

   The live stream is playing in the **Live stream** section of the page.

**Note**: Playback from the console consumes resources, and you will incur live-video output costs. To learn more, see [Live Video Output Costs](https://aws.amazon.com/ivs/pricing/#Live_Video_Output_Costs) on the IVS Pricing page.

**Note**: After you start streaming, there is a short delay (up to 30 seconds, usually less) before your stream can be viewed in the console.