# SUM

Returns the sum of the values from the selected source columns in a new column. Any
non-number is treated as 0.

###### Parameters

- `sourceColumns` – A JSON-encoded string representing a list of existing
  columns.
- `targetColumn` – A name for the newly created column.

###### Example

```
{
    "RecipeAction": {
        "Operation": "SUM",
        "Parameters": {
            "sourceColumns": "[\"age\",\"years_in_service\"]",
            "targetColumn": "SUM Column 1"
        }
    }
}
```
