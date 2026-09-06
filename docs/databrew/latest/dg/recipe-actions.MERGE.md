

# MERGE
<a name="recipe-actions.MERGE"></a>

Merges two or more columns into a new column.

**Parameters**
+ `sourceColumns` – A JSON-encoded string representing a list of one or more columns to be merged.
+ `delimiter` – An optional separator between the values, to appear in the target column.
+ `targetColumn` – The name of the merged column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "MERGE",
        "Parameters": {
            "delimiter": " ",
            "sourceColumns": "[\"first_name\",\"last_name\"]",
            "targetColumn": "Merged Column 1"
        }
    }
}
```