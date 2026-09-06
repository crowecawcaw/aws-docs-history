

# ROW\_NUMBER
<a name="recipe-actions.functions.ROW_NUMBER"></a>

Returns in a new column a session identifier based on a window created by column names from "group by" and "order by" statements.

**Parameters**
+ `groupByColumns` – A JSON-encoded string describing the "group by" columns.
+ `orderByColumns` – A JSON-encoded string describing the "order by" columns.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
{
    "Action": {
        "Operation": "ROW_NUMBER",
        "Parameters": {
            "groupByColumns": "[\"is public domain\"]",
            "orderByColumns": "[\"dimensions\"]",
            "targetColumn": "Row number"
        }
    }
}
```