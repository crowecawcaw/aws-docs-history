

# SPLIT\_COLUMN\_WITH\_INTERVALS
<a name="recipe-actions.SPLIT_COLUMN_WITH_INTERVALS"></a>

Splits a column at intervals of *n* characters, where you specify *n*.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `startPosition` – The character position where the split is to begin.
+ `interval` – The number of characters to skip before the next split.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_WITH_INTERVALS",
        "Parameters": {
            "interval": "4",
            "sourceColumn": "nationality",
            "startPosition": "1"
        }
    }
}
```