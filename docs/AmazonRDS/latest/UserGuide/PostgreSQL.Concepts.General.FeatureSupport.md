# RAM disk for

the stats_temp_directory

You can use the RDS for PostgreSQL parameter `rds.pg_stat_ramdisk_size` to
specify the system memory allocated to a RAM disk for storing the PostgreSQL
`stats_temp_directory`. The RAM disk parameter is only available in
RDS for PostgreSQL version 14 and lower versions.

Under certain workloads, setting this parameter can improve performance and
decrease I/O requirements. For more information about the
`stats_temp_directory`, see [the PostgreSQL documentation.](https://www.postgresql.org/docs/current/static/runtime-config-statistics.html#GUC-STATS-TEMP-DIRECTORY "https://www.postgresql.org/docs/current/static/runtime-config-statistics.html#GUC-STATS-TEMP-DIRECTORY").

To set up a RAM disk for your `stats_temp_directory`, set the
`rds.pg_stat_ramdisk_size` parameter to an integer literal value in
the parameter group used by your DB instance. This parameter denotes MB, so you must
use an integer value. Expressions, formulas, and functions aren't valid for the
`rds.pg_stat_ramdisk_size` parameter. Be sure to reboot the DB
instance so that the change takes effect. For information about setting parameters,
see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

For example, the following AWS CLI command sets the RAM disk parameter to 256
MB.

```
aws rds modify-db-parameter-group \
    --db-parameter-group-name pg-95-ramdisk-testing \
    --parameters "ParameterName=rds.pg_stat_ramdisk_size, ParameterValue=256, ApplyMethod=pending-reboot"
```

After you reboot, run the following command to see the status of the
`stats_temp_directory`.

```
`postgres=>` `SHOW stats_temp_directory;`
```

The command should return the following.

```
stats_temp_directory
---------------------------
/rdsdbramdisk/pg_stat_tmp
(1 row)
```
