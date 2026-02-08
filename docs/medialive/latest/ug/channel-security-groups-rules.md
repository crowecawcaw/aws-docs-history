# Rules and constraints

The following rules apply to channel security groups:

- **Maximum one per channel** – You can attach at most one channel security group to a channel.
- **Required for SRT outputs in listener mode** – If your channel includes at least one SRT output configured in listener mode, you must attach a channel security group to the channel.
- **Not allowed without SRT outputs in listener mode** – You cannot attach a channel security group to a channel that has no SRT outputs configured in listener mode.
- **Not supported for MediaLive Anywhere** – Channel security groups cannot be used with AWS Elemental MediaLive Anywhere channels.
- **Not supported for VPC channels** – Channel security groups cannot be used with channels that have VPC output delivery configured.
- **Cannot change on running channel** – You can add, change, or remove a channel security group only when the channel is stopped.
- **Input security group must exist** – The input security group you select must already exist in your account before you can use it as a channel security group.
- **Automatic updates** – When you update the CIDR rules in an input security group, those changes automatically apply to all channels using that input security group as a channel security group. You don't need to restart the channels.
- **Cannot delete in-use input security group** – You cannot delete an input security group if it is being used as a channel security group by any channel. You must first remove the channel security group from all channels, or delete those channels.
