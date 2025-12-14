# PartiQL insert statements for DynamoDB

Use the `INSERT` statement to add an item to a table in
Amazon DynamoDB.

###### Note

You can only insert one item at a time; you cannot issue a single DynamoDB
PartiQL statement that inserts multiple items. For information on inserting
multiple items, see [Performing transactions
with PartiQL for DynamoDB](ql-reference.multiplestatements.md "ql-reference.multiplestatements.md") or [Running batch operations with
PartiQL for DynamoDB](ql-reference.multiplestatements.md "ql-reference.multiplestatements.md").

###### Topics

- [Syntax](#ql-reference.insert.syntax "#ql-reference.insert.syntax")
- [Parameters](#ql-reference.insert.parameters "#ql-reference.insert.parameters")
- [Return value](#ql-reference.insert.return "#ql-reference.insert.return")
- [Examples](#ql-reference.insert.examples "#ql-reference.insert.examples")

## Syntax

Insert a single item.

```
INSERT INTO `table` VALUE `item`
```

## Parameters

**`table`**

(Required) The table where you want to insert the data. The table
must already exist.

**`item`**

(Required) A valid DynamoDB item represented as a [PartiQL tuple](https://partiql.org/docs.html "https://partiql.org/docs.html"). You
must specify only _one_ item and each attribute
name in the item is case-sensitive and can be denoted with
_single_ quotation marks (`'...'`)
in PartiQL.

String values are also denoted with _single_
quotation marks (`'...'`) in PartiQL.

## Return value

This statement does not return any values.

###### Note

If the DynamoDB table already has an item with the same primary key as the
primary key of the item being inserted, `DuplicateItemException`
is returned.

## Examples

```
INSERT INTO "Music" value {'Artist' : 'Acme Band','SongTitle' : 'PartiQL Rocks'}
```
