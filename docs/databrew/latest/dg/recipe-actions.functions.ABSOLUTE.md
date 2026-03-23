# ABSOLUTE

Returns the absolute value of the input number in a new column. _Absolute value_ is how far the number is from zero,
regardless of whether it is positive or negative

###### Parameters

- `sourceColumn` – The name of an existing column.
- `targetColumn` – The name of the new column to be created.

###### Example

```
{
    "RecipeAction": {
        "Operation": "ABSOLUTE",
        "Parameters": {
            "sourceColumn": "freezingTemps",
            "targetColumn": "absValueOfFreezingTemps"
        }
    }
}
```
