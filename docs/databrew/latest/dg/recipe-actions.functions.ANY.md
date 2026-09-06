

# ANY
<a name="recipe-actions.functions.ANY"></a>

 Returns any values from the selected source columns in a new column. Empty and null values are ignored.

**Parameters**
+ `sourceColumns` – A JSON-encoded string representing a list of existing columns.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "ANY",
        "Parameters": {
            "sourceColumns": "[\"age\",\"last_name\"]",
            "targetColumn": "ANY Column 1"
        }
    }
}
```