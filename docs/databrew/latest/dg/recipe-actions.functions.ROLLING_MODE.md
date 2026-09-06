

# ROLLING\_MODE
<a name="recipe-actions.functions.ROLLING_MODE"></a>

Returns in a new column the rolling mode (most common value) from a specified number of rows before to a specified number of rows after the current row in the specified column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `numRowsBefore` – A number of rows before the current source row, representing the start of the window.
+ `numRowsAfter` – A number of rows after the current source row, representing the end of the window.
+ modeType – The modal function to apply to the window. Valid values are `NONE`, `MINIMUM`, `MAXIMUM`, and `AVERAGE`.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
{
    "Action": {
        "Operation": "ROLLING_MODE",
        "Parameters": {
            "modeType": "MINIMUM",
            "numRowsAfter": "10",
            "numRowsBefore": "10",
            "sourceColumn": "weight_kg",
            "targetColumn": "weight_kg_ROLLING_MODE"
        }
    }
}
```