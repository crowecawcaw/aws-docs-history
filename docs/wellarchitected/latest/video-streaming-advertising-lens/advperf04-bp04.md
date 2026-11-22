

# ADVPERF04-BP04 Enable detailed performance and observability monitoring to tune queries and refine compute and storage

 Provide tools and metric granularity for performance debugging and compute and storage optimization, because of the low-latency requirements for advertising workloads. In programmatic advertising, infrastructure metrics alone are insufficient. Auction-level application metrics (bid timeout rate, auction completion rate, and win rate) reflect the business impact of database and container performance before user-facing degradation appears. 

 **Desired outcome:** 
+  Your engineering and operations teams have the metric granularity and tooling needed to identify performance bottlenecks, diagnose latency issues, and optimize database queries before they affect bid response times. 
+  Infrastructure metrics (database latency, container CPU) are correlated with auction-level application metrics (bid timeout rate, win rate, auction completion rate) so that teams understand the business impact of infrastructure changes, not just the infrastructure state. 
+  All alarm thresholds for bid path databases are defined relative to your RTB latency budget, not as generic absolute values. 

 **Common anti-patterns:** 
+  Relying on basic CloudWatch instance-level metrics for database and container workload monitoring, so query-level, process-level, and container-level signals go unseen. 
+  Waiting for user-facing latency degradation to trigger investigation rather than using ongoing observability. 
+  Setting database alarm thresholds at generic absolute values (for example, ReadLatency > 10ms) without reference to the RTB latency budget. 
+  Monitoring only infrastructure metrics while ignoring auction-level application signals (bid timeout rate, auction completion rate, win rate), which are the leading indicators of advertising performance degradation. 

 **Benefits of establishing this best practice:** 
+  Detailed observability at the database and container level compresses the time between a performance issue occurring and your team identifying and resolving its root cause. 
+  Correlating infrastructure metrics with auction-level business metrics lets teams distinguish a database latency spike that caused bid timeouts (revenue impact) from one that only affected reporting queries (no revenue impact), so they prioritize investigation correctly. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Standard Amazon CloudWatch metrics for RDS report at the hypervisor level, which can miss process-level contention and OS-level resource pressure that affect query latency. RDS Enhanced Monitoring collects metrics from an agent running directly on the DB instance, at intervals as short as one second. The one-second interval matters for advertising workloads because primetime traffic bursts last seconds to minutes, not hours. A five-minute CloudWatch default interval smooths over the spike. You see an average that looks acceptable while the bid path was saturated for 90 seconds during the peak. 

 Advertising databases have two separate query populations that require distinct observability strategies. Bid path databases serve high-frequency single-row lookups (user profile reads, frequency cap checks, audience segment membership) that must complete in single-digit milliseconds. Reporting and analytics databases serve complex joins and aggregations over large datasets that can tolerate hundreds of milliseconds. Performance Insights treats all queries in the same view. Without filtering by specific statement patterns, reporting query load can mask bid path regressions. For bid path databases, filter the top SQL view to the specific lookup queries on the auction critical path, not aggregate load across statement types. 

 [Amazon CloudWatch Container Insights](https://aws.amazon.com/cloudwatch/) collects and aggregates metrics from EKS clusters at pod, node, and namespace level. For advertising, Container Insights connects infrastructure signals (pod CPU saturation, memory pressure) to auction-level outcomes. A pod at 85% CPU running a bid evaluator is a latency risk, but the same load on a batch attribution pod is not. Overlay Container Insights metrics with application-level auction metrics to distinguish these cases. 

 A known gap in generic AWS monitoring for advertising is auction-level application metrics, which measure whether the infrastructure is serving the business outcome. Bid timeout rate is the direct leading indicator of database or compute latency exceeding the RTB budget. It counts the bid requests that exceed the auction deadline before a response returns. Auction completion rate (the fraction of auctions that complete with at least one valid bid) measures the downstream effect. Win rate by SSP adapter measures the quality of bids returned. Because AWS does not provide these metrics, publish them as CloudWatch custom metrics from the bidder application and correlate them with infrastructure metrics in the same dashboard. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable [Amazon RDS Enhanced Monitoring](https://aws.amazon.com/rds/) at one-second intervals for bid path databases:** In the RDS console, enable Enhanced Monitoring for advertising databases on the bid evaluation path with a monitoring interval of 1 second. The one-second granularity is necessary to detect sub-minute burst-spike saturation events that five-minute CloudWatch averages smooth over. Configure metrics to publish to CloudWatch Logs in the RDSOSMetrics log group. Use CloudWatch Logs Insights to query per-process CPU and I/O metrics when investigating slow query events correlated with bid timeout rate spikes. 

1.  **Enable [Amazon EKS](https://aws.amazon.com/eks/) Container Insights and overlay auction metrics on infrastructure dashboards:** Deploy the CloudWatch Container Insights DaemonSet on your EKS clusters. Create CloudWatch dashboards that display pod utilization and node capacity alongside application-level auction metrics: bid response latency, bid timeout rate, and auction completion rate. Infrastructure metrics without auction metrics provide incomplete signal: a pod at 85% CPU running a bid evaluator requires immediate action. The same metric on a batch attribution pod doesn't. 

1.  **Enable RDS Performance Insights and filter to bid path query patterns:** For Aurora and RDS databases in the bid evaluation path, enable Performance Insights. When investigating latency, filter the top SQL view to the specific high-frequency lookup statements that execute on the auction critical path (user profile reads by user ID, frequency cap checks by campaign and user ID, audience segment membership lookups). Don't rely on aggregate load across all statement types. Reporting queries can dominate the view and mask bid path regressions. 

1.  **Publish auction-level application metrics as CloudWatch custom metrics:** Instrument your bidder application to publish bid timeout rate, auction completion rate, and win rate by SSP adapter as CloudWatch custom metrics. Bid timeout rate is the primary leading indicator that database or compute latency has exceeded the RTB budget. Set alarms on bid timeout rate exceeding 1% as the operational threshold requiring investigation. At advertising scale, even a 1% timeout rate represents a significant volume of missed auctions. 

1.  **Configure CloudWatch alarms on database performance metrics relative to your RTB latency budget:** Set ReadLatency and WriteLatency alarms for bid path databases with thresholds proportional to your latency budget allocation. If your total RTB window is 100ms and database access is budgeted at 5ms, your ReadLatency alarm threshold is 5ms, not a generic value. Set alarms on DatabaseConnections before connection pool exhaustion, and CPUUtilization at 70% to investigate before saturation. For DynamoDB, set alarms on SuccessfulRequestLatency, ThrottledRequests, and ConsumedReadCapacityUnits. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Monitor real-time Amazon RDS OS metrics with flexible granularity using Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html) 
+  [Announcing Amazon CloudWatch Container Insights with Enhanced Observability for Amazon EKS on EC2](https://aws.amazon.com/blogs/mt/new-container-insights-with-enhanced-observability-for-amazon-eks/) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [RDS Performance Insights](https://aws.amazon.com/rds/performance-insights/) 