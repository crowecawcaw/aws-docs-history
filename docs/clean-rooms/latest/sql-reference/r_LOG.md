# LOG function

Returns the base 10 logarithm of a number.

Synonym of [DLOG10 function](r_DLOG10.md "r_DLOG10.md").

## Syntax

```
LOG(*number*)
```

## Argument

_number_

The input parameter is a double precision number.

## Return type

The LOG function returns a double precision number.

## Example

The following example returns the base 10 logarithm of the number 100:

```
select log(100);
dlog10
--------
2
(1 row)
```
