# Cross-Region resiliency for Global Database secondary clusters

Aurora PostgreSQL versions 16.6, 15.10, 14.15, 13.18, 12.22, or higher and Aurora MySQL versions 3.09 or higher contain availability improvements that enable
secondary Region read replicas to maintain service continuity during unplanned events such as hardware failures,
network disruptions across AWS Regions, large volumes of data transfers between the clusters, and others.

Although the read replicas remain available for your application requests, the replication lag may continue to
increase until the resolution of the unplanned event. You can monitor the lag between primary and secondary
clusters using the `AuroraGlobalDBProgressLag` CloudWatch metric. To measure the end-to-end lag, including
any lag between the cluster volume and DB instances of the secondary cluster, add the values of the
`AuroraGlobalDBProgressLag` and `AuroraReplicaLag` CloudWatch metrics. For more information
about metrics, refer to [Metrics reference for Amazon Aurora](metrics-reference.md "metrics-reference.md").

The Global Database read availability for Aurora MySQL and earlier versions of Aurora PostgreSQL may be impacted
during such unplanned events.

For more information about new features in Aurora PostgreSQL 16.6, 15.10, 14.15, 13.18, and 12.22, see
[PostgreSQL 16.6](../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#aurorapostgresql-versions-version166x "../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#aurorapostgresql-versions-version166x") in the _Aurora PostgreSQL Release Notes_.

For more information about new features in Aurora MySQL versions 3.09 and higher, see
[Database engine updates for Amazon Aurora MySQL version 3](../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md "../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md") in the _Aurora MySQL Release Notes_.
