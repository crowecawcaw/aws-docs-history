

# Answers to common questions about high availability configuration in Amazon Managed Service for Prometheus
<a name="HA_FAQ"></a>

## Should I include the value *\_\_replica\_\_* into another label to track the sample points?
<a name="HA_FAQ_replica-label"></a>

 In a high availability setting, Amazon Managed Service for Prometheus ensures data samples are not duplicated by electing a leader in the cluster of Prometheus instances. If the leader replica stops sending data samples for 30 seconds, Amazon Managed Service for Prometheus automatically makes another Prometheus instance a leader replica and ingests data from the new leader, including any missed data. Therefore, the answer is no, it is not recommended.  Doing so may cause issues like: 
+  Querying a `count` in **PromQL** may return higher than expected value during the period of electing a new leader.
+  The number of `active series` gets increased during a period of electing a new leader and it reaches the `active series limits`. See [ AMP Quotas ](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html) for more info.

## Kubernetes seems to have it's own *cluster* label, and is not deduplicating my metrics. How can I fix this?
<a name="HA_FAQ_cluster-label"></a>

A new metric, `apiserver_storage_size_bytes` was introduced in Kubernetes 1.28, with a `cluster` label. This can cause issues with deduplication in Amazon Managed Service for Prometheus, which depends on the `cluster` label. In Kubernetes 1.3, the label is renamed to `storage-cluster_id` (it is also renamed in later patches of 1.28 and 1.29). If your cluster is emitting this metric with the `cluster` label, Amazon Managed Service for Prometheus can't dedupe the associated time series. We recommend you upgrade your Kubernetes cluster to the latest patched version to avoid this problem. Alternately, you can relabel the `cluster` label on your `apiserver_storage_size_bytes` metric before ingesting it into Amazon Managed Service for Prometheus.

**Note**  
For more details about the change to Kubernetes, see [Rename Label cluster to storage\_cluster\_id for apiserver\_storage\_size\_bytes metric](https://github.com/kubernetes/kubernetes/pull/124283) in the *Kubernetes GitHub project*.