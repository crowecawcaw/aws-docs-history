# Additional configuration for Neptune

Serverless DB clusters and instances

In addition to [setting minimum
and maximum capacity](neptune-serverless-capacity-scaling.md "neptune-serverless-capacity-scaling.md") for your Neptune Serverless DB cluster, there are a few
other configuration choices to consider.

## Combining serverless and provisioned instances in a DB cluster

A DB cluster doesn't have to be serverless only— you can create a
combination of serverless and provisioned instances (a mixed configuration).

For example, suppose that you need more write capacity than is available in
a serverless instance. In that case, you can set up the cluster with a very large
provisioned writer and still use serverless instances for the readers.

Or, suppose that the write workload on your cluster varies but the read workload
is steady. In that case, you could set up your cluster with a serverless writer and
one or more provisioned readers.

See [Using Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") for information about
how to create a mixed-configuration DB cluster.

## Setting the promotion tiers for Neptune

Serverless instances

For clusters containing multiple serverless instances, or a mixture of provisioned
and serverless instances, pay attention to the promotion tier setting for each serverless
instance. This setting controls more behavior for serverless instances than for
provisioned DB instances.

In the AWS Management Console, you specify this setting using the **Failover priority**
under **Additional configuration** on the **Create database**,
**Modify instance**, and **Add reader** pages. You
see this property for existing instances in the optional **Priority tier**
column on the **Databases** page. You can also see this property on
the details page for a DB cluster or instance.

For provisioned instances, the choice of tier 0–15 determines only the order in
which Neptune chooses which reader instance to promote to the writer during a failover
operation. For Neptune Serverless reader instances, the tier number also determines
whether the instance scales up to match the capacity of the writer instance or scales
independently of it based only on its own workload.

Neptune Serverless reader instances in tier 0 or 1 are kept at a minimum capacity
at least as high as the writer instance so that they are ready to take over from the
writer in case of failover. If the writer is a provisioned instance, Neptune
estimates the equivalent serverless capacity and uses that estimate as the minimum
capacity for the serverless reader instance.

Neptune Serverless reader instances in tiers 2–15 don't have the same constraint
on their minimum capacity, and scale independently of the writer. When they are idle,
they scale down to the minimum NCU value specified in the cluster's [capacity range](neptune-serverless-capacity-scaling.md "neptune-serverless-capacity-scaling.md"). This can
cause problems, however, if the read workload spikes rapidly.

## Keeping reader capacity aligned to writer capacity

One important thing to keep in mind is that you want to make sure your reader
instances can keep up with your writer instance, to prevent excessive replication lag.
This is particularly a concern in two situations, where serverless reader instances
do not automatically scale in sync with the writer instance:

- When your writer is provisioned, and your readers are serverless.
- When your writer is serverless, and your serverless readers are in
  promotion tiers 2-15.

In both of those cases, set the minimum serverless capacity to match that of
the expected writer capacity, to ensure that reader operations don't time out and
potentially cause restarts. In the case of a provisioned writer instance, set
the minimum capacity to match that of the provisioned instance. In the case of
a serverless writer, the optimal setting may be harder to predict.

Because the instance capacity range is set at the cluster level, all serverless
instances are controlled by the same minimum and maximum capacity settings. Reader
instances in tiers 0 and 1 scale in sync with the writer instance, but instances
in promotion tiers 2-15 scale independently of each other and of the writer
instance, depending on their workload. If you set the minimum capacity too low,
idle instances in tiers 2 to 15 can scale down too low to scale back up fast
enough to handle a sudden burst in writer activity.

## Avoid setting the timeout value too high

It is possible to incur unexpected costs if you set the query timeout value too
high on a serverless instance.

Without a reasonable timeout setting, you may inadvertently issue a query that
requires a powerful, expensive instance type and that keeps running for a very long
time, incurring costs you never anticipated. You can avoid that situation by using
a query timeout value which accomodates most of your queries and only causes
unexpectedly long-running ones to time out.

This is true both for general query timeout values set using parameters and for
per-query timeout values set using query hints.

## Optimizing your Neptune Serverless configuration

If your Neptune Serverless DB cluster is not tuned to the workload it is
running, you may notice that it doesn't run optimally. You can adjust the minimum
and/or maximum capacity setting so that it can scale without encountering memory
problems.

- Increase the minimum capacity setting for the cluster. This
  can correct the situation where an idle instance scales back to a capacity
  that has less memory than your application and enabled features need.
- Increase the maximum capacity setting for the cluster. This
  can correct the situation where a busy database can't scale up to a capacity
  with enough memory to handle the workload and any memory-intensive features
  that are enabled.
- Change the workload on the instance in question. For example,
  you can add reader instances to the cluster to spread the read load
  across more instances.
- Tune your application's queries so that they use fewer
  resources.
- Try using a provisioned instance that is larger than the
  maximum NCUs available within Neptune Serverless, to see if it is a
  better fit for the memory and CPU requirements of the workload.
