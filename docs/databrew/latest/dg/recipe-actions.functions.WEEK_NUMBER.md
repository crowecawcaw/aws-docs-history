

# WEEK\_NUMBER
<a name="recipe-actions.functions.WEEK_NUMBER"></a>

Creates a new column containing the number of the week (from 1 to 52), from a string that represents a date.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value` – A character string to evaluate.
+ `targetColumn` – A name for the newly created column.

**Note**  
You can specify either `sourceColumn` or `value`, but not both.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "WEEK_NUMBER",
        "Parameters": {
            "sourceColumn": "DATETIME Column 1",
            "targetColumn": "DATETIME Column 1_WEEK_NUMBER"
        }
    }
}
```