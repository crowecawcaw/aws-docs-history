# Monitoring

| CMPERF_12: Have you implemented end-to-end monitoring and logging (between<br>edge, vehicle, and cloud) of your system along with notifications? |
| ------------------------------------------------------------------------------------------------------------------------------------------------ |
|                                                                                                                                                  |

**[CMPERF\_BP12.1] Monitoring, logging, and setting up notifications
are critical for maintaining the health, performance, and security of a system.**

AWS offers a comprehensive suite of tools to help with these tasks:

- Ensure that all services, applications, and resources report their metrics and
  logs.
- Regularly review and adjust your monitoring strategy to adapt to changes in your
  environment and application.
- Ensure that you're not just collecting data but also deriving actionable insights
  from it.
  **[CMPERF\_BP12.2] Implement device monitoring at the edge device
  (vehicle), data transmission monitoring, monitor cloud services, and log monitoring.**

As a general practice, establish alerts to monitor different workloads, applications,
database services, load balancers, and network monitoring. Notify site reliability
engineering (SRE) team once a certain threshold level is breached. These actions will help
to define KPIs such as round-trip time, and network latency between vehicle-cloud and
internal applications.

| CMPERF_13: Have you built the right dashboards and widgets for your prioritized<br>actionable insights? |
| ------------------------------------------------------------------------------------------------------- |
|                                                                                                         |

Building an effective dashboard involves focusing on the key
performance indicators (KPIs) that matter most to your
organization and displaying them in an easily understandable
and visually appealing way. 

**[CMPERF\_BP13.1] Follow best practices when creating
dashboards**

User-centric design:

- Tailor the dashboard to the needs of its primary users.
  Consider who will be using the dashboard and why.
- Use a clear, organized layout and meaningful naming
  conventions.
  Prioritize key metrics:

- Show the most important data points prominently, ensuring
  they are easily accessible and visible.
- Avoid cluttering the dashboard with non-essential metrics.
  Use appropriate visualizations:

- Choose the right type of graph or visualization based on
  the nature of the data. For instance, time-series data is
  best viewed with line charts.
  Interactive elements:

- Add interactive filters, drill-down capabilities, or
  time-span selectors to allow users to explore the data
  more deeply.
  Consistent refresh rates:

- Determine how frequently the dashboard needs updating.
  Some metrics might require real-time updates, while others
  might be daily or weekly.

Alerting:

- Integrate alert mechanisms, using services like Amazon SNS, to notify stakeholders of important events or
  thresholds.
  Feedback loop:

- Regularly gather feedback from users and iterate on the
  dashboard design and widgets.
  Tools such as dashboards, container insights, serverless insights, along with
  external tools such as Datadog can be used to build custom dashboards that can provide
  better insights. When you are running applications in containers or using serverless
  architectures, visibility into your workloads becomes paramount for optimizing performance,
  troubleshooting issues, and ensuring security. 

**[CMPERF\_BP13.2] Use tools and best practices to gain
insights**

- End-to-end visibility: Ensure that you're tracking the complete lifecycle of a
  request or a transaction across all components of your application.
- Alerts and alarms: Set up meaningful alerts and alarms based on the metrics and
  traces collected.
- Anomaly detection: Anomaly detection to create alarms that watch for anomalies in
  your metrics.
- Regularly review metrics and logs: Periodically review the metrics and logs, even
  if there's no issue, to understand the standard behavior of your applications.
- Security: Always monitor for security threats, especially
  in serverless applications where the application's
  perimeter might not be as defined.
- Cost optimization: Especially for serverless architectures, where you're billed
  for what you use, monitoring can also help in understanding the cost patterns and
  optimize.

Remember, while AWS provides the tools to monitor and gain
insights, it's the combination of these tools with best
practices that will give you the most valuable insights into
your container and serverless environments.
