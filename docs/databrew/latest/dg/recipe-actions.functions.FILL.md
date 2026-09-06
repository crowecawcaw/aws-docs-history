

# FILL
<a name="recipe-actions.functions.FILL"></a>

Returns a new column based on a specified source column. For any missing or null values in the source column, `FILL` chooses the most recent nonblank value from a window of rows before and after the source value in question. The chosen value is then placed in the new column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `numRowsBefore` – A number of rows before the current source row, representing the start of the window.
+ `numRowsAfter` – A number of rows after the current source row, representing the end of the window.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
{
    "Action": {
        "Operation": "FILL",
        "Parameters": {
            "numRowsAfter": "10",
            "numRowsBefore": "10",
            "sourceColumn": "last_name",
            "targetColumn": "last_name_FILL"
        }
    }
}
```