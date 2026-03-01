# Working with read replicas for Amazon RDS for PostgreSQL

You can scale reads for your Amazon RDS for PostgreSQL DB instances by adding read replicas to the
instances. As with other Amazon RDS database engines, RDS for PostgreSQL uses native replication
mechanisms of PostgreSQL to keep read replicas up to date with changes on the source DB. For
general information about read replicas and Amazon RDS, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

Following, you can find information specific to working with read replicas with
RDS for PostgreSQL.

## Read replica limitations with PostgreSQL

The following are limitations for PostgreSQL read replicas:

- PostgreSQL read replicas are read-only. Although a read replica isn't a
  writeable DB instance, you can promote it to become a standalone RDS for PostgreSQL
  DB instance. However, the process isn't reversible.
- You can't create a read replica from another read replica if your
  RDS for PostgreSQL DB instance is running a PostgreSQL version earlier than 14.1.
  RDS for PostgreSQL supports cascading read replicas on RDS for PostgreSQL version 14.1 and
  higher releases only. For more information, see [Using cascading read replicas with RDS for PostgreSQL](USER_PostgreSQL.Replication.ReadReplicas.md "USER_PostgreSQL.Replication.ReadReplicas.md").
- If you promote a PostgreSQL read replica, it becomes a writable DB instance.
  It stops receiving write-ahead log (WAL) files from a source DB instance, and
  it's no longer a read-only instance. You can create new read replicas from
  the promoted DB instance as you do for any RDS for PostgreSQL DB instance. For more
  information, see [Promoting a read replica to be a standalone DB instance](USER_ReadRepl.md "USER_ReadRepl.md").
- If you promote a PostgreSQL read replica from within a replication chain (a
  series of cascading read replicas), any existing downstream read replicas
  continue receiving WAL files from the promoted instance automatically. For more
  information, see [Using cascading read replicas with RDS for PostgreSQL](USER_PostgreSQL.Replication.ReadReplicas.md "USER_PostgreSQL.Replication.ReadReplicas.md").
- If no user transactions are running on the source DB instance, the associated
  PostgreSQL read replica reports a replication lag of up to five minutes. The
  replica lag is calculated as `currentTime -
lastCommitedTransactionTimestamp`, which means that when no
  transactions are being processed, the value of replica lag increases for a
  period of time until the write-ahead log (WAL) segment switches. By default
  RDS for PostgreSQL switches the WAL segment every 5 minutes, which results in a
  transaction record and a decrease in the reported lag.
- You can't turn on automated backups for PostgreSQL read replicas for
  RDS for PostgreSQL versions earlier than 14.1. Automated backups for read replicas
  are supported for RDS for PostgreSQL 14.1 and higher versions only. For RDS for
  PostgreSQL 13 and earlier versions, create a snapshot from a read replica if you
  want a backup of it.
- Point-in-time recovery (PITR) isn't supported for read replicas. You can
  use PITR with a primary (writer) instance only, not a read replica. To learn
  more, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").
- Read replicas for PostgreSQL versions 12 and lower automatically reboot during
  the 60-90 day maintenance window to apply password rotation. If the replica
  loses connection to the source before the scheduled reboot, it still reboots to
  resume replication. For PostgreSQL versions 13 and higher, read replicas might
  experience brief replication disconnections and reconnections during the
  password rotation process.
