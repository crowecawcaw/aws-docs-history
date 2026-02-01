Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# GREATEST and LEAST functions

Returns the largest or smallest value from a list of any number of
expressions.

## Syntax

```
GREATEST (value [, ...])
LEAST (value [, ...])
```

## Parameters

_expression_list_

A comma-separated list of expressions, such as column names. The
expressions must all be convertible to a common data type. NULL values in
the list are ignored. If all of the expressions evaluate to NULL, the result
is NULL.

## Returns

Returns the greatest (for GREATEST) or least (for LEAST) value from the provided list of expressions.

## Example

The following example returns the highest value alphabetically for
`firstname` or `lastname`.

```
select firstname, lastname, greatest(firstname,lastname) from users
where userid < 10
order by 3;

 firstname | lastname  | greatest
-----------+-----------+-----------
 Lars      | Ratliff   | Ratliff
 Reagan    | Hodge     | Reagan
 Colton    | Roy       | Roy
 Barry     | Roy       | Roy
 Tamekah   | Juarez    | Tamekah
 Rafael    | Taylor    | Taylor
 Victor    | Hernandez | Victor
 Vladimir  | Humphrey  | Vladimir
 Mufutau   | Watkins   | Watkins
(9 rows)
```
