

# MOVE\_TO\_END
<a name="recipe-actions.MOVE_TO_END"></a>

Moves a column to the end position (last column) in the dataset.

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "MOVE_TO_END",
        "Parameters": {
            "sourceColumn": "height_cm"
        }
    }
}
```