# Troubleshoot MediaTailor SSAI with CDNs for

uninterrupted ad delivery

This section provides solutions for common issues when using AWS Elemental MediaTailor dynamic ad
insertion with a content delivery network (CDN). These solutions will help you troubleshoot
problems with your video monetization through personalized advertising.

For comprehensive CDN troubleshooting guidance including cache performance issues, HTTP
error resolution, testing procedures, and diagnostic techniques that apply to all MediaTailor
implementations, see [Troubleshoot CDN integration](cdn-troubleshooting.md "cdn-troubleshooting.md"). This section focuses on SSAI-specific
troubleshooting requirements and ad insertion issues.

If you encounter issues with your CDN and SSAI setup, check these common problems:

Personalized advertising not appearing in stream

Verify that your ADS responds correctly and that AWS Elemental MediaTailor communicates with
it. Check these potential issues:

- Ad targeting query parameters not properly forwarded through your
  CDN
- Ad break points incorrectly defined in your content
- ADS connectivity or response problems

Playback errors at ad break points

Ensure that ad segments are properly transcoded to match your content bitrates
and resolutions. Check these common issues:

- CDN incorrectly routing requests for ad segments
- Manifest manipulation errors at transition points
- Mismatched encoding profiles between content and ads

Stale manifests

For live content, verify that your CDN cache TTL settings are appropriate. For
personalized manifests, use TTL of 0 seconds. Consider implementing cache
invalidation for rapidly changing manifests. For comprehensive TTL guidance, see [Caching optimization for CDN and MediaTailor
integrations](cdn-optimize-caching.md "cdn-optimize-caching.md").

High latency

Check your CDN configuration for optimal routing. Ensure that your CDN has
edge locations near your viewers for best performance.

## Advanced troubleshooting

For more complex issues, try these advanced troubleshooting techniques:

Inconsistent ad targeting behavior

Check for query parameter inconsistencies between player requests and ADS
requests. Ensure all required targeting parameters are properly passed
through the CDN.

CDN cache inconsistencies

Verify cache key configurations to ensure proper content differentiation.
Consider implementing cache purging for critical manifest updates.

Ad tracking failures

Check that beacon URLs are properly forwarded and not blocked by the CDN.
Verify that client players can reach the tracking endpoints.

## Performance optimization

To optimize the performance of your dynamic ad insertion and video monetization
workflow:

- Fine-tune TTL settings based on content type and viewer patterns. For detailed
  TTL recommendations, see [Caching optimization for CDN and MediaTailor
  integrations](cdn-optimize-caching.md "cdn-optimize-caching.md").
- Implement geographic routing to minimize latency for global audiences
- Consider using multiple CDNs for redundancy and optimal performance
- Monitor cache hit ratios and adjust configurations accordingly
- Optimize manifest manipulation processes to reduce processing time at ad break
  points
- Pre-transcode ads to match common content profiles for seamless personalized
  advertising insertion

### Performance benchmarks

When optimizing your AWS Elemental MediaTailor ad insertion CDN integration, aim for these
performance benchmarks:

Cache Hit Ratio Targets

Content segments: greater than 95% cache hit ratio

Ad segments: greater than 90% cache hit ratio

Manifests: Not applicable (should not be cached for personalized ad
insertion)

Latency Benchmarks

Manifest request latency: less than 100ms (P95)

Content segment delivery: less than 50ms (P95)

Ad segment delivery: less than 75ms (P95)

End-to-end startup time: less than 2 seconds

Origin Load Metrics

Origin requests per viewer: less than 0.1 requests per minute per
viewer

Origin bandwidth per viewer: less than 5% of total viewer
bandwidth

Error Rate Targets

Manifest errors: less than 0.1%

Segment errors: less than 0.01%

Player-reported rebuffering: less than 1%

Scalability Benchmarks

Support for 10 times the normal traffic during peak events without
degradation

Ability to handle greater than 1000 requests per second per
channel

Use Amazon CloudWatch metrics to track these performance indicators. For detailed
monitoring instructions, see [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch
metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md").

## Related information

For more information about ad insertion with CDNs, see:

Ad insertion documentation

[Getting started with MediaTailor ad
insertion](getting-started-ad-insertion.md "getting-started-ad-insertion.md") - Learn about ad
insertion concepts

[Setting up](setting-up.md "setting-up.md") - Get
started with ad insertion

CDN integration

[Set up CDN integration](cdn-configuration.md "cdn-configuration.md") - General CDN configuration guidance

[CloudFront
integration](cloudfront-specific-recommendations.md "cloudfront-specific-recommendations.md") -
CloudFront specific configuration

Channel assembly integration

[Channel assembly with CDN](ca-cdn-wflw.md "ca-cdn-wflw.md") - Learn
about channel assembly with CDNs

[Implement ad insertion](ca-cdn-setup-advanced.md "ca-cdn-setup-advanced.md") - Implement ad insertion
with channel assembly

Monitoring and optimization

[Monitor operations for CDN and MediaTailor integrations](ssai-cdn-monitor.md "ssai-cdn-monitor.md") -
Comprehensive monitoring and analytics

[Optimize performance for CDN and MediaTailor integrations](ssai-cdn-performance.md "ssai-cdn-performance.md") - Performance optimization guide

[Monitoring AWS Elemental MediaTailor with Amazon CloudWatch
metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md") - CloudWatch metrics for
MediaTailor
