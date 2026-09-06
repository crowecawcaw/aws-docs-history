

# MEDIAN
<a name="recipe-actions.functions.MEDIAN"></a>

 Returns the median, the middle number of a sorted group of numbers, from the selected source columns in a new column. Any non-number is ignored.

**Parameters**
+ `sourceColumns` – A JSON-encoded string representing a list of existing columns.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "MEDIAN",
        "Parameters": {
            "sourceColumns": "[\"age\",\"years_in_service\"]",
            "targetColumn": "MEDIAN Column 1"
        }
    }
}
```