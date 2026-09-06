

# REPLACE\_WITH\_ROLLING\_AVERAGE
<a name="recipe-actions.REPLACE_WITH_ROLLING_AVERAGE"></a>

Replaces each value in a column with the rolling average from a previous "window" of rows.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type of the column. This type must be `number`.
+ `period` - – The size of the window. For example, if `period` is 10, the rolling average is computed using the previous 10 rows.

**Example**  
  

```
{
    "RecipeStep": {
        "Action": {
            "Operation": "REPLACE_WITH_ROLLING_AVERAGE",
            "Parameters": {
                "sourceColumn": "created_at",
                "columnDataType": "number",
                "period": "2"
            }
        }
    }
}
```