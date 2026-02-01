# Crosschecking archived

redo logs

You can crosscheck archived redo logs using the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.crosscheck_archivelog`.

You can use this procedure to crosscheck the archived redo logs registered in the
control file and optionally delete the expired logs records. When RMAN makes a
backup, it creates a record in the control file. Over time, these records increase
the size of the control file. We recommend that you remove expired records
periodically.

###### Note

Standard Amazon RDS backups don't use RMAN and therefore don't create
records in the control file.

This procedure uses the common parameter `p_rman_to_dbms_output` for
RMAN tasks.

For more information, see [Common parameters
for RMAN procedures](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md").

This procedure also uses the following additional parameter.

| Parameter name     | Data type | Valid values    | Default | Required | Description                                                                                                                                                           |
| ------------------ | --------- | --------------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `p_delete_expired` | boolean   | `TRUE`, `FALSE` | `TRUE`  | No       | When `TRUE`, delete expired archived redo log<br>records from the control file.<br>When `FALSE`, retain the expired archived redo log<br>records in the control file. |

This procedure is supported for the following Amazon RDS for Oracle DB engine versions:

- Oracle Database 21c (21.0.0)
- Oracle Database 19c (19.0.0)
  The following example marks archived redo log records in the control file as
  expired, but does not delete the records.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.crosscheck_archivelog(
        p_delete_expired      => `FALSE`,
        p_rman_to_dbms_output => `FALSE`);
END;
/
```

The following example deletes expired archived redo log records from the control
file.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.crosscheck_archivelog(
        p_delete_expired      => `TRUE`,
        p_rman_to_dbms_output => `FALSE`);
END;
/
```
