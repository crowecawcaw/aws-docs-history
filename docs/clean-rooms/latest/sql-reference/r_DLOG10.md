# DLOG10 function

The DLOG10 returns the base 10 logarithm of the input parameter.

The DLOG10 function is a synonym of the [LOG function](r_LOG.md "r_LOG.md").

## Syntax

```
DLOG10(*number*)
```

## Argument

_number_

The input parameter is a double precision number.

## Return type

The DLOG10 function returns a double precision number.

## Example

The following example returns the base 10 logarithm of the number 100:

```
select dlog10(100);

dlog10
--------
2
(1 row)
```
