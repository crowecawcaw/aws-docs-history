

# Monitoring Amazon GameLift Servers
<a name="monitoring-overview"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon GameLift Servers and your other AWS solutions. There are three primary uses for metrics with Amazon GameLift Servers: to monitor system health and set up alarms, to track game server performance and usage, and to manage capacity using manual or auto-scaling. 

AWS provides the following monitoring tools to watch Amazon GameLift Servers, report when something is wrong, and take automatic actions when appropriate:
+ **Amazon GameLift Servers console** – Use the graphical interface to manage your Amazon GameLift Servers resources and track game hosting activity.
+ **Server telemetry metrics** – Amazon GameLift Servers enables you to emit custom metrics directly from your game servers through SDK and plugin integration. You can define and track your own game-specific metrics alongside built-in performance, network, memory, and timing data. All metrics can be published to [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html) and monitored in Amazon Grafana using fully customizable dashboards. You can also publish to Amazon CloudWatch for integration with other AWS services. The telemetry system is fully customizable - you can create custom Prometheus queries to derive additional metrics in addition to the built-in ones. For implementation guides specific to your technology stack, see [Monitor with server telemetry metrics](monitoring-gamelift-servers-metrics.md).
+ **Amazon CloudWatch** – You can monitor Amazon GameLift Servers metrics in real time, as well as metrics for other AWS resources and applications that you're running on AWS services. Amazon CloudWatch offers a suite of monitoring features, including tools to create customized dashboards and the ability to set alarms that notify or take action when a metric reaches a specified threshold.
+ **AWS CloudTrail** – captures all API calls and related events made by or on behalf of your AWS account for Amazon GameLift Servers and other AWS services. Data is delivered as log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred.
+ **Game session logs** – You can output custom server messages for your game sessions to log files that are stored in Amazon S3.

## Metrics comparison across monitoring sources
<a name="monitoring-metrics-comparison"></a>

Amazon GameLift Servers provides metrics through three primary sources: the Amazon GameLift Servers console Fleet Activity metrics, server telemetry metrics, and Amazon CloudWatch Amazon GameLift Servers metrics. Each source has unique capabilities. Server telemetry provides the deepest server-side and OS-level visibility, CloudWatch provides the broadest set of GameLift-side fleet, queue, and matchmaking metrics for alarming and automation, and the console surfaces fleet activity at a glance. The tables below show which metrics each source provides, organized by metric category.

### Metrics availability by source
<a name="metrics-overlap-analysis"></a>

In the tables below:
+ **Console** indicates the metric is displayed natively in the Amazon GameLift Servers console (for example, on a fleet's Activity, Scaling, or Locations tab, or in the fleets table).
+ **CloudWatch** indicates the metric is published to the `AWS/GameLift` namespace and can be graphed, alarmed on, or queried through CloudWatch.
+ **Telemetry** indicates the metric is collected by the Amazon GameLift Servers OpenTelemetry Collector and is available in management portal and the prebuilt dashboards. A **✓\*** means the metric is not emitted directly but can be derived through a custom PromQL query against the collected telemetry.

#### Instance metrics
<a name="instance-metrics-table"></a>

Instance-level capacity and lifecycle metrics:


**Instance metrics availability**  

| Metric | Console | CloudWatch | Telemetry | 
| --- | --- | --- | --- | 
| Active instances | ✓ | ✓ | ✓\* | 
| Idle instances | ✓ | ✓ | ✓\* | 
| Percent idle instances | ✓ | ✓ | ✓\* | 
| Desired instances | ✓ | ✓ |  | 
| Min instances | ✓ | ✓ |  | 
| Max instances | ✓ | ✓ |  | 
| Pending instances | ✓ | ✓ |  | 
| Terminating instances | ✓ | ✓ |  | 
| Instance Spot interruptions | ✓ | ✓ |  | 
| Recycled instances (Spot) | ✓ | ✓ |  | 
| Unhealthy instances replaced | ✓ | ✓ |  | 

#### Instance system and OS metrics
<a name="instance-system-metrics-table"></a>

Operating-system-level instance metrics. Server telemetry collects a much richer set of host metrics than CloudWatch, including detailed memory, filesystem, and network breakdowns. EC2 fleets emit a different set of host metrics than container fleets – container fleet metrics are listed under *Container fleet metrics* below.


**Instance system and OS metrics availability (managed EC2 fleets)**  

| Metric | Console | CloudWatch | Telemetry | 
| --- | --- | --- | --- | 
| CPU utilization | ✓ | ✓ | ✓ | 
| CPU time by state (user, system, idle, iowait) |  |  | ✓ | 
| CPU load average (1m, 5m, 15m) |  |  | ✓ | 
| Memory usage and utilization |  |  | ✓ | 
| Filesystem usage and utilization |  |  | ✓ | 
| Network in/out (bytes) | ✓ | ✓ | ✓ | 
| Network packets, errors, dropped |  |  | ✓ | 
| Active network connections |  |  | ✓ | 
| Disk read/write bytes | ✓ | ✓ | ✓ | 
| Disk read/write operations | ✓ | ✓ | ✓ | 
| Disk operation time and I/O time |  |  | ✓ | 
| Pending disk operations |  |  | ✓ | 
| Per-process CPU time |  |  | ✓ | 
| Per-process memory usage (resident, virtual) |  |  | ✓ | 

#### Game session and server process metrics
<a name="game-server-metrics-table"></a>

Game session counts and server process lifecycle metrics:


**Game session and server process metrics availability**  

| Metric | Console | CloudWatch | Telemetry | 
| --- | --- | --- | --- | 
| Active game sessions | ✓ | ✓ | ✓\* | 
| Activating game sessions | ✓ | ✓ |  | 
| Available game sessions (Game Capacity) | ✓ | ✓ | ✓ | 
| Percent available game sessions (Capacity Usage) | ✓ | ✓ | ✓ | 
| Concurrent activatable game sessions | ✓ | ✓ |  | 
| Game session Spot interruptions | ✓ | ✓ |  | 
| Active server processes | ✓ | ✓ | ✓ | 
| Healthy server processes | ✓ | ✓ | ✓ | 
| Percent healthy server processes | ✓ | ✓ | ✓ | 
| Server process activations | ✓ | ✓ |  | 
| Server process terminations | ✓ | ✓ |  | 
| Server process abnormal terminations | ✓ | ✓ |  | 
| Crashed game sessions |  |  | ✓ | 

#### Server performance metrics
<a name="server-performance-metrics-table"></a>

In-game server performance metrics emitted directly from the game server through the Amazon GameLift Servers SDKs and plugins. These are exclusive to server telemetry and are not available in the console or in CloudWatch.


**Server performance metrics availability**  

| Metric | Console | CloudWatch | Telemetry | 
| --- | --- | --- | --- | 
| Server delta time (and p50, p90, p95) |  |  | ✓ | 
| Server tick time (and p50, p90, p95) |  |  | ✓ | 
| Server tick rate |  |  | ✓ | 
| Server world tick time (and p50, p90, p95) |  |  | ✓ | 
| Server up status |  |  | ✓ | 
| Server connections |  |  | ✓ | 
| Server bytes in/out |  |  | ✓ | 
| Server packets in/out |  |  | ✓ | 
| Server packets lost in/out |  |  | ✓ | 

#### Player metrics
<a name="player-metrics-table"></a>

Player session and concurrent user metrics:


**Player metrics availability**  

| Metric | Console | CloudWatch | Telemetry | 
| --- | --- | --- | --- | 
| Current player sessions | ✓ | ✓ |  | 
| Available player sessions (max) | ✓ | ✓ |  | 
| Player session activations | ✓ | ✓ |  | 
| Concurrent users (CCU), global and per location |  |  | ✓ | 

#### Container fleet metrics
<a name="container-metrics-table"></a>

Metrics specific to managed container fleets. Server telemetry collects a richer set of network and storage breakdowns than CloudWatch, while CloudWatch tracks container group lifecycle counts that are not exposed by telemetry.


**Container fleet metrics availability**  

| Metric | Console | CloudWatch | Telemetry | 
| --- | --- | --- | --- | 
| Active game server container groups | ✓ | ✓ |  | 
| Idle game server container groups | ✓ | ✓ |  | 
| Pending game server container groups | ✓ | ✓ |  | 
| Terminating game server container groups | ✓ | ✓ |  | 
| Unhealthy game server container groups replaced | ✓ | ✓ |  | 
| Container CPU utilization | ✓ | ✓ | ✓ | 
| Container CPU usage by mode (kernel, user, system) |  |  | ✓ | 
| Container CPU reservation | ✓ | ✓ |  | 
| Container memory utilization | ✓ | ✓ | ✓ | 
| Container memory reservation | ✓ | ✓ | ✓ | 
| Container memory limit and max usage |  |  | ✓ | 
| Container network in/out (rate) | ✓ | ✓ | ✓ | 
| Container network packets in/out |  |  | ✓ | 
| Container network errors and dropped packets |  |  | ✓ | 
| Container storage read/write bytes | ✓ | ✓ | ✓ | 
| ECS task CPU usage (total, system) |  |  | ✓ | 
| ECS task memory utilized and reserved |  |  | ✓ | 
| ECS task network rate (rx, tx) |  |  | ✓ | 
| ECS task storage read/write bytes |  |  | ✓ | 

#### Player gateway metrics
<a name="player-gateway-metrics-table"></a>

Player gateway traffic and throttling metrics, available for managed container fleets that use a player gateway. Player gateway metrics are exclusive to CloudWatch (and visible in the console as CloudWatch widgets).


**Player gateway metrics availability**  

| Metric | Console | CloudWatch | Telemetry | 
| --- | --- | --- | --- | 
| Player gateway packets in/out | ✓ | ✓ |  | 
| Player gateway bytes in/out | ✓ | ✓ |  | 
| Player gateway packets throttled | ✓ | ✓ |  | 
| Player gateway bytes throttled | ✓ | ✓ |  | 
| Player gateway player sessions | ✓ | ✓ |  | 

#### Game session queue metrics
<a name="queue-metrics-table"></a>

Metrics for game session placement queues. Queue metrics are exclusive to CloudWatch (and visible in the console as CloudWatch widgets on the queue's Metrics tab).


**Queue metrics availability**  

| Metric | Console | CloudWatch | Telemetry | 
| --- | --- | --- | --- | 
| Average wait time | ✓ | ✓ |  | 
| Queue depth | ✓ | ✓ |  | 
| Game sessions placed | ✓ | ✓ |  | 
| First choice not viable | ✓ | ✓ |  | 
| First choice out of capacity | ✓ | ✓ |  | 
| Lowest latency placement |  | ✓ |  | 
| Lowest price placement |  | ✓ |  | 
| Placements started | ✓ | ✓ |  | 
| Placements succeeded | ✓ | ✓ |  | 
| Placements canceled | ✓ | ✓ |  | 
| Placements failed | ✓ | ✓ |  | 
| Placements timed out | ✓ | ✓ |  | 

#### FlexMatch matchmaking metrics
<a name="matchmaking-metrics-table"></a>

Metrics for FlexMatch matchmaking configurations and rule sets. Matchmaking metrics are exclusive to CloudWatch (and visible in the console as CloudWatch widgets on the matchmaking configuration's Metrics tab).


**Matchmaking metrics availability**  

| Metric | Console | CloudWatch | Telemetry | 
| --- | --- | --- | --- | 
| Current tickets | ✓ | ✓ |  | 
| Tickets started | ✓ | ✓ |  | 
| Tickets failed | ✓ | ✓ |  | 
| Tickets timed out | ✓ | ✓ |  | 
| Players started | ✓ | ✓ |  | 
| Matches created | ✓ | ✓ |  | 
| Matches accepted | ✓ | ✓ |  | 
| Matches rejected | ✓ | ✓ |  | 
| Matches placed | ✓ | ✓ |  | 
| Match acceptances timed out | ✓ | ✓ |  | 
| Matchmaking search time | ✓ | ✓ |  | 
| Time to match | ✓ | ✓ |  | 
| Time to ticket cancel | ✓ | ✓ |  | 
| Time to ticket success | ✓ | ✓ |  | 
| Rule evaluations passed |  | ✓ |  | 
| Rule evaluations failed |  | ✓ |  | 

#### Choosing the right monitoring source
<a name="monitoring-source-selection"></a>

Select your monitoring approach based on your specific needs:
+ **Use server telemetry metrics** to monitor comprehensive performance data from your game servers and emit custom metrics specific to your game. These metrics deliver detailed insights into server performance, network activity, memory usage, and timing data for all game engines and server SDKs. You can define custom metrics for gameplay events, business logic performance, and application-specific data points. All dashboards are fully customizable, and you can create custom Prometheus queries to derive additional metrics from the collected data. For more information, see [Monitor with server telemetry metrics](monitoring-gamelift-servers-metrics.md).
+ **Use the Amazon GameLift Servers console** for fleet management, capacity planning, and general operational oversight. The console provides an integrated view of fleet health and player activity. For more information, see [Manage game hosting resources with Amazon GameLift Servers](gamelift-console-intro.md).
+ **Use Amazon CloudWatch** for automated monitoring, alerting, and integration with other AWS services. CloudWatch enables custom dashboards and alarm-based automation. For more information, see [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md).
+ **Use [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html)** for high-performance metrics collection and storage with PromQL querying capabilities. Prometheus provides scalable time-series data storage for server telemetry metrics.
+ **Use [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html)** for advanced visualization and fully customizable dashboarding. Grafana provides pre-built GameLift dashboards that you can customize and extend, plus supports creating entirely custom dashboards with multiple data sources. You can build custom queries and visualizations to track any metrics important to your game.
+ **Use multiple sources** for comprehensive monitoring. Combine console oversight, server telemetry metrics, and automated alerting for complete visibility into your game hosting infrastructure.

For additional monitoring capabilities, you can also use:
+ [Logging Amazon GameLift Servers API calls with AWS CloudTrail](logging-using-cloudtrail.md) – Track API calls and related events for auditing and compliance.
+ [Logging server messages in Amazon GameLift Servers](logging-server-messages.md) – Capture custom server messages and game session logs.

### Topics
<a name="monitoring-topics"></a>
+ [Manage game hosting resources with Amazon GameLift Servers](gamelift-console-intro.md)
+ [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md)
+ [Monitor with server telemetry metrics](monitoring-gamelift-servers-metrics.md)
+ [Logging Amazon GameLift Servers API calls with AWS CloudTrail](logging-using-cloudtrail.md)
+ [Logging server messages in Amazon GameLift Servers](logging-server-messages.md)