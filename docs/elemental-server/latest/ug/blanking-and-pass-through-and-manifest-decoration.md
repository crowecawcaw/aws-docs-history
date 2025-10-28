This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Blanking and

Passthrough and Manifest Decoration

It is important to understand that the logic for blanking ad content works on the video
content associated with the “ad avail event” while the logic for passthrough and manifest
decoration works with the actual SCTE-35 message.

So you can blank ad avails and not pass through SCTE-35 messages or not blank ad avails
and not pass through SCTE-35 messages and decorate the manifest, or any combination: the
actions are independent.

The only exception to this rule is for HLS outputs: manifest decoration and passthrough
are either both enabled or both disabled.
