# KTH_LARGEST_UNIQUE

Returns the *k*th largest unique number from the
selected source columns in a new column.

###### Parameters

- `sourceColumns` – A JSON-encoded string representing a list of existing
  columns.
- `targetColumn` – A name for the newly created column.

`value` – A number representing
_k_.

###### Example

```
{
    "RecipeAction": {
        "Operation": "KTH_LARGEST_UNIQUE",
        "Parameters": {
            "sourceColumns": "[\"age\",\"height_cm\",\"weight_kg\"]",
            "targetColumn": "KTH_LARGEST_UNIQUE Column 1",
            "value": "3"
        }
    }
}
```
