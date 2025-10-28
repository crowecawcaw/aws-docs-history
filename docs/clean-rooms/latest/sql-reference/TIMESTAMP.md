# TIMESTAMP function

The TIMESTAMP function takes a value (typically a number) and converts it to a timestamp
data type.

This function is useful when you need to convert a numeric value representing a time or
date to a timestamp data type. This can be helpful when you are working with data that is
stored in a numeric format, such as Unix timestamps or epoch time.

## Syntax

```
timestamp(expr)
```

## Arguments

_expr_

Any expression that can be cast to TIMESTAMP.

## Returns

The TIMESTAMP function returns a TIMESTAMP.

## Example

The following example converts a numeric Unix timestamp (`1632416400`) to
its corresponding timestamp data type: September 22, 2021 at 12:00:00 PM UTC.

```
SELECT timestamp(1632416400);
 2021-09-22 12:00:00 UTC

```
