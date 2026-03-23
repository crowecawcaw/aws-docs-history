# KTH_LARGEST

Returns the *k*th largest number from the selected source columns
in a new column.

###### Parameters

- `sourceColumns` – A JSON-encoded string representing a list of existing
  columns.
- `targetColumn` – A name for the newly created column.
- `value` – A number representing
  _k_.

###### Example

```
{
    "RecipeAction": {
        "Operation": "KTH_LARGEST",
        "Parameters": {
            "sourceColumns": "[\"height_cm\",\"weight_kg\",\"age\"]",
            "targetColumn": "KTH_LARGEST Column 1",
            "value": "2"
        }
    }
}
```
