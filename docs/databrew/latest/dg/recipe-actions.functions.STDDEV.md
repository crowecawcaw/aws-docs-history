# STANDARD_DEVIATION

Returns the standard deviation from the selected source columns in a new column.

###### Parameters

- `sourceColumns` – A JSON-encoded string representing a list of existing
  columns.
- `targetColumn` – A name for the newly created column.

###### Example

```
{
    "RecipeAction": {
        "Operation": "STANDARD_DEVIATION",
        "Parameters": {
            "sourceColumns": "[\"years_in_sservice\",\"age\"]",
            "targetColumn": "STANDARD_DEVIATION Column 1"
        }
    }
}
```
