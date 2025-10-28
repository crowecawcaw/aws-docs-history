# Optimize CDN performance and resolve

latency issues for MediaTailor

AWS Elemental MediaTailor content delivery network (CDN) integration performance directly impacts
viewer experience and ad delivery quality. If you experience slow response times or
performance degradation:

## Performance measurement

techniques

Before troubleshooting performance issues, establish baseline measurements and
ongoing monitoring:

1. Measure key performance metrics:
   - **Response times:** Manifest requests
     should complete within 200ms, segment requests within 100ms
   - **Cache hit ratios:** Content
     segments >95%, ad segments >90%
   - **Origin request volume:** Should be
     less than 5% of total requests when cache is optimized
   - **Time to first frame:** Initial
     playback should start within 2-3 seconds

2. Use performance measurement tools:
   - **CDN analytics dashboards:** Monitor
     cache performance, response times, and error rates
   - **CloudWatch metrics:** Track MediaTailor
     service metrics including GetManifest.Latency
   - **Browser developer tools:** Measure
     client-side performance and network timing
   - **Command-line tools:** Use curl with
     timing options to measure specific requests

3. Implement continuous monitoring:
   - Set up automated performance alerts for response time
     degradation
   - Monitor performance across different geographic regions
   - Track performance during peak traffic periods
   - Compare performance metrics before and after configuration
     changes

**Performance measurement resources:**

- For comprehensive performance monitoring setup, see [Monitor MediaTailor CDN operations and performance](cdn-monitoring.md "cdn-monitoring.md")
- For performance testing procedures, see [Testing and validation
  for CDN and MediaTailor integrations](cdn-integration-testing.md "cdn-integration-testing.md")
- For CloudWatch metrics and monitoring, see [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch
  metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md")

## CDN cache performance

issues

Cache performance problems are among the most common CDN integration issues. These
problems affect all MediaTailor implementations and can significantly impact viewer
experience and costs.

**Low cache hit ratio**

**Symptoms**: High origin request volume,
increased latency, higher bandwidth costs, poor viewer experience

**Target values**:

- Content segments: 95% or higher cache hit ratio
- Ad segments: 90% or higher cache hit ratio
- Manifests: Varies by implementation (personalized manifests
  should not be cached)

**Common causes**:

- Incorrect TTL settings for different content types
- Cache key configuration includes unnecessary query
  parameters
- Cache-control headers from origin not properly
  configured
- Frequent cache invalidations or purges
- Geographic distribution issues (content not cached at edge
  locations)

**Solutions**:

1.  Review and optimize TTL settings:

        * Content segments: Set TTL to match segment duration or
         longer
        * Ad segments: Set TTL to 24 hours or longer for
         reusable ads
        * Static assets: Set TTL to 24 hours or longer

    For comprehensive TTL recommendations and caching optimization
    strategies, see [Caching optimization for CDN and MediaTailor
    integrations](cdn-optimize-caching.md "cdn-optimize-caching.md").

2.  Optimize cache key configuration:
    - Remove unnecessary query parameters from cache
      keys
    - Ensure only content-affecting parameters are
      included
    - Normalize parameter order and case sensitivity

3.  Verify origin cache-control headers are properly set
4.  Implement origin shield (or equivalent CDN functionality) for
    high-traffic implementations. Origin shield functionality is
    available across major CDNs but might have different names (such
    as CloudFront Origin Shield, Fastly Shield, Cloudflare Argo Tiered
    Cache). If your CDN doesn't offer this functionality, it can be
    enabled in MediaTailor when you contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").
5.  Review cache invalidation strategies and reduce unnecessary
    purges

**Validation steps**:

1. Monitor cache hit ratios using CDN analytics dashboards
2. Test specific URLs with curl to verify cache headers
3. Compare origin request volume before and after changes

**High origin request volume**

**Symptoms**: Unexpectedly high number of
requests reaching MediaTailor origin, increased origin server load, higher
costs

**Expected pattern**: Origin requests
should be less than 5% of total viewer requests when cache hit ratios
are optimal

**Common causes**:

- Cache misses due to low TTL values
- Cache key fragmentation (too many unique cache keys)
- Geographic traffic spikes in regions without cached
  content
- Frequent cache invalidations

**Solutions**:

1. Analyze request patterns to identify cache miss causes
2. Optimize TTL settings based on content type and update
   frequency
3. Implement cache warming strategies for new content
4. Consider origin shield implementation (available across major
   CDNs with different names - see [Origin Shield implementation](cdn-advanced-optimization.md#origin-shield-optimization "cdn-advanced-optimization.md#origin-shield-optimization") for
   details)

**Alert threshold**: Set alerts when
origin requests exceed 10% of total requests or increase by 50% over
baseline

## Common HTTP error resolution

HTTP errors in CDN integrations often indicate configuration issues or service
problems. These error patterns are consistent across all MediaTailor
implementations.

**404 Not Found errors**

**Symptoms**: Manifest or segment
requests return HTTP 404, players fail to load content,
"MANIFEST_LOAD_ERROR" in player logs

**Common causes**:

- Incorrect CDN origin configuration (wrong MediaTailor endpoint
  URL)
- Missing or incorrect cache behavior path patterns
- URL rewriting issues in CDN configuration
- MediaTailor configuration name or playback endpoint errors
- Timing issues with live content (requesting future
  segments)

**Diagnostic steps**:

1. Test the same URL directly against MediaTailor origin (bypass
   CDN)
2. Verify CDN origin configuration matches MediaTailor playback
   endpoint
3. Check CDN cache behavior path patterns and precedence
4. Review CDN access logs for request routing details
5. Validate MediaTailor configuration name and region settings

**Solutions**:

- Correct CDN origin configuration to match MediaTailor playback
  endpoint
- Update cache behavior path patterns to properly route
  requests
- Fix URL rewriting rules if applicable
- Verify MediaTailor configuration exists and is active

**403 Forbidden errors**

**Symptoms**: Requests return HTTP 403,
access denied messages, authentication failures

**Common causes**:

- Missing or incorrect query parameters required by MediaTailor
- CDN not forwarding required headers or parameters
- IP address restrictions or geographic blocking
- Authentication token issues (if using signed URLs)

**Solutions**:

- Verify all required query parameters are included and
  forwarded
- Check CDN configuration for header and parameter
  forwarding
- Review IP restrictions and geographic settings
- Validate authentication tokens and signing processes

**400 Bad Request errors**

**Symptoms**: Requests return HTTP 400,
malformed request errors, parameter validation failures

**Common causes**:

- Malformed query parameters or URL encoding issues
- Invalid parameter values or formats
- Missing required parameters for specific MediaTailor features
- URL length limitations exceeded

**Solutions**:

- Validate query parameter formats and URL encoding
- Check parameter values against MediaTailor API requirements
- Ensure all required parameters are included
- Review URL length and consider parameter optimization

**5xx Server errors**

**Symptoms**: Requests return HTTP 500,
502, 503, or 504 errors, intermittent service failures

**Common causes**:

- MediaTailor service issues or capacity limitations
- CDN origin connectivity problems
- Timeout issues due to slow origin responses
- Temporary service degradation

**Solutions**:

- Check AWS Service Health Dashboard for MediaTailor service
  status
- Verify CDN origin connectivity and timeout settings
- Implement retry logic with exponential backoff
- Monitor MediaTailor CloudWatch metrics for service health
- Contact AWS Support if issues persist

1.  Measure baseline performance:
    - Test manifest request response times directly to MediaTailor (target:
      <200ms)
    - Measure CDN response times for manifest requests (target: <100ms
      for cache hits)
    - Check segment loading times from both origin and CDN

2.  Analyze CDN performance:

        * Check cache hit ratios for content segments (target: >80% for
         popular content)
        * Verify origin shield (or equivalent CDN functionality) is enabled and
         configured in the same AWS Region as your origin. Different CDNs use
         different names for this functionality
        * Monitor CDN edge location performance and geographic
         distribution

    **Performance benchmarks:**

- Monitor manifest generation response times and compare against your baseline
  performance
- CDN cache hits are significantly faster than origin requests
- ADS response times should not cause manifest generation delays
  **Additional troubleshooting resources:**

- For comprehensive performance optimization strategies, see [Performance optimization guide for CDN and MediaTailor
  integrations](cdn-optimization.md "cdn-optimization.md")
- For origin shield implementation details, see [Origin Shield implementation](cdn-advanced-optimization.md#origin-shield-optimization "cdn-advanced-optimization.md#origin-shield-optimization")
- For CDN caching optimization, see [Caching optimization for CDN and MediaTailor
  integrations](cdn-optimize-caching.md "cdn-optimize-caching.md")
- For performance monitoring and metrics, see [Monitor MediaTailor CDN operations and performance](cdn-monitoring.md "cdn-monitoring.md")
- For performance testing procedures, see [Testing and validation
  for CDN and MediaTailor integrations](cdn-integration-testing.md "cdn-integration-testing.md")
  **Success criteria:** When resolved, response times
  should meet target benchmarks (manifests less than 200ms, segments less than 100ms),
  cache hit ratios should exceed 90% for most content types, and origin request volume
  should be less than 5% of total requests. Performance should be consistent across all
  geographic regions and device types.
