# Creating an SRT caller output group

When you create a AWS Elemental MediaLive channel, you might want to include an SRT caller output group.
For information about the use cases for an SRT caller output group, see [Containers, protocols,
and downstream systems](outputs-supported-containers-downstream-systems.md "outputs-supported-containers-downstream-systems.md").

With an SRT output group, you can create one or more outputs. Each output is an SPTS with
its own destination.

With this output group, MediaLive is always the caller and the sender. The downstream system
is the listener and the receiver. MediaLive initiates the handshake with the downstream system.
The downstream system (the SRT listener) accepts or rejects the handshake. After the
handshake is accepted, MediaLive sends (pushes) the content to the downstream system.

The output content must be encrypted, so you must use AWS Secrets Manager to store a passphrase that
MediaLive will use to encrypt the content.

This section includes specific guidelines if you are sending the SRT output to an
AWS Elemental MediaConnect flow.

###### Topics

- [Organize encodes in an SRT caller output
  group](design-srt-caller-package.md "design-srt-caller-package.md")
- [Plan for delivery using Amazon VPC](srt-caller-get-ready.md "srt-caller-get-ready.md")
- [Coordinate with the downstream system](downstream-system-srt.md "downstream-system-srt.md")
- [Set up the passphrase in AWS Secrets Manager](srt-output-encryption-asm.md "srt-output-encryption-asm.md")
- [Create the SRT caller output
  group](creating-srt-caller-output-group.md "creating-srt-caller-output-group.md")
- [Provide information to the downstream
  system](srt-caller-info-to-emx.md "srt-caller-info-to-emx.md")
