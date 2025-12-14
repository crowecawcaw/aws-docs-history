# TO_STRING_COLUMN

Changes the data type of an existing column to STRING.

###### Note

We recommend using CHANGE_DATA_TYPE recipe action rather than TO_STRING_COLUMN.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `columnDataType` – A value that must be
  `string`.

###### Example

```
{
    "RecipeAction": {
        "Operation": "TO_STRING_COLUMN",
        "Parameters": {
            "columnDataType": "string",
            "sourceColumn": "age"
        }
    }
}
```
