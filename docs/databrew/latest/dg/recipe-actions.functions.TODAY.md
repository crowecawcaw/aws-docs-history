# TODAY

Creates a new column containing the current date in the format
`yyyy-mm-dd`.

###### Parameters

- `timeZone` – The name of a time zone. If no time zone is specified,
  then the default is Universal Coordinated Time (UTC).
- `targetColumn` – A name for the newly created column.

###### Example

```
{
    "RecipeAction": {
        "Operation": "TODAY",
        "Parameters": {
            "timeZone": "US/Pacific",
            "targetColumn": "TODAY Column 1"
        }
    }
}
```
