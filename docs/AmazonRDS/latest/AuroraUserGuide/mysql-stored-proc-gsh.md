# Collecting and maintaining the Global Status History

Amazon RDS provides a set of procedures that take snapshots of the values of status variables over time and write them to a table,
along with any changes since the last snapshot. This infrastructure is called Global Status History. For more information, see
[Managing the Global
Status History](../UserGuide/Appendix.MySQL.md#Appendix.MySQL.CommonDBATasks.GoSH "../UserGuide/Appendix.MySQL.md#Appendix.MySQL.CommonDBATasks.GoSH").

The following stored procedures manage how the Global Status History is collected and maintained.

###### Topics

- [mysql.rds_collect_global_status_history](#mysql_rds_collect_global_status_history "#mysql_rds_collect_global_status_history")
- [mysql.rds_disable_gsh_collector](#mysql_rds_disable_gsh_collector "#mysql_rds_disable_gsh_collector")
- [mysql.rds_disable_gsh_rotation](#mysql_rds_disable_gsh_rotation "#mysql_rds_disable_gsh_rotation")
- [mysql.rds_enable_gsh_collector](#mysql_rds_enable_gsh_collector "#mysql_rds_enable_gsh_collector")
- [mysql.rds_enable_gsh_rotation](#mysql_rds_enable_gsh_rotation "#mysql_rds_enable_gsh_rotation")
- [mysql.rds_rotate_global_status_history](#mysql_rds_rotate_global_status_history "#mysql_rds_rotate_global_status_history")
- [mysql.rds_set_gsh_collector](#mysql_rds_set_gsh_collector "#mysql_rds_set_gsh_collector")
- [mysql.rds_set_gsh_rotation](#mysql_rds_set_gsh_rotation "#mysql_rds_set_gsh_rotation")

## mysql.rds_collect_global_status_history

Takes a snapshot on demand for the Global Status History.

### Syntax

```
CALL mysql.rds_collect_global_status_history;
```

## mysql.rds_disable_gsh_collector

Turns off snapshots taken by the Global Status History.

### Syntax

```
CALL mysql.rds_disable_gsh_collector;
```

## mysql.rds_disable_gsh_rotation

Turns off rotation of the `mysql.global_status_history` table.

### Syntax

```
CALL mysql.rds_disable_gsh_rotation;
```

## mysql.rds_enable_gsh_collector

Turns on the Global Status History to take default snapshots at intervals specified by
`rds_set_gsh_collector`.

### Syntax

```
CALL mysql.rds_enable_gsh_collector;
```

## mysql.rds_enable_gsh_rotation

Turns on rotation of the contents of the `mysql.global_status_history` table to
`mysql.global_status_history_old` at intervals specified by `rds_set_gsh_rotation`.

### Syntax

```
CALL mysql.rds_enable_gsh_rotation;
```

## mysql.rds_rotate_global_status_history

Rotates the contents of the `mysql.global_status_history` table to `mysql.global_status_history_old` on
demand.

### Syntax

```
CALL mysql.rds_rotate_global_status_history;
```

## mysql.rds_set_gsh_collector

Specifies the interval, in minutes, between snapshots taken by the Global Status History.

### Syntax

```
CALL mysql.rds_set_gsh_collector(`intervalPeriod`);
```

### Parameters

`intervalPeriod`

The interval, in minutes, between snapshots. Default value is
`5`.

## mysql.rds_set_gsh_rotation

Specifies the interval, in days, between rotations of the `mysql.global_status_history` table.

### Syntax

```
CALL mysql.rds_set_gsh_rotation(`intervalPeriod`);
```

### Parameters

`intervalPeriod`

The interval, in days, between table rotations. Default value is
`7`.
