# NVL and COALESCE functions

Returns the value of the first expression that isn't null in a series of expressions.
When a non-null value is found, the remaining expressions in the list aren't evaluated.

NVL is identical to COALESCE. They are synonyms. This topic explains the syntax and
contains examples for both.

## Syntax

```
NVL( *expression*, *expression*, ... )
```

The syntax for COALESCE is the same:

```
COALESCE( *expression*, *expression*, ... )
```

If all expressions are null, the result is null.

These functions are useful when you want to return a secondary value when a primary
value is missing or null. For example, a query might return the first of three available
phone numbers: cell, home, or work. The order of the expressions in the function
determines the order of evaluation.

## Arguments

_expression_

An expression, such as a column name, to be evaluated for null
status.

## Return type

AWS Clean Rooms determines the data type of the returned value based on the input expressions.
If the data types of the input expressions don't have a common type, then an error is
returned.

## Examples

If the list contains integer expressions, the function returns an integer.

```
`SELECT COALESCE(NULL, 12, NULL);`

`coalesce
--------------
12`
```

This example, which is the same as the previous example, except that it uses NVL,
returns the same result.

```
`SELECT NVL(NULL, 12, NULL);`

`coalesce
--------------
12`
```

The following example returns a string type.

```
`SELECT COALESCE(NULL, 'AWS Clean Rooms', NULL);`

`coalesce
--------------
AWS Clean Rooms`
```

The following example results in an error because the data types vary in the
expression list. In this case, there is both a string type and a number type in the
list.

```
`SELECT COALESCE(NULL, 'AWS Clean Rooms', 12);`
`ERROR: invalid input syntax for integer: "AWS Clean Rooms"`
```
