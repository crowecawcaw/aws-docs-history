# Performing an incremental backup of a tenant database

You can perform an incremental backup of the current tenant database in your CDB.
Use the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.backup_tenant_incremental`.

For more information about incremental backups, see [Incremental backups](https://docs.oracle.com/database/121/RCMRF/rcmsynta006.htm#GUID-73642FF2-43C5-48B2-9969-99001C52EB50__BGBHABHH "https://docs.oracle.com/database/121/RCMRF/rcmsynta006.htm#GUID-73642FF2-43C5-48B2-9969-99001C52EB50__BGBHABHH") in the Oracle Database documentation.

This procedure applies only to the current tenant database and uses the following
common parameters for RMAN tasks:

- `p_owner`
- `p_directory_name`
- `p_label`
- `p_parallel`
- `p_section_size_mb`
- `p_include_archive_logs`
- `p_include_controlfile`
- `p_optimize`
- `p_compress`
- `p_rman_to_dbms_output`
- `p_tag`
  For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md").

This procedure is supported for the following Amazon RDS for Oracle DB engine versions:

- Oracle Database 21c (21.0.0) CDB
- Oracle Database 19c (19.0.0) CDB
  This procedure also uses the following additional parameter.

| Parameter name | Data type | Valid values | Default | Required | Description                                                                                                          |
| -------------- | --------- | ------------ | ------- | -------- | -------------------------------------------------------------------------------------------------------------------- |
| `p_level`      | number    | `0`, `1`     | `0`     | No       | Specify `0` to enable a full incremental<br>backup.<br>Specify `1` to enable a non-cumulative incremental<br>backup. |

The following example performs an incremental backup of the current tenant
database using the specified values for the parameters.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.backup_tenant_incremental(
        p_owner               => '`SYS`',
        p_directory_name      => '`MYDIRECTORY`',
        p_level               => `1`,
        p_parallel            => `4`,
        p_section_size_mb     => `10`,
        p_tag                 => '`MY_INCREMENTAL_BACKUP`',
        p_rman_to_dbms_output => `FALSE`);
END;
/
```
