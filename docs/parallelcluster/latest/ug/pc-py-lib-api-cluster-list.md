# `list_clusters`

```
list_clusters(region, next_token, cluster_status)
```

Retrieve the list of existing clusters.

###### Parameters:

**`region`**

Lists clusters deployed to a given AWS Region.

**`next_token`**

The token for the next set of results.

**`cluster_status`**

Filters by cluster status. The default is to list all clusters.

Valid values: `CREATE_IN_PROGRESS` | `CREATE_FAILED` | `CREATE_COMPLETE` |
`DELETE_IN_PROGRESS` | `DELETE_FAILED` | `UPDATE_IN_PROGRESS` |
`UPDATE_COMPLETE` | `UPDATE_FAILED`
