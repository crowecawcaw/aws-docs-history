# IS_NOT_NULL expression

The IS_NOT_NULL conditional expression is used to check if a value is not
null.

This expression is a synonym for IS NOT NULL.

## Syntax

```
is_not_null(expr)
```

## Arguments

_expr_

An expression of any type.

## Returns

The IS_NOT_NULL conditional expression returns a Boolean. If
`expr1` is not NULL, returns `true`, otherwise returns
`false`.

## Examples

The following example checks if the value `1` is not null, and returns the
boolean result `true` because 1 is a valid, non-null value.

```
SELECT is not null(1);
 true
```

The following example selects the `id` column from the
`squirrels` table, but only for the rows where the age column is not
`null`.

```
SELECT id FROM squirrels WHERE is_not_null(age)
```
