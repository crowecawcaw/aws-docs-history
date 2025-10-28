# NOW

Creates a new column containing the current date and time in the format
`yyyy-mm-dd HH:MM:SS`.

###### Parameters

- `timeZone` – The name of a time zone. If no time zone is
  specified, then the default is Universal Coordinated Time (UTC).
- `targetColumn` – A name for the newly created column.

###### Example

```
{
    "RecipeAction": {
        "Operation": "NOW",
        "Parameters": {
            "timeZone": "US/Pacific",
            "targetColumn": "NOW Column 1"
        }
}
```
