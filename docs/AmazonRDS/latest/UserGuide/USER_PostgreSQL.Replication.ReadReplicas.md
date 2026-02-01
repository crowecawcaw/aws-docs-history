# How

streaming replication works for different RDS for PostgreSQL versions

As discussed in [Read replica
configuration with PostgreSQL](USER_PostgreSQL.Replication.ReadReplicas.md "USER_PostgreSQL.Replication.ReadReplicas.md"),
RDS for PostgreSQL uses PostgreSQL's native streaming replication protocol to send WAL
data from the source DB instance. It sends source WAL data to read replicas for both
in-Region and cross-Region read replicas. With version 9.4, PostgreSQL introduced
physical replication slots as a supporting mechanism for the replication process.

A _physical replication slot_ prevents a source DB instance from
removing WAL data before it's consumed by all read replicas. Each read replica has
its own physical slot on the source DB instance. The slot keeps track of the oldest WAL
(by logical sequence number, LSN) that might be needed by the replica. After all slots
and DB connections have progressed beyond a given WAL (LSN), that LSN becomes a
candidate for removal at the next checkpoint.

Amazon RDS uses Amazon S3 to archive WAL data. For in-Region read replicas, you can use this
archived data to recover the read replica when necessary. An example of when you might
do so is if the connection between source DB and read replica is interrupted for any
reason.

In the following table, you can find a summary of differences between PostgreSQL
versions and the supporting mechanisms for in-Region and cross-Region used by
RDS for PostgreSQL.

| Version                             | In-Region                                  | Cross-Region        |
| ----------------------------------- | ------------------------------------------ | ------------------- |
| PostgreSQL 14.1 and higher versions | • Replication slots<br>• Amazon S3 archive | • Replication slots |
| PostgreSQL 13 and lower versions    | • Amazon S3 archive                        | • Replication slots |

For more information, see [Monitoring and tuning
the replication process](USER_PostgreSQL.Replication.ReadReplicas.md "USER_PostgreSQL.Replication.ReadReplicas.md").

## Understanding

the parameters that control PostgreSQL replication

The following parameters affect the replication process and determine how well
read replicas stay up to date with the source DB instance:

**max_wal_senders**

The `max_wal_senders` parameter specifies the maximum
number of connections that the source DB instance can support at the
same time over the streaming replication protocol.

The default value varies for RDS for PostgreSQL versions:

- For versions 13, 14, and 15, the default value is 20.
- For versions 16 and above, the default value is 35.

This parameter should be set to slightly higher than the actual number
of read replicas. If this parameter is set too low for the number of
read replicas, replication stops.

For more information, see [max_wal_senders](https://www.postgresql.org/docs/devel/runtime-config-replication.html#GUC-MAX-WAL-SENDERS "https://www.postgresql.org/docs/devel/runtime-config-replication.html#GUC-MAX-WAL-SENDERS") in the PostgreSQL documentation.

###### Note

`max_wal_senders` is a static parameter that requires a
DB instance reboot for changes to take effect.

**wal_keep_segments**

The `wal_keep_segments` parameter specifies the number of
write-ahead log (WAL) files that the source DB instance keeps in the
`pg_wal` directory. The default setting is 32.

If `wal_keep_segments` isn't set to a large enough
value for your deployment, a read replica can fall so far behind that
streaming replication stops. If that happens, Amazon RDS generates a
replication error and begins recovery on the read replica. It does so by
replaying the source DB instance's archived WAL data from Amazon S3.
This recovery process continues until the read replica has caught up
enough to continue streaming replication. You can see this process in
action as captured by the PostgreSQL log in [Example: How
a read replica recovers from replication interruptions](#USER_PostgreSQL.Replication.example-how-it-works "#USER_PostgreSQL.Replication.example-how-it-works").

###### Note

In PostgreSQL version 13, the `wal_keep_segments`
parameter is named `wal_keep_size`. It serves the same
purpose as `wal_keep_segments`, but its default value is
in megabytes (MB) (2048 MB) rather than the number of files. For
more information, see [wal_keep_segments](https://www.postgresql.org/docs/12/runtime-config-replication.html#GUC-WAL-KEEP-SEGMENTS "https://www.postgresql.org/docs/12/runtime-config-replication.html#GUC-WAL-KEEP-SEGMENTS") and [wal_keep_size](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-KEEP-SIZE "https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-KEEP-SIZE") in the PostgreSQL documentation.

**max_slot_wal_keep_size**

The `max_slot_wal_keep_size` parameter controls the
quantity of WAL data that the RDS for PostgreSQL DB instance retains in the
`pg_wal` directory to serve slots. This parameter is used
for configurations that use replication slots. The default value for
this parameter is `-1`, meaning that there's no limit to
how much WAL data is kept on the source DB instance. For information
about monitoring your replication slots, see [Monitoring replication slots for your RDS for PostgreSQL DB instance](USER_PostgreSQL.Replication.ReadReplicas.md#USER_PostgreSQL.Replication.ReadReplicas.Monitor-monitor-replication-slots "USER_PostgreSQL.Replication.ReadReplicas.md#USER_PostgreSQL.Replication.ReadReplicas.Monitor-monitor-replication-slots").

For more information about this parameter, see [max_slot_wal_keep_size](https://www.postgresql.org/docs/devel/runtime-config-replication.html#GUC-MAX-SLOT-WAL-KEEP-SIZE "https://www.postgresql.org/docs/devel/runtime-config-replication.html#GUC-MAX-SLOT-WAL-KEEP-SIZE") in the PostgreSQL
documentation.

Whenever the stream that provides WAL data to a read replica is interrupted,
PostgreSQL switches into recovery mode. It restores the read replica by using
archived WAL data from Amazon S3 or by using the WAL data associated with the replication
slot. When this process is complete, PostgreSQL re-establishes streaming
replication.

### Example: How

a read replica recovers from replication interruptions

In the following example, you find the log details that demonstrate the
recovery process for a read replica. The example is from an RDS for PostgreSQL DB
instance running PostgreSQL version 12.9 in the same AWS Region as the source
DB, so replication slots aren't used. The recovery process is the same for
other RDS for PostgreSQL DB instances running PostgreSQL earlier than version 14.1
with in-Region read replicas.

When the read replica lost contact with the source DB instance, Amazon RDS records
the issue in the log as `FATAL: could not receive data from WAL
 stream` message, along with the `ERROR: requested WAL segment ...
 has already been removed`. As shown in the bold line, Amazon RDS recovers
the replica by replaying an archived WAL file.

```
2014-11-07 19:01:10 UTC::@:[23180]:DEBUG:  switched WAL source from archive to stream after failure
2014-11-07 19:01:10 UTC::@:[11575]:LOG: started streaming WAL from primary at 1A/D3000000 on timeline 1
2014-11-07 19:01:10 UTC::@:[11575]:FATAL: could not receive data from WAL stream:
ERROR:  requested WAL segment 000000010000001A000000D3 has already been removed
2014-11-07 19:01:10 UTC::@:[23180]:DEBUG: could not restore file "00000002.history" from archive: return code 0
2014-11-07 19:01:15 UTC::@:[23180]:DEBUG: switched WAL source from stream to archive after failure recovering 000000010000001A000000D3
**2014-11-07 19:01:16 UTC::@:[23180]:LOG:  restored log file "000000010000001A000000D3" from archive**
```

When Amazon RDS replays enough archived WAL data on the replica to catch up,
streaming to the read replica begins again. When streaming resumes, Amazon RDS writes
an entry to the log file similar to the following.

```
2014-11-07 19:41:36 UTC::@:[24714]:LOG:started streaming WAL from primary at 1B/B6000000 on timeline 1
```

## Setting the parameters that control shared memory

The parameters you set determine the size of shared memory for tracking
transaction IDs, locks, and prepared transactions. The shared
memory structure of a standby instance must be equal or greater than that of a
primary instance. This ensures that the former doesn't run out of
shared memory during recovery. If the parameter values on the replica are less than
the parameter values on the primary, Amazon RDS will automatically adjust the replica
parameters and restart the engine.

The parameters affected are:

- max_connections
- max_worker_processes
- max_wal_senders
- max_prepared_transactions
- max_locks_per_transaction

To avoid RDS reboots of replicas due to insufficient memory, we recommend applying
the parameter changes as a rolling reboot to each replica. You must apply the
following rules, when you set the parameters:

- Increasing the parameter values:
  - You should always increase the parameter values of all the read
    replicas first, and perform a rolling reboot of all replicas. Then,
    apply the parameter changes on the primary instance and
    reboot.

- Decreasing the parameter values:
  - You should first decrease the parameter values of the primary
    instance and perform a reboot. Then, apply the parameter changes to
    all the associated read replicas and perform a rolling
    reboot.
