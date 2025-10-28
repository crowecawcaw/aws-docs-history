# POIS signal conditioning

You can configure an AWS Elemental MediaLive channel so that your POIS server can perform _signal conditioning_ on SCTE 35 messages that are in the
content. Each time MediaLive encounters a SCTE 35 message in the content, MediaLive sends the
message to the POIS server. The POIS server sends back a response to create a new SCTE
35 message, to replace the original message with different content, to delete the
existing message, or to do nothing.

###### Note

To implement POIS signal conditioning, your organization must have access to a
POIS server.

###### Topics

- [Supported version of the
  specification](scte35-pois-about-spec.md "scte35-pois-about-spec.md")
- [About POIS signal conditioning](scte35-pois-about.md "scte35-pois-about.md")
- [Setting up for POIS signal conditioning](scte35-pois-setup.md "scte35-pois-setup.md")
