

# MOVE\_AFTER
<a name="recipe-actions.MOVE_AFTER"></a>

Moves a column to the position immediately after another column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of another column. The column specified by `sourceColumn` will be moved immediately after the column specified by `targetColumn`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "MOVE_AFTER",
        "Parameters": {
            "sourceColumn": "rating",
            "targetColumn": "height_cm"
        }
    }
}
```