

# RANDOM
<a name="recipe-actions.functions.RANDOM"></a>

Returns a random number between 0 and 1 in a new column.

**Parameters**
+ `targetColumn` – The name of the new column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "RANDOM",
        "Parameters": {
            "targetColumn": "RANDOM Column 1"
        }
    }
}
```