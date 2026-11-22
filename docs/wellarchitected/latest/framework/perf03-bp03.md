

# PERF03-BP03 Collect and record data store performance metrics

 Without recorded metrics, slow queries and resource pressure in a data store stay invisible until they affect users. Metrics collected over time support data-driven tuning and confirm the store meets workload requirements. 

 **Desired outcome:** 
+  You have a performance baseline that describes normal behavior for each data store. 
+  You collect both underlying system metrics and data store metrics continuously. 
+  You detect and diagnose abnormal patterns quickly from recorded data. 
+  You use collected metrics to guide optimization decisions. 

 **Common anti-patterns:** 
+  Teams search log files manually to find performance data. 
+  Teams publish metrics only to their own tools and lack a complete view of the workload. 
+  Teams collect only the default metrics their monitoring tool records. 
+  Teams review metrics only after an incident. 
+  Teams monitor system-level metrics but capture no data access or usage metrics. 
+  Teams examine only default-resolution metrics and miss short spikes visible at high resolution. 

 **Benefits of establishing this best practice:** 
+  A baseline makes normal behavior explicit, so deviations stand out. 
+  Faster diagnosis reduces the duration and impact of performance incidents. 
+  Metric-driven tuning replaces guesswork with evidence. 
+  Anomaly detection surfaces problems before users report them. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A performance baseline records how a data store behaves under normal load. Build it by collecting metrics over a period long enough to capture daily and weekly cycles. 

 Capture metrics from both the underlying system and the data store. System-layer metrics include CPU utilization, memory, available disk storage, disk I/O, cache hit ratio, and network traffic. Data-store metrics include transactions per second, top queries, average query rates, response times, index usage, table locks, query timeouts, and open connections. System metrics show whether the host is saturated. Data store metrics show whether the workload is efficient. 

 *Resolution* determines whether a metric captures short-lived spikes. Default-resolution metrics smooth over bursts that high-resolution metrics expose. *Retention* determines how far back you can look. Longer retention supports trend analysis and capacity planning at higher storage cost. Match retention to your operational and security requirements. 

 As data stores multiply, manual thresholds stop scaling. Statistical and machine learning-based detection learns the baseline and flags deviations automatically. [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) collects metrics across your architecture and supports custom metrics for business or derived signals. Services such as [Amazon RDS Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.html) and [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) add engine-specific and machine learning-based analysis. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify the key metrics for each data store:** For every store in the workload, list the system metrics and the store-specific metrics that matter, using the monitoring reference for that engine. Cover both resource consumption and data access patterns so that you see efficiency as well as saturation. 

1.  **Establish a performance baseline:** Collect the identified metrics over a period long enough to capture normal daily and weekly variation. Record this baseline as the reference for what normal looks like, and revisit it after major workload changes. 

1.  **Collect metrics centrally and set alarms:** Use an approved monitoring solution such as [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to gather metrics across resources, and publish custom metrics for business or derived signals. Set alarms on the metrics that predict user impact, and route alerts to the owning teams. 

1.  **Add advanced and anomaly-based monitoring:** Enable engine-specific and machine learning-based detection with tools such as [Amazon RDS Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.html) and [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) to surface problems that fixed thresholds miss. 

1.  **Choose the right metric resolution:** Select high-resolution metrics where short spikes affect the workload, and default resolution where longer-term trends are enough. Confirm that the resolution captures the events you need to diagnose. 

1.  **Configure retention to match your goals:** Set data retention for [CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) and [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) to satisfy your operational and security requirements without paying for storage you will not analyze. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF03-BP02 Evaluate available configuration options for data store](perf03-bp02.md) 
+  [PERF03-BP04 Implement strategies to improve query performance in data store](perf03-bp04.md) 
+  [PERF05-BP05 Review metrics at regular intervals](perf05-bp05.md) 

 **Related documents:** 
+  [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) 
+  [Default data retention for CloudWatch Logs](https://aws.amazon.com/cloudwatch/faqs/#Log_management) 

 **Related workshops:** 
+  [AWS purpose-built databases workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 