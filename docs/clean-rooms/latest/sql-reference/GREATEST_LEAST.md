

# GREATEST and LEAST expression
<a name="GREATEST_LEAST"></a>

Returns the largest or smallest value from a list of any number of expressions.

## Syntax
<a name="GREATEST_LEAST-synopsis"></a>

```
GREATEST (value [, ...])
LEAST (value [, ...])
```

## Parameters
<a name="GREATEST_LEAST-arguments"></a>

*expression\_list*  
A comma-separated list of expressions, such as column names. The expressions must all be convertible to a common data type. NULL values in the list are ignored. If all of the expressions evaluate to NULL, the result is NULL.

## Returns
<a name="GREATEST_LEAST-returns"></a>

Returns the greatest (for GREATEST) or least (for LEAST) value from the provided list of expressions.

## Example
<a name="GREATEST_LEAST-examples"></a>

The following example returns the highest value alphabetically for `firstname` or `lastname`.

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