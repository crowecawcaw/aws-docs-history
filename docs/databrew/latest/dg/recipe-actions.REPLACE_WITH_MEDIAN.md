

# REPLACE\_WITH\_MEDIAN
<a name="recipe-actions.REPLACE_WITH_MEDIAN"></a>

Replaces each invalid value in a column with the median of all other values.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type of the column. This type must be `number`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "REPLACE_WITH_MEDIAN",
        "Parameters": {
            "columnDataType": "number",
            "sourceColumn": "games_won"
        }
    }
}
```