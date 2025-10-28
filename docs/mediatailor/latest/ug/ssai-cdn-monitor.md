# Monitor operations for CDN and MediaTailor integrations

AWS Elemental MediaTailor provides robust analytics capabilities that, when combined with content delivery
network (CDN) metrics, offer comprehensive insights into your SSAI implementation. This
topic covers:

For comprehensive CDN monitoring guidance including essential metrics, monitoring tools
setup, alert configuration, and troubleshooting strategies that apply to all MediaTailor
implementations, see [CDN monitoring](cdn-monitoring.md "cdn-monitoring.md").
This topic focuses on SSAI-specific monitoring requirements and ad insertion
analytics.

- Monitoring strategies for SSAI and CDN integration
- Analytics tools and data collection methods
- Data-driven optimization techniques

## Key metrics for SSAI with CDNs

To effectively monitor your SSAI implementation with CDNs, track these essential
metrics:

Ad insertion metrics

**Ad fill rate**: The percentage of ad
opportunities that were successfully filled with ads.

**Ad error rate**: The percentage of ad
requests that resulted in errors.

**Ad response time**: How long it takes for
the ad decision server to respond to ad requests.

**Ad duration accuracy**: How closely the
actual duration of inserted ads matches the expected duration.

Viewer experience metrics

**Rebuffering ratio**: The percentage of
viewing time spent buffering.

**Start-up time**: How long it takes for
video playback to begin.

**Ad transition smoothness**: How seamlessly
the player transitions between content and ads.

**Session duration**: How long viewers watch
before abandoning the stream.

## Analytics tools and integration

Combine these tools to create a comprehensive analytics solution for your SSAI
implementation:

AWS Elemental MediaTailor server-side metrics

MediaTailor provides built-in metrics through Amazon CloudWatch that track ad requests,
responses, and errors. These metrics can be viewed in the CloudWatch console or
integrated into custom dashboards.

Key MediaTailor metrics include:

- `AdDecisionServer.Ads`: The number of ads returned by
  the ad decision server.
- `AdDecisionServer.Duration`: The total duration of ads
  returned by the ad decision server.
- `AdDecisionServer.Errors`: The number of errors
  returned by the ad decision server.
- `AdDecisionServer.Latency`: The response time of the ad
  decision server.

For a complete list of MediaTailor metrics, see [Monitoring MediaTailor with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

CDN analytics

CDN providers offer detailed analytics on content delivery performance.
For Amazon CloudFront, use CloudWatch metrics and Amazon CloudFront access logs to analyze delivery
patterns.

Important CDN metrics to monitor:

- Request count by content type (manifests vs. segments)
- Cache hit ratio for different content types
- Geographic distribution of viewers
- Error rates by error code

Client-side tracking

Implement client-side tracking to gather viewer experience metrics that
aren't available server-side:

- Player events (play, pause, seek, buffer)
- Ad view completion rates
- Quality of service metrics (resolution changes, bitrate)
- Viewer engagement patterns

Consider using MediaTailor client-side tracking to collect and report these
metrics.

Integrated dashboards

Create comprehensive dashboards that combine metrics from multiple
sources:

- Use CloudWatch dashboards to combine MediaTailor and CloudFront metrics
- Consider third-party analytics platforms for more advanced
  visualization
- Set up cross-service correlation to identify relationships between
  metrics

## Implementing a monitoring

strategy

Follow these steps to implement a comprehensive monitoring strategy for your SSAI with
CDN implementation:

1. **Set up basic monitoring**
   - Enable CloudWatch metrics for MediaTailor
   - Configure CDN logging and metrics collection
   - Implement client-side tracking in your video player

2. **Create custom dashboards**
   - Build a CloudWatch dashboard that combines key metrics
   - Include visualizations for ad fill rate, CDN performance, and viewer
     experience
   - Add annotations for important events (configuration changes, major
     broadcasts)

3. **Configure alerts**
   - Set up CloudWatch alarms for critical metrics
   - Create composite alarms that trigger on multiple related
     conditions
   - Configure notification channels (email, SMS, Amazon SNS)

4. **Implement automated responses**
   - Use CloudWatch Events to trigger automated responses to common issues
   - Create runbooks for manual intervention when needed
   - Document troubleshooting procedures for different alert
     scenarios

###### Example Creating a comprehensive SSAI monitoring dashboard

This example shows how to create a CloudWatch dashboard that combines MediaTailor and CloudFront
metrics:

```
{
  "widgets": [
    {
      "type": "metric",
      "properties": {
        "metrics": [
          [ "AWS/MediaTailor", "AdDecisionServer.Ads", "Configuration", "your-config-name" ],
          [ ".", "AdDecisionServer.Errors", ".", "." ]
        ],
        "period": 300,
        "stat": "Sum",
        "region": "us-west-2",
        "title": "Ad Decision Server Performance"
      }
    },
    {
      "type": "metric",
      "properties": {
        "metrics": [
          [ "AWS/CloudFront", "Requests", "DistributionId", "your-distribution-id" ],
          [ ".", "4xxErrorRate", ".", "." ],
          [ ".", "5xxErrorRate", ".", "." ]
        ],
        "period": 300,
        "stat": "Average",
        "region": "us-east-1",
        "title": "CDN Performance"
      }
    }
  ]
}
```

## Data-driven optimization

Use the analytics data you collect to optimize your SSAI implementation:

CDN cache optimization

Analyze cache hit ratios to identify opportunities for improvement:

- Adjust TTL settings based on content type and update frequency.
  For detailed TTL recommendations, see [Step 1: Configure CDN caching for optimal ad
  delivery](configuring-ssai-cdn.md#configure-cdn-caching "configuring-ssai-cdn.md#configure-cdn-caching").
- Optimize cache key settings to improve cache efficiency
- Consider implementing origin shield for multi-layered
  caching

Ad delivery optimization

Use ad performance metrics to improve ad delivery:

- Identify and address common ad insertion errors
- Optimize ad decision server response times
- Adjust ad targeting parameters based on fill rate analysis

Viewer experience optimization

Improve the viewer experience based on client-side metrics:

- Analyze drop-off patterns during ad breaks
- Optimize ad transition points for smoother playback
- Adjust ad frequency and duration based on viewer engagement
  data

Cost optimization

Balance performance and cost considerations:

- Analyze bandwidth usage patterns to optimize CDN costs
- Consider price class adjustments for CloudFront distributions
- Evaluate the cost-benefit of different caching strategies

## Best practices

Follow these best practices for effective SSAI monitoring and analytics:

- **Establish baselines**: Collect metrics during
  normal operation to establish performance baselines that can be used for
  comparison during troubleshooting.
- **Implement multi-level monitoring**: Monitor at
  different levels of your architecture (origin, CDN, player) to get a complete
  picture of performance.
- **Correlate metrics across services**: Look for
  relationships between metrics from different services to identify root causes of
  issues.
- **Use anomaly detection**: Implement CloudWatch anomaly
  detection to automatically identify unusual patterns in your metrics.
- **Regularly review and refine**: Schedule regular
  reviews of your monitoring strategy and adjust based on changing requirements
  and new insights.
- **Document findings and actions**: Maintain a
  record of optimization efforts and their results to build institutional
  knowledge.

## Related information

For more information about monitoring and analytics for SSAI with CDNs, see:

- [Optimize performance for CDN and MediaTailor integrations](ssai-cdn-performance.md "ssai-cdn-performance.md")
  for performance optimization techniques
- [Troubleshoot MediaTailor SSAI with CDNs for
  uninterrupted ad delivery](troubleshooting-ssai-cdn.md "troubleshooting-ssai-cdn.md") for troubleshooting common
  issues
- [Monitoring MediaTailor with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md") for detailed information about MediaTailor
  metrics
- [Viewing CloudFront and edge function metrics](../../../AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.md "../../../AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.md") for information about
  CloudFront metrics
