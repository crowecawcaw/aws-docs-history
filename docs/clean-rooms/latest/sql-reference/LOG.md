# LOG function

Returns the logarithm of `expr` with `base`.

## Syntax

```
LOG(*base, expr*)
```

## Argument

_expr_

The expression must have an integer, decimal, or floating-point data type.

_base_

The base for the logarithm calculation. Must be a positive number (not equal
to 1) of double precision data type.

## Return type

The LOG function returns a double precision number.

## Example

The following example returns the base 10 logarithm of the number 100:

```
select log(10, 100);
--------
2
(1 row)
```
