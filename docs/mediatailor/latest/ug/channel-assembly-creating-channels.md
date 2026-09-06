

# Create a channel using the MediaTailor console
<a name="channel-assembly-creating-channels"></a>

 The following procedure describes how to create a channel using the MediaTailor console. <a name="create-channel-procedure"></a>

**To create a channel**

1. Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/).

1. In the navigation pane, choose **Channel assembly** > **Channels**.

1. On the navigation bar, choose **Create channel**.

1. Under **Channel details**, enter details about your channel:
   + **Name**: Enter a name for your channel.
   + **Tier**: The tier determines what features the channel supports and how much it costs to run the channel. For more information about pricing, see the [Channel Assembly pricing page](https://aws.amazon.com/mediatailor/pricing/#Channel_Assembly_Pricing). MediaTailor supports the following tiers:
     + **Basic** - The Basic tier supports both the Linear and Loop playback modes, and does not support live sources.
     + **Standard** - The Standard tier supports live sources, and requires the Linear playback mode.

       When you select **Standard** in** Channel details**, you can define the audiences under **Audiences details**. These audiences will be used for programRules when you are going to create audienceMedia for your default program..
       + Choose **Add**.
       + Enter the **Audience** name in the text box. It must be between 1 and 32 alphanumeric characters long.
       +  Choose **Confirm**.
       + Choose **Next**.
   + <a name="playback-mode"></a><a name="playback-mode.title"></a>**Playback mode**: The playback mode sets the channel's playback behavior. MediaTailor supports the following playback modes:
     + **Loop** - The programs in the schedule play back-to-back in an endless loop. After the last program plays in a schedule, playback loops back to the first program. Playback continues looping until you stop the channel.
     + **Linear** - Each program in the schedule plays once, back-to-back.

1. <a name="filler-slate"></a>For **Filler slate**, select the **Source location name** referencing the slate location, and the **VOD source name** to use as slate. MediaTailor uses the slate to fill gaps between programs in the schedule. If the duration of the slate is less than the duration of the gap between programs, MediaTailor loops the slate. You must configure filler slate field is if your channel uses the linear playback mode. MediaTailor doesn't support filler slate for the loop playback mode.

1. Choose **Next**.

1. Specify audience details under program rules.

1. When you select **Standard** in** Channel details**, you can define the audiences under **Audiences** details. These audiences will be used for **programRules** when you are going to create **audienceMedia** for your default program:
   + Select **Add**, and then add an Audience in the text box, then select **Confirm**.
**Note**  
Enter a name that's no longer than\_ 32 alphanumeric characters.
   + **Output type**: Select the streaming format for the channel. DASH and HLS are supported.
   + **Source group**: Enter the name of the source group that you created in your package configuration, as described in [Adding VOD sources to your source location](channel-assembly-add-vod-source.md).

1. Select **Next**.

1. Under **Manifest settings**, enter additional information about your manifest settings:
   + **Manifest window (sec)**: The time window,in seconds, contained in each manifest. The minimum value is 30 seconds, and the maximum value is 3600 seconds.
   + **Ad markup type(HLS outputs only)**: The type of ad tags that appear in VOD program ad breaks. Select `Daterange` to have MediaTailor insert ad breaks into VOD programs with `EXT-X-DATERANGE` tags. Select `Scte35 Enhanced` to have MediaTailor insert ad breaks into VOD programs using `EXT-X-CUE-OUT` and `EXT-X-CUE-IN` tags. For more information about these tag types, see [SCTE-35 messages for ad breaks](ca-scte-35-messages.md). For live workflows, MediaTailor always passes through `DATERANGE` tags, and doesn't pass through any Enhanced Scte35 tags, regardless of the selected Ad markup type.

1. If you want to configure multiple channel outputs, under **Outputs** choose **Add**. Then, configure the details for your output by completing the steps 6 and 7 in this procedure.

1. Choose **Next**.

1. Under **Channel policy**, choose your channel's IAM policy settings:
   + **Do not attach channel policy**: Restrict playback to only those who have access to this account's credentials.
   + **Attach custom policy**: Define your own policy and restrict access to as few or as many as you want. 
   + **Attach public policy**: Accept all incoming client requests to a channel's output. You must use this option if you want to use MediaTailor ad insertion.

1. Choose **Next**.

1. Review your settings on the **Review and create** pane.

1. Choose **Create channel**.
**Note**  
Channels are created in a stopped state. Your channel won't be active until you start it with the MediaTailor console or the MediaTailor StartChannel API.