

# REPLACE\_BETWEEN\_DELIMITERS
<a name="recipe-actions.REPLACE_BETWEEN_DELIMITERS"></a>

Replaces the characters between two delimiters with user-specified text.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `startPattern` – Character or characters or a regular expression, indicating where the substitution is to begin.
+ `endPattern` – Character or characters or a regular expression, indicating where the substitution is to end.
+ `value` – The replacement character or characters to be substituted.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "REPLACE_BETWEEN_DELIMITERS",
        "Parameters": {
            "endPattern": ">",
            "sourceColumn": "last_name",
            "startPattern": "&lt;",
            "value": "?"
        }
    }
}
```