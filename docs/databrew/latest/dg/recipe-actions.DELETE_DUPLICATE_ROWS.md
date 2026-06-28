# DELETE\_DUPLICATE\_ROWS

Deletes any row that is an exact match to an earlier row in the dataset. The initial
occurrence is not deleted, because it doesn't match an earlier row.

###### Example

```
{
    "RecipeAction": {
        "Operation": "DELETE_DUPLICATE_ROWS"
    }
}
```
