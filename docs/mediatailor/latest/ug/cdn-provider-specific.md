# Set up third-party CDNs for MediaTailor ad

delivery

Third-party CDNs like Akamai and Fastly can significantly improve the performance and
scalability of your AWS Elemental MediaTailor ad delivery while reducing bandwidth costs. However, CDN
configuration for personalized advertising requires specific settings that differ from
standard video delivery.

For information about passing query parameters through third-party CDNs, see [MediaTailor manifest query parameters](manifest-query-parameters.md "manifest-query-parameters.md"). For
advanced routing configurations using dynamic variables, see [MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md").

This guide walks you through the complete process of setting up your third-party CDN to
work optimally with MediaTailor. You'll learn how to configure two essential behaviors:

- **Manifest bypass:** Ensures each viewer receives
  personalized ad insertions by preventing manifest caching
- **Segment caching:** Maximizes performance and
  reduces costs by efficiently caching video content
  The configuration process typically takes 30-60 minutes and includes provider selection,
  setup, verification, and optimization. Once complete, you'll have a CDN configuration that
  delivers personalized ads efficiently while maintaining optimal viewer experience.

###### Note

This guide focuses on Akamai and Fastly configurations. For CloudFront setup instructions,
see [CloudFront
integration](cloudfront-specific-recommendations.md "cloudfront-specific-recommendations.md").

## Prerequisites

Before setting up your third-party CDN with MediaTailor, make sure you have:

- An active MediaTailor configuration that includes your content origin and ad
  decision server
- Access to your CDN's configuration interface
- A list of file extensions used in your content (.m3u8, .mpd, .ts, and so
  on)
- Your CDN provider's documentation for reference

For CloudFront setup instructions instead of third-party CDNs, see [CloudFront
integration](cloudfront-specific-recommendations.md "cloudfront-specific-recommendations.md").

###### Terminology

To understand CDN configuration requirements, you need to know these manifest types:

- **HLS manifests**:
  - _Multivariant playlist_: The top-level manifest that contains links to media playlists
  - _Media playlist_: The second-level manifest with links to content segments

- **DASH manifests**:

      + *MPD (Media Presentation Description)*: The standard term for DASH manifests

  This guide refers to all manifest files (multivariant playlists, media playlists, and
  MPDs) collectively as _manifests_ when discussing common
  configuration requirements.

For general CDN configuration principles that apply to all providers, see [Set up CDN integration with MediaTailor](cdn-configuration.md "cdn-configuration.md").

For CDN optimization guidance, see [Performance optimization guide for CDN and MediaTailor
integrations](cdn-optimization.md "cdn-optimization.md").

## Configure CDN caching rules

CDN caching configuration is critical for MediaTailor ad delivery because it determines how
your content reaches viewers. Proper configuration ensures that manifests remain
personalized for each viewer while segments are efficiently cached to reduce origin load
and improve performance.

This configuration typically takes 15-30 minutes per CDN provider and requires two
distinct behaviors:

- **Manifest handling:** Prevents caching to ensure
  each viewer receives personalized ad insertions
- **Segment caching:** Maximizes cache efficiency
  for video content to improve delivery performance

Follow these steps to configure your CDN's caching rules for optimal ad
delivery.

Choose your CDN provider from the following tabs for specific instructions:

Akamai
Configure these two behaviors in your Akamai property:

- Manifest handling to prevent caching
- Segment caching for optimal performance

###### Configure manifest delivery

Configure your Akamai CDN to avoid caching manifests so that each
viewer receives personalized ads.

Manifest files contain the personalized ad insertion points that MediaTailor
generates for each viewer. Caching these files would result in all viewers
seeing identical ads, defeating the purpose of personalized
advertising.

Follow these steps for manifest requests (files ending in .m3u8, .mpd, or
.smil):

1. Create a behavior to match manifest file extensions (.m3u8, .mpd,
   .smil)
2. Set **Caching Option** to **No
   Store**
3. Configure cache keys to include all query parameters
4. Enable **Forward Host Header** for proper origin
   routing
5. Configure header forwarding for all headers. For minimum
   requirements, see [Required headers for MediaTailor CDN
   integration](cdn-configuration.md#cdn-required-headers "cdn-configuration.md#cdn-required-headers").

###### Configure segment delivery

Configure your Akamai CDN to cache video segments to maximize CDN
efficiency and reduce origin load.

Video segments are the actual content files that can be safely cached
because they don't contain personalized information. Proper segment caching
reduces bandwidth costs and improves playback performance for
viewers.

Follow these steps for segment requests (files ending in .ts, .mp4, .m4s,
and so on):

1. Create a behavior to match segment file extensions (.ts, .mp4,
   .m4s)
2. Set **Honor Origin Cache Control** to
   **Yes**
3. Configure default time-to-live (TTL) settings for when origin
   headers are missing:
   - Default TTL: 86400 seconds (24 hours)
   - Maximum TTL: 604800 seconds (7 days)

###### Note

After configuring these behaviors, activate your property changes in
Akamai Control Center.

The changes take effect after activation.

Fastly
Create these two configurations in your Fastly service:

- Manifest handling to prevent caching
- Segment caching for optimal performance

###### Configure manifest delivery

Configure your Fastly CDN to bypass caching for manifest files so that
each viewer receives personalized ad content.

Manifest files must reach MediaTailor for each request to ensure proper ad
personalization. Bypassing the cache for these files ensures that each
viewer's unique targeting parameters are processed correctly.

Follow these steps for manifest requests:

1. Create a request condition to identify manifest paths
2. Set cache condition to **Do not cache** for these
   requests
3. Configure **Forward** settings to include all
   query parameters
4. Add `User-Agent` to your header forwarding
   configuration

###### Configure segment delivery

Configure your Fastly CDN to cache video segments to improve delivery
performance and reduce origin traffic.

Segment caching is essential for cost-effective delivery and optimal
viewer experience. These files are identical for all viewers and benefit
significantly from CDN caching.

Follow these steps for segment requests:

1. Create a request condition to identify segment paths
2. Set **Cache Settings** to **Honor origin
   cache headers**
3. Configure default time-to-live (TTL) to 86400 seconds (24 hours)
   for when origin headers are missing

###### Note

After making these changes, activate a new version of your Fastly
service.

The configuration takes effect after activation.

## Verify your CDN configuration

Verification ensures that your CDN configuration works correctly before you direct
production traffic through it. These tests confirm that ad personalization functions
properly and that caching provides the expected performance benefits.

Complete verification typically takes 10-15 minutes and should be performed from
multiple geographic locations if possible.

After setting up your CDN, perform these checks to verify it's working
correctly:

1. Test manifest personalization:
   1. Request the same content URL with different ad parameters
   2. Verify that each request returns different ad insertions

2. Test segment caching:
   1. Check CDN metrics for segment cache hit ratio (should be greater than
      90%)
   2. Monitor origin traffic to confirm it's lower than direct
      delivery

3. Test playback performance:
   1. Play content through your CDN from different locations
   2. Verify smooth playback with no buffering issues

For comprehensive testing methodologies and advanced validation procedures, see [Testing and validation
for CDN and MediaTailor integrations](cdn-integration-testing.md "cdn-integration-testing.md").

## Optimize CDN performance

After verifying your basic configuration, implement these optimizations to maximize
performance and minimize costs:

### Monitor key performance metrics

Track these metrics to ensure optimal performance:

Cache hit ratio

**Target:** Greater than 90% for video
segments

**Impact:** Higher ratios reduce origin
load and improve viewer experience

**Monitor:** Check your CDN provider's
analytics dashboard daily

Origin response time

**Target:** Less than 200ms for manifest
requests

**Impact:** Faster manifest delivery
reduces startup time for viewers

**Monitor:** Set up alerts for response
times exceeding 500ms

Error rates

**Target:** Less than 0.1% for all
requests

**Impact:** High error rates indicate
configuration issues or origin problems

**Monitor:** Set up alerts for error
rates exceeding 1%

### Fine-tune caching behavior

Adjust these settings based on your content characteristics and viewer
patterns:

Segment TTL optimization

**Live content:** Use shorter TTL (1-4
hours) to ensure timely updates

**VOD content:** Use longer TTL (24-48
hours) to maximize cache efficiency

**Ad segments:** Consider shorter TTL (30
minutes to 2 hours) for frequently updated ad content

For comprehensive TTL recommendations and caching strategies across
all MediaTailor workflows, see [Caching optimization for CDN and MediaTailor
integrations](cdn-optimize-caching.md "cdn-optimize-caching.md").

Geographic optimization

**Multi-region origins:** Configure
origin selection based on viewer location

**Edge locations:** Enable additional
edge locations in regions with high viewer concentration

**Failover:** Configure backup origins
for high availability

### Optimize costs

Implement these strategies to reduce CDN costs while maintaining
performance:

- **Compression:** Enable gzip compression for
  manifest files to reduce bandwidth usage
- **Purging strategy:** Implement selective
  cache purging instead of full cache clears
- **Traffic analysis:** Review traffic patterns
  monthly to identify optimization opportunities
- **Tier selection:** Use appropriate CDN
  service tiers based on your performance requirements

## Troubleshoot third-party CDN issues

CDN configuration issues typically manifest as either ad personalization problems or
performance degradation. Use this systematic approach to identify and resolve the most
common issues that affect MediaTailor ad delivery.

Most troubleshooting can be completed within 15-30 minutes by checking the specific
symptoms and applying the corresponding solutions.

If viewers experience problems with ad delivery or playback quality, use this guide to
identify and resolve common CDN configuration issues:

Akamai: Cached manifests

**Symptom:** Viewers see identical ads even
when you configure different targeting parameters.

**Solution:** Verify that you applied the
**No Store** caching option to manifest paths.

Also verify that you included query parameters in the cache key.

Fastly: Incorrect cache keys

**Symptom:** Viewers experience inconsistent
ad personalization.

Viewers might also see ads intended for other viewers.

**Solution:** Verify that you configured the
**Forward** settings to include all query parameters in
the cache key.

General: High origin traffic

**Symptom:** Your origin servers experience
unexpectedly high traffic

**Solution:** Verify segment caching settings
and time-to-live (TTL) values.

Check cache hit ratios in your CDN metrics.

General: Playback errors

**Symptom:** Viewers experience buffering or
playback failures

**Solution:** Check CDN routing rules and
origin health.

Verify that all required headers are being forwarded correctly.

###### Note

If these solutions don't resolve your issue, check your CDN provider's
documentation. You can also contact their support team for additional
troubleshooting steps.

For general CDN troubleshooting guidance, see [Troubleshoot issues with MediaTailor and CDN
integration](cdn-troubleshooting.md "cdn-troubleshooting.md").
