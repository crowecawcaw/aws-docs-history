

# ROLLING\_KTH\_LARGEST
<a name="recipe-actions.functions.ROLLING_KTH_LARGEST"></a>

Returns in a new column the rolling *k*th largest value from a specified number of rows before to a specified number of rows after the current row in the specified column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `numRowsBefore` – A number of rows before the current source row, representing the start of the window.
+ `numRowsAfter` – A number of rows after the current source row, representing the end of the window.
+ `value` – The value for *k*.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
  {
    "Action": {
      "Operation": "ROLLING_KTH_LARGEST",
      "Parameters": {
        "sourceColumn": "weight_kg",
        "numRowsBefore": "5",
        "numRowsAfter": "5",
        "value": "3"
        "targetColumn": "weight_kg_ROLLING_KTH_LARGEST"
      }
    }
  }
```