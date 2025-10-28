# ARRAY function

Creates an array with the given elements.

## Syntax

```
ARRAY( [ expr1 ] [ , expr2 [ , ... ] ] )
```

## Argument

_expr1, expr2_

Expressions of any data type except date and time types. The arguments
don't need to be of the same data type.

## Return type

The array function returns an ARRAY with the elements in the expression.

## Example

The following example shows an array of numeric values and an array of different data
types.

```
--an array of numeric values
select array(1,50,null,100);
      array
------------------
 [1,50,null,100]
(1 row)

--an array of different data types
select array(1,'abc',true,3.14);
        array
-----------------------
 [1,"abc",true,3.14]
(1 row)

```
