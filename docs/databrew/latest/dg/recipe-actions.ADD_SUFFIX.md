

# ADD\_SUFFIX
<a name="recipe-actions.ADD_SUFFIX"></a>

Adds one more characters concatenating them as a suffix to the end of a column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `pattern` – The character or characters to place at the end of the column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "ADD_SUFFIX",
        "Parameters": {
            "pattern": "bbb",
            "sourceColumn": "info_url"
        }
    }
}
```