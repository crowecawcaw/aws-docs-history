# Working with trace and

dump files for Amazon RDS for SQL Server

This section describes working with trace files and dump files for your Amazon RDS DB
instances running Microsoft SQL Server.

## Generating a trace SQL query

```
declare @rc int
declare @TraceID int
declare @maxfilesize bigint

set @maxfilesize = 5

exec @rc = sp_trace_create @TraceID output,  0, N'D:\rdsdbdata\log\rdstest', @maxfilesize, NULL
```

## Viewing

an open trace

```
select * from ::fn_trace_getinfo(default)
```

## Viewing trace contents

```
select * from ::fn_trace_gettable('D:\rdsdbdata\log\rdstest.trc', default)
```

## Setting the retention period for trace and dump files

Trace and dump files can accumulate and consume disk space. By default, Amazon RDS
purges trace and dump files that are older than seven days.

To view the current trace and dump file retention period, use the
`rds_show_configuration` procedure, as shown in the following
example.

```
exec rdsadmin..rds_show_configuration;
```

To modify the retention period for trace files, use the
`rds_set_configuration` procedure and set the `tracefile
 retention` in minutes. The following example sets the trace file retention
period to 24 hours.

```
exec rdsadmin..rds_set_configuration 'tracefile retention', `1440`;
```

To modify the retention period for dump files, use the
`rds_set_configuration` procedure and set the `dumpfile
 retention` in minutes. The following example sets the dump file retention
period to 3 days.

```
exec rdsadmin..rds_set_configuration 'dumpfile retention', `4320`;
```

For security reasons, you cannot delete a specific trace or dump file on a SQL
Server DB instance. To delete all unused trace or dump files, set the retention
period for the files to 0.
