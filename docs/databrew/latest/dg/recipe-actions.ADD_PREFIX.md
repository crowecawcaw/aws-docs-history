

# ADD\_PREFIX
<a name="recipe-actions.ADD_PREFIX"></a>

Adds one or more characters, concatenating them as a prefix to the beginning of a column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `pattern` – The character or characters to place at the beginning of the column values.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "ADD_PREFIX",
        "Parameters": {
            "pattern": "aaa",
            "sourceColumn": "info_url"
        }
    }
}
```