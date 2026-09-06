

# SPLIT\_COLUMN\_FROM\_START
<a name="recipe-actions.SPLIT_COLUMN_FROM_START"></a>

Splits a column into two new columns, at an offset from the beginning of the string.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `position` – The character position, from the left end of the string, where the split is to occur.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_FROM_START",
        "Parameters": {
            "position": "1",
            "sourceColumn": "first_name"
        }
    }
}
```