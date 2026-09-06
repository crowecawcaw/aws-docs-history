

# MERGE\_COLUMNS\_AND\_VALUES
<a name="recipe-actions.functions.MERGE"></a>

Concatenates the strings in the source columns and returns the result in a new column. You can insert a delimiter between the merged values.

**Parameters**
+ `sourceColumns` – The names of two or more existing columns, in JSON-encoded format.
+ `delimiter` – Optional. One or more characters to place between each two source column values. 
+ `targetColumn` – The name of the new column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "MERGE_COLUMNS_AND_VALUES",
        "Parameters": {
            "sourceColumns": "[\"last_name\",\"birth_date\"]",
            "delimiter": " was born on: ",
            "targetColumn": "merged_column"
        }
    }
}
```