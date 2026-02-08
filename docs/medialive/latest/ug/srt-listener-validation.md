# Validation rules for listener mode

MediaLive enforces the following validation rules when you create or update SRT outputs in listener mode:

- **Channel security group required (Public delivery method only)**: For channels using the Public delivery method, if the channel includes at least one SRT output configured in listener mode, you must attach a channel security group to the channel. If you attempt to create or start a channel using Public delivery with SRT outputs in listener mode but no channel security group, MediaLive returns an error. For channels using VPC delivery or MediaLive Anywhere channels, the channel security group is not required; you must configure your network to allow SRT connections from the caller destination.
- **Port uniqueness**: Within a single channel, each SRT output in listener mode must use a unique port number. If you attempt to create two outputs with the same port, MediaLive returns an error.
- **Listener port range**: The port number must be in the range 5000 to 5200 inclusive.
- **Cannot remove channel security group**: If the channel has SRT outputs in listener mode, you cannot remove the channel security group. You must first remove all SRT outputs configured in listener mode, or change them to caller mode.
- **Cannot change mode on running channel**: You cannot change an output's connection mode (from caller to listener or vice versa) while the channel is running. You must stop the channel first.
