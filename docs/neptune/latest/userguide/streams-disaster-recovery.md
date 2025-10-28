# Using Neptune streams cross-region replication for disaster recovery

Neptune provides two ways of implementing cross-region failover capabilities:

- Cross-region snapshot copy and restore
- Using Neptune streams to replicate data between two clusters in two
  different regions.
  Cross-region snapshot copy and restore has the lowest operational overhead for
  recovering a Neptune cluster in a different region. However, copying a snapshot
  between regions can requires significant data-transfer time, since a snapshot
  is a full backup of the Neptune cluster. As a result, cross-region snapshot
  copy and restore can be used for scenarios that only require a Recovery Point Objective
  (RPO) of hours and a Recovery Time Objective (RTO) of hours.

A Recovery Point Objective (RPO) is measured by the time in between backups.
It defines how much data may be lost between the time the last backup was made and
the time at which the database is recovered.

A Recovery Time Objective (RTO) is measured by the time it takes to perform
a recovery operation. This is the time it takes the DB cluster to fail over to
a recovered database after a failure occurs.

Neptune streams provides a way to keep a backup Neptune cluster in sync
with the primary production cluster at all times. If a failure occurs, your
database then fails over to the backup cluster. This reduces RPO and RTO to
minutes, since data is constantly being copied to the backup cluster, which is
immediately available as a failover target at any time.

The drawback of using Neptune streams in this way is that both the operational
overhead required to maintain the replication components, and the cost of having a
second Neptune DB cluster online all of the time, can be significant.
