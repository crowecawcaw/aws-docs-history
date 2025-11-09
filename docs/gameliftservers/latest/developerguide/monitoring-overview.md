# Monitoring Amazon GameLift Servers

Monitoring is an important part of maintaining the reliability,
availability, and performance of Amazon GameLift Servers and your other AWS solutions. There are three
primary uses for metrics with Amazon GameLift Servers: to monitor system health and set up alarms, to
track game server performance and usage, and to manage capacity using manual or
auto-scaling.

AWS provides the following monitoring tools to watch Amazon GameLift Servers, report when something is
wrong, and take automatic actions when appropriate:

- **Amazon GameLift Servers console** – Use the graphical
  interface to manage your Amazon GameLift Servers resources and track game hosting activity.
- **Server telemetry metrics** – Amazon GameLift Servers
  enables you to emit custom metrics directly from your game servers through SDK and plugin integration.
  You can define and track your own game-specific metrics alongside built-in performance, network, memory, and timing data.
  All metrics can be published to
  [Amazon Managed Service for Prometheus](../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md "../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md") and monitored in Amazon Grafana using fully customizable dashboards. You can also publish to Amazon CloudWatch for integration with other AWS services.
  The telemetry system is fully customizable - you can create custom Prometheus queries to derive additional metrics in addition to the built in ones.
  For implementation guides specific to your technology stack, see
  [Monitor with server telemetry metrics](monitoring-gamelift-servers-metrics.md "monitoring-gamelift-servers-metrics.md").
- **Amazon CloudWatch** – You can monitor Amazon GameLift Servers
  metrics in real time, as well as metrics for other AWS resources and applications
  that you're running on AWS services. Amazon CloudWatch offers a suite of monitoring
  features, including tools to create customized dashboards and the ability to set
  alarms that notify or take action when a metric reaches a specified
  threshold.
- **AWS CloudTrail** – captures all API calls and
  related events made by or on behalf of your AWS account for Amazon GameLift Servers and other
  AWS services. Data is delivered as log files to an Amazon S3 bucket that you specify.
  You can identify which users and accounts called AWS, the source IP address from
  which the calls were made, and when the calls occurred.
- **Game session logs** – You can output custom
  server messages for your game sessions to log files that are stored in Amazon S3.

## Metrics comparison across monitoring sources

Amazon GameLift Servers provides metrics through three primary sources: the Amazon GameLift Servers console Fleet Activity metrics, server telemetry metrics, and Amazon CloudWatch Amazon GameLift Servers metrics. Understanding the overlap and unique capabilities of each source helps you choose the right monitoring approach for your needs.

### Metrics availability by source

The following tables show which metrics are available across different monitoring sources, organized by metric category.

#### Instance metrics

Instance-level metrics for fleet capacity and health monitoring:

| Instance metrics availability | Metric | Console | CloudWatch | Telemetry |
| ----------------------------- | ------ | ------- | ---------- | --------- |
| Active instances              | ✓      | ✓       | ✓          |
| Idle instances                | ✓      | ✓       | ✓\*        |
| Percent idle instances        | ✓      | ✓       | ✓\*        |
| Desired instances             | ✓      | ✓       |            |
| Max instances                 | ✓      | ✓       |            |
| Min instances                 | ✓      | ✓       |            |
| CPU utilization               |        | ✓       | ✓          |
| Network in/out                |        | ✓       | ✓          |
| Disk/Storage read/write       |        | ✓       | ✓          |
| Instance interruptions        | ✓      | ✓       |            |
| Recycled instances            | ✓      | ✓       |            |
| Unhealthy instances replaced  |        | ✓       |            |

**\*** Available through custom Prometheus queries using telemetry data.

#### Game server metrics

Server process and game session metrics:

| Game server metrics availability     | Metric | Console | CloudWatch | Telemetry |
| ------------------------------------ | ------ | ------- | ---------- | --------- |
| Active game sessions                 | ✓      | ✓       | ✓\*        |
| Activating game sessions             | ✓      | ✓       |            |
| Available game sessions              | ✓      | ✓       |            |
| Percent available game sessions      | ✓      | ✓       |            |
| Concurrent activatable game sessions | ✓      | ✓       |            |
| Game session interruptions           | ✓      | ✓       |            |
| Active server processes              |        |         | ✓          |
| Healthy game servers                 |        |         | ✓          |
| Crashed game sessions                |        |         | ✓          |

**\*** Available through custom Prometheus queries using telemetry data.

#### Player usage metrics

Player session and concurrent user metrics:

| Player usage metrics availability | Metric | Console | CloudWatch | Telemetry |
| --------------------------------- | ------ | ------- | ---------- | --------- |
| Current player sessions           | ✓      |         |            |
| Player session activations        | ✓      |         |            |
| Global concurrent users (CCU)     |        |         | ✓          |
| Location concurrent users (CCU)   |        |         | ✓          |
| Location capacity                 |        |         | ✓          |

#### Container fleet metrics

Container-specific metrics (available only in CloudWatch for container fleets):

| Container fleet metrics availability | Metric | Console | CloudWatch | Telemetry |
| ------------------------------------ | ------ | ------- | ---------- | --------- |
| Active container groups              |        | ✓       | ✓          |
| Idle container groups                |        | ✓       | ✓          |
| Container CPU/Memory utilization     |        | ✓       | ✓          |
| Container network traffic            |        | ✓       | ✓          |
| Container storage operations         |        | ✓       | ✓          |

#### Choosing the right monitoring source

Select your monitoring approach based on your specific needs:

- **Use server telemetry metrics** to monitor comprehensive performance data from your game servers and emit custom metrics specific to your game. These metrics deliver detailed insights into server performance, network activity, memory usage, and timing data for all game engines and server SDKs. You can define custom metrics for gameplay events, business logic performance, and application-specific data points. All dashboards are fully customizable, and you can create custom Prometheus queries to derive additional metrics from the collected data. For more information, see [Monitor with server telemetry metrics](monitoring-gamelift-servers-metrics.md "monitoring-gamelift-servers-metrics.md").
- **Use the Amazon GameLift Servers console** for fleet management, capacity planning, and general operational oversight. The console provides an integrated view of fleet health and player activity. For more information, see [Manage game hosting resources with Amazon GameLift Servers](gamelift-console-intro.md "gamelift-console-intro.md").
- **Use Amazon CloudWatch** for automated monitoring, alerting, and integration with other AWS services. CloudWatch enables custom dashboards and alarm-based automation. For more information, see [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- **Use [Amazon Managed Service for Prometheus](../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md "../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md")** for high-performance metrics collection and storage with PromQL querying capabilities. Prometheus provides scalable time-series data storage for server telemetry metrics.
- **Use [Amazon Managed Grafana](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md")** for advanced visualization and fully customizable dashboarding. Grafana provides pre-built GameLift dashboards that you can customize and extend, plus supports creating entirely custom dashboards with multiple data sources. You can build custom queries and visualizations to track any metrics important to your game.
- **Use multiple sources** for comprehensive monitoring. Combine console oversight, server telemetry metrics, and automated alerting for complete visibility into your game hosting infrastructure.

For additional monitoring capabilities, you can also use:

- [Logging Amazon GameLift Servers API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md") – Track API calls and related events for auditing and compliance.
- [Logging server messages in Amazon GameLift Servers](logging-server-messages.md "logging-server-messages.md") – Capture custom server messages and game session logs.

### Topics

- [Manage game hosting resources with Amazon GameLift Servers](gamelift-console-intro.md "gamelift-console-intro.md")
- [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Monitor with server telemetry metrics](monitoring-gamelift-servers-metrics.md "monitoring-gamelift-servers-metrics.md")
- [Logging Amazon GameLift Servers API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Logging server messages in Amazon GameLift Servers](logging-server-messages.md "logging-server-messages.md")
