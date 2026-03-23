# TO_NUMBER_COLUMN

Changes the data type of an existing column to NUMBER.

###### Note

We recommend using CHANGE_DATA_TYPE recipe action rather than TO_NUMBER_COLUMN.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `columnDataType` – A value that must be
  `number`.

###### Example

```
{
    "RecipeAction": {
        "Operation": "TO_NUMBER_COLUMN",
        "Parameters": {
            "columnDataType": "number",
            "sourceColumn": "hours_worked"
        }
    }
}
```
