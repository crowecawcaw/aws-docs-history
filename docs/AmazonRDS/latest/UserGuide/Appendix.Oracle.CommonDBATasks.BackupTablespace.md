

# Backing up a tablespace
<a name="Appendix.Oracle.CommonDBATasks.BackupTablespace"></a>

You can back up a tablespace using the Amazon RDS procedure `rdsadmin.rdsadmin_rman_util.backup_tablespace`.

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

This procedure also uses the following additional parameter.



| Parameter name | Data type | Valid values | Default | Required | Description | 
| --- | --- | --- | --- | --- | --- | 
| `p_tablespace_name` | varchar2 | A valid tablespace name. | — | Yes | The name of the tablespace to back up. | 

This procedure is supported for the following Amazon RDS for Oracle DB engine versions:
+ Oracle Database 26ai (26.0.0)
+ Oracle Database 21c (21.0.0)
+ Oracle Database 19c (19.0.0)

The following example performs a tablespace backup using the specified values for the parameters.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.backup_tablespace(
        p_owner               => '{{SYS}}', 
        p_directory_name      => '{{MYDIRECTORY}}',
        p_tablespace_name     => '{{MYTABLESPACE}}',
        p_parallel            => {{4}},  
        p_section_size_mb     => {{10}},
        p_tag                 => '{{MYTABLESPACE_BACKUP}}',
        p_rman_to_dbms_output => {{FALSE}});
END;
/
```