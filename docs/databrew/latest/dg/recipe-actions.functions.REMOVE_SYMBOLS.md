

# REMOVE\_SYMBOLS
<a name="recipe-actions.functions.REMOVE_SYMBOLS"></a>

Removes characters that aren't letters, numbers, accented Latin characters, or white space from the strings in the source column or custom strings, and returns the result in a new column.

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
        "Operation": "REMOVE_SYMBOLS",
        "Parameters": {
            "sourceColumn": "info_url",
            "targetColumn": "info_url_remove_symbols"
        }
    }
}
```
  

```
{
    "RecipeAction": {
        "Operation": "REMOVE_SYMBOLS",
        "Parameters": {
            "value": "$&#$&HEY!#@@",
            "targetColumn": "without_symbols"
        }
    }
}
```