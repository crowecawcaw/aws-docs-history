# About channel security groups

A channel security group allows you to control which IP addresses can connect to your MediaLive channel outputs. This is similar to how input security groups control which IP addresses can push content to MediaLive inputs.

To configure a channel security group, you select an input security group from your account. MediaLive uses the CIDR allow list rules from that input security group to control which downstream systems can connect to the channel's outputs.

**Key characteristics**

- A channel security group references an input security group and applies its CIDR rules to the channel's outputs.
- You can attach at most one channel security group to a channel.
- The same input security group can be referenced by multiple channels as their channel security group.
- When you update the CIDR rules in an input security group, those changes automatically apply to all channels that reference it as their channel security group.
