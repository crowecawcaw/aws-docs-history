

# DATE\_FORMAT
<a name="recipe-actions.functions.DATE_FORMAT"></a>

Creates a new column containing a date, in a specific format, from a string that represents a date.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value` – A string to evaluate.
+ `dateTimeFormat` – Optional. A format string for the date, as it is to appear in the new column. If not specified, the default format is `yyyy-mm-dd HH:MM:SS`.
+ `targetColumn` – A name for the newly created column.
**Note**  
You can specify either `sourceColumn` or `value`, but not both.

**Examples**  
  

```
{
    "RecipeAction": {
        "Operation": "DATE_FORMAT",
        "Parameters": {
            "sourceColumn": "DATE Column 1",
            "dateTimeFormat": "month*dd*yyyy",
            "targetColumn": "DATE Column 1_DATEFORMAT"
        }
    }
}
```
  

```
{
    "RecipeAction": {
        "Operation": "DATE_FORMAT",
        "Parameters": {
            "value": "22:10:47",
            "dateTimeFormat": "HH:MM:SS",
            "targetColumn": "formatted_date_value"
        }
    }
}
```