

# NEST\_TO\_ARRAY
<a name="recipe-actions.NEST_TO_ARRAY"></a>

Converts user-selected columns into array values. The order of the selected columns is maintained while creating the resultant array. The different column data types are typecast to a common type that supports the data types of all columns.

**Parameters**
+ `sourceColumns` — List of the source columns.
+ `targetColumn` — The name of the target column.
+ `removeSourceColumns` — Contains the value `true` or `false` to indicate whether or not the user wants to remove the selected source columns.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "NEST_TO_ARRAY",
        "Parameters": {
            "sourceColumns": "[\"age\",\"weight_kg\",\"height_cm\"]",
            "targetColumn": "columnName",
            "removeSourceColumns": "true"
        }
    }
}
```