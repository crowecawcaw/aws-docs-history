

# MOD
<a name="recipe-actions.functions.MOD"></a>

Returns the percent that one number is of another number in a new column.

**Parameters**
+ `sourceColumn1` – The name of an existing column.
+ `sourceColumn2` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "MOD",
        "Parameters": {
            "sourceColumn1": "start_date",
            "sourceColumn2": "end_date",
            "targetColumn": "MOD Column 1"
        }
    }
}
```