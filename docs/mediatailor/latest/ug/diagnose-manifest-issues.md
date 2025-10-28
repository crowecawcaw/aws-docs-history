# Diagnose CDN manifest delivery issues and

errors for MediaTailor

AWS Elemental MediaTailor content delivery network (CDN) manifest delivery problems can prevent proper
ad insertion and playback. If viewers receive incorrect or inconsistent ads in
multivariant playlists, media playlists, or MPDs:

1.  Check for cached manifests:
    - Verify TTL settings are set to 0 for all multivariant playlist, media
      playlist, and MPD paths
    - Confirm that your CDN isn't caching multivariant playlists, media
      playlists, or MPDs despite TTL settings
    - Check CDN logs for cache status - manifest requests should show
      `Miss` or `RefreshHit`, not
      `Hit`

2.  Verify CDN routing configuration:
    - Confirm manifest requests are being routed to MediaTailor endpoints, not
      cached or served from origin
    - Check that CDN behavior patterns correctly match manifest paths
      (\*.m3u8, \*.mpd)
    - Verify query parameters are being forwarded to MediaTailor for
      personalization
    - Test manifest URLs directly against MediaTailor to isolate CDN vs service
      issues

3.  Check header forwarding configuration:
    - Verify required headers are being forwarded (see [Required headers for MediaTailor CDN
      integration](cdn-configuration.md#cdn-required-headers "cdn-configuration.md#cdn-required-headers"))
    - Confirm User-Agent header is forwarded for device-specific ad
      targeting
    - Check that X-Forwarded-For header is forwarded for
      geo-targeting
    - Ensure Accept-Encoding header is forwarded for compression
      support

4.  Validate manifest content and structure:
    - Check that manifests contain expected ad insertion markers
      (EXT-X-CUE-OUT/IN for HLS)
    - Verify segment URLs in manifests use your CDN domain, not origin
      domains
    - Confirm ad segments are properly inserted and accessible
    - Test manifest syntax using validation tools (ffprobe for HLS, mp4box
      for DASH)

5.  Test different scenarios:

        * Test with different session IDs to verify personalization is
         working
        * Test from different geographic locations to verify
         geo-targeting
        * Test with different User-Agent strings to verify device
         targeting
        * Compare manifest responses with and without CDN to identify
         differences

    **Additional troubleshooting resources:**

- For detailed CDN caching configuration, see [Caching optimization for CDN and MediaTailor
  integrations](cdn-optimize-caching.md "cdn-optimize-caching.md")
- For comprehensive CDN routing setup, see [Set up CDN routing behaviors for MediaTailor](cdn-routing-behaviors.md "cdn-routing-behaviors.md")
- For header forwarding requirements, see [Required headers for MediaTailor CDN
  integration](cdn-configuration.md#cdn-required-headers "cdn-configuration.md#cdn-required-headers")
- For log analysis and error codes, see [CDN integration log analysis and error code
  reference for MediaTailor](cdn-log-error-reference.md "cdn-log-error-reference.md")
- For testing procedures and validation, see [Testing and validation
  for CDN and MediaTailor integrations](cdn-integration-testing.md "cdn-integration-testing.md")
  **Success criteria:** When resolved, players should start
  playback normally and ads should appear as expected. Manifest requests should return
  HTTP 200 status codes in CDN logs, and manifests should contain properly personalized ad
  content.
