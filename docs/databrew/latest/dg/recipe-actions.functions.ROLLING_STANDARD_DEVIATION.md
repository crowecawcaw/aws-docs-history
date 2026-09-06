

# ROLLING\_STANDARD\_DEVIATION
<a name="recipe-actions.functions.ROLLING_STANDARD_DEVIATION"></a>

Returns in a new column the rolling standard deviation of values from a specified number of rows before to a specified number of rows after the current row in the specified column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `numRowsBefore` – A number of rows before the current source row, representing the start of the window.
+ `numRowsAfter` – A number of rows after the current source row, representing the end of the window.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
{
    "Action": {
        "Operation": "ROLLING_STDEV",
        "Parameters": {
            "numRowsAfter": "10",
            "numRowsBefore": "10",
            "sourceColumn": "weight_kg",
            "targetColumn": "weight_kg_ROLLING_STDEV"
        }
    }
}
```