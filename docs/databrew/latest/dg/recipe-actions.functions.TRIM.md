

# TRIM
<a name="recipe-actions.functions.TRIM"></a>

Removes leading and trailing white space from the strings in the source column or custom strings, and returns the result in a new column. Spaces between words aren't removed.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value` – A character string to evaluate.
+ `targetColumn` – The name of the new column to be created.

**Note**  
You can specify either `sourceColumn` or `value`, but not both.

**Examples**  
  

```
{
    "RecipeAction": {
        "Operation": "TRIM",
        "Parameters": {
            "sourceColumn": "nationality",
            "targetColumn": "nationality_trim"
        }
    }
}
```
  

```
{
    "RecipeAction": {
        "Operation": "TRIM",
        "Parameters": {
            "value": "   This string should be trimmed       ",
            "targetColumn": "string_trimmed"
        }
    }
}
```