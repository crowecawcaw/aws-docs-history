# Excluding DRM session keys in AWS Elemental MediaPackage

MediaPackage supports excluding session keys from HLS and LL-HLS multivariant playlists to
improve compatibility with legacy clients and provide more granular access control.

## Overview

By default, MediaPackage includes `EXT-X-SESSION-KEY` tags in HLS multivariant
playlists when DRM is enabled. These tags allow clients to pre-fetch encryption keys,
which can improve playback performance. However, some scenarios require excluding these
session keys:

- **Legacy client compatibility** - Some older HLS
  clients have issues processing session keys and may fail to play content when these
  tags are present.
- **Access control** - When using manifest filtering to
  control access to specific content variants, you may want to provide key information
  only for the streams a client actually has access to, rather than exposing all keys in
  the session key tags.

When session keys are excluded, encryption key information is still available in the
individual media playlists through `EXT-X-KEY` tags, ensuring that DRM
functionality remains intact.

## Configuration options

You can exclude session keys using two methods:

- **Static configuration** - Configure the setting on the
  origin endpoint to exclude session keys from manifests. This is done through the DRM
  settings in the filter configuration. For console instructions, see [Creating an origin endpoint](endpoints-create.md "endpoints-create.md").
- **Dynamic exclusion** - Use the
  `aws.drmsettings=exclude_session_keys` query parameter to exclude
  session keys on a per-request basis. For more information, see [Manifest filtering](manifest-filtering.md "manifest-filtering.md").

###### Note

If session key exclusion is enabled in the static configuration, it cannot be
overridden using query parameters. This follows the standard MediaPackage pattern where static
filters take precedence over dynamic parameters.
