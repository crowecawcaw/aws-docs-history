# Delivering TS using the SRT protocol

In AWS Elemental Live , you can deliver a transport stream (TS) output from using the SRT protocol.
You can choose to encrypt the content with AES. This SRT delivery option
is part of the Reliable TS output group.

###### Note

The SRT option is intended for sending to a downstream system other
than AWS Elemental MediaConnect.

To send to an SRT flow on MediaConnect, we recommend that you use the
Reliable TS output group with the AWS Elemental MediaConnect option.
See [Setting up
Elemental Live as a Contribution Encoder for AWS Elemental MediaConnect](setting-up-live-as-contribution-encoder-for-mediaconnect.md "setting-up-live-as-contribution-encoder-for-mediaconnect.md").

There are two ways to configure the transmission, one with
Elemental Live as the SRT caller, one with Elemental Live as the SRT
listener. (In both cases, Elemental Live is the sender. In other words,
don't confuse the sender/receiver roles with the caller/listener
roles.)

Typically, the decision about the caller/listener roles is made by the
downstream destination:

- If the downstream destination is set up as the listener, then
  Elemental Live must set up as the caller.
- If the downstream destination is set up as the caller, then
  Elemental Live must set up as the listener.
  The SRT caller always initiates the handshake that precedes successful
  transmission of the output. The SRT listener accepts or rejects the
  handshake.

###### Topics

- [Getting ready](output-srt-get-ready.md "output-srt-get-ready.md")
- [Creating the output](output-srt-setup.md "output-srt-setup.md")
