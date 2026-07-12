# Backing up a control file

You can back up a control file using the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.backup_current_controlfile`.

This procedure uses the following common parameters for RMAN tasks:

- `p_owner`
- `p_directory_name`
- `p_label`
- `p_compress`
- `p_rman_to_dbms_output`
- `p_tag`
  For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md "Appendix.Oracle.CommonDBATasks.CommonParameters.md").

This procedure is supported for the following Amazon RDS for Oracle DB engine versions:

- Oracle Database 26ai (26.0.0)
- Oracle Database 21c (21.0.0)
- Oracle Database 19c (19.0.0)
  The following example backs up a control file using the specified values for the
  parameters.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.backup_current_controlfile(
        p_owner               => '`SYS`',
        p_directory_name      => '`MYDIRECTORY`',
        p_tag                 => '`CONTROL_FILE_BACKUP`',
        p_rman_to_dbms_output => `FALSE`);
END;
/
```
