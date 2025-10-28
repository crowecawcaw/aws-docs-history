# How SCTE-35 messages work in AWS Elemental MediaPackage works

The **Ad markers** and **SCTE filtering**
settings work
together to determine what MediaPackage does with SCTE-35 messages from the source
content.

When there are SCTE-35 messages in the source content, MediaPackage takes the following
actions based on the value that you selected in **Ad markers**:

- For **Daterange**, MediaPackage inserts `EXT-X-DATERANGE`
  tags to signal ads and program transition events in HLS output manifests.
- For **SCTE-35 enhanced**, MediaPackage inserts
  `EXT-X-CUE-OUT`, `EXT-X-CUE-IN`, and related CUE tags
  to signal ads and program transition events in HLS output manifests.
- For **XML** or **Binary**, MediaPackage inserts
  EventStream elements in the DASH manifests, with the selected signaling type,
  and create new periods when detecting markers defined as Ad markers.

###### Important note on SCTE-35 data tracks

MediaPackage also signals SCTE-35 markers present in the source that are not ad markers.
MediaPackage selects the first available data track from the input content for SCTE-35
signal processing (typically identified as PID 500). For proper
handling by MediaPackage, ensure that your SCTE-35 ad signals are included in this first
data track.

For DASH manifests, SCTE-35 markers that aren't ad markers don't create a new period.
Instead, MediaPackage places these markers in the period that corresponds to the marker
timing.
