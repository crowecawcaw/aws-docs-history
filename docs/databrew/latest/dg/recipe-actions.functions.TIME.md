

# TIME
<a name="recipe-actions.functions.TIME"></a>

Creates a new column containing the time value, from the source columns or values provided.

**Parameters**
+ `dateTimeFormat` – Optional. A format string for the date, as it is to appear in the new column. If this string isn't specified, the default format is `yyyy-mm-dd HH:MM:SS`.
+ `dateTimeParameters` – A JSON-encoded string representing the components of the date and time:
  + `year`
  + `value`
  + `month`
  + `day`
  + `hour`
  + `second`

  Each component must specify one of the following:
  + `sourceColumn` – The name of an existing column.
  + `value` – A character string to evaluate.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "TIME",
        "Parameters": {
            "dateTimeFormat": "HH:MM:SS",
            "dateTimeParameters": "{\"year\":{},\"month\":{},\"day\":{},\"hour\":{\"sourceColumn\":\"rand_hour\"},\"minute\":{\"sourceColumn\":\"rand_minute\"},\"second\":{\"sourceColumn\":\"rand_second\"}}",
            "targetColumn": "TIME Column 1"
        }
    }
}
```