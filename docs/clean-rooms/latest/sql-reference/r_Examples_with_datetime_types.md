# Examples with datetime types

The following examples show you how to work with datetime types that are supported by
AWS Clean Rooms.

## Date examples

The following examples insert dates that have different formats and display the
output.

```
`select * from datetable order by 1;

start_date | end_date
-----------------------
2008-06-01 | 2008-12-31
2008-06-01 | 2008-12-31`
```

If you insert a timestamp value into a DATE column, the time portion is ignored
and only the date is loaded.

## Time examples

The following examples insert TIME and TIMETZ values that have different formats
and display the output.

```
`select * from timetable order by 1;
start_time | end_time
------------------------
 19:11:19 | 20:41:19+00
 19:11:19 | 20:41:19+00`
```

## Time stamp

examples

If you insert a date into a TIMESTAMP or TIMESTAMPTZ column, the time defaults to
midnight. For example, if you insert the literal `20081231`, the stored
value is `2008-12-31 00:00:00`.

The following examples insert timestamps that have different formats and display
the output.

```
`timeofday
---------------------
2008-06-01 09:59:59
2008-12-31 18:20:00
(2 rows)`
```
