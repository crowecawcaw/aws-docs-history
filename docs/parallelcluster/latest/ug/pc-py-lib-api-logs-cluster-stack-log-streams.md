# `list_cluster_log_streams`

```
list_cluster_log_streams(cluster_name, region, filters, next_token)
```

List log streams for a given cluster.

###### Parameters:

**`cluster_name` (required)**

The cluster name.

**`region`**

The cluster AWS Region.

**`filters`**

Filters the cluster log streams.

Format: `'Name=a,Values=1 Name=b,Values=2,3'`

###### Accepted filters:

**code-dns-name**

The short form of the private DNS name of the instance; for example, `ip-10-0-0-101`.

**node-type**

The node type.

Valid values: `HeadNode`

**`next_token`**

The token for the next set of results.
