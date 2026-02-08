# Create the SRT output in listener mode

After you have completed the prerequisites and coordinated with the downstream systems, you can create the SRT output in listener mode.

1. On the **Create channel** page, choose **Channel and input details** in the navigation pane.
2. **For channels using Public delivery method only**: In the **General settings** section, find the **Channel security groups** field.
3. **For channels using Public delivery method only**: From the dropdown list, select the input security group that you want to use as the channel security group.
4. Navigate to the **Output groups** section and choose **Add**.
5. In the **Add output group** section, choose **SRT**, and then choose **Confirm**.
6. In the **SRT settings** section, complete the fields:
   - **Name**: Enter a name for the output group.
   - **Input loss action**: Choose a value. For details, see [Handling loss of video input](feature-input-loss.md "feature-input-loss.md").

7. In the **SRT outputs** section, choose the **Settings** link for the output.
8. In the **Destinations** section, configure the listener mode settings:
   - **Connection mode**: Select **LISTENER**.
   - **Listener port**: Enter the port number that MediaLive will listen on. The valid range is 5000 to 5200.

   You must have unique ports for each of the SRT listener outputs on your channel.

   For a standard channel with two pipelines, you must have unique listener ports for each pipeline destination as well.
   - **Stream ID**: Optional. Enter the stream ID if you agreed on one with the downstream systems.
   - **Encryption passphrase secret ARN**: Select the ARN of the secret you created in Secrets Manager.

9. Complete the **Output settings** and **Stream settings** sections as described in [Output > Output settings](creating-srt-caller-output-group.md#srt-caller-output-settings "creating-srt-caller-output-group.md#srt-caller-output-settings") and [Output > Stream settings](srt-streams.md "srt-streams.md").
10. After you have finished setting up this output group and its outputs, you can create another output group (of any type), if your plan requires it. Otherwise, go to [Save the channel](creating-a-channel-step9.md "creating-a-channel-step9.md").
