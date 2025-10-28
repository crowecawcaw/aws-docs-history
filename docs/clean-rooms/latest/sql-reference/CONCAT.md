# CONCAT function

The CONCAT function concatenates two expressions and returns the resulting expression.
To concatenate more than two expressions, use nested CONCAT functions. The concatenation
operator (`||`) between two expressions produces the same results as the CONCAT
function.

###### Note

For both the CONCAT function and the concatenation operator, if one or both
expressions is null, the result of the concatenation is null.

## Syntax

```
CONCAT ( *expression1*, *expression2* )
```

## Arguments

_expression1_, _expression2_

Both arguments can be a fixed-length character string, a variable-length
character string, a binary expression, or an expression that evaluates to one
of these inputs.

## Return type

CONCAT returns an expression. The data type of the expression is the same type as
the input arguments.

If the input expressions are of different types, AWS Clean Rooms tries to implicitly type casts
one of the expressions. If values can't be cast, an error is returned.

## Examples

The following example concatenates two character literals:

```
select concat('December 25, ', '2008');

concat
-------------------
December 25, 2008
(1 row)
```

The following query, using the `||` operator instead of CONCAT, produces
the same result:

```
select 'December 25, '||'2008';

concat
-------------------
December 25, 2008
(1 row)
```

The following example uses two CONCAT functions to concatenate three character
strings:

```
select concat('Thursday, ', concat('December 25, ', '2008'));

concat
-----------------------------
Thursday, December 25, 2008
(1 row)
```

To concatenate columns that might contain nulls, use the [NVL and COALESCE functions](NVL_function.md "NVL_function.md"). The following example uses NVL to return a 0 whenever
NULL is encountered.

```
select concat(venuename, concat(' seats ', nvl(venueseats, 0))) as seating
from venue where venuestate = 'NV' or venuestate = 'NC'
order by 1
limit 5;

seating
-----------------------------------
Ballys Hotel seats 0
Bank of America Stadium seats 73298
Bellagio Hotel seats 0
Caesars Palace seats 0
Harrahs Hotel seats 0
(5 rows)
```

The following query concatenates CITY and STATE values from the VENUE table:

```
select concat(venuecity, venuestate)
from venue
where venueseats > 75000
order by venueseats;

concat
-------------------
DenverCO
Kansas CityMO
East RutherfordNJ
LandoverMD
(4 rows)
```

The following query uses nested CONCAT functions. The query concatenates CITY and
STATE values from the VENUE table but delimits the resulting string with a comma and a
space:

```
select concat(concat(venuecity,', '),venuestate)
from venue
where venueseats > 75000
order by venueseats;

concat
---------------------
Denver, CO
Kansas City, MO
East Rutherford, NJ
Landover, MD
(4 rows)
```
