# Scheduling automatic snapshots

For any MemoryDB cluster, you can enable automatic snapshots. When automatic snapshots are
enabled, MemoryDB creates a snapshot of the cluster on a daily basis. There is no impact on the cluster and the change is immediate. For more information, see [Restoring from a snapshot](snapshots-restoring.md "snapshots-restoring.md").

When you schedule automatic snapshots, you should plan the following settings:

- Snapshot window – A period during each day
  when MemoryDB begins creating a snapshot. The minimum length for the snapshot window is
  60 minutes. You can set the snapshot window for any time when it's most convenient
  for you, or for a time of day that avoids doing snapshots during particularly
  high-utilization periods.

If you don't specify a snapshot window, MemoryDB assigns one
automatically.

- Snapshot retention limit – The number of
  days the snapshot is retained in Amazon S3. For example, if you set the retention limit
  to 5, then a snapshot taken today is retained for 5 days. When the retention limit
  expires, the snapshot is automatically deleted.

The maximum snapshot retention limit is 35 days. If the snapshot retention limit
is set to 0, automatic snapshots are disabled for the cluster. MemoryDB data is still
fully durable even with automatic snapshotting disabled.
You can enable or disable automatic snapshots when creating a MemoryDB cluster using the MemoryDB console, the AWS CLI, or the MemoryDB API.
You can enable automatic snapshots when you create a MemoryDB cluster by checking the
**Enable Automatic Backups** box in the **Snapshots** section. For more information,
[Creating a MemoryDB cluster](getting-started.md#clusters.create "getting-started.md#clusters.create").
