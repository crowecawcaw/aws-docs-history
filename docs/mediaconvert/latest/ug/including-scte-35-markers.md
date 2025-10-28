# Including SCTE-35 markers

SCTE-35 markers indicate where downstream systems can insert other content (usually
advertisements or local programs). You can include SCTE-35 markers in transport stream (TS),
DASH, HLS, and CMAF outputs.

AWS Elemental MediaConvert puts SCTE-35 markers into your outputs in one of two ways:

- The service passes markers through from your input to the output. For more
  information, see [Configuring SCTE-35 marker passthrough from
  your input](passing-through-scte-35-markers.md "passing-through-scte-35-markers.md").
- The service inserts markers at the points that you specify in an Event Signaling
  and Management (ESAM) XML document. For more information, see [Specifying SCTE-35 markers
  using ESAM XML](specifying-scte-35-markers-using-esam-xml.md "specifying-scte-35-markers-using-esam-xml.md").
  Regardless of which way you put in the SCTE-35 markers, for outputs that have them, you
  can optionally do the following:

- You can have the service blank out audio and video during the ad avails indicated
  by the SCTE-35 markers. For more information, see [Configuring ad avail blanking](ad-avail-blanking.md "ad-avail-blanking.md").
- For HLS outputs, you can have the service include SCTE-35 information in your
  output HLS manifest. For more information, see [Including SCTE-35
  information in your HLS manifest](including-scte-35-information-in-your-hls-manifest.md "including-scte-35-information-in-your-hls-manifest.md").
  MediaConvert doesn't write SCTE-35 information to DASH manifests.

###### Note

MediaConvert does not process information from input manifests.
By default, the service doesn't pass through SCTE-35 markers from your input. When you set
up your job to pass through markers from the input or from an ESAM document, by default, the
service doesn't include SCTE-35 information in HLS manifests or do ad avail blanking.

###### Topics

- [Configuring SCTE-35 marker passthrough from
  your input](passing-through-scte-35-markers.md "passing-through-scte-35-markers.md")
- [Specifying SCTE-35 markers
  using ESAM XML](specifying-scte-35-markers-using-esam-xml.md "specifying-scte-35-markers-using-esam-xml.md")
- [Including SCTE-35
  information in your HLS manifest](including-scte-35-information-in-your-hls-manifest.md "including-scte-35-information-in-your-hls-manifest.md")
- [Configuring ad avail blanking](ad-avail-blanking.md "ad-avail-blanking.md")
- [SCTE-35 limitations](scte-35-limitations.md "scte-35-limitations.md")
