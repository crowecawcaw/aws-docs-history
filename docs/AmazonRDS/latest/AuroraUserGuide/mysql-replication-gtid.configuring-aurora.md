# Enabling GTID-based replication for an Aurora MySQL cluster

When GTID-based replication is enabled for an Aurora MySQL DB cluster, the GTID settings apply
to both inbound and outbound binlog replication.

###### To enable GTID-based replication for an Aurora MySQL cluster

1. Create or edit a DB cluster parameter group using the following parameter settings:
   - `gtid_mode` – `ON` or `ON_PERMISSIVE`
   - `enforce_gtid_consistency` – `ON`

2. Associate the DB cluster parameter group with the Aurora MySQL cluster.
   To do so, follow the procedures in
   [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
3. (Optional) Specify how to assign GTIDs to transactions that don't include them. To do so, call the stored
   procedure in [mysql.rds_assign_gtids_to_anonymous_transactions (Aurora MySQL version 3)](mysql-stored-proc-gtid.md#mysql_assign_gtids_to_anonymous_transactions "mysql-stored-proc-gtid.md#mysql_assign_gtids_to_anonymous_transactions").
