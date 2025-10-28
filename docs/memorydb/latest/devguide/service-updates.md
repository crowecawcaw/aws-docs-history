# Service updates in MemoryDB

MemoryDB automatically monitors your fleet of clusters and nodes to apply service
updates as they become available. Typically, you set up a predefined maintenance window so
that MemoryDB can apply these updates. However, in some cases you might find this approach too
rigid and likely to constrain your business flows.

With Service updates in MemoryDB, you control when and which updates are applied. You can also
monitor the progress of these updates to your selected MemoryDB cluster in real time.

## Applying the service updates using the AWS CLI

After you receive notification that service updates are available, you can
inspect and apply them using the AWS CLI:

- To retrieve a description of the service updates that are available,
  run the following command:

`aws memorydb describe-service-updates --status available`

For more information, see [describe-service-updates](../../../cli/latest/reference/memorydb/describe-service-updates.md "../../../cli/latest/reference/memorydb/describe-service-updates.md").

- To apply a service update on a list of clusters, run the following command:

`aws memorydb batch-update-cluster --service-update ServiceUpdateNameToApply=sample-service-update --cluster-names cluster-1 cluster2`

For more information, see [batch-update-cluster](../../../cli/latest/reference/memorydb/batch-update-cluster.md "../../../cli/latest/reference/memorydb/batch-update-cluster.md").
