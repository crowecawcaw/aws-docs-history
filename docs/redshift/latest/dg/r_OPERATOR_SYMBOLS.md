Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Mathematical operator symbols

The following table lists the supported mathematical operators.

## Supported operators

| Operator | Description         | Example     | Result    |
| -------- | ------------------- | ----------- | --------- | ------ | --- | ------ | --- |
| +        | addition            | 2 + 3       | 5         |
| -        | subtraction         | 2<br>• 3    | -1        |
| \*       | multiplication      | 2 \<br>• 3  | 6         |
| /        | division            | 4 / 2       | 2         |
| %        | modulo              | 5 % 4       | 1         |
| ^        | exponentiation      | 2.0 ^ 3.0   | 8         |
|          | /                   | square root |           | / 25.0 | 5   |
|          |                     | /           | cube root |        |     | / 27.0 | 3   |
| @        | absolute value      | @ -5.0      | 5         |
| <<       | bitwise shift left  | 1 << 4      | 16        |
| >>       | bitwise shift right | 8 >> 2      | 2         |
| &        | bitwise and         | 8 & 2       | 0         |

## Examples

The following examples use the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To calculate the commission paid plus a $2.00 handling for a given transaction, use the following example.

```
`SELECT
 commission,
 (commission + 2.00) AS comm
FROM
 sales
WHERE
 salesid = 10000;`

`+------------+-------+
| commission | comm |
+------------+-------+
| 28.05 | 30.05 |
+------------+-------+`
```

To calculate 20 percent of the sales price for a given transaction, use the following example.

```
`SELECT pricepaid, (pricepaid * .20) as twentypct
FROM sales
WHERE salesid=10000;`

`+-----------+-----------+
| pricepaid | twentypct |
+-----------+-----------+
| 187 | 37.4 |
+-----------+-----------+`
```

To forecast ticket sales based on a continuous growth pattern, use the following example. In this example, the
subquery returns the number of tickets sold in 2008. That result is multiplied
exponentially by a continuous growth rate of 5% over 10 years.

```
`SELECT (SELECT SUM(qtysold) FROM sales, date
WHERE sales.dateid=date.dateid AND year=2008)^((5::float/100)*10) AS qty10years;`

`+------------------+
| qty10years |
+------------------+
| 587.664019657491 |
+------------------+`
```

To find the total price paid and commission for sales with a date ID that is greater
than or equal to 2000, use the following example. Then subtract the total commission from the total price paid.

```
`SELECT SUM(pricepaid) AS sum_price, dateid,
SUM(commission) AS sum_comm, (SUM(pricepaid) - SUM(commission)) AS value
FROM sales
WHERE dateid >= 2000
GROUP BY dateid
ORDER BY dateid
LIMIT 10;`

`+-----------+--------+----------+-----------+
| sum_price | dateid | sum_comm | value |
+-----------+--------+----------+-----------+
| 305885 | 2000 | 45882.75 | 260002.25 |
| 316037 | 2001 | 47405.55 | 268631.45 |
| 358571 | 2002 | 53785.65 | 304785.35 |
| 366033 | 2003 | 54904.95 | 311128.05 |
| 307592 | 2004 | 46138.8 | 261453.2 |
| 333484 | 2005 | 50022.6 | 283461.4 |
| 317670 | 2006 | 47650.5 | 270019.5 |
| 351031 | 2007 | 52654.65 | 298376.35 |
| 313359 | 2008 | 47003.85 | 266355.15 |
| 323675 | 2009 | 48551.25 | 275123.75 |
+-----------+--------+----------+-----------+`
```
