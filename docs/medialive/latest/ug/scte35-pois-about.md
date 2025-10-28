# About POIS signal conditioning

You can configure a MediaLive channel so that your POIS server handles SCTE 35 message
that are in the content.

###### Note

To implement POIS signal conditioning, your organization must have access to a
POIS server.

## Supported conditioning actions

Each time MediaLive encounters a SCTE 35 message in the content, MediaLive sends the
message to the POIS server. The POIS server responds in one of these way:

- Replace: It replaces the content of the original SCTE 35 message and
  sends it to MediaLive. The output will contain only the original SCTE 35
  message, but with the new content.
- Delete: It instructs MediaLive to delete the SCTE 35 message. The output
  won't contain the original SCTE 35 message.
- No op: It instructs MediaLive to do nothing. The output will contain the
  original SCTE 35 message, with the original content.

The SCTE 35 messages that the POIS server returns are completely compliant
with the SCTE 35 standard.

## Number of channels and number of

POIS servers

- Each MediaLive channel can communicate with only one POIS server.
- One POIS server can communicate with multiple MediaLive channels. In this
  case, the POIS server identifies each channel using a unique combination
  of a POIS acquisition point identity and a zone identity.

## POIS signal conditioning and

standard channels

If the channel is a standard channel (with two pipelines), then each pipeline
sends the SCTE 35 message to the POIS server. The POIS server responds to each
request. Each pipeline handles its own response. Typically, the POIS server
sends the identical instruction to both pipelines.
