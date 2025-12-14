# CONVERT_TIMEZONE

Converts a time value from the source column into a new column based on a
specified timezone.

###### Parameters

- `sourceColumn` – The name of an existing column. The source column can be of type `string`, `date`, or `timestamp`.
- `fromTimeZone` – Source value timezone. If nothing is
  specified, the default timezone is UTC.
- `toTimeZone` – Timezone to be converted to. If nothing is specified, the default timezone is UTC.
- `targetColumn` – A name for the newly-created
  column.
- `dateTimeFormat` – Optional. A format string for the date. If the format isn't specified, the default format is used: `yyyy-mm-dd HH:MM:SS`.

###### Example

```
{
    "RecipeAction": {
        "Operation": "CONVERT_TIMEZONE",
        "Parameters": {
            "sourceColumn": "DATETIME Column 1",
            "fromTimeZone": "UTC+08:00",
            "toTimeZone": "UTC+08:00",
            "targetColumn": "DATETIME Column CONVERT_TIMEZONE",
            "dateTimeFormat": "yyyy-mm-dd HH:MM:SS"
        }
    }
}
```
