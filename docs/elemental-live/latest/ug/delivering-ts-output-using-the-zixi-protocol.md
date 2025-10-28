# Delivering

TS output using the Zixi protocol

In AWS Elemental Live , you can deliver TS output using the Zixi protocol. The destination is
considered to be a _Zixi broadcaster_.
You can choose to encrypt the content with AES. This Zixi delivery option
is part of the Reliable TS output group.

###### Note

The Zixi option is intended for sending to a downstream system other
than AWS Elemental MediaConnect.

To send to a Zixi flow on MediaConnect, we recommend that you use the
Reliable TS output group with the AWS Elemental MediaConnect option.
See [Setting up
Elemental Live as a Contribution Encoder for AWS Elemental MediaConnect](setting-up-live-as-contribution-encoder-for-mediaconnect.md "setting-up-live-as-contribution-encoder-for-mediaconnect.md").

The Zixi protocol involves two roles—the
Zixi
_feeder_ (also known as the
caller)
and the
Zixi
_receiver_ (the
listener).
The
Zixi
feeder always initiates the handshake that precedes
successful transmission of the output. The
Zixi
receiver accepts or rejects the handshake.

With the Zixi option in the Reliable TS output group, Elemental Live is
always the Zixi
feeder,
which means the downstream system must be the Zixi
receiver.
