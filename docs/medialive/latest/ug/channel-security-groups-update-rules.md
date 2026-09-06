

# Updating CIDR rules
<a name="channel-security-groups-update-rules"></a>

To update the CIDR allow list rules for a channel security group, you update the underlying input security group. The changes automatically apply to all channels using that input security group as a channel security group.

**To update CIDR rules for a channel security group**

1. In the navigation pane, choose **Input security groups**.

1. Select the input security group that is being used as a channel security group, and then choose **Edit**.

1. Update the CIDR rules as needed. For instructions, see [Editing an input security group](edit-input-security-group.md).

1. Choose **Update**.

**Result**

MediaLive automatically applies the updated CIDR rules to all channels using this input security group as a channel security group. You don't need to restart the channels. The changes take effect immediately.