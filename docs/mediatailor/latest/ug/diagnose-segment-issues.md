# Troubleshoot CDN segment delivery and loading

issues for MediaTailor

AWS Elemental MediaTailor content delivery network (CDN) segment delivery problems can cause buffering
and playback interruptions. If players can't load segments or experience
buffering:

1.  Check CDN routing rules:
    - Verify content segments are being routed to the correct origin
    - Confirm ad segments are being routed to the correct MediaTailor ad storage
      location
    - Check that segment file extensions match your CDN behavior
      patterns
    - Verify that segment URLs in manifests use the correct CDN
      domain
    - For detailed instructions on setting up routing and behavior path
      patterns, see [Set up CDN routing behaviors for MediaTailor](cdn-routing-behaviors.md "cdn-routing-behaviors.md")

2.  Verify CORS configuration:
    - For web players, ensure your CDN is passing through or properly
      setting CORS headers
    - Test with browser developer tools to identify CORS-related
      errors
    - Verify that preflight OPTIONS requests are handled correctly

3.  Test segment accessibility and performance:
    - Test individual segment URLs directly to verify they're
      accessible
    - Check segment response times and identify performance
      bottlenecks
    - Verify segment file sizes are appropriate for your bandwidth
      targets
    - Test segment loading from different geographic locations

4.  Validate CDN caching behavior for segments:
    - Verify content segments have appropriate TTL settings (typically
      longer than manifests)
    - Check that ad segments are cached appropriately based on
      personalization requirements
    - Monitor cache hit ratios for both content and ad segments
    - Ensure cache keys don't include unnecessary parameters that reduce
      cache efficiency

5.  Check origin server connectivity and health:
    - Verify origin servers are responding correctly to segment
      requests
    - Check origin server capacity and response times under load
    - Validate that origin servers have the expected segment files
      available
    - Test origin failover scenarios if multiple origins are
      configured

6.  Troubleshoot ad segment specific issues:
    - Verify ad segments are properly transcoded and available in
      MediaTailor
    - Check that ad segment URLs are correctly generated in manifests
    - Test ad segment loading with different ad targeting parameters
    - Monitor for ad transcoding delays that might cause segment
      unavailability

7.  Validate player compatibility and behavior:

        * Test segment loading with different player types and versions
        * Check player buffer settings and segment request patterns
        * Verify player error handling for failed segment requests
        * Test adaptive bitrate switching and segment selection logic

    **Additional troubleshooting resources:**

- For CDN routing and behavior configuration, see [Set up CDN routing behaviors for MediaTailor](cdn-routing-behaviors.md "cdn-routing-behaviors.md")
- For CDN caching optimization, see [Caching optimization for CDN and MediaTailor
  integrations](cdn-optimize-caching.md "cdn-optimize-caching.md")
- For CORS configuration guidance, see [CDN integration security best practices for
  MediaTailor](cdn-security-best-practices.md "cdn-security-best-practices.md")
- For performance monitoring and analysis, see [Monitor MediaTailor CDN operations and performance](cdn-monitoring.md "cdn-monitoring.md")
- For comprehensive testing procedures, see [Testing and validation
  for CDN and MediaTailor integrations](cdn-integration-testing.md "cdn-integration-testing.md")
- For log analysis and error diagnosis, see [CDN integration log analysis and error code
  reference for MediaTailor](cdn-log-error-reference.md "cdn-log-error-reference.md")
  **Success criteria:** When resolved, players should load
  segments smoothly without buffering interruptions. Segment requests should return HTTP
  200 status codes with appropriate response times, and both content and ad segments
  should be accessible and properly cached.
