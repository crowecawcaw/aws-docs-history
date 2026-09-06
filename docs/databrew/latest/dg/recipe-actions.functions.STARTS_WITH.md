

# STARTS\_WITH
<a name="recipe-actions.functions.STARTS_WITH"></a>

Returns `true` in a new column if a specified number of leftmost characters, or custom string, matches a pattern.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value` – A character string to evaluate.
+ `pattern` – A regular expression that must match the start of the string.
+ `targetColumn` – The name of the new column to be created.

**Note**  
You can specify either `sourceColumn` or `value`, but not both.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "STARTS_WITH",
        "Parameters": {
            "sourceColumn": "nationality",
            "pattern": "[AEIOU]",
            "targetColumn": "nationality_starts_with"
        }
    }
}
```