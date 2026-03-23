# NEST_TO_MAP

Converts user-selected columns into key-value pairs, each with a key representing the
column name and a value representing the row value. The order of the selected column is
not maintained while creating the resultant map. The different column data types are
typecast to a common type that supports the data types of all columns.

###### Parameters

- `sourceColumns` — List of the source columns.
- `targetColumn` — The name of the target column.
- `removeSourceColumns` — Contains the value
  `true` or `false` to indicate whether or not the
  user wants to remove the selected source columns.

###### Example

```
{
    "RecipeAction": {
        "Operation": "NEST_TO_MAP",
        "Parameters": {
            "sourceColumns": "[\"age\",\"weight_kg\",\"height_cm\"]",
            "targetColumn": "columnName",
            "removeSourceColumns": "true"
        }
    }
}
```
