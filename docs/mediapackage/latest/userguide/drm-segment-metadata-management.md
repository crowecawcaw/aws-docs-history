# Managing DRM segment metadata in AWS Elemental MediaPackage

AWS Elemental MediaPackage includes DRM segment metadata boxes (SEIG and SGPD) in CMAF container segments
by default. These boxes contain key rotation metadata that helps players manage DRM key
changes during playback. However, some devices and players don't support these metadata boxes,
which can cause compatibility issues.

## Overview of SEIG and SGPD boxes

DRM segment metadata boxes serve specific functions in encrypted content
delivery:

- **SEIG (Sample Encryption Information Group) boxes** -
  Contain sample-level encryption information including initialization vectors and
  subsample encryption patterns.
- **SGPD (Sample Group Description) boxes** - Define the
  structure and parameters for sample groups, including encryption-related
  groupings.

These boxes work together to provide detailed encryption metadata at the segment level,
enabling fine-grained control over DRM key rotation and sample encryption patterns.

## Device compatibility challenges

While SEIG and SGPD boxes provide valuable functionality, they can cause compatibility
issues with certain devices and players:

- **MatchPoint and FairPlay devices** - Some devices that
  use MatchPoint or FairPlay DRM systems may not properly parse or handle these metadata
  boxes, leading to playback failures.
- **MP browser implementations** - Certain browser-based
  media players may encounter parsing errors when processing segments with these metadata
  boxes.
- **Vuze devices** - Some Vuze-based players may not
  support the additional metadata complexity, resulting in compatibility issues.
- **Legacy FairPlay implementations** - Older FairPlay
  implementations may not handle the metadata boxes correctly, particularly in combination
  with other DRM features.

When these compatibility issues occur, players may fail to start playback, encounter
buffering problems, or display error messages related to DRM or segment parsing.

## When to exclude segment

metadata

Consider excluding DRM segment metadata in the following scenarios:

- **Device compatibility requirements** - When your
  content must play on devices known to have issues with SEIG and SGPD boxes.
- **Simplified DRM workflows** - When you can handle key
  rotation through media playlist signaling instead of segment-level metadata.
- **Legacy player support** - When supporting older
  players that don't implement full support for these metadata boxes.
- **Troubleshooting playback issues** - As a diagnostic
  step when investigating DRM-related playback problems.

###### Note

Excluding segment metadata doesn't affect other DRM functionality. PSSH (Protection
System Specific Header) and TENC (Track Encryption) boxes remain unaffected and continue
to provide essential DRM information.

## Alternative key rotation

methods

When you exclude segment metadata, key rotation can still be handled through alternative
methods:

- **Media playlist signaling** - Key rotation information
  can be communicated through HLS media playlists using EXT-X-KEY tags or DASH manifests
  using ContentProtection elements.
- **Manifest-level metadata** - DRM key information can
  be provided at the manifest level rather than within individual segments.
- **Player-side key management** - Players can manage key
  rotation based on timing information and DRM license responses rather than segment
  metadata.

These alternative methods ensure that DRM functionality remains intact while improving
compatibility with devices that don't support segment-level metadata boxes.

## Configuration requirements

The segment metadata exclusion feature has specific requirements and limitations:

- **Container format requirement** - This setting only
  affects CMAF container formats. TS (Transport Stream) containers don't include SEIG and
  SGPD boxes, so this setting doesn't apply.
- **Encryption requirement** - The setting is only
  available when DRM encryption is enabled on the origin endpoint.
- **Default behavior** - By default, MediaPackage includes
  segment metadata boxes. You must explicitly enable the exclusion setting to omit
  them.
- **Existing endpoints** - Existing origin endpoints that
  don't have this setting configured will continue to include segment metadata boxes
  (default behavior).

To configure this setting using the MediaPackage console, see [Encryption fields](endpoints-create.md#endpoints-encryption "endpoints-create.md#endpoints-encryption").
