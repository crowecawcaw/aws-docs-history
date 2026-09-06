

# SPLIT\_COLUMN\_MULTIPLE\_DELIMITER
<a name="recipe-actions.SPLIT_COLUMN_MULTIPLE_DELIMITER"></a>

Splits a column according to multiple delimiters.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `patternOptions` – A JSON-encoded string representing one or more patterns that determine the split criteria.
+ `pattern` – One or more characters to use as a separator, when splitting the data.
+ `limit` – How many splits to perform. The minimum is 1; the maximum is 20.
+ `includeInSplit` – If true, includes the pattern in the new column; otherwise, the pattern is discarded.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_MULTIPLE_DELIMITER",
        "Parameters": {
            "limit": "1",
            "patternOptions": "[{\"pattern\":\",\",\"includeInSplit\":true},{\"pattern\":\" \",\"includeInSplit\":true}]",
            "sourceColumn": "description"
        }
    }
}
```