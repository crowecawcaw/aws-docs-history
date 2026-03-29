# Amazon DocumentDB serverless scaling configuration

###### Topics

- [Choosing the scaling capacity range for a DocumentDB serverless cluster](#docdb-serverless-scaling-capacity-choosing "#docdb-serverless-scaling-capacity-choosing")
- [Choosing the MinCapacity setting for a DocumentDB serverless cluster](#docdb-serverless-scaling-mincapacity-choosing "#docdb-serverless-scaling-mincapacity-choosing")
- [Choosing the MaxCapacity setting for a DocumentDB serverless cluster](#docdb-serverless-scaling-maxcapacity-choosing "#docdb-serverless-scaling-maxcapacity-choosing")
- [Avoiding out-of-memory errors](#docdb-serverless-scaling-mem-errors "#docdb-serverless-scaling-mem-errors")
- [Why is my serverless instance not scaling down?](#docdb-serverless-scaling-down "#docdb-serverless-scaling-down")

## Choosing the scaling capacity range for a DocumentDB serverless cluster

Before adding any DocumentDB serverless instances to an Amazon DocumentDB cluster, the cluster must also have the `ServerlessV2ScalingConfiguration` parameter set.

The `ServerlessV2ScalingConfiguration` parameter consists of two values which define the serverless scaling capacity range of any serverless instance in the cluster:

- **`MinCapacity`** — The minimum scaling capacity of any DocumentDB serverless instances in the cluster.
- **`MaxCapacity`** — The maximum scaling capacity of any DocumentDB serverless instances in the cluster.

## Choosing the `MinCapacity` setting for a DocumentDB serverless cluster

It's tempting to always choose 0.5 for `MinCapacity`.
That value allows the instance to scale down to the smallest capacity when it's completely idle, while remaining active.
However, depending on how you use that cluster and the other settings that you configure, a different minimum capacity might be the most effective.
Consider the following factors when choosing the minimum capacity setting:

- The scaling rate for a DocumentDB serverless instance depends on its current capacity.
  The higher the current capacity, the faster it can scale up.
  If you need the instance to quickly scale up to a very high capacity, consider setting the minimum capacity to a value where the scaling rate meets your requirement.
- If you typically modify the instance class of your instances in anticipation of especially high or low workload, you can use that experience to make a rough estimate of the equivalent DocumentDB serverless capacity range.
  To determine the memory size of a provisioned Amazon DocumentDB instance type, see [Instance limits](limits.md#limits.instance "limits.md#limits.instance").

For example, suppose that you use the `db.r6g.xlarge` instance class when your cluster has a low workload.
That instance class has 32 GiB of memory.
Thus, you can specify a `MinCapacity` of 16 to set up a serverless instance that can scale down to approximately that same capacity.
That's because each DCU corresponds to approximately 2 GiB of memory.
You might specify a somewhat lower value to let the instance scale down further in case your `db.r6g.xlarge` instance was sometimes underutilized.

- If your application works most efficiently when the instances have a certain amount of data in the buffer cache, consider specifying a minimum DCU setting where the memory is large enough to hold the frequently accessed data.
  Otherwise, some data is evicted from the buffer cache when the serverless instances scale down to a lower memory size.
  Then when the instances scale back up, the information is read back into the buffer cache over time.
  If the amount of I/O to bring the data back into the buffer cache is substantial, it might be more effective to choose a higher minimum DCU value.
  For more information, see [Instance sizing](best_practices.md#best_practices-instance_sizing "best_practices.md#best_practices-instance_sizing").
- If your DocumentDB serverless instances run most of the time at a particular capacity, consider specifying a minimum capacity setting that's lower than that baseline, but not too much lower.
  Serverless instances can most effectively estimate how much and how fast to scale up when the current capacity isn't drastically lower than the required capacity.
- If your provisioned workload has memory requirements that are too high for small instance classes such as T3 or T4g, choose a minimum DCU setting that provides memory comparable to an R5 or R6g instance.
- In particular, we recommend the following minimum `MinCapacity` for use with the specified features (these recommendations are subject to change):
  - Performance Insights — 2 DCUs

- In Amazon DocumentDB, replication occurs at the storage layer, so reader capacity doesn't directly affect replication.
  However, for DocumentDB serverless reader instances that scale independently, make sure that the minimum capacity is sufficient to handle workloads during write-intensive periods to avoid query latency.
  If reader instances in promotion tiers 2–15 experience performance issues, consider increasing the cluster's minimum capacity.
  For details on changing whether reader instances scale along with the writer or independently, see [Viewing and modifying the promotion tier of serverless readers](docdb-serverless-managing.md#docdb-serverless-promo-tier "docdb-serverless-managing.md#docdb-serverless-promo-tier").

If you have a cluster with DocumentDB serverless reader instances, the readers don't scale along with the writer instance when the promotion tier of the readers isn't 0 or 1.
In that case, setting a low minimum capacity can result in excessive replication lag.
That's because the readers might not have enough capacity to apply changes from the writer when the database is busy.
We recommend that you set the minimum capacity to a value that represents a comparable amount of memory and CPU to the writer instance.

- The time it takes for a DocumentDB serverless instance to scale from its minimum capacity to its maximum capacity depends on the difference between its minimum and maximum DCU values.
  When the current capacity of the instance is large, DocumentDB serverless scales up in larger increments than when the instance starts from a small capacity.
  Thus, if you specify a relatively large maximum capacity and the instance spends most of its time near that capacity, consider increasing the minimum DCU setting.
  That way, an idle instance can scale back up to maximum capacity more quickly.
- Certain instance limits are determined by the serverless instance’s current capacity, such as connections limit, cursor limit, and open transactions limit.
  If the instance’s current capacity is small, then the limits will correspondingly also be small.
  If these limits are an issue when your serverless instance is scaled down to its `MinCapacity` value, then consider increasing `MinCapacity` to a higher value.
  For more information, see [Amazon DocumentDB serverless instance limits](docdb-serverless-instance-limits.md "docdb-serverless-instance-limits.md").
- Furthermore, certain instance limits are capped at a lower maximum value if the `MinCapacity` is set to less than or equal to 1.0 DCUs, such as active connections limit, cursor limit, and open transactions limit.
  If these capped limits are insufficient for your workload, please use a `MinCapacity` value of at least 1.5 DCUs.
  For more information, see [Amazon DocumentDB serverless instance limits](docdb-serverless-instance-limits.md "docdb-serverless-instance-limits.md").

For instructions on how to modify a cluster’s scaling configuration, see [Managing Amazon DocumentDB serverless](docdb-serverless-managing.md "docdb-serverless-managing.md").

## Choosing the `MaxCapacity` setting for a DocumentDB serverless cluster

It's tempting to always choose some high value for the maximum DocumentDB serverless capacity setting.
A large maximum capacity allows the instance to scale up the most when it's running an intensive workload.
A low value avoids the possibility of unexpected charges.
Depending on how you use that cluster and the other settings that you configure, the most effective value might be higher or lower than you originally thought.
Consider the following factors when choosing the maximum capacity setting:

- The maximum capacity must be at least as high as the minimum capacity.
  You can set the minimum and maximum capacity to be identical.
  However, in that case the capacity never scales up or down.
  Thus, using identical values for minimum and maximum capacity isn't appropriate outside of testing situations.
- The maximum capacity must be at least 1.0 DCUs and must be at most 256 DCUs.
- We recommend monitoring the scaling and resource usage of your serverless instances.
  If your serverless instance is frequently scaling to maximum capacity and hitting resource constraints (e.g. when `DCUUtilization` metric is at 100.0), we recommend selecting a higher `MaxCapacity` value.
  For more information, see [Monitoring Amazon DocumentDB serverless](docdb-serverless-monitoring.md "docdb-serverless-monitoring.md").
- If you typically modify the instance class of your provisioned instances in anticipation of especially high or low workload, you can use that experience to estimate the equivalent DocumentDB serverless capacity range.
  To determine the memory size of provisioned Amazon DocumentDB instances, see [Instance limits](limits.md#limits.instance "limits.md#limits.instance").

For example, suppose that you use the `db.r6g.4xlarge` instance class when your cluster has a high workload.
That instance class has 128 GiB of memory.
Thus, you can specify a maximum DCU setting of 64 to set up a serverless instance that can scale up to approximately that same capacity.
That's because each DCU corresponds to approximately 2 GiB of memory.
You might specify a somewhat higher value to let the instance scale up farther in case your `db.r6g.4xlarge` instance sometimes doesn't have enough capacity to handle the workload effectively.

- If you have a budgetary cap on your database usage, choose a value that stays within that cap even if all your serverless instances run at maximum capacity all the time.
  Remember that when you have n serverless instances in your cluster, the theoretical maximum serverless capacity that the cluster can consume at any moment is n times the maximum DCU setting for the cluster.
  (The actual amount consumed might be less, for example if some readers scale independently from the writer.)
- If you make use of serverless reader instances to offload some of the read-only workload from the writer instance, you might be able to choose a lower maximum capacity setting.
  You do this to reflect that each reader instance doesn't need to scale as high as if the cluster contains only a single instance.
- Suppose that you want to protect against excessive usage due to misconfigured database parameters or inefficient queries in your application.
  In that case, you might avoid accidental overuse by choosing a maximum capacity setting that's lower than the absolute highest that you could set.
- If spikes due to real user activity are rare but do happen, you can take those occasions into account when choosing the maximum capacity setting.
  If the priority is for the application to keep running with full performance and scalability, you can specify a maximum capacity setting that's higher than you observe in normal usage.
  If it's OK for the application to run with reduced throughput during very extreme spikes in activity, you can choose a slightly lower maximum capacity setting.
  Make sure that you choose a setting that still has enough memory and CPU resources to keep the application running.
- If you turn on settings in your cluster that increase the memory usage for each instance, take that memory into account when deciding on the maximum DCU value.
  Such settings include those for Performance Insights.
  Make sure that the maximum DCU value allows the serverless instances to scale up enough to handle the workload when those feature are being used.
  For information about troubleshooting problems caused by the combination of a low maximum DCU setting and Amazon DocumentDB features that impose memory overhead, see [Avoiding out-of-memory errors](#docdb-serverless-scaling-mem-errors "#docdb-serverless-scaling-mem-errors") (below).
- In particular, we recommend the following minimum `MaxCapacity` for use with the specified features (these recommendations are subject to change):
  - Serverless instance creation on a cluster with a large data volume – 2 DCUs (this includes serverless instance creation as part of a cluster restore.)

- Certain instance limits are determined by the instance’s current capacity, such as connections limit, cursor limit, and open transactions limit.
  When choosing the `MaxCapacity` value for your workload, make sure to keep these instance limits in mind in order to avoid being bottlenecked by one of these limits.
  For more information, see [Amazon DocumentDB serverless instance limits](docdb-serverless-instance-limits.md "docdb-serverless-instance-limits.md").

For instructions on how to modify a cluster’s scaling configuration, see [Managing Amazon DocumentDB serverless](docdb-serverless-managing.md "docdb-serverless-managing.md").

## Avoiding out-of-memory errors

If one of your DocumentDB serverless instances consistently reaches the limit of its maximum capacity, Amazon DocumentDB indicates this condition by setting the instance to a status of **incompatible-parameters**.
While the instance has the **incompatible-parameters** status, some operations are blocked.
For example, you can't upgrade the engine version.
For more information on the status of an Amazon DocumentDB instance, see [Monitoring an Amazon DocumentDB instance's status](monitoring_docdb-instance_status.md "monitoring_docdb-instance_status.md").

Typically, your instance goes into this status when it restarts frequently due to out-of-memory errors.
Amazon DocumentDB records an event when this type of restart happens.
To view resource events, see [Viewing Amazon DocumentDB events](managing-events.md#viewing-events "managing-events.md#viewing-events").
Unusually high memory usage can happen because of overhead from turning on settings such as Performance Insights.
It can also come from a heavy workload on your instance or from managing the metadata associated with a large number of schema objects.

If the memory pressure becomes lower so that the instance doesn't reach its maximum capacity very often, Amazon DocumentDB automatically changes the instance status back to available.

To recover from this condition, you can take some or all of the following actions:

- Increase the lower limit on capacity for serverless instances by changing the minimum DocumentDB capacity unit (DCU) value for the cluster.
  Doing so avoids issues where an idle database scales down to a capacity with less memory than is needed for the features that are turned on in your cluster.
  After changing the DCU settings for the cluster, reboot the serverless instance.
  Doing so evaluates whether Amazon DocumentDB can reset the status back to available.
- Increase the upper limit on capacity for serverless instances by changing the maximum DCU value for the cluster.
  Doing so avoids issues where a busy database can't scale up to a capacity with enough memory for the features that are turned on in your cluster and the database workload.
  After changing the DCU settings for the cluster, reboot the serverless instance.
  Doing so evaluates whether Amazon DocumentDB can reset the status back to available.
- Turn off configuration settings that require memory overhead.
  For example, suppose that you have a feature such as Performance Insights turned on but don't use it.
  If so, you can turn it off. Or you can adjust the minimum and maximum capacity values for the cluster higher to account for the memory used by those types of features.
  For guidelines about choosing minimum and maximum capacity settings, see [Choosing the scaling capacity range for a DocumentDB serverless cluster](#docdb-serverless-scaling-capacity-choosing "#docdb-serverless-scaling-capacity-choosing").
- Reduce the workload on the instance. For example, you can add reader instances to the cluster to spread the load from read-only queries across more instances.

## Why is my serverless instance not scaling down?

In some cases, DocumentDB serverless doesn't scale down to the minimum capacity, even with no load on the database.
This can happen for the following reasons:

- Performance Insights can increase resource usage and prevent the database from scaling down to minimum capacity. These features include the following:
- If a reader instance isn't scaling down to the minimum and stays at the same or higher capacity than the writer instance, then check the priority tier of the reader instance.
  DocumentDB serverless reader instances in tier 0 or 1 are kept at a minimum capacity at least as high as the writer instance.
  Change the priority tier of the reader to 2 or higher so that it scales up and down independently of the writer.
  For more information, see [Amazon DocumentDB serverless scaling](docdb-serverless-how-it-works.md#docdb-serverless-scaling "docdb-serverless-how-it-works.md#docdb-serverless-scaling").
- Heavy database workloads can increase resource usage.
- Large database volumes can increase resource usage.
  Amazon DocumentDB uses memory and CPU resources for cluster management.
  Amazon DocumentDB requires more CPU and memory to manage clusters with larger database volumes.
  If your cluster’s minimum capacity is less than the minimum required for cluster management, your cluster won't scale down to the minimum capacity.
- Background maintenance activity can periodically increase resource usage.

If the database still doesn't scale down to the minimum capacity configured, then stop and restart the database to reclaim any memory fragments that might have built up over time.
Stopping and starting a database results in downtime, so we recommend doing this sparingly.
