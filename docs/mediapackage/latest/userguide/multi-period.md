# Multi-period DASH in AWS Elemental MediaPackage

The ability to insert multiple periods in DASH manifests for
live is available in AWS Elemental MediaPackage.

A period is a chunk of content in the DASH manifest, defined by a start time and duration.
MediaPackage can partition the DASH manifest into multiple periods to indicate boundaries between
changes in the content. MediaPackage can signal new periods based on several triggers including:

- DRM configuration changes
- Avails
- DRM key rotation
- Source stream changes
- Source disruptions
  MediaPackage will always create a period at the beginning of content and whenever DRM
  configuration changes. The other triggers can be configured per DASH manifest, and have the
  following effects:

- **Avails** - MediaPackage will create a new period whenever it detects a SCTE-35 message
  which matches the Segment SCTE Filter configuration as an ad. All SCTE-35 messages will be
  signaled in the DASH manifest, whether it triggers a new period or not.
- **DRM key rotation** - MediaPackage will create a new period whenever the underlying DRM
  key rotates. This setting allows MediaPackage to signal the `default_KID` and `pssh` values in
  the manifest when key rotation is enabled. If this period trigger is not enabled, endpoints
  with DRM key rotation will not show the `default_KID` and `pssh` values in the manifest.
- **Source stream changes** - MediaPackage will create a new period when it detects stream
  set changes, allowing all streams to be signaled in the manifest, rather than just those
  available at manifest publish time.
- **Source disruptions** - MediaPackage will create a new period after source input has been
  lost and restored, enabling the gap in content to be signaled to the player.
