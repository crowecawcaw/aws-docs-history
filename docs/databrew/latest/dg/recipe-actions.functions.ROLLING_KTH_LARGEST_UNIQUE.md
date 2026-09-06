

# ROLLING\_KTH\_LARGEST\_UNIQUE
<a name="recipe-actions.functions.ROLLING_KTH_LARGEST_UNIQUE"></a>

Returns in a new column the rolling unique *k*th largest value from a specified number of rows before to a specified number of rows after the current row in the specified column.

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
      "Operation": "ROLLING_KTH_LARGEST_UNIQUE",
      "Parameters": {
        "sourceColumn": "games_played",
        "numRowsBefore": "3",
        "numRowsAfter": "3",
        "value": "5",
        "targetColumn": "weight_kg_ROLLING_KTH_LARGEST_UNIQUE"
      }
    }
  }
```