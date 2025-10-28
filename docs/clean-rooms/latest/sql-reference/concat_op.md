# || (Concatenation) operator

Concatenates two expressions on either side of the || symbol and returns the
concatenated expression.

The concatentation operator is similar to [CONCAT function](CONCAT.md "CONCAT.md").

###### Note

For both the CONCAT function and the concatenation operator, if one or both
expressions is null, the result of the concatenation is null.

## Syntax

```
*expression1* || *expression2*

```

## Arguments

_expression1_, _expression2_

Both arguments can be fixed-length or variable-length character strings or
expressions.

## Return type

The || operator returns a string. The type of string is the same as the input
arguments.

## Example

The following example concatenates the FIRSTNAME and LASTNAME fields from the USERS
table:

```
select firstname || ' ' || lastname
from users
order by 1
limit 10;

concat
-----------------
Aaron Banks
Aaron Booth
Aaron Browning
Aaron Burnett
Aaron Casey
Aaron Cash
Aaron Castro
Aaron Dickerson
Aaron Dixon
Aaron Dotson
(10 rows)
```

To concatenate columns that might contain nulls, use the [NVL and COALESCE functions](NVL_function.md "NVL_function.md") expression. The following
example uses NVL to return a 0 whenever NULL is encountered.

```
select venuename || ' seats ' || nvl(venueseats, 0)
from venue where venuestate = 'NV' or venuestate = 'NC'
order by 1
limit 10;

seating
-----------------------------------
Ballys Hotel seats 0
Bank of America Stadium seats 73298
Bellagio Hotel seats 0
Caesars Palace seats 0
Harrahs Hotel seats 0
Hilton Hotel seats 0
Luxor Hotel seats 0
Mandalay Bay Hotel seats 0
Mirage Hotel seats 0
New York New York seats 0
```
