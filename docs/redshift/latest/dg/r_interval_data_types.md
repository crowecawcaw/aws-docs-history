Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Interval data types and

literals

You can use an interval data type to store durations of time in units such
as, `seconds`, `minutes`, `hours`,
`days`, `months`, and `years`. Interval
data types and literals can be used in datetime calculations, such as, adding
intervals to dates and timestamps, summing intervals, and subtracting an
interval from a date or timestamp. Interval literals can be used as input
values to interval data type columns in a table.

## Syntax of interval data

type

To specify an interval data type to store a duration of time in years and
months:

```
INTERVAL *year\_to\_month\_qualifier*
```

To specify an interval data type to store a duration in days, hours,
minutes, and seconds:

```
INTERVAL *day\_to\_second\_qualifier* [ (*fractional\_precision*) ]
```

## Syntax of interval

literal

To specify an interval literal to define a duration of time in years and
months:

```
INTERVAL *quoted-string* *year\_to\_month\_qualifier*
```

To specify an interval literal to define a duration in days, hours,
minutes, and seconds:

```
INTERVAL *quoted-string* *day\_to\_second\_qualifier* [ (*fractional\_precision*) ]
```

## Arguments

_quoted-string_

Specifies a positive or negative numeric value specifying a
quantity and the datetime unit as an input string. If the
_quoted-string_ contains only a numeric, then
Amazon Redshift determines the units from the
_year_to_month_qualifier_ or
_day_to_second_qualifier_. For example,
`'23' MONTH` represents `1 year 11
 months`, `'-2' DAY` represents `-2 days 0
 hours 0 minutes 0.0 seconds`, `'1-2' MONTH`
represents `1 year 2 months`, and `'13 day 1 hour 1
 minute 1.123 seconds' SECOND` represents `13 days 1
 hour 1 minute 1.123 seconds`. For more information about
output formats of an interval, see [Interval
styles](#r_interval_data_types-interval-styles "#r_interval_data_types-interval-styles").

_year_to_month_qualifier_

Specifies the range of the interval. If you use a qualifier and
create an interval with time units smaller than the qualifier,
Amazon Redshift truncates and discards the smaller parts of the interval.
Valid values for _year_to_month_qualifier_
are:

- `YEAR`
- `MONTH`
- `YEAR TO MONTH`

_day_to_second_qualifier_

Specifies the range of the interval. If you use a qualifier and
create an interval with time units smaller than the qualifier,
Amazon Redshift truncates and discards the smaller parts of the interval.
Valid values for _day_to_second_qualifier_
are:

- `DAY`
- `HOUR`
- `MINUTE`
- `SECOND`
- `DAY TO HOUR`
- `DAY TO MINUTE`
- `DAY TO SECOND`
- `HOUR TO MINUTE`
- `HOUR TO SECOND`
- `MINUTE TO SECOND`

The output of the INTERVAL literal is truncated to the smallest
INTERVAL component specified. For example, when using a MINUTE
qualifier, Amazon Redshift discards the time units smaller than
MINUTE.

```
select INTERVAL '1 day 1 hour 1 minute 1.123 seconds' MINUTE
```

The resulting value is truncated to `'1 day
 01:01:00'`.

_fractional_precision_

Optional parameter that specifies the number of fractional
digits allowed in the interval. The
_fractional_precision_ argument should only
be specified if your interval contains SECOND. For example,
`SECOND(3)` creates an interval that allows only
three fractional digits, such as 1.234 seconds. The maximum number
of fractional digits is six.

The session configuration `interval_forbid_composite_literals`
determines whether an error is returned when an interval is specified with
both YEAR TO MONTH and DAY TO SECOND parts. For more information, see [interval_forbid_composite_literals](r_interval_forbid_composite_literals.md "r_interval_forbid_composite_literals.md").

## Interval

arithmetic

You can use interval values with other datetime values to perform
arithmetic operations. The following tables describe the available
operations and what data type results from each operation.

###### Note

Operations that can produce both `date` and
`timestamp` results do so based on the smallest unit of
time involved in the equation. For example, when you add an
`interval` to a `date` the result is a
`date` if it is a YEAR TO MONTH interval, and a timestamp
if it is a DAY TO SECOND interval.

Operations where the first operand is an `interval` produce
the following results for the given second operand:

| Operator | Date | Timestamp      | Interval | Numeric  |
| -------- | ---- | -------------- | -------- | -------- |
| -        | N/A  | N/A            | Interval | N/A      |
| +        | Date | Date/Timestamp | Interval | N/A      |
| \*       | N/A  | N/A            | N/A      | Interval |
| /        | N/A  | N/A            | N/A      | Interval |

Operations where the first operand is a `date` produce the
following results for the given second operand:

| Operator | Date    | Timestamp | Interval       | Numeric |
| -------- | ------- | --------- | -------------- | ------- |
| -        | Numeric | Interval  | Date/Timestamp | Date    |
| +        | N/A     | N/A       | N/A            | N/A     |

Operations where the first operand is a `timestamp` produce
the following results for the given second operand:

| Operator | Date    | Timestamp | Interval  | Numeric   |
| -------- | ------- | --------- | --------- | --------- |
| -        | Numeric | Interval  | Timestamp | Timestamp |
| +        | N/A     | N/A       | N/A       | N/A       |

## Interval

styles

You can use the SQL [SET](r_SET.md "r_SET.md") command to change the output
display format of your interval values. When you use the interval data type
in SQL, cast it to text to see the expected interval style, for example,
`YEAR TO MONTH::text`. Available values to SET the
`IntervalStyle` value are:

- `postgres` – follows PostgreSQL style. This is
  the default.
- `postgres_verbose` – follows PostgreSQL verbose
  style.
- `sql_standard` – follows the SQL standard
  interval literals style.

The following command sets the interval style to
`sql_standard`.

```
SET IntervalStyle to 'sql_standard';
```

**postgres output format**

The following is the output format for `postgres` interval
style. Each numeric value can be negative.

```
'<numeric> <unit> [, <numeric> <unit> ...]'
```

```
`select INTERVAL '1-2' YEAR TO MONTH::text`
`varchar
---------------
1 year 2 mons`
```

```
`select INTERVAL '1 2:3:4.5678' DAY TO SECOND::text`
`varchar
------------------
1 day 02:03:04.5678`
```

**postgres_verbose output format**

postgres_verbose syntax is similar to postgres, but postgres_verbose
outputs also contain the unit of time.

```
'[@] <numeric> <unit> [, <numeric> <unit> ...] [direction]'
```

```
`select INTERVAL '1-2' YEAR TO MONTH::text`
`varchar
-----------------
@ 1 year 2 mons`
```

```
`select INTERVAL '1 2:3:4.5678' DAY TO SECOND::text`
`varchar
---------------------------
@ 1 day 2 hours 3 mins 4.56 secs`
```

**sql_standard output format**

Interval year to month values are formatted as the following. Specifying
a negative sign before the interval indicates the interval is a negative
value and applies to the entire interval.

```
'[-]yy-mm'
```

Interval day to second values are formatted as the following.

```
'[-]dd hh:mm:ss.ffffff'
```

```
`SELECT INTERVAL '1-2' YEAR TO MONTH::text`
 `varchar
-------
1-2`
```

```
`select INTERVAL '1 2:3:4.5678' DAY TO SECOND::text`
`varchar
---------------
1 2:03:04.5678`
```

## Examples of interval

data type

The following examples demonstrate how to use INTERVAL data types with
tables.

```
`create table sample_intervals (y2m interval month, h2m interval hour to minute);
insert into sample_intervals values (interval '20' month, interval '2 days 1:1:1.123456' day to second);
select y2m::text, h2m::text from sample_intervals;`
`y2m | h2m
---------------+-----------------
 1 year 8 mons | 2 days 01:01:00`
```

```
`update sample_intervals set y2m = interval '2' year where y2m = interval '1-8' year to month;
select * from sample_intervals;`
`y2m | h2m
---------+-----------------
 2 years | 2 days 01:01:00`
```

```
`delete from sample_intervals where h2m = interval '2 1:1:0' day to second;
select * from sample_intervals;`
`y2m | h2m
-----+-----`
```

## Examples of

interval literals

The following examples are run with interval style set to
`postgres`.

The following example demonstrates how to create an INTERVAL literal of 1
year.

```
`select INTERVAL '1' YEAR`
`intervaly2m
---------------
1 years 0 mons`
```

If you specify a _quoted-string_ that exceeds the
qualifier, the remaining units of time are truncated from the interval. In
the following example, an interval of 13 months becomes 1 year and 1 month,
but the remaining 1 month is left out because of the YEAR qualifier.

```
`select INTERVAL '13 months' YEAR`
`intervaly2m
---------------
1 years 0 mons`
```

If you use a qualifier lower than your interval string, leftover units
are included.

```
`select INTERVAL '13 months' MONTH`
`intervaly2m
---------------
1 years 1 mons`
```

Specifying a precision in your interval truncates the number of
fractional digits to the specified precision.

```
`select INTERVAL '1.234567' SECOND (3)`
`intervald2s
--------------------------------
0 days 0 hours 0 mins 1.235 secs`
```

If you don't specify a precision, Amazon Redshift uses the maximum precision of 6.

```
`select INTERVAL '1.23456789' SECOND`
`intervald2s
-----------------------------------
0 days 0 hours 0 mins 1.234567 secs`
```

The following example demonstrates how to create a ranged
interval.

```
`select INTERVAL '2:2' MINUTE TO SECOND`
`intervald2s
------------------------------
0 days 0 hours 2 mins 2.0 secs`
```

Qualifiers dictate the units that you're specifying. For example, even
though the following example uses the same
_quoted-string_ of '2:2' as the previous example,
Amazon Redshift recognizes that it uses different units of time because of the
qualifier.

```
`select INTERVAL '2:2' HOUR TO MINUTE`
`intervald2s
------------------------------
0 days 2 hours 2 mins 0.0 secs`
```

Abbreviations and plurals of each unit are also supported. For example,
`5s`, `5 second`, and `5 seconds` are
equivalent intervals. Supported units are years, months, hours, minutes, and
seconds.

```
`select INTERVAL '5s' SECOND`
`intervald2s
------------------------------
0 days 0 hours 0 mins 5.0 secs`
```

```
`select INTERVAL '5 HOURS' HOUR`
`intervald2s
------------------------------
0 days 5 hours 0 mins 0.0 secs`
```

```
`select INTERVAL '5 h' HOUR`
`intervald2s
------------------------------
0 days 5 hours 0 mins 0.0 secs`
```
