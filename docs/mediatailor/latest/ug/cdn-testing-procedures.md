# CDN integration testing procedures

Proper testing is essential before deploying your MediaTailor CDN integration to production.
These testing procedures help identify configuration issues, performance problems, and
compatibility issues across different devices and platforms.

## Basic integration validation

Perform these fundamental tests to verify your CDN integration is working
correctly:

1. **Test manifest delivery**:
   - Request a manifest through your CDN and verify it returns a valid
     response
   - Verify the manifest contains expected content and ad insertion
     points
   - Check that manifest URLs use your CDN domain, not the
     origin
   - Validate manifest syntax using HLS or DASH validation tools

2. **Verify URL rewriting**:
   - Check that content segment URLs in manifests point to your CDN
     domain
   - Verify ad segment URLs point to your CDN domain
   - Ensure all relative URLs are properly resolved

3. **Test content playback**:
   - Play content through a video player and verify smooth
     playback
   - Verify both content and ads play without interruption
   - Check for proper transitions between content and ads
   - Test seeking and scrubbing functionality

4. **Validate CDN routing**:
   - Monitor CDN access logs to ensure requests are routed
     correctly
   - Verify cache hit/miss patterns are as expected
   - Check that origin requests only occur for cache misses

## Advanced testing procedures

Perform these additional tests for comprehensive validation:

1. **Cross-platform compatibility
   testing**:
   - Test on multiple devices (desktop, mobile, tablet, smart
     TV)
   - Verify compatibility across different browsers
   - Test with various video players (HLS.js, Video.js, native
     players)
   - Validate on different operating systems

2. **Performance testing**:
   - Measure manifest request response times (target: <100ms for
     cached)
   - Test segment loading performance across different bitrates
   - Verify startup time meets performance targets
   - Test under various network conditions

3. **Ad tracking validation**:
   - Verify ad tracking beacons fire correctly
   - Check ad analytics data for accuracy
   - Test impression and completion tracking
   - Validate click-through functionality

4. **Error condition testing**:
   - Test behavior when origin is temporarily unavailable
   - Verify graceful handling of malformed requests
   - Test CDN failover scenarios
   - Validate error message clarity and usefulness

## Create a test environment

Set up a test environment that mirrors your production configuration for
comprehensive validation:

1. Set up separate CDN distributions for testing:
   - Create test CDN distributions with the same cache behaviors as
     production
   - Configure test origins that mirror your production setup
   - Use separate domain names to avoid conflicts with production
     traffic

2. Create test MediaTailor configurations:
   - Set up test playback configurations with the same settings as
     production
   - Configure test ad decision server endpoints
   - Use test ad content that matches your production ad formats

3. Implement systematic testing processes:
   - Create testing checklists for configuration changes
   - Document test procedures for your team
   - Set up automated testing where possible

## Test across multiple scenarios

Validate your integration across different scenarios and conditions to ensure
comprehensive coverage:

1. Test with multiple player types and devices:
   - Test with different video players (web, mobile, connected
     TV)
   - Validate across different operating systems and browsers
   - Test on various network conditions and connection speeds

2. Create automated testing scripts:
   - Automate manifest request validation
   - Create scripts to test ad insertion scenarios
   - Implement performance testing for high-traffic scenarios

3. Validate ad targeting and personalization:
   - Test with different user profiles and targeting parameters
   - Validate ad decision server integration
   - Test fallback scenarios when ads are unavailable

## Testing tools and techniques

Use these tools and techniques for effective testing:

Browser developer tools

Use Network tab to inspect HTTP requests and responses

Monitor console for JavaScript errors and warnings

Verify response headers and caching behavior

Check timing information for performance analysis

Command-line testing

Use curl to test specific URLs and inspect headers:

```
curl -I "https://your-cdn-domain.com/path/to/manifest.m3u8"
```

Use wget for download testing and timing analysis

Employ tools like httpie for more readable HTTP testing

Video player testing

Test with multiple player implementations

Use player debug modes to inspect internal behavior

Monitor player events and error callbacks

Validate adaptive bitrate switching behavior

CDN analytics and monitoring

Monitor real-time CDN metrics during testing

Review access logs for request patterns

Use CDN-specific testing tools when available

Set up temporary alerts for testing validation

For additional comprehensive testing methodologies and systematic validation approaches, see [Testing and validation
for CDN and MediaTailor integrations](cdn-integration-testing.md "cdn-integration-testing.md").
