# Using the ATTRIBUTE_TYPE function with PartiQL for DynamoDB

Returns `TRUE` if the attribute at the specified path is of a particular
data type.

## Syntax

```
attribute_type( `attributename`, `type` )
```

## Arguments

`attributename`

(Required) The attribute name to use.

`type`

(Required) The attribute type to check for. For a list of valid
values, see DynamoDB [attribute_type](Expressions.md#Expressions.OperatorsAndFunctions.Functions "Expressions.md#Expressions.OperatorsAndFunctions.Functions").

## Return type

`bool`

## Examples

```
SELECT * FROM "Music" WHERE attribute_type("Artist", 'S')
```
