

# SPLIT\_COLUMN\_BETWEEN\_POSITIONS
<a name="recipe-actions.SPLIT_COLUMN_BETWEEN_POSITIONS"></a>

Splits a column into three new columns, according to offsets that you specify.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `startPosition` – The character position where the split is to begin.
+ `endPosition` – The character position where the split is to end.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_BETWEEN_POSITIONS",
        "Parameters": {
            "endPosition": "12",
            "sourceColumn": "last_name",
            "startPosition": "2"
        }
    }
}
```