# Set up monitoring and scaling for CDN and MediaTailor integrations

Effective monitoring and scaling strategies are crucial for maintaining optimal
performance and viewer experience with your AWS Elemental MediaTailor content delivery network (CDN) integration. Implement these approaches to ensure your CDN
integration performs reliably at scale.

Implement these monitoring and scaling strategies that follow:

1.  Configure monitoring for these key metrics. For guidance on appropriate target
    values, see [Monitoring MediaTailor with Amazon CloudWatch](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md") and consult your CDN provider's best
    practices:

        * CDN cache hit ratios (establish baseline metrics and targets based on
         your content type and delivery patterns)
        * Origin request volumes (monitor patterns during normal operation to
         establish baselines for anomaly detection)
        * Error rates by error type (define thresholds based on your service
         level objectives and MediaTailor best practices)
        * Response times (set appropriate latency targets based on your viewer
         experience requirements and geographic distribution)

    For detailed implementation instructions, see [Creating CloudWatch dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") to visualize your MediaTailor and
    CDN metrics together.

2.  Set up alerts for unexpected traffic patterns or performance degradation.
    Configure thresholds based on your baseline metrics and service level
    objectives. For guidance on setting up alerts, see [Creating Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md"). Consider monitoring:

        * Significant deviations from baseline cache hit ratios (typically alert
         when falling under 85-90%)
        * Sudden increases in origin request volume (alert on 30% or greater
         increase from baseline)
        * Error rate spikes exceeding your defined thresholds (typically 1-2%
         for 4xx errors, 0.5% for 5xx errors)
        * Response time degradation beyond acceptable levels (typically >500ms
         for manifests, >200ms for segments)

    For implementation examples, see [CloudWatch concepts](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md") for creating effective monitoring dashboards
    and alerts.

3.  Create scaling plans for predictable high-traffic events. Your plans should
    include these key elements:

        * Pre-event capacity increases (24-48 hours before event start)
        * Gradual viewer ramp-up schedules (typically 10-20% of expected
         audience per 5-minute interval)
        * Regional capacity distribution based on audience (allocate capacity
         proportionally to expected regional viewership)
        * Post-event scaling procedures (maintain peak capacity for 30-60
         minutes after event conclusion)

    For implementation guidance on scaling for high-traffic events, see [Setting up a resilient end-to-end live workflow](https://aws.amazon.com/blogs/media/part-1-how-to-set-up-a-resilient-end-to-end-live-workflow/ "https://aws.amazon.com/blogs/media/part-1-how-to-set-up-a-resilient-end-to-end-live-workflow/") on the AWS Media
    Blog.

4.  Implement failover and redundancy measures for critical streams,
    including:

        * Multi-region CDN deployments (at least two regions for critical
         content)
        * Backup origin servers (configured with automated health checks every
         30 seconds)
        * Automated failover triggers based on health checks (typically after
         2-3 failed checks)
        * Recovery procedures for different failure scenarios (documented with
         specific response time targets)

    For detailed implementation steps, see [Optimizing high availability with CloudFront origin
    failover](../../../AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.md "../../../AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.md").
