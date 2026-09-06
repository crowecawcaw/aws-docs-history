

# ROUND
<a name="recipe-actions.functions.ROUND"></a>

Rounds a numerical value to the nearest integer in a new column. It rounds up when the fraction is 0.5 or more. 

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "ROUND",
        "Parameters": {
            "sourceColumn": "rating",
            "targetColumn": "rating_ROUND"
        }
    }
}
```