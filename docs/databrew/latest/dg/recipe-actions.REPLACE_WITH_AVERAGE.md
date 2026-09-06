

# REPLACE\_WITH\_AVERAGE
<a name="recipe-actions.REPLACE_WITH_AVERAGE"></a>

Replaces each invalid value in a column with the average of all other values.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type of the column. This type must be `number`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "REPLACE_WITH_AVERAGE",
        "Parameters": {
            "columnDataType": "number",
            "sourceColumn": "age"
        }
    }
}
```