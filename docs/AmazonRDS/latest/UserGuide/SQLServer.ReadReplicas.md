# Troubleshooting a SQL Server read replica problem

You can monitor replication lag in Amazon CloudWatch by viewing the Amazon RDS `ReplicaLag`
metric. For information about replication lag time, see [Monitoring read replication](USER_ReadRepl.md "USER_ReadRepl.md").

If replication lag is too long, you can use the following query to get information
about the lag.

```
SELECT AR.`replica_server_name`
     , DB_NAME (ARS.database_id) '`database_name`'
     , AR.availability_mode_desc
     , ARS.synchronization_health_desc
     , ARS.last_hardened_lsn
     , ARS.last_redone_lsn
     , ARS.secondary_lag_seconds
FROM sys.dm_hadr_database_replica_states ARS
INNER JOIN sys.availability_replicas AR ON ARS.replica_id = AR.`replica_id`
--WHERE DB_NAME(ARS.database_id) = '`database_name`'
ORDER BY AR.`replica_server_name`;
```
