# Deduplicating high availability metrics sent to

Amazon Managed Service for Prometheus

You can send data from multiple Prometheus _agents_ (Prometheus
instances running in Agent mode) to your Amazon Managed Service for Prometheus workspace. If some of these
instances are recording and sending the same metrics, your data will have a higher
availability (even if one of the agents stops sending data, the Amazon Managed Service for Prometheus workspace
will still receive the data from another instance). However, you want your Amazon Managed Service for Prometheus
workspace to automatically de-duplicate the metrics so that you don't see the
metrics multiple times, and aren't charged for the data ingestion and storage
multiple times.

For Amazon Managed Service for Prometheus to automatically de-duplicate data from multiple Prometheus agents,
you give the set of agents that are sending the duplicate data a single
_cluster name_, and each of the instances a _replica
name_. The cluster name identifies the instances as having shared
data, and the replica name allows Amazon Managed Service for Prometheus to identify the source of each metric.
The final stored metrics include the cluster label, but not the replica, so the
metrics appear to be coming from a single source.

###### Note

Certain versions of Kubernetes (1.28 and 1.29) may emit their own
metric with a `cluster` label. This can cause issues with
Amazon Managed Service for Prometheus deduplication. See the [High
availability FAQ](HA_FAQ.md#HA_FAQ_cluster-label "HA_FAQ.md#HA_FAQ_cluster-label") for more information.

The following topics show how to send data and include the `cluster`
and `__replica__` labels, so that Amazon Managed Service for Prometheus de-duplicates the data
automatically.

###### Important

If you do not set up deduplication, you will be charged for all data samples
that are sent to Amazon Managed Service for Prometheus. These data samples include duplicate samples.
