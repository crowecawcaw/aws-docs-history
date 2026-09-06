

# ENDS\_WITH
<a name="recipe-actions.functions.ENDS_WITH"></a>

Returns `true` in a new column if a specified number of rightmost characters, or custom string, matches a pattern.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value` – A character string to evaluate.
+ `pattern` – A regular expression that must match the end of the string.
+ `targetColumn` – The name of the new column to be created.

**Note**  
You can specify either `sourceColumn` or `value`, but not both.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "ENDS_WITH",
        "Parameters": {
            "sourceColumn": "nationality",
            "pattern": "[Ss]",
            "targetColumn": "nationality_ends_with"
        }
    }
}
```