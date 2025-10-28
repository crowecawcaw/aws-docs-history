# CEILING (or CEIL) function

The CEILING or CEIL function is used to round a number up to the next whole number. (The
[FLOOR function](FLOOR.md "FLOOR.md") rounds a number down to the next whole
number.)

## Syntax

```
CEIL | CEILING(*number*)
```

## Arguments

_number_

The number or expression that evaluates to a number. It can be the SMALLINT,
INTEGER, BIGINT, DECIMAL, FLOAT4, or FLOAT8 type.

## Return type

CEILING and CEIL return the same data type as its argument.

## Example

Calculate the ceiling of the commission paid for a given sales transaction:

```
select ceiling(commission) from sales
where salesid=10000;

ceiling
---------
29
(1 row)
```
