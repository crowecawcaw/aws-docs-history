

# ADVANCED\_DATATYPE\_FILTER
<a name="recipe-actions.ADVANCED_DATATYPE_FILTER"></a>

Filters the current source column based on advanced data type detection. For example, given a column that DataBrew has identified as containing zip codes, this transform can filter the column based on timezone. The details that you can extract depend on the pattern that is detected, as described in **Notes** below.

**Parameters**
+ `sourceColumn` – The name of a string source column.
+ `pattern` – The pattern to extract.
+ `advancedDataType` – Can be one of Phone, Zip Code, Date Time, State, Credit Card, URL, Email, SSN, or Gender.
+ `filter values` – List of string values that the user wants to filter the column based on.
+ `strategy` – KEEP\_ROWS or DISCARD\_ROWS or CLEAR\_FILTERS or CLEAR\_OTHERS.
+ `clearWithEmpty` – Boolean `true` or `false`, to clear rows with `empty` instead of `null`.

**Notes**
+ If advancedDataType is **Phone**, then the pattern can be AREA\_CODE, TIME\_ZONE, or COUNTRY\_CODE.
+ If advancedDataType is **Zip Code**, then the pattern can be TIME\_ZONE, COUNTRY, STATE, CITY, TYPE, or REGION.
+ If advancedDataType is **Date Time**, then the pattern can be DAY, MONTH, MONTH\_NAME, WEEK, QUARTER, or YEAR.
+ If advancedDataType is **State**, then the pattern can be TIME\_ZONE.
+ If advancedDataType is **Credit Card**, then the pattern can be LENGTH or NETWORK.
+ If advancedDataType is **URL**, then the pattern can be PROTOCOL, TLD, or DOMAIN.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "ADVANCED_DATATYPE_FILTER",
        "Parameters": {
            "pattern": "AREA_CODE",
            "sourceColumn": "phoneColumn",
            "advancedDataType": "Phone",
            "filterValues": ['Ohio'],
            "strategy": "KEEP_ROWS"
        }
    }
}
```