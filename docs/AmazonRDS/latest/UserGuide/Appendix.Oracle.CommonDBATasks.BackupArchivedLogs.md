# Backing up archived redo log files

You can use the Amazon RDS package `rdsadmin.rdsadmin_rman_util` to back up archived redo logs for an
Amazon RDS Oracle DB instance.

The procedures for backing up archived redo logs are supported for the following Amazon RDS for Oracle DB engine
versions:

- Oracle Database 26ai (26.0.0)
- Oracle Database 21c (21.0.0)
- Oracle Database 19c (19.0.0)

###### Topics

- [Backing up all archived redo logs](#Appendix.Oracle.CommonDBATasks.BackupArchivedLogs.All "#Appendix.Oracle.CommonDBATasks.BackupArchivedLogs.All")
- [Backing up an archived redo log from a date range](#Appendix.Oracle.CommonDBATasks.BackupArchivedLogs.Date "#Appendix.Oracle.CommonDBATasks.BackupArchivedLogs.Date")
- [Backing up an archived redo log from an SCN range](#Appendix.Oracle.CommonDBATasks.BackupArchivedLogs.SCN "#Appendix.Oracle.CommonDBATasks.BackupArchivedLogs.SCN")
- [Backing up an archived redo log from a sequence number range](#Appendix.Oracle.CommonDBATasks.BackupArchivedLogs.Sequence "#Appendix.Oracle.CommonDBATasks.BackupArchivedLogs.Sequence")

## Backing up all archived redo logs

To back up all of the archived redo logs for an Amazon RDS Oracle DB instance, use
the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.backup_archivelog_all`.

This procedure uses the following common parameters for RMAN tasks:

- `p_owner`
- `p_directory_name`
- `p_label`
- `p_parallel`
- `p_compress`
- `p_rman_to_dbms_output`
- `p_tag`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md "Appendix.Oracle.CommonDBATasks.CommonParameters.md").

The following example backs up all archived redo logs for the DB
instance.

```

BEGIN
    rdsadmin.rdsadmin_rman_util.backup_archivelog_all(
        p_owner               => '`SYS`',
        p_directory_name      => '`MYDIRECTORY`',
        p_parallel            => `4`,
        p_tag                 => '`MY_LOG_BACKUP`',
        p_rman_to_dbms_output => `FALSE`);
END;
/

```

## Backing up an archived redo log from a date range

To back up specific archived redo logs for an Amazon RDS Oracle DB instance by
specifying a date range, use the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.backup_archivelog_date`. The date
range specifies which archived redo logs to back up.

This procedure uses the following common parameters for RMAN tasks:

- `p_owner`
- `p_directory_name`
- `p_label`
- `p_parallel`
- `p_compress`
- `p_rman_to_dbms_output`
- `p_tag`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md "Appendix.Oracle.CommonDBATasks.CommonParameters.md").

This procedure also uses the following additional parameters.

| Parameter name | Data type | Valid values                                                                                                                                                                                    | Default | Required | Description                                     |
| -------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | ----------------------------------------------- |
| `p_from_date`  | date      | A date that is between the `start_date` and<br>`next_date` of an archived redo log that<br>exists on disk. The value must be less than or equal to the<br>value specified for `p_to_date`.      | —       | Yes      | The starting date for the archived log backups. |
| `p_to_date`    | date      | A date that is between the `start_date` and<br>`next_date` of an archived redo log that<br>exists on disk. The value must be greater than or equal to<br>the value specified for `p_from_date`. | —       | Yes      | The ending date for the archived log backups.   |

The following example backs up archived redo logs in the date range for the DB
instance.

```

BEGIN
    rdsadmin.rdsadmin_rman_util.backup_archivelog_date(
        p_owner               => '`SYS`',
        p_directory_name      => '`MYDIRECTORY`',
        p_from_date           => '`03/01/2019 00:00:00`',
        p_to_date             => '`03/02/2019 00:00:00`',
        p_parallel            => `4`,
        p_tag                 => '`MY_LOG_BACKUP`',
        p_rman_to_dbms_output => `FALSE`);
END;
/

```

## Backing up an archived redo log from an SCN range

To back up specific archived redo logs for an Amazon RDS Oracle DB instance by
specifying a system change number (SCN) range, use the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.backup_archivelog_scn`. The SCN
range specifies which archived redo logs to back up.

This procedure uses the following common parameters for RMAN tasks:

- `p_owner`
- `p_directory_name`
- `p_label`
- `p_parallel`
- `p_compress`
- `p_rman_to_dbms_output`
- `p_tag`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md "Appendix.Oracle.CommonDBATasks.CommonParameters.md").

This procedure also uses the following additional parameters.

| Parameter name | Data type | Valid values                                                                                                                               | Default | Required | Description                                    |
| -------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------- | ---------------------------------------------- |
| `p_from_scn`   | number    | An SCN of an archived redo log that exists on disk. The<br>value must be less than or equal to the value specified for<br>`p_to_scn`.      | —       | Yes      | The starting SCN for the archived log backups. |
| `p_to_scn`     | number    | An SCN of an archived redo log that exists on disk. The<br>value must be greater than or equal to the value specified<br>for `p_from_scn`. | —       | Yes      | The ending SCN for the archived log backups.   |

The following example backs up archived redo logs in the SCN range for the DB
instance.

```

BEGIN
    rdsadmin.rdsadmin_rman_util.backup_archivelog_scn(
        p_owner               => '`SYS`',
        p_directory_name      => '`MYDIRECTORY`',
        p_from_scn            => `1533835`,
        p_to_scn              => `1892447`,
        p_parallel            => `4`,
        p_tag                 => '`MY_LOG_BACKUP`',
        p_rman_to_dbms_output => `FALSE`);
END;
/

```

## Backing up an archived redo log from a sequence number range

To back up specific archived redo logs for an Amazon RDS Oracle DB instance by
specifying a sequence number range, use the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.backup_archivelog_sequence`. The
sequence number range specifies which archived redo logs to back up.

This procedure uses the following common parameters for RMAN tasks:

- `p_owner`
- `p_directory_name`
- `p_label`
- `p_parallel`
- `p_compress`
- `p_rman_to_dbms_output`
- `p_tag`

For more information, see [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md "Appendix.Oracle.CommonDBATasks.CommonParameters.md").

This procedure also uses the following additional parameters.

| Parameter name    | Data type | Valid values                                                                                                                                               | Default | Required | Description                                                   |
| ----------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | ------------------------------------------------------------- |
| `p_from_sequence` | number    | A sequence number an archived redo log that exists on<br>disk. The value must be less than or equal to the value<br>specified for `p_to_sequence`.         | —       | Yes      | The starting sequence number for the archived log<br>backups. |
| `p_to_sequence`   | number    | A sequence number of an archived redo log that exists on<br>disk. The value must be greater than or equal to the value<br>specified for `p_from_sequence`. | —       | Yes      | The ending sequence number for the archived log<br>backups.   |

The following example backs up archived redo logs in the sequence number range
for the DB instance.

```
BEGIN
    rdsadmin.rdsadmin_rman_util.backup_archivelog_sequence(
        p_owner               => '`SYS`',
        p_directory_name      => '`MYDIRECTORY`',
        p_from_sequence       => `11160`,
        p_to_sequence         => `11160`,
        p_parallel            => `4`,
        p_tag                 => '`MY_LOG_BACKUP`',
        p_rman_to_dbms_output => `FALSE`);
END;
/
```
