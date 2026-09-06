

# MOVE\_TO\_INDEX
<a name="recipe-actions.MOVE_TO_INDEX"></a>

Moves a column to a position specified by a number.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetIndex` – The new position for the column. Positions start with 0—so, for example, `1` refers to the second column, `2` refers to the third column, and so on.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "MOVE_TO_INDEX",
        "Parameters": {
            "sourceColumn": "nationality",
            "targetIndex": "5"
        }
    }
}
```