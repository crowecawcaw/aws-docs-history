# IF expression

The IF conditional function returns one of two values based on a condition.

This function is a common control flow statement used in SQL to make decisions and
return different values based on the evaluation of a condition. It's useful for
implementing simple if-else logic within a query.

## Syntax

```
if(expr1, expr2, expr3)
```

## Arguments

_expr1_

The condition or expression that is evaluated. If it is `true`,
the function will return the value of _expr2_.
If _expr1_ is `false`, the function
will return the value of _expr3_.

_expr2_

The expression that is evaluated and returned if _expr1_ is `true`.

_expr3_

The expression that is evaluated and returned if _expr1_ is `false`.

## Returns

If `expr1` evaluates to `true`, then returns
`expr2`; otherwise returns `expr3`.

## Example

The following example uses the `if()` function to return one of two values
based on a condition. The condition being evaluated is `1 < 2`, which is
`true`, so the first value `'a'` is returned.

```
SELECT if(1 < 2, 'a', 'b');
 a]
```
