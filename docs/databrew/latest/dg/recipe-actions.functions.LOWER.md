

# LOWER
<a name="recipe-actions.functions.LOWER"></a>

Converts all alphabetical characters from the strings in the source column or custom strings to lowercase, and returns the result in a new column.

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
        "Operation": "LOWER",
        "Parameters": {
            "sourceColumn": "last_name",
            "targetColumn": "last_name_lower"
        }
    }
}
```
  

```
{
    "RecipeAction": {
        "Operation": "LOWER",
        "Parameters": {
            "value": "GOODBYE",
            "targetColumn": "goodbye_lower"
        }
    }
}
```