

# UNIX\_TIME
<a name="recipe-actions.functions.UNIX_TIME"></a>

Creates a new column containing a number representing epoch time (Unix time)—the number of seconds since January 1, 1970—based on a source column or input value. If time zone can be inferred, the output is in that time zone. Otherwise, the output is in Universal Coordinated Time (UTC).

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value` – A character string to evaluate.
+ `targetColumn` – A name for the newly created column.

**Note**  
You can specify either `sourceColumn` or `value`, but not both.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "UNIX_TIME",
        "Parameters": {
            "sourceColumn": "TIME Column 1",
            "targetColumn": "TIME Column 1_UNIXTIME"
        }
    }
}
```