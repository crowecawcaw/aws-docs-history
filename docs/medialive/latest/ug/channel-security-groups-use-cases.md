# When to use channel security groups

Channel security groups are required in the following situations:

- **SRT outputs in listener mode** – When you configure an SRT output in listener mode, you must attach a channel security group to the channel. The channel security group defines which downstream systems (SRT callers) are allowed to connect to the MediaLive listener endpoint.
  Channel security groups are not used in the following situations:

- **SRT caller outputs** – When MediaLive acts as the caller (initiating connections to downstream listeners), no channel security group is needed because MediaLive is making outbound connections.
- **Other output types** – Channel security groups are not applicable to other output types such as HLS, MediaPackage, Archive, or UDP outputs.
- **MediaLive Anywhere channels** – Channel security groups cannot be used with AWS Elemental MediaLive Anywhere channels. MediaLive Anywhere channels use different security mechanisms.
