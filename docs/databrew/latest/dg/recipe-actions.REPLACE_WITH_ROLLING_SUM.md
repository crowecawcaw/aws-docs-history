

# REPLACE\_WITH\_ROLLING\_SUM
<a name="recipe-actions.REPLACE_WITH_ROLLING_SUM"></a>

Replaces each value in a column with the rolling sum from a previous "window" of rows.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type of the column. This type must be `number`.
+ `period` - – The size of the window. For example, if `period` is 10, the rolling sum is computed using the previous 10 rows.

**Example**  
  

```
{
    "RecipeStep": {
        "Action": {
            "Operation": "REPLACE_WITH_ROLLING_SUM",
            "Parameters": {
                "sourceColumn": "created_at",
                "columnDataType": "number",
                "period": "2"
            }
        }
    }
}
```