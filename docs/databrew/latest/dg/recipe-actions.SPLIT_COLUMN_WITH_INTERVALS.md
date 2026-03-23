# SPLIT_COLUMN_WITH_INTERVALS

Splits a column at intervals of _n_ characters, where you specify
_n_.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `startPosition` – The character position where the split is
  to begin.
- `interval` – The number of characters to skip before the next
  split.

###### Example

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
