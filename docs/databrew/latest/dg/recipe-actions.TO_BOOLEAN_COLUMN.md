# TO_BOOLEAN_COLUMN

Changes the data type of an existing column to BOOLEAN.

###### Note

We recommend using CHANGE_DATA_TYPE recipe action rather than TO_BOOLEAN_COLUMN.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `columnDataType` – A value that must be
  `boolean`.

###### Example

```
{
    "RecipeAction": {
        "Operation": "TO_BOOLEAN_COLUMN",
        "Parameters": {
            "columnDataType": "boolean",
            "sourceColumn": "is_present"
        }
    }
}
```
