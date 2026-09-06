

# Updating or removing a channel security group
<a name="channel-security-groups-update"></a>

You can change which input security group is used as the channel security group, or you can remove the channel security group entirely. However, you can only make these changes when the channel is stopped.

**To update or remove a channel security group**

1. Stop the channel if it is running.

1. In the navigation pane, choose **Channels**.

1. Select the channel, and then choose **Edit**.

1. Choose **Channel and input details** in the navigation pane.

1. In the **General settings** section, find the **Channel security groups** field.

1. To change the channel security group, select a different input security group from the dropdown list.

   To remove the channel security group, clear the selection. Note that you can only remove the channel security group if you also remove all SRT outputs configured in listener mode from the channel.

1. Choose **Update channel**.