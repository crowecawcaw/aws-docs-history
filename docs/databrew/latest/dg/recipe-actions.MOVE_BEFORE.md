

# MOVE\_BEFORE
<a name="recipe-actions.MOVE_BEFORE"></a>

Moves a column to the position immediately before another column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of another column. The column specified by `sourceColumn` will be moved immediately after the column specified by `targetColumn`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "MOVE_BEFORE",
        "Parameters": {
            "sourceColumn": "height_cm",
            "targetColumn": "weight_kg"
        }
    }
}
```