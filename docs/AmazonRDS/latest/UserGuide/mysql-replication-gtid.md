# Enabling GTID-based replication for existing read replicas for RDS for MySQL

For an existing MySQL DB instance with read replicas that doesn't use GTID-based replication, you can configure GTID-based
replication between the DB instance and the read replicas.

###### To enable GTID-based replication for existing read replicas

1. If the DB instance or any read replica is using an 8.0 version of RDS for MySQL
   version lower than 8.0.26, upgrade the DB instance or read replica to 8.0.26 or
   a higher MySQL 8.0 version. All RDS for MySQL 8.4 versions and 5.7 versions support
   GTID-based replication.

For more information, see [Upgrades of the RDS for MySQL DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md"). 2. (Optional) Reset the GTID parameters and test the behavior of the DB instance
and read replicas:

    1. Make sure that the parameter group associated with the DB instance and
     each read replica has the `enforce_gtid_consistency`
     parameter set to `WARN`.


    For more information about setting configuration parameters using parameter groups, see
     [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
    2. If you changed the parameter group of the DB instance, reboot the DB
     instance. If you changed the parameter group for a read replica, reboot
     the read replica.


    For more information, see [Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").
    3. Run your DB instance and read replicas with your normal workload and
     monitor the log files.


    If you see warnings about GTID-incompatible transactions, adjust
     your application so that it only uses GTID-compatible features. Make
     sure that the DB instance is not generating any warnings about
     GTID-incompatible transactions before proceeding to the next
     step.

3. Reset the GTID parameters for GTID-based replication that allows anonymous
   transactions until the read replicas have processed all of them.
   1. Make sure that the parameter group associated with the DB instance and
      each read replica has the following parameter settings:
      - `gtid_mode` – `ON_PERMISSIVE`
      - `enforce_gtid_consistency` – `ON`

   2. If you changed the parameter group of the DB instance, reboot the DB
      instance. If you changed the parameter group for a read replica, reboot
      the read replica.

4. Wait for all of your anonymous transactions to be replicated. To check
   that these are replicated, do the following:
   1. Run the following statement on your source DB instance.

   **MySQL 8.4**

   ```
   SHOW BINARY LOG STATUS;
   ```

   **MySQL 5.7 and 8.0**

   ```
   SHOW MASTER STATUS;
   ```

   Note the values in the `File` and `Position`
   columns. 2. On each read replica, use the file and position information from its
   source instance in the previous step to run the following query.

   ```
   SELECT MASTER_POS_WAIT('`file`', `position`);
   ```

   For example, if the file name is `mysql-bin-changelog.000031` and the position is `107`, run the following statement.

   ```
   SELECT MASTER_POS_WAIT('mysql-bin-changelog.000031', 107);
   ```

   If the read replica is past the specified position, the query returns
   immediately. Otherwise, the function waits. Proceed to the next step
   when the query returns for all read replicas.

5. Reset the GTID parameters for GTID-based replication only.
   1. Make sure that the parameter group associated with the DB instance and
      each read replica has the following parameter settings:
      - `gtid_mode` – `ON`
      - `enforce_gtid_consistency` – `ON`

   2. Reboot the DB instance and each read replica.

6. On each read replica, run the following procedure.

**MySQL 8.4 and higher major versions**

```
CALL mysql.rds_set_source_auto_position(1);
```

**MySQL 8.0 and lower major versions**

```
CALL mysql.rds_set_master_auto_position(1);
```
