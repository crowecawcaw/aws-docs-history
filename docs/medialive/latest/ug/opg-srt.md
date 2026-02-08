# Creating an SRT output group

When you create a AWS Elemental MediaLive channel, you might want to include an SRT output group.
For information about the use cases for an SRT output group, see [Containers, protocols,
and downstream systems](outputs-supported-containers-downstream-systems.md "outputs-supported-containers-downstream-systems.md").

With an SRT output group, you can create one or more outputs. Each output is an SPTS with
its own destination.

SRT outputs support two connection modes:

- **Caller mode**: MediaLive initiates connections to downstream systems. MediaLive is the caller and sender. The downstream system is the listener and receiver. MediaLive initiates the handshake with the downstream system, and after the handshake is accepted, MediaLive sends the content to the downstream system.
- **Listener mode**: Downstream systems initiate connections to MediaLive. MediaLive is the listener and sender. The downstream system is the caller and receiver. The downstream system initiates the handshake with MediaLive, and after the handshake is accepted, MediaLive sends the content to the downstream system.
  The output content must be encrypted, so you must use AWS Secrets Manager to store a passphrase that
  MediaLive will use to encrypt the content.

This section includes specific guidelines if you are sending the SRT output to an AWS Elemental MediaConnect flow.

###### Topics

- [Selecting the SRT connection mode](srt-connection-mode-selection.md "srt-connection-mode-selection.md")
- [Organize encodes in an SRT output
  group](design-srt-package.md "design-srt-package.md")
- [Plan for delivery using Amazon VPC](srt-get-ready.md "srt-get-ready.md")
- [Set up the passphrase in AWS Secrets Manager](srt-output-encryption-asm.md "srt-output-encryption-asm.md")
- [Creating SRT outputs in caller mode](creating-srt-caller-output.md "creating-srt-caller-output.md")
- [Creating SRT outputs in listener mode](creating-srt-listener-output.md "creating-srt-listener-output.md")
- [Output > Stream settings](srt-streams.md "srt-streams.md")
