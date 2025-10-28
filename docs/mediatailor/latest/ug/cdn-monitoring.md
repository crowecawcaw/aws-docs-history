# Monitor MediaTailor CDN operations and performance

Effective monitoring of your AWS Elemental MediaTailor and content delivery network (CDN) integration
ensures reliable content delivery, optimal performance, and quick issue detection. This
monitoring approach applies to all MediaTailor implementations including server-side ad insertion
(SSAI), channel assembly, and combined workflows.

Monitoring your CDN integration enables you to:

- Detect and resolve issues before they impact viewers
- Track key performance indicators and maintain service quality
- Maintain optimal cache performance and reduce origin load
- Ensure ad insertion success rates meet business requirements
  For troubleshooting parameter-related issues that may appear in monitoring data, see [MediaTailor parameter troubleshooting
  guide](parameter-troubleshooting.md "parameter-troubleshooting.md"). For
  information about monitoring query parameter usage, see [MediaTailor manifest query parameters](manifest-query-parameters.md "manifest-query-parameters.md").

## Essential CDN performance

metrics

Track these core metrics to evaluate your CDN's effectiveness with MediaTailor
implementations:

Cache hit ratio

**What it measures**: The percentage of
requests served from the CDN cache versus from origin.

**Target values**:

- Content segments: 95% or higher cache hit ratio
- Ad segments: 90% or higher cache hit ratio
- Manifests: Varies by implementation (personalized manifests should
  not be cached)

**Why it matters**: Higher cache hit ratios
reduce origin load, improve response times, and lower bandwidth
costs.

Origin request volume

**What it measures**: The number of requests
reaching your MediaTailor origin servers.

**Target pattern**: Should remain low and
stable, with occasional spikes for cache misses or new content.

**Why it matters**: High origin request
volumes indicate caching inefficiencies and can impact MediaTailor
performance.

Response latency

**What it measures**: How quickly the CDN
responds to viewer requests.

**Target values**:

- Cached content: Less than 100ms (P95)
- Origin requests: Less than 500ms (P95)
- Manifest requests: Less than 100ms (P95)
- Segment requests: Less than 50ms (P95)

**Why it matters**: Low latency ensures
smooth playback and good viewer experience.

Error rates

**What it measures**: The percentage of
requests that result in HTTP errors.

**Target values**:

- 4xx errors: Less than 0.1% of total requests
- 5xx errors: Less than 0.01% of total requests
- Origin errors: Less than 0.05% of origin requests

**Why it matters**: High error rates indicate
configuration issues or service problems that impact viewer
experience.

### MediaTailor specific metrics

Monitor these MediaTailor metrics alongside CDN metrics for complete visibility:

Ad fill rates

**Key metrics**:
`Avail.FillRate` and
`AdDecisionServer.FillRate`

**Target values**: Above 90% for both
metrics

**Why it matters**: Directly impacts ad
revenue and viewer experience

Manifest generation performance

**Key metrics**:
`GetManifest.Latency` and
`GetManifest.Errors`

**Target values**: Latency under 200ms,
error rate under 1%

**Why it matters**: Affects playback
startup time and reliability

Ad decision server health

**Key metrics**:
`AdDecisionServer.Latency`,
`AdDecisionServer.Errors`, and
`AdDecisionServer.Timeouts`

**Target values**: Latency under 1000ms,
error rate under 5%, minimal timeouts

**Why it matters**: ADS performance
directly affects ad insertion success

## Set up monitoring tools

Configure these tools to monitor your MediaTailor and CDN integration effectively:

### Amazon CloudWatch integration

Amazon CloudWatch provides the foundation for monitoring your MediaTailor and CDN
integration:

MediaTailor metrics

MediaTailor automatically publishes metrics to CloudWatch that track requests,
responses, and errors. Key metrics include:

- `RequestCount`: Total number of requests to
  MediaTailor
- `ResponseTime`: MediaTailor response latency
- `4xxErrorCount` and `5xxErrorCount`:
  Error tracking

For a complete list of MediaTailor metrics, see [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch
metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md").

CDN metrics

Enable CDN metrics collection in CloudWatch including:

- Cache hit ratios for different content types
- Origin request counts and response times
- Error rates by status code

For CloudFront specific metrics, enable detailed monitoring in your
distribution settings.

### Dashboard configuration

Create dashboards that provide visibility into your MediaTailor and CDN
performance:

1. **Create a unified dashboard**: Combine MediaTailor
   and CDN metrics in a single CloudWatch dashboard for complete visibility.
2. **Organize by workflow**: Group metrics by
   implementation type (SSAI, channel assembly, or combined workflows).
3. **Include key performance
   indicators**:
   - Cache hit ratio trends over time
   - Response latency percentiles (P50, P95, P99)
   - Error rate trends and spikes

For detailed dashboard creation guidance, see [CloudWatch
dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

### Alert configuration

Configure alerts to detect issues before they impact viewers:

Critical alerts

Configure immediate alerts for severe issues:

- **High error rates**: Alert when
  5xx errors exceed 0.1% of requests over 5 minutes
- **Origin server issues**: Alert
  when origin response time exceeds 2 seconds
- **Cache hit ratio drops**: Alert
  when cache hit ratio falls below 70% for manifests or 85% for
  segments

Warning alerts

Configure early warning alerts for performance degradation:

- **Latency increases**: Alert when
  P95 response time exceeds 200ms
- **Cache efficiency decline**:
  Alert when cache hit ratio drops below 90% for segments

## Implementation checklist

Use this checklist to ensure comprehensive monitoring coverage:

1. **Metrics collection**:
   - ✓ MediaTailor metrics enabled in CloudWatch
   - ✓ CDN detailed monitoring enabled

2. **Dashboard setup**:
   - ✓ Unified CloudWatch dashboard created
   - ✓ Key metrics visualized with appropriate time ranges
   - ✓ Dashboard shared with relevant teams

3. **Alert configuration**:
   - ✓ Critical alerts configured with immediate notification
   - ✓ Warning alerts set up for early detection
   - ✓ Alert escalation procedures documented

4. **Operational procedures**:
   - ✓ Incident response procedures documented
   - ✓ Regular review schedule established
   - ✓ Team training completed

## Related topics

For additional guidance on specific monitoring scenarios:

- **Performance optimization**: For detailed
  optimization techniques based on monitoring data, see [CDN performance optimization](cdn-optimization.md "cdn-optimization.md").
- **Troubleshooting**: For detailed troubleshooting
  procedures using monitoring data, see your workflow-specific troubleshooting
  documentation.
- **Log analysis**: For comprehensive log analysis
  and monitoring, see [CDN integration log analysis and error code
  reference for MediaTailor](cdn-log-error-reference.md "cdn-log-error-reference.md").
