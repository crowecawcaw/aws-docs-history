

# CEILING
<a name="recipe-actions.functions.CEILING"></a>

Returns the smallest integer number greater than or equal to the input decimal numbers in a new column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value1` – A numeric value.
+ `targetColumn` – The name of the new column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "CEILING",
        "Parameters": {
            "sourceColumn": "weight_kg",
            "targetColumn": "weight_kg_CEILING"
        }
    }
}
```