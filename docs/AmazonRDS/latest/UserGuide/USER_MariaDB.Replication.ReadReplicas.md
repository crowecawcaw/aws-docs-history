# Starting and stopping replication with MariaDB read replicas

You can stop and restart the replication process on an Amazon RDS DB instance by calling the
system stored procedures
[mysql.rds_stop_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication "mysql-stored-proc-replicating.md#mysql_rds_stop_replication") and
[mysql.rds_start_replication](mysql-stored-proc-replicating.md#mysql_rds_start_replication "mysql-stored-proc-replicating.md#mysql_rds_start_replication").
You can do this when replicating between two Amazon RDS instances for long-running operations
such as creating large indexes. You also need to stop and start replication when
importing or exporting databases.
For more information, see
[Importing data to an
Amazon RDS for MariaDB DB instance with reduced downtime](mariadb-importing-data-reduced-downtime.md "mariadb-importing-data-reduced-downtime.md")
and
[Exporting data from a MySQL DB instance by using replication](MySQL.Procedural.Exporting.md "MySQL.Procedural.Exporting.md").

If replication is stopped for more than 30 consecutive days, either manually or due to
a replication error, Amazon RDS ends replication between the source DB instance and
all read replicas. It does so to prevent increased storage requirements on the
source DB instance and long failover times. The read replica DB instance is still
available. However, replication can't be resumed because the binary logs required by
the read replica are deleted from the source DB instance after replication is
ended. You can create a new read replica for the source DB instance to
reestablish replication.
