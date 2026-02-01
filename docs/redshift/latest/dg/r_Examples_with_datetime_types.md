Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Examples with datetime

types

Following, you can find examples for working with datetime types supported
by Amazon Redshift.

## Date

examples

The following examples insert dates that have different formats and
display the output.

```
`create table datetable (start_date date, end_date date);`
```

```
`insert into datetable values ('2008-06-01','2008-12-31');

insert into datetable values ('Jun 1,2008','20081231');`
```

```
`select * from datetable order by 1;

start_date | end_date
-----------------------
2008-06-01 | 2008-12-31
2008-06-01 | 2008-12-31`
```

If you insert a timestamp value into a DATE column, the time portion is
ignored and only the date is loaded.

## Time

examples

The following examples insert TIME and TIMETZ values that have different
formats and display the output.

```
`create table timetable (start_time time, end_time timetz);`
```

```
`insert into timetable values ('19:11:19','20:41:19 UTC');
insert into timetable values ('191119', '204119 UTC');`
```

```
`select * from timetable order by 1;
start_time | end_time
------------------------
 19:11:19 | 20:41:19+00
 19:11:19 | 20:41:19+00`
```

## Time

stamp examples

If you insert a date into a TIMESTAMP or TIMESTAMPTZ column, the time
defaults to midnight. For example, if you insert the literal
`20081231`, the stored value is `2008-12-31
 00:00:00`.

To change the time zone for the current session, use the [SET](r_SET.md "r_SET.md") command to set the [timezone](r_timezone_config.md "r_timezone_config.md")
configuration parameter.

The following example inserts timestamps that have different formats and
display the resulting table.

```
`create table tstamp(timeofday timestamp, timeofdaytz timestamptz);

insert into tstamp values('Jun 1,2008 09:59:59', 'Jun 1,2008 09:59:59 EST' );
insert into tstamp values('Dec 31,2008 18:20','Dec 31,2008 18:20');
insert into tstamp values('Jun 1,2008 09:59:59 EST', 'Jun 1,2008 09:59:59');

SELECT * FROM tstamp;`

`+---------------------+------------------------+
| timeofday | timeofdaytz |
+---------------------+------------------------+
| 2008-06-01 09:59:59 | 2008-06-01 14:59:59+00 |
| 2008-12-31 18:20:00 | 2008-12-31 18:20:00+00 |
| 2008-06-01 09:59:59 | 2008-06-01 09:59:59+00 |
+---------------------+------------------------+`
```
