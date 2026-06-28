# SQUARE\_ROOT

Returns the square root of a value in a new column.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `targetColumn` – The name of the new column to be
  created.

###### Example

```
{
    "RecipeAction": {
        "Operation": "SQUARE_ROOT",
        "Parameters": {
            "sourceColumn": "age",
            "targetColumn": "age_SQUARE_ROOT"
        }
    }
}
```
