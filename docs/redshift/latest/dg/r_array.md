Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ARRAY function

Creates an array of the SUPER data type.

## Syntax

```
ARRAY( [ *expr1* ] [, *expr2* [, ... ]] )
```

## Argument

_expr1, expr2_

Expressions of any Amazon Redshift data type except date and time types, since Amazon Redshift doesn't cast the date and time types to the SUPER data type. The arguments don't need to be of the same data type.

## Return type

The ARRAY function returns the SUPER data type.

## Example

The following examples show an array of numeric values and an array of different data types.

```
--an array of numeric values
select ARRAY(1,50,null,100);
      array
------------------
 [1,50,null,100]
(1 row)

--an array of different data types
select ARRAY(1,'abc',true,3.14);
        array
-----------------------
 [1,"abc",true,3.14]
(1 row)

```

## See also

- [ARRAY_CONCAT function](r_array_concat.md "r_array_concat.md")
- [SPLIT_TO_ARRAY function](split_to_array.md "split_to_array.md")
- [ARRAY_FLATTEN function](array_flatten.md "array_flatten.md")
