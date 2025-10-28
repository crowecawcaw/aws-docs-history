# Performance benchmarks for CDN and MediaTailor

integrations

When optimizing your AWS Elemental MediaTailor CDN integration, aim for these performance benchmarks.
These targets apply to all MediaTailor implementations including SSAI, channel assembly, and
combined workflows:

Cache Hit Ratio Targets

Content segments: greater than 95% cache hit ratio

Ad segments: greater than 90% cache hit ratio

Manifests: Not applicable for SSAI (should not be cached for personalized
ad insertion); 85%+ for channel assembly

Latency Benchmarks

Manifest request latency: less than 100ms (P95)

Content segment delivery: less than 50ms (P95)

Ad segment delivery: less than 75ms (P95)

End-to-end startup time: less than 2 seconds

Origin Load Metrics

Origin requests per viewer: less than 0.1 requests per minute per
viewer

Origin bandwidth per viewer: less than 5% of total viewer bandwidth

Error Rate Targets

Manifest errors: less than 0.1%

Segment errors: less than 0.01%

Player-reported rebuffering: less than 1%

Scalability Benchmarks

Support for 10 times the normal traffic during peak events without
degradation

Ability to handle greater than 1000 requests per second per channel

Use Amazon CloudWatch metrics to track these performance indicators. For detailed monitoring
instructions, see [Set up monitoring tools](cdn-monitoring.md#cdn-monitor-tools-setup "cdn-monitoring.md#cdn-monitor-tools-setup").
