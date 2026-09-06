

# FLAG\_COLUMN\_FROM\_NULL
<a name="recipe-actions.FLAG_COLUMN_FROM_NULL"></a>

Creates a new column, based on the presence of null values in an existing column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of a new column to be created.
+ `flagType` – A value that must be set to `Null values`.
+ `trueString` – A value for the new column, if a null value is found in the source. If no value is specified, the default is `True`.
+ `falseString` – A value for the new column, if a non-null value is found in the source. If no value is specified, the default is `False`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "FLAG_COLUMN_FROM_NULL",
        "Parameters": {
            "flagType": "Null values",
            "sourceColumn": "weight_kg",
            "targetColumn": "is_weight_kg_missing"
        }
    }
}
```