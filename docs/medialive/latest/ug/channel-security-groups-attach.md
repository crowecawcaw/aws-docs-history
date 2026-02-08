# Step 2: Attach the channel security group to the channel

When you create a channel with SRT outputs in listener mode, you must attach a channel security group.

1. On the **Create channel** page, choose **Channel and input details** in the navigation pane.
2. In the **General settings** section, find the **Channel security groups** field.
3. From the dropdown list, select the input security group that you want to use as the channel security group.

The dropdown list shows all input security groups in your account, identified by their ID and any tags. 4. Continue creating the channel, including configuring your SRT outputs in listener mode. For information about creating SRT outputs, see [Creating an SRT output group](opg-srt.md "opg-srt.md").
**Result**

When you create the channel, MediaLive retrieves the CIDR rules from the input security group and applies them to control access to the channel's outputs. Downstream systems with IP addresses in the allow list can now connect to the SRT listener endpoints on your channel.
