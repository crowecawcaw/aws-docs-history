# Setting up an SRT Caller input

This section describes how to set up to ingest transport stream (TS) content that is
sent from an upstream system that is set up as an SRT listener. This section describes
how to set up the source content on the upstream system, and how to create an input that
connects the upstream system to MediaLive.

The transport stream source can be encrypted with AES.

**Roles**

With an SRT input, MediaLive has two roles and the upstream system has two roles:

- For the SRT connection handshake: MediaLive is the SRT caller (the party that
  initiates the handshake). The upstream system is the SRT listener. The upstream
  system waits for MediaLive to call and initiate the SRT connection handshake that
  precedes the transmission of the source content.

- For the transmission: After the connection is made, the upstream system is
  always the sender of the content. MediaLive is always the receiver of the
  content.
  In terms of the categorization of inputs into push and pull, an SRT input is a pull
  input. You don't use an input security group with an SRT input.

###### Topics

- [Get ready](input-caller-srt-prereqs.md "input-caller-srt-prereqs.md")
- [Create an SRT input](input-caller-srt-setup.md "input-caller-srt-setup.md")
- [Ensure correct setup in the upstream system](setup-uss-srt-caller.md "setup-uss-srt-caller.md")
- [Result of this procedure](input-caller-srt-result.md "input-caller-srt-result.md")
