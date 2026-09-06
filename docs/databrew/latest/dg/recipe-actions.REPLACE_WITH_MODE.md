

# REPLACE\_WITH\_MODE
<a name="recipe-actions.REPLACE_WITH_MODE"></a>

Replaces each invalid value in a column with the mode of all other values.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type of the column. This type must be `number`.
+ `modeType` – How to resolve tie values in the data. This value must be `MINIMUM`, `NONE`, `AVERAGE`, or `MAXIMUM`. 

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "REPLACE_WITH_MODE",
        "Parameters": {
            "columnDataType": "number",
            "modeType": "MAXIMUM",
            "sourceColumn": "height_cm"
        }
    }
}
```