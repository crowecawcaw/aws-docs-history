# Checking your data after the

update of the time zone file

We recommend that you check your data after you update the time zone file. During the prepare step, RDS for
Oracle automatically creates the following tables:

- `rdsadmin.rds_dst_affected_tables` – Lists the tables that contain data affected by the
  update
- `rdsadmin.rds_dst_error_table` – Lists the errors generated during the update
  These tables are independent of any tables that you create in the prepare window. To see the results of the
  update, query the tables as follows.

```
SELECT * FROM rdsadmin.rds_dst_affected_tables;
SELECT * FROM rdsadmin.rds_dst_error_table;
```

For more information about the schema for the affected data and error tables, see [FIND_AFFECTED_TABLES Procedure](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DST.html#GUID-1F977505-671C-4D5B-8570-86956F136199 "https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DST.html#GUID-1F977505-671C-4D5B-8570-86956F136199") in the Oracle documentation.
