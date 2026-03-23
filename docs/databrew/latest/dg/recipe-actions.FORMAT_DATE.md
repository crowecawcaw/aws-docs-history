# FORMAT_DATE

Returns a column in which a date string is converted into a formatted value.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `targetDateFormat` – One of the following date
  formats:
  - `mm/dd/yyyy`
  - `mm-dd-yyyy`
  - `dd month yyyy`
  - `month yyyy`
  - `dd month`

###### Example

```
{
    "RecipeAction": {
        "Operation": "FORMAT_DATE",
        "Parameters": {
            "sourceColumn": "birth_date",
            "targetDateFormat": "mm-dd-yyyy"
        }
    }
}

```
