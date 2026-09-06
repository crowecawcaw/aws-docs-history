

# Disabling GTID-based replication for an Aurora MySQL DB cluster
<a name="mysql-replication-gtid.disabling"></a>

You can disable GTID-based replication for an Aurora MySQL DB cluster. Doing so means that the Aurora cluster can't perform inbound or outbound binlog replication with external databases that use GTID-based replication. 

**Note**  
In the following procedure, *read replica* means the replication target in an Aurora configuration with binlog replication to or from an external database. It doesn't mean the read-only Aurora Replica DB instances. For example, when an Aurora cluster accepts incoming replication from an external source, the Aurora primary instance acts as the read replica for binlog replication. 

For more details about the stored procedures mentioned in this section, see [Aurora MySQL stored procedure reference](AuroraMySQL.Reference.StoredProcs.md). 

**To disable GTID-based replication for an Aurora MySQL DB cluster**

1. On the Aurora replicas, run the following procedure:

   For version 3

   ```
   CALL mysql.rds_set_source_auto_position(0);
   ```

   For version 2

   ```
   CALL mysql.rds_set_master_auto_position(0);
   ```

1. Reset the `gtid_mode` to `ON_PERMISSIVE`.

   1. Make sure that the DB cluster parameter group associated with the Aurora MySQL cluster has `gtid_mode` set to `ON_PERMISSIVE`.

      For more information about setting configuration parameters using parameter groups, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md).

   1. Restart the Aurora MySQL DB cluster.

1. Reset the `gtid_mode` to `OFF_PERMISSIVE`.

   1. Make sure that the DB cluster parameter group associated with the Aurora MySQL cluster has `gtid_mode` set to `OFF_PERMISSIVE`.

   1. Restart the Aurora MySQL DB cluster.

1. Wait for all of the GTID transactions to be applied on the Aurora primary instance. To check that these are applied, do the following steps:

   1. On the Aurora primary instance, run the `SHOW MASTER STATUS` command.

      Your output should be similar to the following output.

      ```
      File                        Position
      ------------------------------------
      mysql-bin-changelog.000031      107
      ------------------------------------
      ```

      Note the file and position in your output.

   1. On each read replica, use the file and position information from its source instance in the previous step to run the following query:

      For version 3

      ```
      SELECT SOURCE_POS_WAIT('{{file}}', {{position}});
      ```

      For version 2

      ```
      SELECT MASTER_POS_WAIT('{{file}}', {{position}});
      ```

      For example, if the file name is `mysql-bin-changelog.000031` and the position is `107`, run the following statement:

      For version 3

      ```
      SELECT SOURCE_POS_WAIT('mysql-bin-changelog.000031', 107);
      ```

      For version 2

      ```
      SELECT MASTER_POS_WAIT('mysql-bin-changelog.000031', 107);
      ```

1. Reset the GTID parameters to disable GTID-based replication.

   1. Make sure that the DB cluster parameter group associated with the Aurora MySQL cluster has the following parameter settings:
      + `gtid_mode` – `OFF`
      + `enforce_gtid_consistency` – `OFF`

   1. Restart the Aurora MySQL DB cluster.