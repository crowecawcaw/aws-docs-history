

# NEST\_TO\_STRUCT
<a name="recipe-actions.NEST_TO_STRUCT"></a>

Converts user-selected columns into key-value pairs, each with a key representing the column name and a value representing the row value. The order of the selected columns and the data type of each column are maintained in the resultant struct.

**Parameters**
+ `sourceColumns` — List of the source columns.
+ `targetColumn` — The name of the target column.
+ `removeSourceColumns` — Contains the value `true` or `false` to indicate whether or not the user wants to remove the selected source columns.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "NEST_TO_STRUCT",
        "Parameters": {
            "sourceColumns": "[\"age\",\"weight_kg\",\"height_cm\"]",
            "targetColumn": "columnName",
            "removeSourceColumns": "true"
        }
    }
}
```