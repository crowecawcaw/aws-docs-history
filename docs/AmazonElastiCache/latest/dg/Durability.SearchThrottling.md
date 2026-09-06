

# Search write throttling
<a name="Durability.SearchThrottling"></a>

To maintain optimal performance and data durability, ElastiCache in **durable mode** implements write throttling on search traffic when necessary. Throttling helps ensure that automatic backup mechanisms operate effectively without falling behind during periods of high write activity. By temporarily reducing write throughput, the system preserves the integrity of the Multi-AZ transactional log, which is essential for fast database recovery and restart.

## Scope of throttling
<a name="Durability.SearchThrottling.Scope"></a>

Only write commands targeting keys that belong to a search index are throttled. Writes to non-indexed keys and all read commands are **not** affected.

The following commands are subject to throttling when they target indexed keys:


**Commands subject to search write throttling**  

| Category | Commands | 
| --- | --- | 
| Hash | HSET, HSETNX, HMSET, HINCRBY, HINCRBYFLOAT, HDEL | 
| JSON | JSON.SET, JSON.DEL, JSON.NUMINCRBY, JSON.NUMMULTBY, JSON.STRAPPEND, JSON.ARRAPPEND, JSON.ARRINSERT, JSON.ARRPOP, JSON.ARRTRIM, JSON.TOGGLE, JSON.CLEAR, JSON.MERGE | 
| Generic | DEL, UNLINK, RENAME, RENAMENX, COPY, RESTORE | 

## What clients experience
<a name="Durability.SearchThrottling.ClientExperience"></a>

Throttled commands are **delayed, not rejected**. Affected writes take longer to complete but still succeed. No errors are returned to the client.

You can observe the impact through the following Amazon CloudWatch metrics:
+ `SuccessfulWriteRequestLatency` and `SearchBasedSetCmdsLatency` — Reflect increased latency on affected writes.
+ `SearchWriteThrottleActive`, `SearchWriteThrottledClientsCount`, and `SearchWriteThrottleEvents` — Indicate whether throttling is active and to what degree. See [Monitoring](#Durability.SearchThrottling.Monitoring) for details.

## When throttling activates
<a name="Durability.SearchThrottling.Activation"></a>

The system monitors CPU usage of the search module's writer threads over a rolling 2-hour window. Throttling activates when the average CPU usage during that window exceeds 50%, and adjusts the allowed write rate to bring average utilization back to 50%.

Because the metric is averaged over a 2-hour window, short bursts of elevated CPU usage do not trigger throttling on their own — as long as they are offset by lower usage within the same window.

To prevent over-throttling, the system also evaluates current CPU usage in real time. If current CPU usage is already at 50% or below, the system holds the write rate steady rather than reducing it further, even if the 2-hour average remains above the threshold. This ensures that write capacity never falls below 50% of normal throughput.

## When throttling deactivates
<a name="Durability.SearchThrottling.Deactivation"></a>

Once the 2-hour average CPU usage drops below 50%, the system gradually increases the allowed write rate until full throughput is restored and throttling deactivates.

## Monitoring
<a name="Durability.SearchThrottling.Monitoring"></a>

The following Amazon CloudWatch metrics are available for monitoring search write throttling:


**Search write throttling CloudWatch metrics**  

| Metric | Description | Unit | 
| --- | --- | --- | 
| SearchWriteThrottleActive | Indicates whether throttling is currently active. 1 = active, 0 = inactive. | Boolean | 
| SearchWriteThrottledClientsCount | The number of client connections currently being throttled. | Count | 
| SearchWriteThrottleEvents | The number of throttle events within the reporting interval. | Count | 
| SearchWriteCPUUtilization | Current CPU utilization of the search writer threads. | Percent | 

## Best practices
<a name="Durability.SearchThrottling.BestPractices"></a>
+ **Monitor `SearchWriteCPUUtilization`** — Track your search write CPU usage to understand your workload patterns and anticipate when you might approach the throttling threshold.
+ **Monitor `SearchWriteThrottleActive`** — Track whether throttling is active so you can investigate and respond promptly.
+ **Plan sustained ingestion around the 2-hour window** — The system uses a 2-hour rolling average, so short bursts of high write activity are fully supported as long as they are offset by lower usage within the same window.
+ **Scale your cluster if you observe sustained or frequent throttling** — If your workload consistently exceeds the threshold and throttling impacts your application's latency requirements, consider scaling to add capacity.