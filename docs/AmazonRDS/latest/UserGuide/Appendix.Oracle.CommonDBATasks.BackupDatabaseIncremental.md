

# Performing an incremental database backup
<a name="Appendix.Oracle.CommonDBATasks.BackupDatabaseIncremental"></a>

You can perform an incremental backup of your DB instance using the Amazon RDS procedure `rdsadmin.rdsadmin_rman_util.backup_database_incremental`.

For more information about incremental backups, see [Incremental backups](https://docs.oracle.com/en/database/oracle/oracle-database/19/rcmrf/BACKUP.html) in the Oracle documentation.

This procedure uses the following common parameters for RMAN tasks:
+ `p_owner`
+ `p_directory_name`
+ `p_label`
+ `p_parallel`
+ `p_section_size_mb`
+ `p_include_archive_logs`
+ `p_include_controlfile`
+ `p_optimize`
+ `p_compress`
+ `p_rman_to_dbms_output`
+ `p_tag`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md).

This procedure is supported for the following Amazon RDS for Oracle DB engine versions:
+ Oracle Database 26ai (26.0.0)
+ Oracle Database 21c (21.0.0)
+ Oracle Database 19c (19.0.0)

This procedure also uses the following additional parameter.



| Parameter name | Data type | Valid values | Default | Required | Description | 
| --- | --- | --- | --- | --- | --- | 
| `p_level` | number | `0`, `1` | `0` | No | Specify `0` to enable a full incremental backup.<br />Specify `1` to enable a non-cumulative incremental backup. | 

The following example performs an incremental backup of the DB instance using the specified values for the parameters.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.backup_database_incremental(
        p_owner               => '{{SYS}}', 
        p_directory_name      => '{{MYDIRECTORY}}',
        p_level               => {{1}},
        p_parallel            => {{4}},  
        p_section_size_mb     => {{10}},
        p_tag                 => '{{MY_INCREMENTAL_BACKUP}}',
        p_rman_to_dbms_output => {{FALSE}});
END;
/
```