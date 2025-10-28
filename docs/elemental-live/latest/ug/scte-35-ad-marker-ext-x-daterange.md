# SCTE-35 ad marker

EXT-X-DATERANGE

This section is an addendum to [SCTE-35 and SCTE-104 message
processing in Elemental Live](scte-message-processing.md "scte-message-processing.md"). Elemental Live supports the
EXT-X-DATERANGE ad marker style in the manifest created for an HLS
output.

To select this marker, do the following:

- In the event, go to **Output Group** > **Apple
  HLS** > **Advanced** > **Ad Markers**
  and select **EXT-X-DATERANGE**.
  The structure and contents of the line are as described in HTTP Live Streaming,
  draft-pantos-http-live-streaming-23 (Version 23).

This marker style applies when the SCTE-35 messages are time_signal or splice_insert,
and when the messages are passed through from the input or inserted at runtime using the
REST API.

###### Example

This example shows an ad avail with an ID of 999 and a planned duration of 30
seconds. The first `EXT-X-DATERANGE`, for the start of the ad avail, includes
a `START-DATE`. The second `EXT-X-DATERANGE` includes an
`END-DATE` and a time that is 30.03 seconds later.

###### Note

The `DURATION`, `PLANNED-DURATION` and `END-DATE`
tags are optional. If they are not present in the input or not specified in the REST API
command, then these tags are omitted from the manifest.

```
#EXT-X-DATERANGE:ID="999",START-DATE="2018-08-22T21:54:00.079Z",PLANNED-DURATION=30.000,
SCTE35-OUT=0xFC302500000000000000FFF01405000003E77FEFFE0011FB9EFE002932E00001010100004D192A59
.
.
.
#EXT-X-DATERANGE:ID="999",END-DATE="2018-08-22T21:54:30.109Z",DURATION=30.030,
SCTE35-IN=0xFC0000425100FFF0140500000300000000E77FEFFE0011FB9EFE0029004D1932E0000100101002A22
```
