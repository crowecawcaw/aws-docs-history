# TO_DOUBLE_COLUMN

Changes the data type of an existing column to DOUBLE.

###### Note

We recommend using CHANGE_DATA_TYPE recipe action rather than TO_DOUBLE_COLUMN.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `columnDataType` – A value that must be
  `number`.

###### Example

```
{
    "RecipeAction": {
        "Operation": "TO_DOUBLE_COLUMN",
        "Parameters": {
            "columnDataType": "number",
            "sourceColumn": "hourly_rate"
        }
    }
}
```
