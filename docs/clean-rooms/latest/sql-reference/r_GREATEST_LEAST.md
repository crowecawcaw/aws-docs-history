# GREATEST and LEAST expression

Returns the largest or smallest value from a list of any number of expressions.

## Syntax

```
GREATEST (value [, ...])
LEAST (value [, ...])
```

## Parameters

_expression_list_

A comma-separated list of expressions, such as column names. The expressions
must all be convertible to a common data type. NULL values in the list are
ignored. If all of the expressions evaluate to NULL, the result is NULL.

## Returns

Returns the greatest (for GREATEST) or least (for LEAST) value from the provided list
of expressions.

## Example

The following example returns the highest value alphabetically for
`firstname` or `lastname`.

```
select firstname, lastname, greatest(firstname,lastname) from users
where userid < 10
order by 3;

 firstname | lastname  | greatest
-----------+-----------+-----------
 Alejandro | Rosalez   | Ratliff
 Carlos    | Salazar   | Carlos
 Jane      | Doe       | Doe
 John      | Doe       | Doe
 John      | Stiles    | John
 Shirley   | Rodriguez | Rodriguez
 Terry     | Whitlock  | Terry
 Richard   | Roe       | Richard
 Xiulan    | Wang      | Wang
(9 rows)
```
