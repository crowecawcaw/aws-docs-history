# Modifying a Neptune global database

The DB cluster parameter groups can be configured independently for each Neptune
DB cluster in a global database, but it's best to keep settings consistent across the
clusters to avoid unexpected behavior changes if a secondary cluster has to be promoted
to primary.

You can modify the settings of the global database itself using the [modify-global-cluster](../../../cli/latest/reference/neptune/modify-global-cluster.md "../../../cli/latest/reference/neptune/modify-global-cluster.md")
CLI command (which wraps the [ModifyGlobalCluster](api-global-dbs.md#ModifyGlobalCluster "api-global-dbs.md#ModifyGlobalCluster") API). For example, you could change the
global database identifier and at the same time turn off deletion protection like this:

```
aws neptune modify-global-cluster \
  --region `(region of the DB cluster to modify)` \
  --global-cluster-identifier `(current global database ID)` \
  --new-global-cluster-identifier `(new global database ID to assign)` \
  --deletion-protection false
```
