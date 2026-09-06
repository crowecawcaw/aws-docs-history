

# SESSION
<a name="recipe-actions.functions.SESSION"></a>

Returns in a new column a session identifier based on a window created by column names from "group by" and "order by" statements. 

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `units` – A unit of measure for describe the session length. Valid values are `MONTHS`, `YEARS`, `MILLISECONDS`, `QUARTERS`, `HOURS`, `MICROSECONDS`, `WEEKS`, `SECONDS`, `DAYS`, and `MINUTES`.
+ `value` – The number of `units` to define the time period.
+ `groupByColumns` – A JSON-encoded string describing the "group by" columns.
+ `orderByColumns` – A JSON-encoded string describing the "order by" columns.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
{
    "Action": {
        "Operation": "SESSION",
        "Parameters": {
            "sourceColumn": "object number",
            "units": "MINUTES",
            "value": "10",
            "groupByColumns": "[\"is public domain\"]",
            "orderByColumns": "[\"dimensions\"]",
            "targetColumn": "object number_SESSION",
        }
    }
}
```