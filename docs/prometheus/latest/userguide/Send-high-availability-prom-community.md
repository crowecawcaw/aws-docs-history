# Send high availability data

to Amazon Managed Service for Prometheus with the Prometheus community Helm chart

To set up a high availability configuration with the Prometheus community Helm
chart, you must apply external labels on all instances of a high availability group,
so Amazon Managed Service for Prometheus can identify them. Here is an example of how you could add the
`external_labels` to a single instance of Prometheus from the
Prometheus community Helm chart.

```
server:
global:
  external_labels:
      cluster: monitoring-cluster
      __replica__: replica-1
```

###### Note

If you want multiple replicas, you have to deploy the chart multiple times
with different replica values, because the Prometheus community Helm chart does
not let you dynamically set the replica value when increasing the number of
replicas directly from the controller group. If you prefer to have the
`replica` label auto-set, use the prometheus-operator Helm
chart.

###### Note

Certain versions of Kubernetes (1.28 and 1.29) may emit their own
metric with a `cluster` label. This can cause issues with
Amazon Managed Service for Prometheus deduplication. See the [High
availability FAQ](HA_FAQ.md#HA_FAQ_cluster-label "HA_FAQ.md#HA_FAQ_cluster-label") for more information.
