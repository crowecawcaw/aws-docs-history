# Monitor REST API execution with Amazon CloudWatch metrics

You can monitor API execution by using CloudWatch, which collects and processes raw data from
API Gateway into readable, near-real-time metrics. These statistics are recorded for a
period of 15 months so you can access historical information and gain a better
perspective on how your web application or service is performing. By default,
API Gateway metric data is automatically sent to CloudWatch in one-minute periods. For more
information, see [What Is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_.

The metrics reported by API Gateway provide information that you can analyze in different ways.
The following list shows some common uses for the metrics that are suggestions to get you
started:

- Monitor the **IntegrationLatency** metrics to measure the
  responsiveness of the backend.
- Monitor the **Latency** metrics to measure the overall
  responsiveness of your API calls.
- Monitor the **CacheHitCount** and
  **CacheMissCount** metrics to optimize cache capacities to
  achieve a desired performance.

###### Topics

- [Amazon API Gateway dimensions and metrics](api-gateway-metrics-and-dimensions.md "api-gateway-metrics-and-dimensions.md")
- [View CloudWatch metrics with the API dashboard in API Gateway](how-to-api-dashboard.md "how-to-api-dashboard.md")
- [View API Gateway metrics in the CloudWatch console](metrics_dimensions_view_in_cloud_watch.md "metrics_dimensions_view_in_cloud_watch.md")
- [View API Gateway log events in the CloudWatch console](view-cloudwatch-log-events-in-cloudwatch-console.md "view-cloudwatch-log-events-in-cloudwatch-console.md")
- [Monitoring tools in AWS for API Gateway](monitoring_automated_manual.md "monitoring_automated_manual.md")
