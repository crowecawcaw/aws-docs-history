# `describe_cluster_instances`

```
describe_cluster_instances(cluster_name, region, next_token, node_type, queue_name)
```

Describe a cluster's instances.

###### Parameters:

**`cluster_name` (required)**

The cluster name.

**`region`**

The cluster AWS Region.

**`next_token`**

The token for the next set of results.

**`node_type`**

Filters the instances by `node_type`.

Valid values: `HeadNode` | `ComputeNode`

**`queue_name`**

Filters the instances by queue name.
