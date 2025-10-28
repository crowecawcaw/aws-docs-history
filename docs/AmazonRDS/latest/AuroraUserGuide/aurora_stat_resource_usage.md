# aurora_stat_resource_usage

Reports the real-time resource utilization which consists of backend resource metrics and cpu usage for all Aurora PostgreSQL backend processes.

## Syntax

```
aurora_stat_resource_usage()
```

## Arguments

None

## Return type

SETOF record with columns:

- pid - Process identifier
- allocated_memory - Total memory allocated by process in bytes
- used_memory - Actually used memory by process in bytes
- cpu_usage_percent - CPU usage percentage of the process

## Usage notes

This function displays the backend resource usage for each Aurora PostgreSQL backend process.

This function is available starting with the following Aurora PostgreSQL versions:

- Aurora PostgreSQL 17.5 and higher 17 versions
- Aurora PostgreSQL 16.9 and higher 16 versions
- Aurora PostgreSQL 15.13 and higher 15 versions
- Aurora PostgreSQL 14.18 and higher 14 versions
- Aurora PostgreSQL 13.21 and higher 13 versions

## Examples

The following example shows the output of the `aurora_stat_resource_usage` function.

```
`=>` `select * from aurora_stat_resource_usage();`
 `pid | allocated_memory | used_memory | cpu_usage_percent
------+------------------+-------------+-----------------------
 666 | 1074032 | 333544 | 0.00729274882897963
 667 | 787312 | 287360 | 0.0029263928146372746
 668 | 3076776 | 1563488 | 0.006013116835953961
 684 | 803744 | 307480 | 0.002226855426881142
 2401 | 1232992 | 943144 | 0
 647 | 8000 | 944 | 0.48853387812429855
 659 | 319344 | 243000 | 0.0004135602076683591
 663 | 262000 | 185736 | 0.008181301476644002
 664 | 9024 | 1216 | 0.10992313082653653
(9 rows)`
```
