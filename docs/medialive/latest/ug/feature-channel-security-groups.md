# Using channel security groups

You can configure a MediaLive channel to use a channel security group. A channel security group controls inbound traffic associated with the channel's outputs. This feature enables pull-style outputs, where downstream systems initiate connections to MediaLive.

Channel security groups are required when you configure SRT outputs in listener mode. In listener mode, MediaLive acts as the server, listening on a local socket for external systems to establish connections.

###### Topics

- [About channel security groups](channel-security-groups-about.md "channel-security-groups-about.md")
- [When to use channel security groups](channel-security-groups-use-cases.md "channel-security-groups-use-cases.md")
- [How channel security groups work](channel-security-groups-how-it-works.md "channel-security-groups-how-it-works.md")
- [Rules and constraints](channel-security-groups-rules.md "channel-security-groups-rules.md")
- [Setting up a channel security group](channel-security-groups-setup.md "channel-security-groups-setup.md")
- [Managing channel security groups](channel-security-groups-manage.md "channel-security-groups-manage.md")
