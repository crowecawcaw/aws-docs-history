# Computations with numeric values

In AWS Clean Rooms, _computation_ refers to binary mathematical operations:
addition, subtraction, multiplication, and division. This section describes the expected
return types for these operations, as well as the specific formula that is applied to
determine precision and scale when DECIMAL data types are involved.

When numeric values are computed during query processing, you might encounter cases
where the computation is impossible and the query returns a numeric overflow error. You
might also encounter cases where the scale of computed values varies or is unexpected.
For some operations, you can use explicit casting (type promotion) or AWS Clean Rooms
configuration parameters to work around these problems.

For information about the results of similar computations with SQL functions, see
[AWS Clean Rooms Spark SQL functions](sql-functions-topic-spark.md "sql-functions-topic-spark.md").

## Return types for

computations

Given the set of numeric data types supported in AWS Clean Rooms, the following table shows
the expected return types for addition, subtraction, multiplication, and division
operations. The first column on the left side of the table represents the first
operand in the calculation, and the top row represents the second operand.

| Operand 1         | Operand 2         | Return type       |
| ----------------- | ----------------- | ----------------- |
| SMALLINT or SHORT | SMALLINT or SHORT | SMALLINT or SHORT |
| SMALLINT or SHORT | INTEGER           | INTEGER           |
| SMALLINT or SHORT | BIGINT            | BIGINT            |
| SMALLINT or SHORT | DECIMAL           | DECIMAL           |
| SMALLINT or SHORT | FLOAT4            | FLOAT8            |
| SMALLINT or SHORT | FLOAT8            | FLOAT8            |
| INTEGER           | INTEGER           | INTEGER           |
| INTEGER           | BIGINT or LONG    | BIGINT or LONG    |
| INTEGER           | DECIMAL           | DECIMAL           |
| INTEGER           | FLOAT4            | FLOAT8            |
| INTEGER           | FLOAT8            | FLOAT8            |
| BIGINT or LONG    | BIGINT or LONG    | BIGINT or LONG    |
| BIGINT or LONG    | DECIMAL           | DECIMAL           |
| BIGINT or LONG    | FLOAT4            | FLOAT8            |
| BIGINT or LONG    | FLOAT8            | FLOAT8            |
| DECIMAL           | DECIMAL           | DECIMAL           |
| DECIMAL           | FLOAT4            | FLOAT8            |
| DECIMAL           | FLOAT8            | FLOAT8            |
| FLOAT4            | FLOAT8            | FLOAT8            |
| FLOAT8            | FLOAT8            | FLOAT8            |

## Precision and scale of computed DECIMAL results

The following table summarizes the rules for computing resulting precision and
scale when mathematical operations return DECIMAL results. In this table,
`p1` and `s1` represent the precision and scale of the first
operand in a calculation. `p2` and `s2` represent the precision
and scale of the second operand. (Regardless of these calculations, the maximum
result precision is 38, and the maximum result scale is 38.)

| Operation | Result precision and scale                                     |
| --------- | -------------------------------------------------------------- |
| + or -    | Scale = `max(s1,s2)`<br>Precision = `max(p1-s1,p2-s2)+1+scale` |
| \*        | Scale = `s1+s2`<br>Precision = `p1+p2+1`                       |
| /         | Scale = `max(4,s1+p2-s2+1)`<br>Precision = `p1-s1+ s2+scale`   |

For example, the PRICEPAID and COMMISSION columns in the SALES table are both
DECIMAL(8,2) columns. If you divide PRICEPAID by COMMISSION (or vice versa), the
formula is applied as follows:

```
Precision = 8-2 + 2 + max(4,2+8-2+1)
= 6 + 2 + 9 = 17

Scale = max(4,2+8-2+1) = 9

Result = DECIMAL(17,9)
```

The following calculation is the general rule for computing the resulting
precision and scale for operations performed on DECIMAL values with set operators
such as UNION, INTERSECT, and EXCEPT or functions such as COALESCE and DECODE:

```
Scale = max(s1,s2)
Precision = min(max(p1-s1,p2-s2)+*scale*,19)
```

For example, a DEC1 table with one DECIMAL(7,2) column is joined with a DEC2 table
with one DECIMAL(15,3) column to create a DEC3 table. The schema of DEC3 shows that
the column becomes a NUMERIC(15,3) column.

```
select * from dec1 union select * from dec2;


```

In the above example, the formula is applied as follows:

```
Precision = min(max(7-2,15-3) + max(2,3), 19)
= 12 + 3 = 15

Scale = max(2,3) = 3

Result = DECIMAL(15,3)

```

## Notes on division

operations

For division operations, divide-by-zero conditions return errors.

The scale limit of 100 is applied after the precision and scale are calculated. If
the calculated result scale is greater than 100, division results are scaled as
follows:

- Precision = `precision - (scale - max_scale)`
- Scale = `max_scale`

If the calculated precision is greater than the maximum precision (38), the
precision is reduced to 38, and the scale becomes the result of: `max(38 + scale

- precision), min(4, 100))`

## Overflow

conditions

Overflow is checked for all numeric computations. DECIMAL data with a precision of
19 or less is stored as 64-bit integers. DECIMAL data with a precision that is
greater than 19 is stored as 128-bit integers. The maximum precision for all DECIMAL
values is 38, and the maximum scale is 37. Overflow errors occur when a value exceeds
these limits, which apply to both intermediate and final result sets:

- Explicit casting results in runtime overflow errors when specific data
  values don't fit the requested precision or scale specified by the cast
  function. For example, you can't cast all values from the PRICEPAID column in
  the SALES table (a DECIMAL(8,2) column) and return a DECIMAL(7,3) result:

```
select pricepaid::decimal(7,3) from sales;
ERROR:  Numeric data overflow (result precision)
```

This error occurs because _some_ of the larger values in
the PRICEPAID column can't be cast.

- Multiplication operations produce results in which the result scale is the
  sum of the scale of each operand. If both operands have a scale of 4, for
  example, the result scale is 8, leaving only 10 digits for the left side of the
  decimal point. Therefore, it is relatively easy to run into overflow conditions
  when multiplying two large numbers that both have significant scale.

## Numeric calculations with INTEGER and DECIMAL types

When one of the operands in a calculation has an INTEGER data type and the other
operand is DECIMAL, the INTEGER operand is implicitly cast as a DECIMAL.

- SMALLINT or SHORT is cast as DECIMAL(5,0)
- INTEGER is cast as DECIMAL(10,0)
- BIGINT or LONG is cast as DECIMAL(19,0)

For example, if you multiply SALES.COMMISSION, a DECIMAL(8,2) column, and
SALES.QTYSOLD, a SMALLINT column, this calculation is cast as:

```
DECIMAL(8,2) * DECIMAL(5,0)
```
