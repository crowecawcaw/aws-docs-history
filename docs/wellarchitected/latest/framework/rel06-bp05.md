

# REL06-BP05 Analyze logs

 Analyzing accumulated log data reveals trends, recurring failure patterns, and slow regressions that no single alarm exposes. This analysis also requires a data-management strategy that retains logs long enough to be useful and controls storage cost. 

 **Desired outcome:** 
+  You analyze historical logs and metrics to find broader trends and recurring issues. 
+  You query log data across sources to investigate incidents and confirm root causes. 
+  Your log retention is governed by lifecycle policies that match your analytical and compliance needs. 
+  Your storage costs are controlled through tiering and expiration of aged log data. 

 **Common anti-patterns:** 
+  Teams collect logs but never analyze them for trends beyond the moment of an incident. 
+  Teams retain all log data indefinitely and absorb rising storage costs with no lifecycle policy. 
+  Teams delete logs too soon, which removes the history needed for trend and regression analysis. 
+  Teams store logs in formats or locations that make querying at scale impractical. 

 **Benefits of establishing this best practice:** 
+  You uncover long-term patterns and regressions that real-time monitoring misses. 
+  You investigate incidents faster by querying logs across many sources. 
+  You control storage cost by tiering and expiring data according to its value. 
+  You retain the history that compliance and post-incident analysis require. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Log analysis shows what has been changing over time and why the same incidents keep recurring. A latency regression that creeps up two percent a week never trips a static threshold. It is plainly visible when you query a month of history. Interactive query tools help you search and analyze this accumulated data. [Amazon CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) supports a purpose-built query language for data held in CloudWatch Logs. For very large datasets, route logs to Amazon S3 and query them with [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) across [many supported formats](https://docs.aws.amazon.com/athena/latest/ug/). At petabyte scale, an Amazon EMR cluster can run the analysis. For operational investigations, [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) performs natural-language log analysis. It finds patterns in high-volume log streams and correlates events with metrics and traces to surface root causes without manual queries. 

 AWS Partner and third-party products also handle aggregation, processing, storage, and analytics. The trade-off is integration effort against consistency with an existing observability stack. Whichever path you choose, system and application logs are generated differently across cloud providers and often across services. Normalize log formats before you analyze them together. 

 Decide how long each class of log is worth keeping, then enforce that decision with lifecycle policies rather than manual cleanup. Amazon S3 applies lifecycle management at the bucket level, and you can apply different rules to different paths within a bucket. Toward the end of a log's useful life, transition it to a lower-cost archival tier such as Amazon Glacier Flexible Retrieval. Expire it once the retention period ends. Where access patterns are unpredictable, the S3 Intelligent-Tiering storage class moves data to the most cost-effective tier automatically, with no performance impact or operational overhead. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Query logs interactively with CloudWatch Logs Insights:** Use [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) to search and analyze data held in CloudWatch Logs. Start from the [sample queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html) and adapt them to the components and behaviors specific to your workload. 

1.  **Route logs to Amazon S3 for large-scale analysis:** Send logs from CloudWatch Logs to Amazon S3, then query them with Amazon Athena. For a common case, see [how to analyze Amazon S3 server access logs with Athena](https://repost.aws/knowledge-center/analyze-logs-athena). 

1.  **Apply lifecycle policies to log storage:** Create an [S3 lifecycle policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html) for your log buckets that transitions aged data to archival storage and expires it after the retention period. Removing stale log files also reduces the data Athena scans on each query, which lowers query cost. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL06-BP02 Define and calculate metrics (Aggregation)](rel06-bp02.md) 
+  [REL06-BP06 Regularly review monitoring scope and metrics](rel06-bp06.md) 
+  [REL12-BP02 Perform post-incident analysis](rel12-bp02.md) 

 **Related documents:** 
+  [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) 
+  [Sample queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html) 
+  [What is Amazon Athena?](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) 
+  [Setting an S3 Lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html) 
+  [Use Athena to analyze Amazon S3 server access logs](https://repost.aws/knowledge-center/analyze-logs-athena) 
+  [Canaries and X-Ray tracing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html) 
+  [About AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) 

 **Related examples:** 
+  [The Amazon Builders' Library: Instrumenting distributed systems for operational visibility](https://builder.aws.com/content/3EuxPBdIiiUhB5IK47p3O3fxhy7/instrumenting-distributed-systems-for-operational-visibility) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/) 