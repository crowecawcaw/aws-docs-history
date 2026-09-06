

# SPLIT\_COLUMN\_FROM\_END
<a name="recipe-actions.SPLIT_COLUMN_FROM_END"></a>

Splits a column into two new columns, at an offset from the end of the string.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `position` – The character position, from the right end of the string, where the split is to occur.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_FROM_END",
        "Parameters": {
            "position": "1",
            "sourceColumn": "nationality"
        }
    }
}
```