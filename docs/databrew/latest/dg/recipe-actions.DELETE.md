# DELETE

Removes a column from the dataset.

###### Parameters

- `sourceColumn` – The name of an existing column.

###### Example

```
{
    "RecipeAction": {
        "Operation": "DELETE",
        "Parameters": {
            "sourceColumn": "extra_data"
        }
    }
}
```
