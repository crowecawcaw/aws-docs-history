# EXACT

Creates a new column populated with one of the following:

- `True` if one string in a column (or value) exactly matches another string in a
  different column (or value).
- `False` if there is no match.

###### Parameters

- `sourceColumn1` – The name of an existing column.
- `sourceColumn2` – The name of an existing column.
- `value1` – A character string to evaluate.
- `value2` – A character string to evaluate.
- `targetColumn` – The name of the new column to be created.

###### Note

You can specify only one of the following combinations:

- Both of `sourceColumn`N``.
- One of `sourceColumn`N`` and one of
`value`N``.
- Both of `value`N``.

###### Example

```
{
    "RecipeAction": {
        "Operation": "EXACT",
        "Parameters": {
            "sourceColumn1": "nationality",
            "value2": "Argentina",
            "targetColumn": "nationality_exact"
        }
    }
}
```
