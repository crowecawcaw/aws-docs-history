# COS function

COS is a trigonometric function that returns the cosine of a number.
The return value
is in radians and is between `-1` and `1`, inclusive.

## Syntax

```
COS(*double\_precision*)
```

## Argument

_number_

The input parameter is a double precision number.

## Return type

The COS function returns a double precision number.

## Examples

The following example returns cosine of 0:

```
select cos(0);
cos
-----
1
(1 row)
```

The following example returns the cosine of PI:

```
select cos(pi());
cos
-----
-1
(1 row)
```
