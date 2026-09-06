

# ADD\_DOUBLE\_QUOTES
<a name="recipe-actions.ADD_DOUBLE_QUOTES"></a>

Encloses the characters in a column with double quotation marks.

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "ADD_DOUBLE_QUOTES",
        "Parameters": {
            "sourceColumn": "info_url"
        }
    }
}
```