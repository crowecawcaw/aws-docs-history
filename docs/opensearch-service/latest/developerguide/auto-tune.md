# Auto-Tune for Amazon OpenSearch Service

Auto-Tune in Amazon OpenSearch Service uses performance and usage metrics from your OpenSearch cluster to
suggest memory-related configuration changes, including queue and cache sizes and Java
virtual machine (JVM) settings on your nodes. These optional changes improve cluster speed
and stability.

Some changes deploy immediately, while others are scheduled during your domain's off-peak
window. You can revert to the default OpenSearch Service settings at any time. As Auto-Tune gathers and
analyzes performance metrics for your domain, you can view its recommendations in the OpenSearch Service
console on the **Notifications** page.

Auto-Tune is available in commercial AWS Regions on domains running any OpenSearch
version, or Elasticsearch 6.7 or later, with a [supported instance type](supported-instance-types.md "supported-instance-types.md").

## Types of changes

Auto-Tune has two broad categories of changes:

- Nondisruptive changes that it applies as the cluster runs.
- Changes that require a [blue/green deployment](managedomains-configuration-changes.md "managedomains-configuration-changes.md"), which it applies during the domain's off-peak
  window.

Based on your domain's performance metrics, Auto-Tune can suggest adjustments to the
following settings:

| Change type                   | Category      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| JVM heap size                 | Blue/green    | By default, OpenSearch Service uses 50% of an instance's RAM for the JVM heap,<br>up to a heap size of 32 GiB.<br>Increasing this percentage gives OpenSearch more memory, but leaves<br>less for the operating system and other processes. Larger values can<br>decrease the number of garbage collection pauses, but increase the<br>length of those pauses.                                                                                                                                                                                                                                                        |
| JVM young generation settings | Blue/green    | JVM "young generation" settings affect the frequency of minor<br>garbage collections. More frequent minor collections can decrease<br>the number of major collections and pauses.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Queue size                    | Nondisruptive | By default, the search queue size is `1000` and the<br>write queue size is `10000`. Auto-Tune automatically<br>scales the search and write queues if additional heap is available<br>to handle requests.                                                                                                                                                                                                                                                                                                                                                                                                              |
| Cache size                    | Nondisruptive | The *field cache<br>• monitors on-heap data<br>structures, so it's important to monitor the cache's use. Auto-Tune<br>scales the field data cache size to avoid out of memory and circuit<br>breaker issues.<br>The *shard request cache<br>• is managed at the<br>node level and has a default maximum size of 1% of the heap.<br>Auto-Tune scales the shard request cache size to accept more search<br>and index requests than what the configured cluster can<br>handle.                                                                                                                                          |
| Request size                  | Nondisruptive | By default, when the aggregated size of in-flight requests<br>surpasses 10% of total JVM (2% for `t2` instance types<br>and 1% for `t3.small`), OpenSearch throttles all new<br>`_search` and `_bulk` requests until the<br>existing requests complete.<br>Auto-Tune automatically tunes this threshold, typically between<br>5-15%, based on the amount of JVM that is currently occupied on the<br>system. For example, if JVM memory pressure is high, Auto-Tune might<br>reduce the threshold to 5%, at which point you might see more<br>rejections until the cluster stabilizes and the threshold<br>increases. |

## Monitoring Auto-Tune changes

You can monitor Auto-Tune statistics in Amazon CloudWatch. For a full list of
metrics, see [Auto-Tune
metrics](managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-autotune-metrics "managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-autotune-metrics").

OpenSearch Service sends Auto-Tune events to Amazon EventBridge. You can use EventBridge to configure rules that send
an email or perform a specific action when an event is received. To see the format of
each Auto-Tune event sent to EventBridge, see [Auto-Tune events](monitoring-events.md#monitoring-events-autotune "monitoring-events.md#monitoring-events-autotune").
