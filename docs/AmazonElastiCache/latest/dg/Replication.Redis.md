# How synchronization and backup are implemented

All supported versions of Valkey and Redis OSS support backup and synchronization between the primary and replica nodes.
However, the way that backup and synchronization is implemented varies depending on the version.

## Redis OSS Version 2.8.22 and Later

Redis OSS replication, in versions 2.8.22 and later, choose between two methods.
For more information, see [Redis OSS Versions Before 2.8.22](#Replication.Redis.Earlier2-8-22 "#Replication.Redis.Earlier2-8-22")
and [Snapshot and restore](backups.md "backups.md").

During the forkless process, if the write loads are heavy,
writes to the cluster are delayed to ensure that you don't
accumulate too many changes and thus prevent a successful snapshot.

## Redis OSS Versions Before 2.8.22

Redis OSS backup and synchronization in versions before 2.8.22 is a three-step
process.

1. Fork, and in the background process, serialize the cluster data to disk.
   This creates a point-in-time snapshot.
2. In the foreground, accumulate a change log in the _client output
   buffer_.

###### Important

If the change log exceeds the _client output buffer_ size,
the backup or synchronization fails.
For more information, see [Ensuring you have enough memory to make a Valkey or Redis OSS snapshot](BestPractices.md "BestPractices.md"). 3. Finally, transmit the cache data and then the change log to the replica node.
