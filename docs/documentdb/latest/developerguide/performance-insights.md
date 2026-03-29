# Monitoring with Performance Insights

Performance Insights adds to the existing Amazon DocumentDB monitoring features to illustrate your
cluster performance and help you analyze any issues that affect it. With the Performance
Insights dashboard, you can visualize the database load and filter the load by waits, query
statements, hosts, or application.

###### Note

Performance Insights is only available for Amazon DocumentDB 3.6, 4.0, and 5.0 instance-based clusters.

**How is it useful?**

- Visualize database performance — Visualize the load to determine when and
  where the load is on the database
- Determine what is causing load on database — Determine which queries,
  hosts, and applications are contributing to the load on your instance
- Determine when there is load on your database — Zoom in on the Performance
  Insights dashboard to focus on specific events or zoom out to look at trends across
  a larger time span
- Alert on database load — Access new database load metrics automatically
  from CloudWatch where you can monitor the DB load metrics alongside other Amazon DocumentDB
  metrics and set alerts on them
  **What are the limitations of Amazon DocumentDB Performance
  Insights?**

- Performance Insights in the AWS GovCloud (US-East) and AWS GovCloud (US-West) regions are not available
- Performance Insights for Amazon DocumentDB retains up to 7 days of performance
  data
- Queries longer than 1,024 bytes are not aggregated in Performance Insights

###### Topics

- [Performance Insights concepts](performance-insights-concepts.md "performance-insights-concepts.md")
- [Enabling and disabling Performance Insights](performance-insights-enabling.md "performance-insights-enabling.md")
- [Configuring access policies for Performance Insights](performance-insights-policies.md "performance-insights-policies.md")
- [Analyzing metrics with the Performance Insights dashboard](performance-insights-analyzing.md "performance-insights-analyzing.md")
- [Retrieving metrics with the Performance Insights API](performance-insights-metrics.md "performance-insights-metrics.md")
- [Amazon CloudWatch metrics for Performance Insights](performance-insights-cloudwatch.md "performance-insights-cloudwatch.md")
- [Performance Insights for counter metrics](performance-insights-counter-metrics.md "performance-insights-counter-metrics.md")
