

# FLAG\_COLUMN\_FROM\_PATTERN
<a name="recipe-actions.FLAG_COLUMN_FROM_PATTERN"></a>

Creates a new column, based on the presence of a user-specified pattern in an existing column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of a new column to be created.
+ `flagType` – A value that must be set to `Pattern`.
+ `pattern` – A regular expression, indicating the pattern to be evaluated.
+ `trueString` – A value for the new column, if a null value is found in the source. If no value is specified, the default is `True`.
+ `falseString` – A value for the new column, if a non-null value is found in the source. If no value is specified, the default is `False`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "FLAG_COLUMN_FROM_PATTERN",
        "Parameters": {
            "falseString": "No",
            "flagType": "Pattern",
            "pattern": "N.*",
            "sourceColumn": "wind_direction",
            "targetColumn": "northerly",
            "trueString": "yes"
        }
    }
}
```