

# Operational best practices
<a name="aurora-analytics-operational"></a>

**Topics**
+ [Handling instance restarts and failovers](#aurora-analytics-restarts-failovers)
+ [Setting up alarms](#aurora-analytics-alarms)

## Handling instance restarts and failovers
<a name="aurora-analytics-restarts-failovers"></a>

After a restart or failover, the on-disk cache starts empty, so the first queries run more slowly while they read from Amazon S3, and performance improves once the data is cached again. For latency-sensitive workloads, run a script of representative queries after a restart to populate the cache before production traffic resumes.

## Setting up alarms
<a name="aurora-analytics-alarms"></a>

Create Amazon CloudWatch alarms that signal resource pressure, so you are notified before queries fail. For proactive monitoring, watch the following metrics.
+ `AuroraAnalyticsMemoryUsage`: Memory consumed by foreign table queries. A rising value signals memory pressure and the risk of out-of-memory errors.
+ `AuroraAnalyticsCacheHitRatio`: The share of reads served from the on-disk cache. A falling value means more queries are re-reading from Amazon S3, often because the working set exceeds the cache.
+ `AuroraAnalyticsDiskSpillSize`: How much data queries are spilling to local storage. A rising value means queries are exceeding their `query_mem` and can benefit from more memory or tuning.
+ `FreeLocalStorage` (or `FreeEphemeralStorage` on NVMe instance classes): Local storage available for the cache and spill files. A falling value means the volume is filling up.

For the metric definitions, see [Monitoring and troubleshooting](aurora-analytics-monitoring-troubleshooting.md).

For how to create alarms, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.