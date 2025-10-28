# Enabling manifest decoration in the

output

You can choose to interpret SCTE 35 messages from the input sources in a MediaLive channel
and insert corresponding instructions into the output manifest. This manifest decoratino
is supported in the following types of MediaLive outputs:

- HLS
- Microsoft Smooth (the instructions are inserted in the sparse track).
  MediaPackage outputs, which are a type of HLS output, are set up with manifest
  decoration enabled. You can't disable decoration in these outputs.

Manifest decoration is enabled at the output group level. If you enable the feature in
a specific output group, all the outputs in that group have their manifests
decorated.

To include manifest decoration in some outputs and not others, you must create two
output groups of the specified type, for example, two HLS output groups.

###### Topics

- [Enabling decoration –
  HLS](procedure-to-enable-decoration-hls.md "procedure-to-enable-decoration-hls.md")
- [Enabling decoration –
  Microsoft Smooth](procedure-to-enable-decoration-ms-smooth.md "procedure-to-enable-decoration-ms-smooth.md")
- [How SCTE 35 events are
  handled in manifests and sparse tracks](how-scte-35-events-are-handled-in-manifests.md "how-scte-35-events-are-handled-in-manifests.md")
- [Sample manifests - HLS](sample-manifests-hls.md "sample-manifests-hls.md")
