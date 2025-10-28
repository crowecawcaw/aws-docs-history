# Snapshot constraints

Consider the following constraints when planning or making snapshots:

- For MemoryDB clusters, snapshot and restore are available for all supported node
  types.
- During any contiguous 24-hour period, you can create no more than 20 manual snapshots per cluster.
- MemoryDB only supports taking snapshots on the cluster level. MemoryDB doesn't support taking
  snapshots at the shard or node level.
- During the snapshot process, you can't run any other API or CLI operations on
  the cluster.
- If you delete a cluster and request a final snapshot, MemoryDB always takes
  the snapshot from the primary nodes. This ensures that you capture the very latest
  data before the cluster is deleted.
