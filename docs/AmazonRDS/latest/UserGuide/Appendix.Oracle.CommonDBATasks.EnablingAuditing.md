# Enabling auditing for the SYS.AUD$ table

To enable auditing on the database audit trail table `SYS.AUD$`, use the Amazon RDS procedure
`rdsadmin.rdsadmin_master_util.audit_all_sys_aud_table`. The only supported audit property is
`ALL`. You can't audit or not audit individual statements or operations.

Enabling auditing is supported for Oracle DB instances running the following versions:

- Oracle Database 26ai (26.0.0)
- Oracle Database 21c (21.0.0)
- Oracle Database 19c (19.0.0)
  The `audit_all_sys_aud_table` procedure has the following
  parameters.

| Parameter name | Data type | Default | Required | Description                                                                  |
| -------------- | --------- | ------- | -------- | ---------------------------------------------------------------------------- |
| `p_by_access`  | boolean   | true    | No       | Set to `true` to audit `BY ACCESS`. Set<br>to `false` to audit `BY SESSION`. |

The following query returns the current audit configuration for
`SYS.AUD$` for a database.

```
SELECT * FROM DBA_OBJ_AUDIT_OPTS WHERE OWNER='SYS' AND OBJECT_NAME='AUD$';
```

The following commands enable audit of `ALL` on `SYS.AUD$`
`BY ACCESS`.

```
EXEC rdsadmin.rdsadmin_master_util.audit_all_sys_aud_table;

EXEC rdsadmin.rdsadmin_master_util.audit_all_sys_aud_table(p_by_access => true);
```

The following command enables audit of `ALL` on `SYS.AUD$`
`BY SESSION`.

```
EXEC rdsadmin.rdsadmin_master_util.audit_all_sys_aud_table(p_by_access => false);
```

For more information, see [AUDIT (traditional auditing)](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/AUDIT-Traditional-Auditing.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/AUDIT-Traditional-Auditing.html") in the Oracle documentation.
