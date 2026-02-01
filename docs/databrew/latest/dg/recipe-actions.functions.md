# IS_ODD

Returns a Boolean value in a new column that indicates whether the source column or
value is odd. If the source column or value is a decimal, the result is false.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `targetColumn` – The name of the new column to be
  created.
- `trueString` – A string that indicates whether the value is
  odd.
- `falseString` – A string that indicates whether the value is
  _not_ odd.

###### Example

```
{
    "RecipeAction": {
        "Operation": "IS_ODD",
        "Parameters": {
            "falseString": "Value is even",
            "sourceColumn": "weight_kg",
            "targetColumn": "weight_kg_IS_ODD",
            "trueString": "Value is odd"
        }
    }
}
```
