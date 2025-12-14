# ADVOPS02-BP02 Collect and analyze detailed metrics for successful operations and ad campaigns

Advertising workloads can experience significant spikes in traffic
and resource utilization, which can impact performance and
availability. To maintain observability across these dynamic
workloads, collect granular, one-second metrics with near
real-time latency. Use advanced analytics, machine learning, and
anomaly detection to continuously analyze this data and
proactively identify issues before they impact campaigns. This
level of observability and proactive issue detection improves the
reliability and responsiveness of your advertising infrastructure,
even during periods of high demand.

## Implementation guidance

Consider the following for collecting important ad-serving
metrics:

- **Granular metrics:** Collect
  metrics at a one-second granularity to capture spikes and
  fluctuations in advertising workloads. Key metrics to
  monitor include:
  - **Bid requests per
    second:** Number of bid requests received.
  - **Bid response time:**
    Time taken to respond to bid requests.
  - **Successful bids:**
    Number of successful bids placed.
  - **Bid win rate:**
    Percentage of bids won compared to total bids placed.
  - **Latency metrics:**
    Measure network latency, processing time, and database
    query times.

For database metrics for RTB platforms:

- **Read and write latency:**
  Measure the time taken for read and write operations in your
  databases including
  [DynamoDB](../../../amazondynamodb/latest/developerguide/metrics-dimensions.md "../../../amazondynamodb/latest/developerguide/metrics-dimensions.md")
  and
  [Amazon RDS](../../../AmazonRDS/latest/UserGuide/rds-metrics.md "../../../AmazonRDS/latest/UserGuide/rds-metrics.md").
- **Throughput:** Monitor
  [read
  and write capacity units](../../../amazondynamodb/latest/developerguide/metrics-dimensions.md "../../../amazondynamodb/latest/developerguide/metrics-dimensions.md") to verify that your database
  can handle the load.
- **Error rates:** Track the
  number of failed read/write operations.
- **Connection count:** Monitor
  the number of
  [active
  connections](../../../AmazonRDS/latest/UserGuide/rds-metrics.md "../../../AmazonRDS/latest/UserGuide/rds-metrics.md") to the database.

Consider the following for effective analysis of ad serving
insights:

- **Anomaly detection:** Use
  Amazon CloudWatch anomaly detection to detect anomalies in
  your metrics based on historical data patterns
  automatically. This can help identify potential issues
  before they impact campaigns.

Create useful alarms for monitoring and alerting. Configure
CloudWatch alarms for critical metrics such as:

- **High latency:** Set alarms
  for when bid response times exceed a defined threshold (for
  example, 100ms).
- **Low bid win rate:**
  Initiate alerts if the bid win rate drops below a specific
  percentage.
- **Database latency:** Create alarms for read or write
  latency thresholds to ensure database performance.

Configure your notification mechanisms. Use Amazon Simple Notification Service (Amazon SNS) to send alerts to relevant
stakeholders using email or SMS when alarms go off. This makes
it possible for the appropriate teams to respond quickly to
potential issues.

Other important considerations for observability of advertising
workloads:

- **Impact on cost:**
  CloudWatch has charges for custom metrics, alarms, and API
  requests, which can add to the overall AWS costs. The cost
  can vary based on the number of metrics, alarms, and API
  calls configured. SNS has charges for the number of
  notifications sent, which can also contribute to the overall
  cost.
- **To reduce impact on cost:**
  Analyze the expected usage patterns and configure CloudWatch
  and SNS based on specific needs to optimize costs. Consider
  cost-optimized approaches, such as using sampling or
  aggregation for high-volume metrics, to reduce the number of
  custom metrics and API calls.
- **Impact on latency:** The
  monitoring and logging solutions recommended, when
  implemented correctly, should have minimal impact on the
  latency of your advertising workloads. CloudWatch provides
  near real-time data ingestion and processing, which helps in
  quickly detecting and diagnosing issues. However, it's
  important to verify that the monitoring and logging
  solutions are non-blocking and do not introduce additional
  latency in your critical advertising workflows.
- **To reduce impact on
  latency:** Implement monitoring and logging
  solutions using asynchronous, non-blocking approaches to
  minimize the impact on latency. Consider using sampling or
  batching techniques to reduce the number of API calls and
  optimize the performance of your monitoring and logging
  solutions.
- **Ad fraud metrics:** Monitor
  invalid traffic rates, bot detection rates, and suspicious
  activity patterns.
- **Brand safety metrics:**
  Track content classification accuracy, moderation response
  times, and policy violation rates.
- **Measurement consistency:**
  Monitor cross-system measurement discrepancies,
  attribution model performance, and conversion path
  integrity.

## Resources

- Set up
  [custom
  metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md") in CloudWatch
- [Monitoring
  metrics in an Amazon RDS instance](../../../AmazonRDS/latest/UserGuide/CHAP_Monitoring.md "../../../AmazonRDS/latest/UserGuide/CHAP_Monitoring.md")
- [Creating
  cross-service dashboards](../../../prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/cloudwatch-dashboards-visualizations.md "../../../prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/cloudwatch-dashboards-visualizations.md")
- [Aggregating
  metrics using CloudWatch](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md#publishingDataPoints1 "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md#publishingDataPoints1")
- [Analyzing
  performance anomalies with Amazon DevOps Guru for Amazon RDS](../../../AmazonRDS/latest/UserGuide/devops-guru-for-rds.md "../../../AmazonRDS/latest/UserGuide/devops-guru-for-rds.md")
