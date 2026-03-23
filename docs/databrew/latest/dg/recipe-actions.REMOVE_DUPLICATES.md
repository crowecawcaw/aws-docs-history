# REMOVE_DUPLICATES

Deletes an entire row, if a duplicate value is encountered in a selected source column.

###### Parameters

- `sourceColumn` – The name of an existing column.

###### Example

```
{
    "RecipeAction": {
        "Operation": "REMOVE_DUPLICATES",
        "Parameters": {
            "sourceColumn": "nationality"
        }
    }
}
```
