# DASH in AWS Elemental MediaPackage

MediaPackage supports Dynamic Adaptive Streaming over HTTP (DASH) for delivering content to a wide range of devices. DASH is an adaptive bitrate streaming protocol that enables high-quality streaming experiences by dynamically adapting to changing network conditions.

## DASH features and capabilities

When using DASH in MediaPackage, you can take advantage of the following features:

- **Container type**: DASH requires the CMAF container type.
- **Multi-period support**: MediaPackage supports multi-period DASH manifests, which enable advanced features like ad insertion, content switching, and DRM key rotation.
- **Segment template formats**: MediaPackage supports the Number with timeline segment template format, which uses the `$Number$` variable to refer to segments in the `media` attribute of the `SegmentTemplate` tag.
- **UTC timing options**: MediaPackage provides multiple options for synchronizing players to coordinated universal time (UTC), including UTC Direct, HTTP Head, HTTP Iso, and HTTP Xsdate.
- **SCTE-35 ad markers**: MediaPackage supports signaling ad markers in DASH manifests using either Binary or XML formats.
- **Encryption**: DASH supports both CENC and CBCS encryption methods with PlayReady, Widevine, and Irdeto (CENC only) DRM systems.

## DASH manifest structure

A DASH manifest, also known as a Media Presentation Description (MPD), is an XML document that describes the available media segments, their relationships, and other characteristics. The main components of a DASH manifest include:

- **MPD**: The root element containing metadata about the presentation, including profiles, type (static or dynamic), and availability start time.
- **Period**: Represents a period of time in the media presentation. A manifest can contain multiple periods for features like ad insertion.
- **AdaptationSet**: Groups related media content, such as different encodings of the same audio or video content.
- **Representation**: Describes a specific version of the content, such as a particular bitrate or resolution.
- **SegmentTemplate**: Defines how to construct URLs for media segments and provides timing information.

MediaPackage generates DASH manifests that conform to the DASH-IF Interoperability Guidelines, ensuring broad compatibility with DASH players.

## DASH period triggers

MediaPackage allows you to configure how periods are created in DASH manifests. You can choose from the following period triggers:

- **Avails**: Creates new periods when SCTE-35 ad markers that pass the configured filter are encountered.
- **DRM key rotation**: Creates new periods when encryption keys are rotated.
- **Source changes**: Creates new periods when there are changes in the stream set.
- **Source disruptions**: Creates new periods when there are gaps in all content streams.
- **None**: Formats the manifest as a single period, only creating additional periods when DRM settings change.

For more information about multi-period DASH, see [Multi-period DASH in AWS Elemental MediaPackage](multi-period.md "multi-period.md").

## DASH use cases

Consider using DASH endpoints in the following scenarios:

- Delivering content to Android devices and smart TVs that support DASH
- Implementing advanced advertising workflows with multi-period DASH
- Supporting DRM-protected content with PlayReady, Widevine, or Irdeto
- Creating multi-protocol streaming workflows that need to include DASH alongside other formats

For information about creating DASH endpoints, see [Create a DASH manifest](endpoints-create.md#dash-manifest "endpoints-create.md#dash-manifest").
