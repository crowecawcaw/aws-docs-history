

# SPLIT\_COLUMN\_SINGLE\_DELIMITER
<a name="recipe-actions.SPLIT_COLUMN_SINGLE_DELIMITER"></a>

Splits a column into one or more new columns, according to a specific delimiter.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `pattern` – One or more characters to use as a separator, when splitting the data.
+ `limit` – How many splits to perform. The minimum is 1; the maximum is 20.
+ `includeInSplit` – If true, includes the pattern in the new column; otherwise, the pattern is discarded.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_SINGLE_DELIMITER",
        "Parameters": {
            "includeInSplit": "true",
            "limit": "1",
            "pattern": "/",
            "sourceColumn": "info_url"
        }
    }
}
```