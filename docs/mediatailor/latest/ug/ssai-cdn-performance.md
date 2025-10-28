# Optimize performance for CDN and MediaTailor integrations

Maximize the performance of your AWS Elemental MediaTailor ad insertion implementation by optimizing your
content delivery network (CDN) configuration. These settings ensure efficient content
delivery and optimal viewer experience.

For detailed caching and routing optimization guidance specific to SSAI implementations,
see [CDN performance optimization](cdn-optimization.md "cdn-optimization.md"). The
consolidated optimization guide provides comprehensive caching settings, request routing
configuration, and performance benchmarks that apply to all MediaTailor CDN integrations.

## Common performance challenges

SSAI implementations with CDNs can face several performance challenges:

Manifest manipulation overhead

MediaTailor performs real-time manifest manipulation, which can introduce
latency if not optimized properly. The following can introduce
latency:

- Processing time for ad decision server (ADS) requests
- Time required to modify manifests with ad segment
  references
- Additional processing for personalization

Cache efficiency issues

Personalized manifests can reduce CDN cache efficiency because:

- Each viewer may receive a unique manifest
- Session parameters can fragment the cache
- Dynamic content requires careful cache configuration

Origin load spikes

Improper caching can lead to origin load spikes during:

- High-traffic events
- Cache refreshes
- CDN configuration changes

Ad-related playback issues

Ad insertion can cause playback disruptions such as:

- Buffering during ad transitions
- Quality differences between content and ads
- Playback failures when ads cannot be retrieved

For comprehensive performance optimization guidance including caching strategies, request
routing, performance benchmarks, and advanced optimization techniques, see [CDN performance optimization](cdn-optimization.md "cdn-optimization.md"). The consolidated
optimization guide provides detailed settings and benchmarks that apply to all MediaTailor CDN
integrations, including SSAI implementations.

## Best practices summary

Follow these best practices to ensure optimal SSAI performance with CDNs:

Architecture best practices

- Choose the right architectural pattern for your scale and
  requirements
- Deploy services in close proximity to minimize latency
- Implement redundancy for critical components

Caching best practices

- Use different caching strategies for different content
  types
- Optimize cache keys to balance personalization and
  efficiency
- Set appropriate TTLs based on content type and update frequency.
  For detailed TTL recommendations, see [Caching optimization for CDN and MediaTailor
  integrations](cdn-optimize-caching.md "cdn-optimize-caching.md").

Ad delivery best practices

- Optimize ADS interactions with timeouts and fallbacks
- Prepare ads to match content specifications
- Implement efficient ad segment delivery

Monitoring best practices

- Monitor all components of your SSAI implementation
- Set up alerts for performance degradation
- Regularly review and optimize your configuration

## Complete optimization guidance

For comprehensive CDN optimization guidance including detailed caching strategies,
request routing configuration, performance benchmarks, and advanced optimization
techniques, see [CDN performance optimization](cdn-optimization.md "cdn-optimization.md"). The consolidated optimization guide provides complete settings and benchmarks that
apply to all MediaTailor CDN integrations, including SSAI implementations.
