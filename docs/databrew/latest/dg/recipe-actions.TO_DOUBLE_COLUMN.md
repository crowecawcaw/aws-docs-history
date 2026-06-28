# TO\_DOUBLE\_COLUMN

Changes the data type of an existing column to DOUBLE.

###### Note

We recommend using CHANGE\_DATA\_TYPE recipe action rather than TO\_DOUBLE\_COLUMN.

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
