# Validating database files in RDS for Oracle

You can use the Amazon RDS package `rdsadmin.rdsadmin_rman_util` to validate
Amazon RDS for Oracle database files, such as data files, tablespaces, control files, and
server parameter files (SPFILEs).

For more information about RMAN validation, see [Validating database files and backups](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/validating-database-files-and-backups.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/validating-database-files-and-backups.html") and [VALIDATE](https://docs.oracle.com/en/database/oracle/oracle-database/19/rcmrf/VALIDATE.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/rcmrf/VALIDATE.html") in the Oracle documentation.

###### Topics

- [Validating a database](#Appendix.Oracle.CommonDBATasks.ValidateDB "#Appendix.Oracle.CommonDBATasks.ValidateDB")
- [Validating a tenant database](#Appendix.Oracle.CommonDBATasks.ValidateTenantDB "#Appendix.Oracle.CommonDBATasks.ValidateTenantDB")
- [Validating a tablespace](#Appendix.Oracle.CommonDBATasks.ValidateTablespace "#Appendix.Oracle.CommonDBATasks.ValidateTablespace")
- [Validating a control file](#Appendix.Oracle.CommonDBATasks.ValidateControlFile "#Appendix.Oracle.CommonDBATasks.ValidateControlFile")
- [Validating an SPFILE](#Appendix.Oracle.CommonDBATasks.ValidateSpfile "#Appendix.Oracle.CommonDBATasks.ValidateSpfile")
- [Validating an Oracle data file](#Appendix.Oracle.CommonDBATasks.ValidateDataFile "#Appendix.Oracle.CommonDBATasks.ValidateDataFile")

## Validating a database

To validate all of the relevant files used by an Oracle database in RDS for Oracle,
use the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.validate_database`.

This procedure uses the following common parameters for RMAN tasks:

- `p_validation_type`
- `p_parallel`
- `p_section_size_mb`
- `p_rman_to_dbms_output`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md "Appendix.Oracle.CommonDBATasks.CommonParameters.md").

The following example validates the database using the default values for the
parameters.

```
EXEC rdsadmin.rdsadmin_rman_util.validate_database;
```

The following example validates the database using the specified values for
the parameters.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.validate_database(
        p_validation_type     => '`PHYSICAL+LOGICAL`',
        p_parallel            => `4`,
        p_section_size_mb     => `10`,
        p_rman_to_dbms_output => `FALSE`);
END;
/
```

When the `p_rman_to_dbms_output` parameter is set to
`FALSE`, the RMAN output is written to a file in the
`BDUMP` directory.

To view the files in the `BDUMP` directory, run the following
`SELECT` statement.

```
SELECT * FROM table(rdsadmin.rds_file_util.listdir('BDUMP')) order by mtime;
```

To view the contents of a file in the `BDUMP` directory, run the
following `SELECT` statement.

```
SELECT text FROM table(rdsadmin.rds_file_util.read_text_file('BDUMP','rds-rman-validate-`nnn`.txt'));
```

Replace the file name with the name of the file you want to view.

## Validating a tenant database

To validate the data files of the tenant database in a container database
(CDB), use the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.validate_tenant`.

This procedure applies only to the current tenant database and uses the
following common parameters for RMAN tasks:

- `p_validation_type`
- `p_parallel`
- `p_section_size_mb`
- `p_rman_to_dbms_output`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md "Appendix.Oracle.CommonDBATasks.CommonParameters.md"). This
procedure is supported for the following DB engine versions:

- Oracle Database 26ai (26.0.0) CDB
- Oracle Database 21c (21.0.0) CDB
- Oracle Database 19c (19.0.0) CDB

The following example validates the current tenant database using the default
values for the parameters.

```
EXEC rdsadmin.rdsadmin_rman_util.validate_tenant;
```

The following example validates the current tenant database using the
specified values for the parameters.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.validate_tenant(
        p_validation_type     => '`PHYSICAL+LOGICAL`',
        p_parallel            => `4`,
        p_section_size_mb     => `10`,
        p_rman_to_dbms_output => `FALSE`);
END;
/
```

When the `p_rman_to_dbms_output` parameter is set to
`FALSE`, the RMAN output is written to a file in the
`BDUMP` directory.

To view the files in the `BDUMP` directory, run the following
`SELECT` statement.

```
SELECT * FROM table(rdsadmin.rds_file_util.listdir('BDUMP')) order by mtime;
```

To view the contents of a file in the `BDUMP` directory, run the
following `SELECT` statement.

```
SELECT text FROM table(rdsadmin.rds_file_util.read_text_file('BDUMP','rds-rman-validate-`nnn`.txt'));
```

Replace the file name with the name of the file you want to view.

## Validating a tablespace

To validate the files associated with a tablespace, use the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.validate_tablespace`.

This procedure uses the following common parameters for RMAN tasks:

- `p_validation_type`
- `p_parallel`
- `p_section_size_mb`
- `p_rman_to_dbms_output`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md "Appendix.Oracle.CommonDBATasks.CommonParameters.md").

This procedure also uses the following additional parameter.

| Parameter name      | Data type | Valid values            | Default | Required | Description                 |
| ------------------- | --------- | ----------------------- | ------- | -------- | --------------------------- |
| `p_tablespace_name` | varchar2  | A valid tablespace name | —       | Yes      | The name of the tablespace. |

## Validating a control file

To validate only the control file used by an Amazon RDS Oracle DB instance, use the
Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.validate_current_controlfile`.

This procedure uses the following common parameter for RMAN tasks:

- `p_validation_type`
- `p_rman_to_dbms_output`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md "Appendix.Oracle.CommonDBATasks.CommonParameters.md").

## Validating an SPFILE

To validate only the server parameter file (SPFILE) used by an Amazon RDS Oracle DB
instance, use the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.validate_spfile`.

This procedure uses the following common parameter for RMAN tasks:

- `p_validation_type`
- `p_rman_to_dbms_output`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md "Appendix.Oracle.CommonDBATasks.CommonParameters.md").

## Validating an Oracle data file

To validate a data file, use the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.validate_datafile`.

This procedure uses the following common parameters for RMAN tasks:

- `p_validation_type`
- `p_parallel`
- `p_section_size_mb`
- `p_rman_to_dbms_output`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md "Appendix.Oracle.CommonDBATasks.CommonParameters.md").

This procedure also uses the following additional parameters.

| Parameter name | Data type | Valid values                                                                   | Default | Required | Description                                                                                                                                    |
| -------------- | --------- | ------------------------------------------------------------------------------ | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `p_datafile`   | varchar2  | A valid datafile ID number or a valid datafile name<br>including complete path | —       | Yes      | The datafile ID number (from<br>`v$datafile.file#`) or the full datafile name<br>including the path (from<br>`v$datafile.name`).               |
| `p_from_block` | number    | A valid integer                                                                | `NULL`  | No       | The number of the block where the validation starts within<br>the data file. When this is `NULL`,<br>`1` is used.                              |
| `p_to_block`   | number    | A valid integer                                                                | `NULL`  | No       | The number of the block where the validation ends within<br>the data file. When this is `NULL`, the maximum<br>block in the data file is used. |
