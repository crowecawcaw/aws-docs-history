# Canceling pending add or delete node operations in ElastiCache

If you elected to not apply an ElastiCache cluster change immediately, the operation has
**pending** status until it is performed at your next
maintenance window. You can cancel any pending add or delete operation.

To cancel a pending add or delete node operation with the AWS CLI, use the
`modify-cache-cluster` command. Set `num-cache-nodes` equal to the current
number of cache nodes in the cluster, and then add the `--apply-immediately` flag. This will override the pending change.

To cancel a pending node addition or deletion:

```
aws elasticache modify-cache-cluster
	--cache-cluster-id <your-cluster-id>
	--num-cache-nodes <current-number-of-nodes>
	--apply-immediately
```

If it isn't clear whether any node additions or deletions are pending, you can confirm their
status with the `describe-cache-clusters` command:

```
aws elasticache describe-cache-clusters
	--cache-cluster-id <your-cluster-id>
```

Any pending nodes should appear in the `PendingModifiedValues`output. For example:

```
"PendingModifiedValues": {
	"NumCacheNodes": 3
	},
```
