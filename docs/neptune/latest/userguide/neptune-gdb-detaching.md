# Removing a DB cluster from a Neptune global database

There are several reasons you might want to remove a DB cluster from a global
database. For example:

- If the primary cluster becomes degraded or isolated, you can remove
  it from the global database and it becomes a standalone provisioned cluster that
  can be used to create a new global database (see [Detach-and-promote a Neptune global database
  in the case of an unplanned outage](neptune-gdb-disaster-recovery.md#neptune-gdb-detach-and-promote "neptune-gdb-disaster-recovery.md#neptune-gdb-detach-and-promote")).
- If you want to delete a global database, first you have to you remove
  (detach) all associated clusters from it, leaving the primary for last (see [Deleting a Neptune global database](neptune-gdb-deleting.md "neptune-gdb-deleting.md").
  You can use the [remove-from-global-cluster](../../../cli/latest/reference/rds/remove-from-global-cluster.md "../../../cli/latest/reference/rds/remove-from-global-cluster.md")
  CLI command (which wraps the [RemoveFromGlobalCluster](api-global-dbs.md#RemoveFromGlobalCluster "api-global-dbs.md#RemoveFromGlobalCluster") API) to detach a Neptune
  DB cluster from a global database:

```
aws neptune remove-from-global-cluster \
  --region `(region of the cluster to remove)` \
  --global-cluster-identifier `(global database ID)` \
  --db-cluster-identifier `(ARN of the cluster to remove)`
```

The detached DB cluster then becomes a standalone DB cluster.
