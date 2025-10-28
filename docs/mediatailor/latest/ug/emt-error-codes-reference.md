# MediaTailor error codes and CDN integration

troubleshooting

AWS Elemental MediaTailor error codes provide specific information about integration issues when
passed through your content delivery network (CDN). When MediaTailor returns errors through
your content delivery network, these codes indicate specific issues:

**Note:** These error codes are returned by MediaTailor and
passed through your CDN. For CDN-specific errors, consult your CDN provider's
documentation.

400 Bad Request

**Common causes:** Malformed query
parameters, missing required parameters, invalid session IDs

**Check:** CDN query string forwarding
configuration, parameter encoding

403 Forbidden

**Common causes:** Client player requesting a
segment that does not exist or lacks permission to access. For ad segments,
MediaTailor might have specified a non-existent segment (contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") to
investigate). For content segments, origin provider access restrictions or
authentication issues

**Check:** For ad segments: contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/")
if MediaTailor is generating invalid segment URLs. For content segments: Verify
origin server permissions, authentication credentials, and access policies.
Check if segments exist at the requested URLs

404 Not Found

**Common causes:** MediaTailor configuration
doesn't exist or is inactive, incorrect playback URL path, manifest or
segment requests to non-existent resources

**Check:** Verify MediaTailor configuration exists
and is active, confirm playback URL matches the
`ManifestEndpointPrefix` from
`GetPlaybackConfiguration`, check CDN routing rules forward
requests to correct MediaTailor endpoints

500 Internal Server Error

**Common causes:** Origin server issues, ADS
connectivity problems, manifest processing errors

**Check:** Origin server health, ADS response
validity, MediaTailor service status

502 Bad Gateway

**Common causes:** Origin server unreachable,
invalid origin response, `UnsupportedManifestException` due to
HLS playlist alignment issues (SCTE markers not aligned across playlists,
missing SCTE markers on some playlists, inconsistent ad break timing across
bitrate variants)

**Check:** Origin server connectivity and
firewall rules, DNS resolution, HLS playlist consistency across all bitrate
variants, SCTE-35 marker alignment on same segments across all playlists,
verify all playlists contain required ad break markers

**Error code analysis resources:**

- [Troubleshooting MediaTailor](troubleshooting.md "troubleshooting.md") - Complete MediaTailor error code
  reference
- [Troubleshooting CloudFront error responses](../../../AmazonCloudFront/latest/DeveloperGuide/troubleshooting-response-errors.md "../../../AmazonCloudFront/latest/DeveloperGuide/troubleshooting-response-errors.md") - CDN-specific error
  analysis
- [HTTP
  response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status") - Comprehensive HTTP status code
  reference
- [Failure management](../../../wellarchitected/latest/reliability-pillar/failure-management.md "../../../wellarchitected/latest/reliability-pillar/failure-management.md") - Well-Architected error handling
  patterns
