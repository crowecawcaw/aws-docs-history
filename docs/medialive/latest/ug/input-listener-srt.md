# Setting up an SRT Listener input

This section describes how to set up to receive transport stream (TS) content that is
pushed from an upstream system that is set up as an SRT caller. This section describes
how to set up the source content on the upstream system, and how to create an input that
connects the upstream system to MediaLive.

The transport stream source must be encrypted with AES.

**Roles**

With an SRT Listener input, MediaLive has two roles and the upstream system has two roles:

- For the SRT connection handshake: MediaLive is the SRT listener (the party that
  waits for the connection). The upstream system is the SRT caller. The upstream
  system initiates the SRT connection handshake that precedes the transmission of
  the source content.

- For the transmission: After the connection is made, the upstream system is
  always the sender of the content. MediaLive is always the receiver of the
  content.
  In terms of the categorization of inputs into push and pull, an SRT Listener input is a
  push input. You must use an input security group with an SRT Listener input to control which
  IP addresses are allowed to push content to MediaLive.

###### Topics

- [Get ready](input-listener-srt-prereqs.md "input-listener-srt-prereqs.md")
- [Create an SRT Listener input](input-listener-srt-setup.md "input-listener-srt-setup.md")
- [Provide connection information to the upstream system](setup-uss-srt-listener.md "setup-uss-srt-listener.md")
- [Result of this procedure](input-listener-srt-result.md "input-listener-srt-result.md")
- [Network locations for SRT Listener inputs](input-listener-srt-network-locations.md "input-listener-srt-network-locations.md")
