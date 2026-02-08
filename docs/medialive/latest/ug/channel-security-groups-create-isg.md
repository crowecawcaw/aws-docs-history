# Step 1: Create or identify an input security group

Before you create the channel, you must have an input security group that contains the CIDR allow list rules for the downstream systems that will connect to your SRT outputs configured in listener mode.

1. Identify the IP addresses of the downstream systems (SRT callers) that will connect to your MediaLive channel. These are the systems that will initiate connections to MediaLive.
2. If you don't already have an input security group with these IP addresses, create one. For instructions, see [Creating an input security group](create-input-security-groups.md "create-input-security-groups.md").

If you already have an input security group with the appropriate CIDR rules, you can reuse it. The same input security group can be used for both input security and channel security. 3. Make a note of the input security group ID. You will need this when you create the channel.
