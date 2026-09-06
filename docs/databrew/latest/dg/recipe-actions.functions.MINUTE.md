

# MINUTE
<a name="recipe-actions.functions.MINUTE"></a>

Creates a new column containing the minute value, from a string that represents a date.

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
        "Operation": "MINUTE",
        "Parameters": {
            "sourceColumn": "DATETIME Column 1",
            "targetColumn": "DATETIME Column 1_MINUTE"
        }
    }
}
```