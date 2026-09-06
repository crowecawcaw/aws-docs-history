

# COUNT
<a name="recipe-actions.functions.COUNT"></a>

 Returns the number of values from the selected source columns in a new column. Empty and null values are ignored.

**Parameters**
+ `sourceColumns` – A JSON-encoded string representing a list of existing columns.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "COUNT",
        "Parameters": {
            "sourceColumns": "[\"ANY Column 1\",\"birth_date\",\"last_name\"]",
            "targetColumn": "COUNT Column 1"
        }
    }
}
```