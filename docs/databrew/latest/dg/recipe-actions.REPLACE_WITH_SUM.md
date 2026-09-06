

# REPLACE\_WITH\_SUM
<a name="recipe-actions.REPLACE_WITH_SUM"></a>

Replaces each invalid value in a column with the sum of all other values.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type of the column. This type must be `number`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "REPLACE_WITH_SUM",
        "Parameters": {
            "columnDataType": "number",
            "sourceColumn": "games_won"
        }
    }
}
```