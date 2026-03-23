# UPPER_CASE

Changes each string in a column to uppercase, for example: THE QUICK BROWN FOX
JUMPED OVER THE FENCE

###### Parameters

- `sourceColumn` – The name of an existing column.

###### Example

```
{
    "RecipeAction": {
        "Operation": "UPPER_CASE",
        "Parameters": {
            "sourceColumn": "nationality"
        }
    }
}
```
