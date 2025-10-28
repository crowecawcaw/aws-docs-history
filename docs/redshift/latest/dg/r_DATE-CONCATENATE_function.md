Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# + (Concatenation) operator

Concatenates a DATE to a TIME or TIMETZ on either side of the + symbol and returns a TIMESTAMP or TIMESTAMPTZ.

## Syntax

```
*date* + {*time* | *timetz*}
```

The order of the arguments can be reversed. For example, _time_ + _date_.

## Arguments

_date_

A column of data type `DATE` or an expression that implicitly
evaluates to a `DATE` type.

_time_

A column of data type `TIME` or an expression that implicitly
evaluates to a `TIME` type.

_timetz_

A column of data type `TIMETZ` or an expression that implicitly
evaluates to a `TIMETZ` type.

## Return type

TIMESTAMP if input is _date_ + _time_.

TIMESTAMPTZ if input is _date_ + _timetz_.

## Examples

### Example setup

To set up the TIME_TEST and TIMETZ_TEST tables used in the examples, use the following command.

```
create table time_test(time_val time);

insert into time_test values
('20:00:00'),
('00:00:00.5550'),
('00:58:00');

create table timetz_test(timetz_val timetz);

insert into timetz_test values
('04:00:00+00'),
('00:00:00.5550+00'),
('05:58:00+00');
```

### Examples with a time column

The following example table TIME_TEST has a column TIME_VAL (type TIME) with three
values inserted.

```
`select time_val from time_test;`

`time_val
---------------------
20:00:00
00:00:00.5550
00:58:00`
```

The following example concatenates a date literal and a TIME_VAL column.

```
`select date '2000-01-02' + time_val as ts from time_test;`

`ts
---------------------
2000-01-02 20:00:00
2000-01-02 00:00:00.5550
2000-01-02 00:58:00`
```

The following example concatenates a date literal and a time literal.

```
`select date '2000-01-01' + time '20:00:00' as ts;`

 `ts
---------------------
 2000-01-01 20:00:00`
```

The following example concatenates a time literal and a date literal.

```
`select time '20:00:00' + date '2000-01-01' as ts;`

 `ts
---------------------
 2000-01-01 20:00:00`
```

### Examples with a TIMETZ column

The following example table TIMETZ_TEST has a column TIMETZ_VAL (type TIMETZ) with
three values inserted.

```
`select timetz_val from timetz_test;`

`timetz_val
------------------
04:00:00+00
00:00:00.5550+00
05:58:00+00`
```

The following example concatenates a date literal and a TIMETZ_VAL column.

```
`select date '2000-01-01' + timetz_val as ts from timetz_test;`
`ts
---------------------
2000-01-01 04:00:00+00
2000-01-01 00:00:00.5550+00
2000-01-01 05:58:00+00`
```

The following example concatenates a TIMETZ_VAL column and a date literal.

```
`select timetz_val + date '2000-01-01' as ts from timetz_test;`
`ts
---------------------
2000-01-01 04:00:00+00
2000-01-01 00:00:00.5550+00
2000-01-01 05:58:00+00`
```

The following example concatenates a DATE literal and a TIMETZ literal. The example returns a TIMESTAMPTZ which is in the time zone UTC by default. UTC is 8 hours ahead of PST, so the result is 8 hours ahead of the input time.

```
`select date '2000-01-01' + timetz '20:00:00 PST' as ts;`

 `ts
------------------------
 2000-01-02 04:00:00+00`
```
