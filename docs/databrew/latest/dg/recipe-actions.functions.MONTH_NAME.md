# MONTH_NAME

Creates a new column containing the name of the month, from a string that represents a
date.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `value` – A character string to evaluate.
- `targetColumn` – A name for the newly created column.

###### Note

You can specify either `sourceColumn` or `value`, but not
both.

###### Example

```
{
    "RecipeAction": {
        "Operation": "MONTH_NAME",
        "Parameters": {
            "value": "2018-05-27",
            "targetColumn": "MONTHNAME Column 1"
        }
    }
}
```
