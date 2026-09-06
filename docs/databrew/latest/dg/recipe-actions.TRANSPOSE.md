

# TRANSPOSE
<a name="recipe-actions.TRANSPOSE"></a>

Converts all selected rows to columns and columns to rows.

![Table transformation from rows to columns, showing data reorganization for improved analysis.](http://docs.aws.amazon.com/databrew/latest/dg/images/transpose.png)


**Parameters**
+ `pivotColumns` — A JSON-encoded string representing a list of columns whose rows will be converted to column names.
+ `valueColumns` — A JSON-encoded string representing a list of one or more columns to be converted to rows.
+ `aggregateFunction` — The name of an aggregation function. If you don't want aggregation, use the keyword `COLLECT_LIST`.
+ `newColumn` — The column to hold transposed columns as values.

**Example**  
  

```
{
    "Action": {
        "Operation": "TRANSPOSE",
        "Parameters": {
            "pivotColumns": "[\"Teacher\"]",
            "valueColumns": "[\"Tom\",\"John\",\"Harry\"]",
            "aggregateFunction": "COLLECT_LIST",
            "newColumn": "Student"
        }
    }

}
```