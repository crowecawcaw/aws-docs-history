# Monitor performance for MediaPackage, CDN, and MediaTailor

integrations

AWS Elemental MediaTailor requires effective monitoring to maintain optimal performance of your AWS Elemental MediaPackage
and content delivery network (CDN) integration. This topic provides guidance on key metrics
to track, monitoring tools to use, and how to set up alerts for proactive issue
detection.

Before setting up monitoring, ensure your basic integration is working correctly. If you
haven't completed your basic content delivery network integration setup, start with [Integrate MediaTailor with MediaPackage and CDN](mediapackage-integration.md "mediapackage-integration.md") . If you
need to troubleshoot issues identified through monitoring, see [CDN integration
troubleshooting](cdn-emp-troubleshooting.md "cdn-emp-troubleshooting.md")..

## Key performance metrics

Monitor these essential metrics to ensure optimal performance of your MediaPackage and CDN
integration:

### CDN performance metrics

For comprehensive CDN performance metrics including cache hit ratio targets,
origin request volume monitoring, and response time benchmarks, see [Performance benchmarks for CDN and MediaTailor
integrations](cdn-performance-benchmarks.md "cdn-performance-benchmarks.md") in the CDN optimization guide.

Key EMP-specific considerations for CDN metrics:

**EMP cache-control headers**

**What to verify**: Ensure your CDN
honors EMP's cache-control headers for optimal TTL behavior

**Expected behavior**: Different content
types should have different cache durations based on EMP's
headers

For detailed guidance on EMP cache optimization, see [Optimize CDN caching for MediaTailor and MediaPackage content
delivery](cdn-emp-caching.md "cdn-emp-caching.md").

**Query parameter impact**

**What to monitor**: Track how
EMP-specific query parameters affect cache efficiency

**Optimization target**: Ensure only
necessary EMP query parameters are included in cache keys

**CDN response times**

**What to monitor**: Track response times
for different content types (manifests vs. segments).

**Target values**:

- Cached content: less than 100ms
- Origin requests: less than 500ms

### MediaPackage performance metrics

**Error rates**

**What to monitor**: Monitor HTTP error
rates from both your CDN and MediaPackage endpoints. Pay particular attention
to 4xx errors, which might indicate configuration issues.

**Key error codes**:

- 400 errors: Often related to manifest filtering issues
- 404 errors: Might indicate routing or configuration
  problems
- 504 errors: Timeout issues, especially with LL-HLS

**Request volume and patterns**

**What to monitor**: Track request
patterns to MediaPackage endpoints to identify usage trends and capacity
needs.

**Patterns to watch**:

- Peak usage times
- Geographic distribution of requests
- Content type distribution (live vs. on-demand)

### Latency metrics

**End-to-end latency**

**What to monitor**: For LL-HLS
implementations, monitor end-to-end latency from content ingest to
viewer playback. High latency might indicate CDN configuration
issues.

**Target values**:

- LL-HLS: less than 3 seconds glass-to-glass latency
- Regular HLS: less than 30 seconds

**Manifest generation time**

**What to monitor**: Time taken by MediaPackage
to generate manifests, especially with filtering applied.

**Target values**: less than 200ms for
manifest generation

## Monitoring tools and setup

Setting up comprehensive monitoring tools is essential for maintaining optimal
performance and quickly identifying issues before they impact viewers. Without proper
monitoring, performance degradation, cache inefficiencies, or integration problems might
go unnoticed until viewers experience poor playback quality. The right monitoring setup
provides visibility into all aspects of your MediaPackage and CDN integration.

Use these AWS services and tools to monitor your MediaPackage and CDN integration:

### Amazon CloudWatch

Amazon CloudWatch provides the foundation for monitoring your MediaPackage and CDN integration by
collecting and storing metrics from both services. Proper CloudWatch configuration ensures
you have the data needed to identify performance trends, troubleshoot issues, and
optimize your integration. Without CloudWatch metrics, you'll lack visibility into system
performance and might not detect issues until they become critical.

Set up CloudWatch monitoring for comprehensive metrics collection:

1. **MediaPackage metrics**: Enable CloudWatch metrics for
   your MediaPackage endpoints to track request volumes, error rates, and response
   times.
2. **CDN metrics**: Configure CloudWatch to collect
   CloudFront metrics including cache hit ratios, origin request counts, and error
   rates.
3. **Custom metrics**: Create custom metrics for
   business-specific KPIs like viewer engagement or content popularity.

### CloudWatch dashboards

Create comprehensive dashboards to visualize your metrics:

1. **Overview dashboard**: High-level metrics
   showing overall system health
2. **CDN performance dashboard**: Detailed CDN
   metrics including cache performance and geographic distribution
3. **MediaPackage performance dashboard**:
   MediaPackage-specific metrics including request patterns and error rates
4. **Latency dashboard**: End-to-end latency
   metrics for different content types and regions

### Log analysis

Set up log analysis for detailed troubleshooting:

1. **CDN access logs**: Enable and analyze CDN
   access logs to understand request patterns and identify issues
2. **MediaPackage CloudWatch logs**: Monitor MediaPackage logs for
   errors and performance issues
3. **Log aggregation**: Use Amazon CloudWatch Logs
   Insights or third-party tools to analyze log patterns

## Set up alerts and notifications

Alert configuration is crucial for proactive issue detection and resolution. Without
proper alerts, issues might go unnoticed until they significantly impact viewer
experience or cause service disruptions. Well-configured alerts help you identify and
address problems before they affect your viewers, and ensure your team is notified of
critical issues that require immediate attention.

Configure proactive alerts to identify issues before they impact viewers:

### Critical alerts

Set up immediate alerts for critical issues:

- **High error rates**: Alert when 4xx or 5xx
  error rates exceed 5% over a 5-minute period
- **Cache hit ratio drops**: Alert when cache
  hit ratio falls below 70% for manifests or 85% for segments
- **High latency**: Alert when end-to-end
  latency exceeds target thresholds
- **Origin request spikes**: Alert when origin
  requests increase by more than 50% compared to baseline

### Warning alerts

Set up warning alerts for trends that might indicate developing issues:

- **Gradual performance degradation**: Alert
  when response times increase by 20% over a 30-minute period
- **Cache efficiency trends**: Alert when cache
  hit ratios show declining trends over time
- **Unusual traffic patterns**: Alert for
  unexpected changes in request volume or geographic distribution

## Use monitoring data for optimization

Leverage monitoring data to continuously improve performance:

### Regular performance reviews

1. **Weekly reviews**: Analyze weekly
   performance trends and identify optimization opportunities
2. **Monthly capacity planning**: Use traffic
   patterns to plan for capacity needs and CDN optimization
3. **Quarterly architecture reviews**: Evaluate
   overall architecture efficiency and identify areas for improvement

### Common optimization actions

Based on monitoring data, consider these optimization actions:

- **Cache policy adjustments**: Modify TTL
  values based on actual content update patterns. For detailed TTL
  optimization guidance, see [Caching optimization for CDN and MediaTailor
  integrations](cdn-optimize-caching.md "cdn-optimize-caching.md").
- **Geographic optimization**: Add CDN edge
  locations in regions with high traffic
- **Query parameter optimization**: Remove
  unnecessary query parameters that fragment cache
- **Origin shield configuration**: Implement
  origin shield in regions with high origin request volumes

For detailed monitoring guidance specific to MediaPackage, see [Monitoring MediaPackage](../../../mediapackage/latest/ug/monitoring.md "../../../mediapackage/latest/ug/monitoring.md") in the MediaPackage user
guide.
