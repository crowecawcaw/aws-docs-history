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
