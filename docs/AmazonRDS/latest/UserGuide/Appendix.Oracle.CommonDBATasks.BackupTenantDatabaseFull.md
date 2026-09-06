

# Performing a full backup of a tenant database
<a name="Appendix.Oracle.CommonDBATasks.BackupTenantDatabaseFull"></a>

You can perform a backup of all data blocks in a tenant database in a container database (CDB). Use the Amazon RDS procedure `rdsadmin.rdsadmin_rman_util.backup_tenant_full`. This procedure applies only to the current database backup and uses the following common parameters for RMAN tasks:
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

The `rdsadmin_rman_util.backup_tenant_full` procedure is supported for the following RDS for Oracle DB engine versions:
+ Oracle Database 26ai (26.0.0) CDB
+ Oracle Database 21c (21.0.0) CDB
+ Oracle Database 19c (19.0.0) CDB

The following example performs a full backup of the current tenant database using the specified values for the parameters.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.backup_tenant_full(
        p_owner               => '{{SYS}}', 
        p_directory_name      => '{{MYDIRECTORY}}',
        p_parallel            => {{4}},  
        p_section_size_mb     => {{10}},
        p_tag                 => '{{FULL_TENANT_DB_BACKUP}}',
        p_rman_to_dbms_output => {{FALSE}});
END;
/
```