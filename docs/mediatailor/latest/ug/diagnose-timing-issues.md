# Resolve CDN ad break timing and synchronization

issues for MediaTailor

AWS Elemental MediaTailor content delivery network (CDN) ad break timing must be precisely
synchronized with content markers. If ads appear at incorrect times or ad break timing
is inconsistent:

1.  Verify ad break markers in content:
    - Check that SCTE-35 markers are properly placed in your origin
      content
    - Verify ad break duration matches actual ad content length
    - Confirm that ad break timing aligns with content boundaries
    - Validate SCTE-35 marker format and timing accuracy in your origin
      manifests
    - Test ad break markers with different content types (live vs
      VOD)

2.  Check CDN caching impact on timing:
    - Ensure manifest TTL is set to 0 to prevent timing drift
    - Verify that time-sensitive parameters are not being cached
    - Check for clock synchronization issues between the content source,
      MediaTailor, and the CDN
    - Monitor for timing drift in long-running live streams
    - Verify CDN edge server time synchronization with NTP

3.  Validate SCTE-35 marker implementation:
    - Verify EXT-X-DATERANGE tags include proper SCTE35-OUT and DURATION
      specifications
    - Check for paired SCTE35-OUT and SCTE35-IN markers when using explicit
      cue-in timing
    - Validate START-DATE timestamps align with actual content timing
    - Test different SCTE-35 marker formats (duration-based vs paired
      markers)

4.  Test ad break timing across different scenarios:
    - Compare ad break timing with direct MediaTailor requests vs CDN
      requests
    - Test timing consistency across different CDN edge locations
    - Verify ad break timing with different player types and buffering
      behaviors
    - Monitor timing accuracy during peak traffic periods

5.  Debug timing issues using logs and monitoring:

        * Enable debug logging to track ad break processing timing
        * Monitor CloudWatch metrics for ad insertion timing patterns
        * Check CDN logs for timing-related request patterns
        * Use player debugging tools to verify ad break timing from client
         perspective

    **Expected timing tolerances:**

- Ad break timing should align with SCTE-35 markers in your content
- Ad duration should match the duration specified in your ad decision server
  response
- Clock synchronization between content source, MediaTailor, and CDN should be within
  1 second
- SCTE-35 marker timing should be accurate to within 100ms of actual content
  timing
  **Additional troubleshooting resources:**

- For SCTE-35 marker format and implementation, see [Integrating a content source for MediaTailor ad insertion](integrating-origin.md "integrating-origin.md")
- For debug logging setup and timing analysis, see [Generating AWS Elemental MediaTailor debug logs](debug-log-mode.md "debug-log-mode.md")
- For CDN caching configuration and timing impact, see [Caching optimization for CDN and MediaTailor
  integrations](cdn-optimize-caching.md "cdn-optimize-caching.md")
- For comprehensive testing procedures including timing validation, see [Testing and validation
  for CDN and MediaTailor integrations](cdn-integration-testing.md "cdn-integration-testing.md")
- For monitoring ad insertion timing and performance, see [Monitor MediaTailor CDN operations and performance](cdn-monitoring.md "cdn-monitoring.md")
  **Success criteria:** When resolved, ad breaks should
  appear at precisely the times specified by SCTE-35 markers, with consistent timing
  across all CDN edge locations and player types. Debug logs should show accurate ad break
  processing timing without drift or synchronization errors.
