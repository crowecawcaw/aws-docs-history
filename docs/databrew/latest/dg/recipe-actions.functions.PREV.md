

# PREV
<a name="recipe-actions.functions.PREV"></a>

Returns a new column, where each value represents a value that is *n* rows earlier in the source column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `numRows` – A value that represents *n* rows earlier in the source column. For example, if `numRows` is 3, then `PREV` uses the third-previous `sourceColumn` value as the new `targetColumn` value.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
{
    "Action": {
        "Operation": "PREV",
        "Parameters": {
            "numRows": "1",
            "sourceColumn": "age",
            "targetColumn": "age_PREV"
        }
    }
}
```