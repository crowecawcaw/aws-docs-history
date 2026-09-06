

# PIVOT
<a name="recipe-actions.PIVOT"></a>

Converts all the row values in a selected column into individual columns with values.

![Diagram showing pivot column transformation: original table to new table with columns as values.](http://docs.aws.amazon.com/databrew/latest/dg/images/pivot.png)


**Parameters**
+ `sourceColumn` — The name of an existing column. The column can have a maximum of 10 distinct values.
+ `valueColumn` — The name of an existing column. The column can have a maximum of 10 distinct values.
+ `aggregateFunction` — The name of an aggregation function. If you don't want aggregation, use the keyword `COLLECT_LIST`.

**Example**  
  

```
{
    "Action": {
        "Operation": "PIVOT",
        "Parameters": {
            "aggregateFunction": "SUM",
            "sourceColumn": "state_name",
            "valueColumn": "all_votes"
        }
    }
}
```