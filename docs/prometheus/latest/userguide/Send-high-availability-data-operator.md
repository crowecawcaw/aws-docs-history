# Set up high availability data

to Amazon Managed Service for Prometheus using the Prometheus Operator Helm chart

To set up a high availability configuration with the Prometheus Operator in Helm,
you must apply external labels on all instances of a high availability group, so
Amazon Managed Service for Prometheus can identify them. You also must set the attributes
`replicaExternalLabelName` and `externalLabels` on the
Prometheus Operator Helm chart.

**Example: YAML header**

In the following YAML header, `cluster` is added to
`externalLabel` to identify a Prometheus instance agent as part of a
high-availability group, and `replicaExternalLabels` identifies each
replica in the group.

```
replicaExternalLabelName: __replica__
externalLabels:
cluster: prom-dev
```

###### Note

Certain versions of Kubernetes (1.28 and 1.29) may emit their own
metric with a `cluster` label. This can cause issues with
Amazon Managed Service for Prometheus deduplication. See the [High
availability FAQ](HA_FAQ.md#HA_FAQ_cluster-label "HA_FAQ.md#HA_FAQ_cluster-label") for more information.
