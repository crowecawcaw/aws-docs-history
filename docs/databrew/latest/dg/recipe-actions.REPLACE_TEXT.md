

# REPLACE\_TEXT
<a name="recipe-actions.REPLACE_TEXT"></a>

Replaces a specified sequence of characters with another.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `pattern` – Character or characters or a regular expression, indicating which characters should be replaced in the source column.
+ `value` – The replacement character or characters to be substituted.

**Examples**  
  

```
{
    "RecipeAction": {
        "Operation": "REPLACE_TEXT",
        "Parameters": {
            "pattern": "x",
            "sourceColumn": "first_name",
            "value": "a"
        }
    }
}
```

```
{
    "RecipeAction": {
        "Operation": "REPLACE_TEXT",
        "Parameters": {
            "pattern": "[0-9]",
            "sourceColumn": "nationality",
            "value": "!"
        }
    }
}
```