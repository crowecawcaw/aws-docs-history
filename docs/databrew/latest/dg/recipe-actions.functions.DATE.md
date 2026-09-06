

# DATE
<a name="recipe-actions.functions.DATE"></a>

Creates a new column containing the date value, from the source columns or from values provided.

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
        "Operation": "DATE",
        "Parameters": {
            "dateTimeFormat": "mm/dd/yy",
            "dateTimeParameters": "{\"year\":{\"value\":\"2019\"},\"month\":{\"value\":\"12\"},\"day\":{\"value\":\"31\"},\"hour\":{},\"minute\":{},\"second\":{}}",
            "targetColumn": "DATE Column 1"
        }
    }
}
```