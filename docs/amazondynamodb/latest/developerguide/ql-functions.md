# Using the SIZE function with PartiQL for amazon DynamoDB

Returns a number representing an attribute's size in bytes. The following are valid data types
for use with size. For more information, see the DynamoDB [size](Expressions.md#Expressions.OperatorsAndFunctions.Functions "Expressions.md#Expressions.OperatorsAndFunctions.Functions") function.

## Syntax

```
size( `path`)
```

## Arguments

`path`

(Required) The attribute name or document path.

For supported types, see DynamoDB [size](Expressions.md#Expressions.OperatorsAndFunctions.Functions "Expressions.md#Expressions.OperatorsAndFunctions.Functions") function.

## Return type

`int`

## Examples

```
 SELECT * FROM "Orders" WHERE "OrderID"=1 AND size("Image") >300
```
