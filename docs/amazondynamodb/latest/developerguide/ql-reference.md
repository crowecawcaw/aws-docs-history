# PartiQL delete statements for DynamoDB

Use the `DELETE` statement to delete an existing item from your
Amazon DynamoDB table.

###### Note

You can only delete one item at a time. You cannot issue a single DynamoDB
PartiQL statement that deletes multiple items. For information on deleting
multiple items, see [Performing transactions
with PartiQL for DynamoDB](ql-reference.multiplestatements.md "ql-reference.multiplestatements.md") or [Running batch operations with
PartiQL for DynamoDB](ql-reference.multiplestatements.md "ql-reference.multiplestatements.md").

###### Topics

- [Syntax](#ql-reference.delete.syntax "#ql-reference.delete.syntax")
- [Parameters](#ql-reference.delete.parameters "#ql-reference.delete.parameters")
- [Return value](#ql-reference.delete.return "#ql-reference.delete.return")
- [Examples](#ql-reference.delete.examples "#ql-reference.delete.examples")

## Syntax

```
DELETE FROM `table`
 WHERE `condition` [RETURNING `returnvalues`]
 <returnvalues>  ::= ALL OLD *
```

## Parameters

**`table`**

(Required) The DynamoDB table containing the item to be
deleted.

**`condition`**

(Required) The selection criteria for the item to be deleted; this
condition must resolve to a single primary key value.

**`returnvalues`**

(Optional) Use `returnvalues` if you want to get the
item attributes as they appeared before they were deleted. The valid
values are:

- `ALL OLD *`- The content of the old item is
  returned.

## Return value

This statement does not return a value unless `returnvalues`
parameter is specified.

###### Note

If the DynamoDB table does not have any item with the same primary key as
that of the item for which the DELETE is issued, SUCCESS is returned with 0
items deleted. If the table has an item with same primary key, but the
condition in the WHERE clause of the DELETE statement evaluates to false,
`ConditionalCheckFailedException` is returned.

## Examples

The following query deletes an item in the `"Music"` table.

```
DELETE FROM "Music" WHERE "Artist" = 'Acme Band' AND "SongTitle" = 'PartiQL Rocks'
```

You can add the parameter `RETURNING ALL OLD *` to return the data
that was deleted.

```
DELETE FROM "Music" WHERE "Artist" = 'Acme Band' AND "SongTitle" = 'PartiQL Rocks' RETURNING ALL OLD *
```

The `Delete` statement now returns the following:

```
{
    "Items": [
        {
            "Artist": {
                "S": "Acme Band"
            },
            "SongTitle": {
                "S": "PartiQL Rocks"
            }
        }
    ]
}
```
