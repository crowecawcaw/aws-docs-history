# EXTRACT_ADVANCED_DATATYPE_DETAILS

Extracts details for the advanced data type. The details that you can extract depend on the pattern
that is detected, as described in **Notes** below.

###### Parameters

- `sourceColumn` – The name of a string source column.
- `pattern` – The pattern to extract.
- `targetColumn` – The name of the target column.
- `advancedDataType` – Can be one of Phone, Zip Code, Date Time,
  State, Credit Card, URL, Email, SSN, or Gender.

###### Notes

- If advancedDataType is **Phone**, then the
  pattern can be AREA_CODE, TIME_ZONE, or COUNTRY_CODE.
- If advancedDataType is **Zip Code**, then the
  pattern can be TIME_ZONE, COUNTRY, STATE, CITY, TYPE, or REGION.
- If advancedDataType is **Date Time**, then the
  pattern can be DAY, MONTH, MONTH_NAME, WEEK, QUARTER, or YEAR.
- If advancedDataType is **State**, then the
  pattern can be TIME_ZONE.
- If advancedDataType is **Credit Card**, then the
  pattern can be LENGTH or NETWORK.
- If advancedDataType is **URL**, then the
  pattern can be PROTOCOL, TLD, or DOMAIN.

###### Example

```
{
    "RecipeAction": {
        "Operation": "EXTRACT_ADVANCED_DATATYPE_DETAILS",
        "Parameters": {
            "pattern": "TIMEZONE"
            "sourceColumn": "zipCode",
            "targetColumn": "timeZoneFromZipCode",
            "advancedDataType": "ZipCode"
        }
    }
}
```
