# Using the BEGINS_WITH function with PartiQL for DynamoDB

Returns `TRUE` if the attribute specified begins with a particular substring.

## Syntax

```
begins_with(`path`, `value` )
```

## Arguments

`path`

(Required) The attribute name or document path to use.

`value`

(Required) The string to search for.

## Return type

`bool`

## Examples

```
SELECT * FROM "Orders" WHERE "OrderID"=1 AND begins_with("Address", '7834 24th')
```
