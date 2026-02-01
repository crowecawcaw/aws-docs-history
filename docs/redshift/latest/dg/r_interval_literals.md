Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Examples of interval literals without

qualifier syntax

###### Note

The following examples demonstrate using an interval literal without a
`YEAR TO MONTH` or `DAY TO SECOND` qualifier.
For information about using the recommended interval literal with a
qualifier, see [Interval data types and
literals](r_interval_data_types.md "r_interval_data_types.md").

Use an interval literal to identify specific periods of time, such as
`12 hours` or `6 months`. You can use these
interval literals in conditions and calculations that involve datetime
expressions.

An interval literal is expressed as a combination of the INTERVAL
keyword with a numeric quantity and a supported date part, for example
`INTERVAL '7 days'` or `INTERVAL '59 minutes'`. You
can connect several quantities and units to form a more precise interval,
for example: `INTERVAL '7 days, 3 hours, 59 minutes'`.
Abbreviations and plurals of each unit are also supported; for example:
`5 s`, `5 second`, and `5 seconds` are
equivalent intervals.

If you don't specify a date part, the interval value represents
seconds. You can specify the quantity value as a fraction (for example:
`0.5 days`).

The following examples show a series of calculations with different
interval values.

The following adds 1 second to the specified date.

```
select caldate + interval '1 second' as dateplus from date
where caldate='12-31-2008';
dateplus
---------------------
2008-12-31 00:00:01
(1 row)
```

The following adds 1 minute to the specified date.

```
select caldate + interval '1 minute' as dateplus from date
where caldate='12-31-2008';
dateplus
---------------------
2008-12-31 00:01:00
(1 row)
```

The following adds 3 hours and 35 minutes to the specified date.

```
select caldate + interval '3 hours, 35 minutes' as dateplus from date
where caldate='12-31-2008';
dateplus
---------------------
2008-12-31 03:35:00
(1 row)
```

The following adds 52 weeks to the specified date.

```
select caldate + interval '52 weeks' as dateplus from date
where caldate='12-31-2008';
dateplus
---------------------
2009-12-30 00:00:00
(1 row)
```

The following adds 1 week, 1 hour, 1 minute, and 1 second to the
specified date.

```
select caldate + interval '1w, 1h, 1m, 1s' as dateplus from date
where caldate='12-31-2008';
dateplus
---------------------
2009-01-07 01:01:01
(1 row)
```

The following adds 12 hours (half a day) to the specified date.

```
select caldate + interval '0.5 days' as dateplus from date
where caldate='12-31-2008';
dateplus
---------------------
2008-12-31 12:00:00
(1 row)
```

The following subtracts 4 months from February 15, 2023 and the result is
October 15, 2022.

```
select date '2023-02-15' - interval '4 months';

?column?
---------------------
2022-10-15 00:00:00

```

The following subtracts 4 months from March 31, 2023 and the result is
November 30, 2022. The calculation considers the number of days in a
month.

```
select date '2023-03-31' - interval '4 months';

?column?
---------------------
2022-11-30 00:00:00

```
