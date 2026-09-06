

# ADD
<a name="recipe-actions.functions.ADD"></a>

 Sums the input column values in a new column, using (`sourceColumn1` \+ `sourceColumn2`) or (`sourceColumn1` \+ `value1`).

**Parameters**
+ `sourceColumn1` – The name of an existing column.
+ `value1` – A numeric value.
+ `sourceColumn2` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "ADD",
        "Parameters": {
            "sourceColumn1": "weight_kg",
            "sourceColumn2": "height_cm",
            "targetColumn": "weight_plus_height"
        }
    }
}
```