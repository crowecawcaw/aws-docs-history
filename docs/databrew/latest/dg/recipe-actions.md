# SPLIT_COLUMN_BETWEEN_DELIMITER

Splits a column into three new columns, according to a beginning and ending
delimiter.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `patternOption1` – A JSON-encoded string representing one or more
  characters that indicate the first delimiter.
- `patternOption2` – A JSON-encoded string representing one or more
  characters that indicate the second delimiter.
- `pattern` – One or more characters to use as a separator,
  when splitting the data.
- `includeInSplit` – If true, includes the pattern in the new
  column; otherwise, the pattern is discarded.

###### Example

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_BETWEEN_DELIMITER",
        "Parameters": {
            "patternOption1": "{\"pattern\":\"H\",\"includeInSplit\":true}",
            "patternOption2": "{\"pattern\":\"M\",\"includeInSplit\":true}",
            "sourceColumn": "last_name"
        }
    }
}
```
