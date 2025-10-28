# FLOOR function

The FLOOR function rounds a number down to the next whole number.

## Syntax

```
FLOOR (*number*)
```

## Argument

_number_

The number or expression that evaluates to a number. It can be the SMALLINT,
INTEGER, BIGINT, DECIMAL, FLOAT4, or FLOAT8 type.

## Return type

FLOOR returns the same data type as its argument.

## Example

The example shows the value of the commission paid for a given sales transaction
before and after using the FLOOR function.

```
select commission from sales
where salesid=10000;

floor
-------
28.05
(1 row)

select floor(commission) from sales
where salesid=10000;

floor
-------
28
(1 row)

```
