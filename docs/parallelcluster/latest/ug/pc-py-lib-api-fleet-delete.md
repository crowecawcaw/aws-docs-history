# `delete_cluster_instances`

```
delete_cluster_instances(cluster_name, region, force)
```

Initiate the forced termination of all cluster compute nodes. This action doesn't support AWS Batch clusters.

###### Parameters:

**`cluster_name` (required)**

The cluster name.

**`region`**

The cluster AWS Region.

**`force`**

If set to `True`, forces deletion when the cluster with the given `cluster_name` isn't found. The default is
`False`.
