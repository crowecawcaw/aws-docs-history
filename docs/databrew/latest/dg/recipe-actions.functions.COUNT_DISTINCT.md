

# COUNT\_DISTINCT
<a name="recipe-actions.functions.COUNT_DISTINCT"></a>

 Returns the total number of distinct values from the selected source columns in a new column. Empty and null values are ignored.

**Parameters**
+ `sourceColumns` – A JSON-encoded string representing a list of existing columns.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "COUNT_DISTINCT",
        "Parameters": {
            "sourceColumns": "[\"long_name\",\"weight_kg\"]",
            "targetColumn": "COUNT_DISTINCT Column 1"
        }
    }
}
```