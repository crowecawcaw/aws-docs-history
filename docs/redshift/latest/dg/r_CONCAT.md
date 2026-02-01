Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CONCAT function

The CONCAT function concatenates two expressions and returns the resulting
expression. To concatenate more than two expressions, use nested CONCAT functions. The
concatenation operator (`||`) between two expressions produces the same results
as the CONCAT function.

## Syntax

```
CONCAT ( *expression1*, *expression2* )
```

## Arguments

_expression1_, _expression2_

Both arguments can be a fixed-length character string, a variable-length character string,
a binary expression, or an expression that evaluates to one of these inputs.

## Return type

CONCAT returns an expression. The data type of the expression is the same type as the
input arguments.

If the input expressions are of different types, Amazon Redshift tries to implicitly type casts one of the expressions.
If values can't be cast, an error is returned.

## Usage notes

- For both the CONCAT function and the concatenation operator, if one or both
  expressions is null, the result of the concatenation is null.

## Examples

The following example concatenates two character literals:

```
SELECT CONCAT('December 25, ', '2008');

`concat
-------------------
December 25, 2008
(1 row)`
```

The following query, using the `||` operator instead of CONCAT,
produces the same result:

```
SELECT 'December 25, '||'2008';

`?column?
-------------------
December 25, 2008
(1 row)`
```

The following example uses a nested CONCAT function inside another CONCAT function to concatenate three character
strings:

```
SELECT CONCAT('Thursday, ', CONCAT('December 25, ', '2008'));

`concat
-----------------------------
Thursday, December 25, 2008
(1 row)`
```

To concatenate columns that might contain NULLs, use the [NVL and COALESCE functions](r_NVL_function.md "r_NVL_function.md"), which returns a given value
when it encounters NULL. The following example
uses NVL to return a 0 whenever NULL is encountered.

```
SELECT CONCAT(venuename, CONCAT(' seats ', NVL(venueseats, 0))) AS seating
FROM venue WHERE venuestate = 'NV' OR venuestate = 'NC'
ORDER BY 1
LIMIT 5;

`seating
-----------------------------------
Ballys Hotel seats 0
Bank of America Stadium seats 73298
Bellagio Hotel seats 0
Caesars Palace seats 0
Harrahs Hotel seats 0
(5 rows)`
```

The following query concatenates CITY and STATE values from the VENUE table:

```
SELECT CONCAT(venuecity, venuestate)
FROM venue
WHERE venueseats > 75000
ORDER BY venueseats;

`concat
-------------------
DenverCO
Kansas CityMO
East RutherfordNJ
LandoverMD
(4 rows)`
```

The following query uses nested CONCAT functions. The query concatenates CITY and
STATE values from the VENUE table but delimits the resulting string with a comma and
a space:

```
SELECT CONCAT(CONCAT(venuecity,', '),venuestate)
FROM venue
WHERE venueseats > 75000
ORDER BY venueseats;

`concat
---------------------
Denver, CO
Kansas City, MO
East Rutherford, NJ
Landover, MD
(4 rows)`
```

The following example concatenates two binary expressions.
Where `abc` is a binary value (with a hexadecimal representation of `616263`) and
`def` is a binary value (with hexadecimal representation of `646566`).
The result is automatically shown as the hexadecimal representation of the binary value.

```
SELECT CONCAT('abc'::VARBYTE, 'def'::VARBYTE);

`concat
-------------------
616263646566`
```
