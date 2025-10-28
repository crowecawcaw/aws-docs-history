# CONVERT function

Like the [CAST function](r_CAST_function.md "r_CAST_function.md"), the CONVERT
function converts one data type to another compatible data type. For instance, you can
convert a string to a date, or a numeric type to a string. CONVERT performs a runtime
conversion, which means that the conversion doesn't change a value's data type in a source
table. It's changed only in the context of the query.

Certain data types require an explicit conversion to other data types using the CONVERT
function. Other data types can be converted implicitly, as part of another command, without
using CAST or CONVERT. See [Type compatibility and conversion](r_Type_conversion.md "r_Type_conversion.md").

## Syntax

```
CONVERT ( *type*, *expression* )
```

## Arguments

_type_

One of the supported [Data types](c_Supported_data_types.md "c_Supported_data_types.md"), except for VARBYTE, BINARY, and
BINARY VARYING data types.

_expression_

An expression that evaluates to one or more values, such as a column name or
a literal. Converting null values returns nulls. The expression can't contain
blank or empty strings.

## Return type

CONVERT returns the data type specified by the _type_
argument.

###### Note

AWS Clean Rooms returns an error if you try to perform a problematic conversion, such as a
DECIMAL conversion that loses precision, like the following:

```
`SELECT CONVERT(decimal(2,1), 123.456);`
```

or an INTEGER conversion that causes an overflow:

```
`SELECT CONVERT(smallint, 12345678);`
```

## Examples

The following query uses the CONVERT function to convert a column of decimals into
integers

```
`SELECT CONVERT(integer, pricepaid)
FROM sales WHERE salesid=100;`
```

This example converts an integer into a character string.

```
`SELECT CONVERT(char(4), 2008);`
```

In this example, the current date and time is converted to a variable character data
type:

```
`SELECT CONVERT(VARCHAR(30), GETDATE());`
`getdate
---------
2023-02-02 04:31:16`
```

This example converts the saletime column into just the time, removing the dates from
each row.

```
SELECT CONVERT(time, saletime), salesid
FROM sales order by salesid limit 10;

```

The following example converts variable character data into a datetime object.

```
`SELECT CONVERT(datetime, '2008-02-18 02:36:48') as mysaletime;`
```
