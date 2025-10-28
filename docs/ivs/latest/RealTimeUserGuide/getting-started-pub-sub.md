# Step 5: Publish and Subscribe to Video

You can publish/subscribe (real-time) to IVS with:

- The native [IVS broadcast SDKs](../LowLatencyUserGuide/getting-started-set-up-streaming.md#broadcast-sdk "../LowLatencyUserGuide/getting-started-set-up-streaming.md#broadcast-sdk"), which support WebRTC and RTMPS. We recommend
  this, especially for production scenarios. See the details below for [Web](getting-started-pub-sub-web.md "getting-started-pub-sub-web.md"), [Android](getting-started-pub-sub-android.md "getting-started-pub-sub-android.md"), and [iOS](getting-started-pub-sub-ios.md "getting-started-pub-sub-ios.md").
- The Amazon IVS console — This is suitable for testing streams. See
  below.
- Other streaming software and hardware encoders — You can use any streaming
  encoder that supports the RTMP, RTMPS, or WHIP protocols. See [Stream Ingest](rt-stream-ingest.md "rt-stream-ingest.md") for more information.

## IVS Console

1. Open the [Amazon IVS
   console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs").

(You can also access the Amazon IVS console through the [AWS Management
Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").) 2. In the navigation pane, select **Stages**.
(If the nav pane is collapsed, expand it by selecting the hamburger
icon.) 3. Select the stage to which you want to subscribe or publish, to go to its
details page. 4. To subscribe: If the stage has one or more publishers, you can subscribe
to it by pressing the **Subscribe** button,
under the **Subscribe** tab. (Tabs are below
the **General Configuration** section.) 5. To publish:

    1. Select the **Publish** tab.
    2. You will be prompted to grant the IVS console access to your
     camera and microphone; **Allow** those
     permissions.
    3. Toward the bottom of the **Publish**
     tab, use the dropdown boxes to select input devices for the
     microphone and camera.
    4. To begin publishing, select **Start
     publishing**.
    5. To view your published content, go back to the **Subscribe** tab.
    6. To stop publishing, go to the **Publish** tab and press the **Stop
     publishing** button towards the bottom.

**Note**: Subscribing and publishing consume
resources, and you will incur an hourly rate for the time you are connected to the
stage. To learn more, see [Real-Time
Streaming](https://aws.amazon.com/ivs/pricing/#Real-Time_Streaming "https://aws.amazon.com/ivs/pricing/#Real-Time_Streaming") on the IVS Pricing page.
