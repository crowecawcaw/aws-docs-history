# SCTE-35 message options in AWS Elemental MediaPackage

This section describes the options that AWS Elemental MediaPackage offers for configuring
how SCTE-35 messages are handled in live TS and CMAF
outputs.

SCTE-35 messages accompany video in your source content. These messages signal where MediaPackage
should insert ad markers when it packages the content for output. By default, MediaPackage inserts
markers for the following message types in the source content:

- Splice insert
- Break
- Provider advertisement
- Distributor advertisement
- Provider placement opportunity
- Distributor placement opportunity
- Provider overlay placement opportunity
- Distributor overlay placement opportunity
- Program
  When these commands are present, MediaPackage inserts corresponding ad markers in the output
  manifests:

- For daterange in HLS manifests on TS and CMAF origin endpoints, MediaPackage inserts
  `EXT-X-DATERANGE` tags.
- For SCTE-35 enhanced on TS and CMAF origin endpoints, MediaPackage inserts
  `EXT-X-CUE-OUT`, `EXT-X-CUE-IN`, and related CUE
  tags.
- For DASH manifests on CMAF origin endpoints, MediaPackage inserts
  `EventStream` tags to create multiple periods, when you have
  multi-period manifests enabled.
  The following sections describe how you can modify MediaPackage SCTE-35 message handling
  behavior.

###### Topics

- [How it works](scte-works.md "scte-works.md")
- [SCTE-35 settings](scte-settings.md "scte-settings.md")
- [HLS EXT-X-DATERANGE ad
  markers](ext-x-daterange-ad-marker.md "ext-x-daterange-ad-marker.md")
- [HLS CUE tag ad markers](ext-x-cue-ad-marker.md "ext-x-cue-ad-marker.md")
- [DASH ad markers](dash-ad-markers.md "dash-ad-markers.md")
