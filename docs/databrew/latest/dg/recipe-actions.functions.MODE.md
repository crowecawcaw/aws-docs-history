# MODE

Returns the mode, the number that appears most often, from the selected source columns
in a new column. Any non-number is ignored. For multiple modes, the mode is calculated
with the modal function.

###### Parameters

- `sourceColumns` – A JSON-encoded string representing a list of existing columns.
- `targetColumn` – A name for the newly created column.

###### Example

```
{
    "RecipeAction": {
        "Operation": "MODE",
        "Parameters": {
            "modeType": "MINIMUM",
            "sourceColumns": "[\"years_in_service\",\"age\"]",
            "targetColumn": "MODE Column 1"
        }
    }
}
```
