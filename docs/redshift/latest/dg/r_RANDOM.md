Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# RANDOM function

The RANDOM function generates a random value between 0.0 (inclusive) and 1.0
(exclusive).

## Syntax

```
RANDOM()
```

## Return type

`DOUBLE PRECISION`

## Usage notes

Call RANDOM after setting a seed value with the [SET](r_SET.md "r_SET.md") command to cause RANDOM to generate numbers in a
predictable sequence.

## Examples

To compute a random value between 0 and 99, use the following example. If the random number is 0 to
1, this query produces a random number from 0 to 100.

```
`SELECT CAST(RANDOM() * 100 AS INT);`

`+------+
| int4 |
+------+
| 59 |
+------+`
```

This example uses the [SET](r_SET.md "r_SET.md")
command to set a SEED value so that RANDOM generates a predictable
sequence of numbers.

To return three RANDOM integers without setting the SEED value, use the following example.

```
`SELECT CAST(RANDOM() * 100 AS INT);`
`+------+
| int4 |
+------+
| 6 |
+------+`

`SELECT CAST(RANDOM() * 100 AS INT);`
`+------+
| int4 |
+------+
| 68 |
+------+`

`SELECT CAST(RANDOM() * 100 AS INT);`
`+------+
| int4 |
+------+
| 56 |
+------+`
```

To set the SEED value to `.25`, and return three more
RANDOM numbers, use the following example.

```
`SET SEED TO .25;
SELECT CAST(RANDOM() * 100 AS INT);`
`+------+
| int4 |
+------+
| 21 |
+------+`

`SELECT CAST(RANDOM() * 100 AS INT);`
`+------+
| int4 |
+------+
| 79 |
+------+`

`SELECT CAST(RANDOM() * 100 AS INT);`
`+------+
| int4 |
+------+
| 12 |
+------+`
```

To reset the SEED value to `.25`, and verify that
RANDOM returns the same results as the previous three calls, use the following example.

```
`SET SEED TO .25;
SELECT CAST(RANDOM() * 100 AS INT);`
`+------+
| int4 |
+------+
| 21 |
+------+`

`SELECT CAST(RANDOM() * 100 AS INT);`
`+------+
| int4 |
+------+
| 79 |
+------+`

`SELECT CAST(RANDOM() * 100 AS INT);`
`+------+
| int4 |
+------+
| 12 |
+------+`
```

The following examples use the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To retrieve a uniform random sample of 10 items from the SALES table, use the following example.

```
`SELECT *
FROM sales
ORDER BY RANDOM()
LIMIT 10;`

`+---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------+
| salesid | listid | sellerid | buyerid | eventid | dateid | qtysold | pricepaid | commission | saletime |
+---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------+
| 45422 | 51114 | 5983 | 24482 | 4369 | 2118 | 1 | 195 | 29.25 | 2008-10-19 05:20:07 |
| 42481 | 47638 | 4573 | 6198 | 6479 | 1987 | 4 | 1140 | 171 | 2008-06-10 09:39:19 |
| 31494 | 34759 | 18895 | 4719 | 7753 | 2090 | 4 | 1024 | 153.6 | 2008-09-21 03:44:26 |
| 119388 | 136685 | 21815 | 41905 | 2071 | 1884 | 1 | 359 | 53.85 | 2008-02-27 10:43:10 |
| 166990 | 225037 | 18529 | 7628 | 746 | 2113 | 1 | 2009 | 301.35 | 2008-10-14 10:07:44 |
| 11146 | 12096 | 42685 | 6619 | 1876 | 2123 | 1 | 29 | 4.35 | 2008-10-24 06:23:54 |
| 148537 | 172056 | 15102 | 11787 | 6122 | 1923 | 2 | 480 | 72 | 2008-04-07 03:58:23 |
| 68945 | 78387 | 7359 | 18323 | 6636 | 1910 | 1 | 457 | 68.55 | 2008-03-25 08:31:03 |
| 52796 | 59576 | 9909 | 15102 | 7958 | 1951 | 1 | 479 | 71.85 | 2008-05-05 02:25:08 |
| 90684 | 103522 | 38052 | 21549 | 7384 | 2117 | 1 | 313 | 46.95 | 2008-10-18 05:43:11 |
+---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------+`
```

To retrieve a random sample of 10 items, but choose the items in
proportion to their prices, use the following example. For example, an item that is twice the price
of another would be twice as likely to appear in the query
results.

```
`SELECT *
FROM sales
ORDER BY -LOG(RANDOM()) / pricepaid
LIMIT 10;`

`+---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------+
| salesid | listid | sellerid | buyerid | eventid | dateid | qtysold | pricepaid | commission | saletime |
+---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------+
| 158340 | 208208 | 17082 | 42018 | 1211 | 2160 | 4 | 6852 | 1027.8 | 2008-11-30 12:21:43 |
| 53250 | 60069 | 12644 | 7066 | 7942 | 1838 | 4 | 1528 | 229.2 | 2008-01-12 11:24:56 |
| 22929 | 24938 | 47314 | 6503 | 179 | 2000 | 3 | 741 | 111.15 | 2008-06-23 08:04:50 |
| 164980 | 221181 | 1949 | 19670 | 1471 | 1906 | 1 | 1330 | 199.5 | 2008-03-21 07:59:51 |
| 159641 | 211179 | 44897 | 16652 | 7458 | 2128 | 1 | 1019 | 152.85 | 2008-10-29 02:02:15 |
| 73143 | 83439 | 5716 | 5727 | 7314 | 1903 | 1 | 248 | 37.2 | 2008-03-18 11:07:42 |
| 84778 | 96749 | 46608 | 32980 | 3883 | 1999 | 2 | 958 | 143.7 | 2008-06-22 12:13:31 |
| 171096 | 232929 | 43683 | 8536 | 8353 | 1870 | 1 | 929 | 139.35 | 2008-02-13 01:36:36 |
| 74212 | 84697 | 39809 | 15569 | 5525 | 2105 | 2 | 896 | 134.4 | 2008-10-06 11:47:50 |
| 158011 | 207556 | 25399 | 16881 | 232 | 2088 | 2 | 2526 | 378.9 | 2008-09-19 06:00:26 |
+---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------+`
```
