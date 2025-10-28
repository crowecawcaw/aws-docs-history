# Send high availability data to

Amazon Managed Service for Prometheus with Prometheus

To set up a high availability configuration with Prometheus, you must apply
external labels on all instances of a high availability group, so Amazon Managed Service for Prometheus can
identify them. Use the `cluster` label to identify a Prometheus instance
agent as part of a high availability group. Use the `__replica__` label
to identify each replica in the group separately. You need to apply both
`__replica__` and `cluster` labels for de-duplication to
work.

###### Note

The `__replica__` label is formatted with two underscore symbols
before and after the word `replica`.

**Example: code snippets**

In the following code snippets, the `cluster` label identifies the
Prometheus instance agent `prom-team1`, and the `_replica_`
label identifies the replicas `replica1` and
`replica2`.

```
cluster: prom-team1
__replica__: replica1
```

```
cluster: prom-team1
__replica__: replica2
```

As Amazon Managed Service for Prometheus stores data samples from high availability replicas with these
labels, it strips the `replica` label when the samples are accepted. This
means that you will only have a 1:1 series mapping for your current series instead
of a series per replica. The `cluster` label is kept.

###### Note

Certain versions of Kubernetes (1.28 and 1.29) may emit their own
metric with a `cluster` label. This can cause issues with
Amazon Managed Service for Prometheus deduplication. See the [High
availability FAQ](HA_FAQ.md#HA_FAQ_cluster-label "HA_FAQ.md#HA_FAQ_cluster-label") for more information.
