

# DATE\_TIME
<a name="recipe-actions.functions.DATETIME"></a>

Creates a new column containing the date and time value, from the source columns or from values provided.

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

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "DATE_TIME",
        "Parameters": {
            "dateTimeFormat": "yyyy-mm-dd HH:MM:SS",
            "dateTimeParameters": "{\"year\":{\"value\":\"2010\"},\"month\":{\"value\":\"5\"},\"day\":{\"value\":\"21\"},\"hour\":{\"value\":\"13\"},\"minute\":{\"value\":\"34\"},\"second\":{\"value\":\"25\"}}",
            "targetColumn": "DATETIME Column 1"
        }
    }
}
```