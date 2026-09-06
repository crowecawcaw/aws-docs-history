

# UNIX\_TIME\_FORMAT
<a name="recipe-actions.functions.UNIX_TIME_FORMAT"></a>

Converts Unix time for a source column or input value to a specified numerical date format, and returns the result in a new column. 

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value` – An integer that represents a Unix epoch timestamp.
+ `dateTimeFormat` – Optional. A format string for the date, as it is to appear in the new column. If not specified, the default format is `yyyy-mm-dd HH:MM:SS`.
+ `targetColumn` – A name for the newly created column.

**Note**  
You can specify either `sourceColumn` or `value`, but not both.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "UNIX_TIME_FORMAT",
        "Parameters": {
            "value": "1601936554",
            "dateTimeFormat": "yyyy-mm-dd HH:MM:SS",
            "targetColumn": "UNIXTIMEFORMAT Column 1"
        }
    }
}
```