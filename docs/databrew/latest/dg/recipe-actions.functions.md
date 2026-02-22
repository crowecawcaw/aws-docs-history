# LN

Returns the natural logarithm (Euler’s number) of a value in a new column.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `targetColumn` – The name of the new column to be
  created.

###### Example

```
{
    "RecipeAction": {
        "Operation": "LN",
        "Parameters": {
            "sourceColumn": "weight_kg",
            "targetColumn": "weight_kg_LN"
        }
    }
}
```
