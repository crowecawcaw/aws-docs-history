# Systematic testing methodology for CDN and

MediaTailor integrations

AWS Elemental MediaTailor content delivery network (CDN) integration testing should follow a
systematic, phased approach to ensure comprehensive coverage. Follow this structured
approach to comprehensively test your content delivery network and MediaTailor integration.
Each phase builds on the previous one to isolate potential issues.

For additional guidance on systematic testing approaches, see [Testing for
reliability](../../../wellarchitected/latest/reliability-pillar/test-reliability.md "../../../wellarchitected/latest/reliability-pillar/test-reliability.md") in the AWS Well-Architected Framework.

## Phase 1: Test direct MediaTailor

connectivity

Start by testing MediaTailor functionality without CDN involvement to establish a
baseline.

1. Test manifest requests directly to MediaTailor endpoints:
   - Test HLS multivariant playlist requests: `curl -v
"https://your-emt-endpoint.mediatailor.region.amazonaws.com/v1/master/hls/config-name/master.m3u8"`
   - Test DASH MPD requests: `curl -v
"https://your-emt-endpoint.mediatailor.region.amazonaws.com/v1/dash/config-name/manifest.mpd"`
   - Verify manifest responses contain expected ad break markers
   - Check that segment URLs point to correct origins

2. Verify ad insertion works correctly:
   - Test with different ad targeting parameters
   - Verify ad segments are properly transcoded and available
   - Check ad break timing and duration
   - Test fallback behavior when ads are unavailable

3. Measure baseline performance:
   - Record manifest request response times
   - Measure ad decision server response times
   - Test session creation and management

**Success criteria:** All direct MediaTailor requests
return HTTP 200 responses with properly formatted manifests containing expected ad
content.

## Phase 2: Test basic CDN

integration

Add CDN to the request path and test basic functionality.

1. Test manifest requests through CDN:
   - Configure CDN with simple routing rules
   - Test manifest requests through CDN endpoints
   - Verify CDN correctly forwards requests to MediaTailor
   - Check that manifest responses are not cached (TTL = 0)

2. Test segment routing:
   - Verify content segments route to origin server
   - Verify ad segments route to MediaTailor ad storage
   - Test segment caching behavior

3. Compare CDN vs direct performance:
   - Measure response time differences
   - Check for any content differences in responses
   - Verify error handling works correctly

**Success criteria:** CDN should successfully proxy
requests to MediaTailor and origin servers with minimal performance impact.

## Phase 3: Test query parameter

forwarding

Add query parameter forwarding and test ad personalization.

1. Configure query parameter forwarding at the CDN:
   - Enable forwarding of all query parameters to MediaTailor
   - Test session initialization (session ID is automatically generated
     by MediaTailor upon first request)
   - Test with custom targeting parameters

2. Test ad personalization:
   - Verify different parameters produce different ad responses
   - Test parameter encoding and special characters
   - Check that parameters are correctly passed to ADS

3. Validate session management:
   - Test session creation and persistence
   - Verify session ID consistency across requests
   - Test session expiration handling

**Success criteria:** Ad content varies based on
query parameters, and sessions are managed correctly.

## Phase 4: Test header forwarding

Add header forwarding in the CDN and test device-specific targeting.

1. Configure header forwarding for all headers. For minimum requirements, see
   [Required headers for MediaTailor CDN
   integration](cdn-configuration.md#cdn-required-headers "cdn-configuration.md#cdn-required-headers").
2. Test device targeting:
   - Test with different User-Agent strings (mobile, desktop,
     TV)
   - Verify device-specific ad responses
   - Test geographic targeting with different IP addresses

3. Validate CORS handling:
   - Test CORS headers for web player compatibility
   - Verify preflight OPTIONS requests work correctly
   - Test from different domains

**Success criteria:** Device and geographic targeting
should work correctly, and web players should not encounter CORS errors.

## Phase 5: Comprehensive scenario

testing

Test across multiple scenarios to ensure robust operation.

1. Test with different player types:
   - HLS.js players in web browsers
   - Video.js players with HLS and DASH support
   - Native players on mobile devices
   - Smart TV and set-top box players

2. Test on different devices and platforms:
   - Mobile devices (iOS, Android)
   - Desktop browsers (Chrome, Firefox, Safari, Edge)
   - Smart TVs and streaming devices
   - Different operating system versions

3. Test different content types:
   - Live streaming content
   - Video on demand (VOD) content
   - Different video formats and bitrates
   - Content with different ad break patterns

4. Test ad targeting scenarios:
   - Different demographic targeting parameters
   - Geographic targeting across different regions
   - Time-based targeting (different times of day)
   - Custom business logic parameters

**Success criteria:** All player and device
combinations should work correctly with appropriate ad targeting.

## Phase 6: Load and performance

testing

Validate performance under realistic load conditions.

###### Important

**Before load testing, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/"):**
Before conducting load and performance testing, create an AWS Support ticket
to notify the MediaTailor service team of your planned testing. This ensures:

- The service is prepared for your expected load levels
- Appropriate capacity is available during your testing window
- Your testing won't be mistaken for a production incident
- You receive guidance on testing best practices and limitations
  Include in your support ticket: expected concurrent users, testing duration,
  geographic regions, and any specific scenarios you plan to test.

1. Test concurrent user scenarios:
   - Simulate multiple concurrent viewers
   - Test CDN scaling and cache performance
   - Monitor origin server performance under load
   - Verify MediaTailor can handle concurrent sessions

2. Measure performance metrics:
   - Monitor response times under load
   - Check cache hit ratios meet expectations (>80% for popular
     content)
   - Measure time to first frame for different scenarios
   - Track error rates during peak load

3. Test failover scenarios:
   - Test behavior when ADS is unavailable
   - Test origin server failover
   - Verify error handling and recovery
   - Test CDN edge location failover

**Success criteria:** System should maintain
acceptable performance under expected load with graceful degradation during
failures. Ensure that you contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") and they approve your load testing plan
before execution.
