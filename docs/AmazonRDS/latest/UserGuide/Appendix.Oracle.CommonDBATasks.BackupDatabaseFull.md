

# Performing a full database backup
<a name="Appendix.Oracle.CommonDBATasks.BackupDatabaseFull"></a>

You can perform a backup of all blocks of data files included in the backup using Amazon RDS procedure `rdsadmin.rdsadmin_rman_util.backup_database_full`.

This procedure uses the following common parameters for RMAN tasks:
+ `p_owner`
+ `p_directory_name`
+ `p_label`
+ `p_parallel`
+ `p_section_size_mb`
+ `p_include_archive_logs`
+ `p_optimize`
+ `p_compress`
+ `p_rman_to_dbms_output`
+ `p_tag`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md).

This procedure is supported for the following Amazon RDS for Oracle DB engine versions:
+ Oracle Database 26ai (26.0.0)
+ Oracle Database 21c (21.0.0)
+ Oracle Database 19c (19.0.0)

**Note**  
Before running a backup, ensure the target directory exists. To create a directory: `EXEC rdsadmin.rdsadmin_util.create_directory('MYDIRECTORY');`

The following example performs a full backup of the DB instance using the specified values for the parameters.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.backup_database_full(
        p_owner               => '{{SYS}}', 
        p_directory_name      => '{{MYDIRECTORY}}',
        p_parallel            => {{4}},  
        p_section_size_mb     => {{10}},
        p_tag                 => '{{FULL_DB_BACKUP}}',
        p_rman_to_dbms_output => {{FALSE}});
END;
/
```

To verify the backup completed and list the output files:

```
SELECT FILENAME, FILESIZE FROM TABLE(rdsadmin.rds_file_util.listdir('MYDIRECTORY'));
```