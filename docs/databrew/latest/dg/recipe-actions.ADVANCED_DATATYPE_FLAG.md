

# ADVANCED\_DATATYPE\_FLAG
<a name="recipe-actions.ADVANCED_DATATYPE_FLAG"></a>

Creates a new flag column based on the values for the current source column. For example, given a source column containing zip codes, this transform can be used to flag values as `true` or `false` based on a particular timezone. The details that you can extract depend on the pattern that is detected, as described in **Notes** below.

**Parameters**
+ `sourceColumn` – The name of a string source column.
+ `pattern` – The pattern to extract.
+ `targetColumn` – The name of the target column.
+ `advancedDataType` – Can be one of Phone, Zip Code, Date Time, State, Credit Card, URL, Email, SSN, or Gender.
+ `filter values` – List of string values that the user wants to filter the column based on.
+ `trueString` – The `true` value for the target column.
+ `falseString` – The `false` value for the target column.

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
        "Operation": "ADVANCED_DATATYPE_FLAG",
        "Parameters": {
            "pattern": "AREA_CODE",
            "sourceColumn": "phoneColumn",
            "advancedDataType": "Phone",
            "filterValues": ['Ohio'],
            "targetColumn": "targetColumnName",
            "trueString": "trueValue",
            "falseString": "falseValue"
        }
    }
}
```