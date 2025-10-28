# Troubleshoot MediaPackage, CDN, and MediaTailor

integrations

AWS Elemental MediaTailor integration with AWS Elemental MediaPackage and content delivery network (CDN) can encounter
common issues that affect playback, caching, or other integration functionality. Use this
guide when you encounter playback problems, caching issues, or other integration-related
errors.

For comprehensive CDN troubleshooting guidance including universal cache performance
issues, HTTP error resolution, testing procedures, and diagnostic techniques that apply to
all MediaTailor implementations, see [Troubleshoot CDN integration](cdn-troubleshooting.md "cdn-troubleshooting.md"). This section focuses on
MediaPackage specific troubleshooting requirements.

Before troubleshooting, ensure you've completed the basic integration setup correctly. If
you haven't set up your integration yet or need to review the setup steps, see [Integrate MediaTailor with MediaPackage and CDN](mediapackage-integration.md "mediapackage-integration.md") . For
guidance on optimizing cache performance after resolving issues, see [CDN caching](cdn-emp-caching.md "cdn-emp-caching.md").

## Manifest filtering errors

Issues with MediaPackage manifest filtering functionality, based on documented error
conditions:

**HTTP 400 errors with manifest filtering**

**Symptoms**: Requests with
`aws.manifestfilter` parameters return HTTP 400 Bad
Request

**Validated causes (from AWS
documentation)**:

- Filter criteria result in an empty manifest (no streams match the
  filter conditions)
- Invalid filter parameter names or values
- Malformed query string syntax
- Duplicate or repeated filter parameters
- Filter parameter string exceeds 1024 characters
- Query parameters applied to media playlists or segments (not
  supported)

**Solutions**:

1. Review your filter parameters to ensure they match available
   content streams. If filtering results in no matching streams, MediaPackage
   returns HTTP 400.
2. Validate filter syntax against supported parameter names and value
   formats.
3. Check for duplicate parameters in your query string.
4. Ensure filter parameters are only applied to multivariant
   playlists, not to media playlists or segments.
5. Verify that your total parameter string is under 1024
   characters.

**Reference**: [AWS Elemental MediaPackage manifest filtering error
conditions](../../../mediapackage/latest/userguide/error-conditions-and-handling.md "../../../mediapackage/latest/userguide/error-conditions-and-handling.md")

**Manifest filtering not working (HTTP 200 but no filtering applied)**

**Symptoms**: Requests return HTTP 200 but
manifest contains all streams instead of filtered subset

**Possible causes**:

- CDN not forwarding `aws.manifestfilter` query parameter
  to MediaPackage
- Filter parameter not found in available streams (returns
  unfiltered manifest with HTTP 200)

**Solutions**:

1. Verify that your CDN cache policy includes
   `aws.manifestfilter` in the list of forwarded query
   strings.
2. Test filter parameters directly against MediaPackage endpoints (bypassing
   CDN) to verify they work as expected.
3. Check that filter values match the actual characteristics of your
   content streams.

**Reference**: [AWS Elemental MediaPackage manifest filtering error
conditions](../../../mediapackage/latest/userguide/error-conditions-and-handling.md "../../../mediapackage/latest/userguide/error-conditions-and-handling.md")

## Diagnostic procedures

Systematic diagnostic procedures help you identify the root cause of integration
issues quickly and efficiently. Following a structured approach prevents wasted time on
incorrect assumptions and ensures you address the actual problem rather than symptoms.
These evidence-based diagnostic steps are designed to isolate issues and guide you to
the appropriate solution.

Follow these evidence-based diagnostic steps to identify issues:

### Analyze cache performance

Cache performance analysis is crucial for EMP integrations because poor cache efficiency leads to increased origin load, higher costs, and potential playback issues.

For comprehensive cache performance troubleshooting including cache hit ratio analysis, cache key optimization, and systematic diagnostic steps, see [CDN cache performance
issues](diagnose-performance-issues.md#cache-performance-troubleshooting "diagnose-performance-issues.md#cache-performance-troubleshooting") in the main CDN troubleshooting guide.

EMP-specific cache considerations:

- **EMP cache-control headers**: Verify that your CDN honors EMP's cache-control headers rather than overriding them
- **EMP query parameters**: Ensure only necessary EMP query parameters are included in cache keys
- **EMP TTL behavior**: Confirm different EMP content types have appropriate cache durations

For detailed guidance on optimizing EMP cache policies and TTL settings, see [Optimize CDN caching for MediaTailor and MediaPackage content
delivery](cdn-emp-caching.md "cdn-emp-caching.md").

### Validate manifest filtering

configuration

Manifest filtering validation is essential because filtering issues can result in
viewers receiving incorrect content, unsupported formats, or content they shouldn't
have access to. Systematic testing helps identify whether issues are related to CDN
configuration, filter parameter syntax, or content availability.

Test manifest filtering functionality systematically:

1. Test filter parameters directly against MediaPackage endpoints (bypassing CDN) to
   verify they work correctly.
2. Compare filtered and unfiltered manifests to confirm expected streams are
   included/excluded.
3. Verify that your CDN cache policy forwards the
   `aws.manifestfilter` query parameter.
4. Check for HTTP 400 errors and match them against the documented error
   conditions.

If you need to implement or modify manifest filtering after resolving issues, see
[Set up manifest filtering with MediaTailor, MediaPackage,
and CDN](cdn-emp-manifest-filtering.md "cdn-emp-manifest-filtering.md") for complete setup guidance.

### Validate query parameter

configuration

Ensure your CDN forwards only the required query parameters:

1. Review your CDN cache policy to confirm it includes only AWS recommended
   parameters:
   - `aws.manifestfilter` - for manifest filtering
   - `aws.manifestsettings` - for time-shifted
     viewing
   - `_HLS_msn` and `_HLS_part` - for LL-HLS
     support

2. Remove any other query parameters from your cache key, as MediaPackage ignores
   them and they reduce cache efficiency.

**Reference**: [Working with AWS Elemental MediaPackage and CDNs](../../../mediapackage/latest/userguide/cdns.md "../../../mediapackage/latest/userguide/cdns.md")

## Error code reference

Reference for documented error conditions and their causes:

**HTTP 400 Bad Request (Manifest Filtering)**

**Documented causes**:

- Application of filter results in empty manifest
- Invalid parameter names or values
- Malformed query string syntax
- Duplicate filter parameters
- Parameter string exceeds 1024 characters
- Query parameters on
  media playlists or segments

**Reference**: [MediaPackage manifest filtering error conditions](../../../mediapackage/latest/userguide/error-conditions-and-handling.md "../../../mediapackage/latest/userguide/error-conditions-and-handling.md")

**HTTP 200 OK (No Filtering Applied)**

**Documented causes**:

- Filter parameter not found in available streams (returns
  unfiltered manifest)
- Only subtitle streams present after filtering (returns unfiltered
  manifest)

**Reference**: [MediaPackage manifest filtering error conditions](../../../mediapackage/latest/userguide/error-conditions-and-handling.md "../../../mediapackage/latest/userguide/error-conditions-and-handling.md")

## Additional troubleshooting resources

For issues not covered in this topic, consult these official AWS resources:

- [Previewing a manifest from AWS Elemental MediaPackage](../../../mediapackage/latest/userguide/endpoints-preview.md "../../../mediapackage/latest/userguide/endpoints-preview.md") - Use
  manifest preview to troubleshoot content packaging issues
- [Increase CloudFront cache hit ratio](../../../AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.md "../../../AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.md") - Comprehensive guide to CDN
  cache optimization
- [Manifest filtering](../../../mediapackage/latest/userguide/manifest-filtering.md "../../../mediapackage/latest/userguide/manifest-filtering.md") - Complete guide to MediaPackage filtering
  functionality
