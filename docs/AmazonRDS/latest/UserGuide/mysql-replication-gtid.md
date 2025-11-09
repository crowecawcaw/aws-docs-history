# Disabling GTID-based replication for

a MySQL DB instance with read
replicas

You can disable GTID-based replication for
a MySQL DB instance with read replicas.

###### To disable GTID-based replication for a MySQL DB instance with read replicas

1. On each read replica, run the following
   procedure:

**MySQL 8.4 and higher major versions**

```
CALL mysql.rds_set_source_auto_position(0);
```

**MySQL 8.0 and lower major
versions**

```
CALL mysql.rds_set_master_auto_position(0);
```

2. Reset the `gtid_mode` to `ON_PERMISSIVE`.
   1. Make sure that the parameter group associated
      with the MySQL DB instance and each read replica has
      `gtid_mode` set to `ON_PERMISSIVE`.

   For more information about setting configuration parameters using parameter groups, see
   [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 2. Reboot the MySQL DB instance and each read
   replica. For more information about rebooting, see [Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").

3. Reset the `gtid_mode` to `OFF_PERMISSIVE`.
   1. Make sure that the parameter group associated
      with the MySQL DB instance and each read replica has
      `gtid_mode` set to `OFF_PERMISSIVE`.
   2. Reboot the MySQL DB instance and each read
      replica.

4. Wait for all of the GTID transactions to be applied on
   all of the read replicas. To check that these are applied, do the following
   steps:
   1. On the MySQL DB
      instance, run the following command:

   **MySQL 8.4**

   ```
   SHOW BINARY LOG STATUS
   ```

   **MySQL 5.7 and 8.0**

   ```
   SHOW MASTER STATUS
   ```

   Your output should be similar to the following output.

   ```

   File                        Position
   ------------------------------------
   mysql-bin-changelog.000031      107
   ------------------------------------

   ```

   Note the file and position in your output. 2. On each read replica, use the file and position information from its
   source instance in the previous step to run the following query:

   **MySQL 8.4 and MySQL 8.0.26
   and higher MySQL 8.0 versions**

   ```
   SELECT SOURCE_POS_WAIT('`file`', `position`);
   ```

   **MySQL
   5.7**

   ```
   SELECT MASTER_POS_WAIT('`file`', `position`);
   ```

   For example, if the file name is `mysql-bin-changelog.000031` and the position is `107`, run the following statement:

   **MySQL 8.4 and MySQL 8.0.26
   and higher MySQL 8.0 versions**

   ```
   SELECT SOURCE_POS_WAIT('mysql-bin-changelog.000031', 107);
   ```

   **MySQL
   5.7**

   ```
   SELECT MASTER_POS_WAIT('mysql-bin-changelog.000031', 107);
   ```

5. Reset the GTID parameters to disable GTID-based replication.
   1. Make sure that the parameter group associated
      with the MySQL DB instance and each read replica has the following
      parameter settings:
      - `gtid_mode` – `OFF`
      - `enforce_gtid_consistency` – `OFF`

   2. Reboot the MySQL DB instance and each read
      replica.
