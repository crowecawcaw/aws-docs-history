

# REPLACE\_WITH\_LAST\_VALID
<a name="recipe-actions.REPLACE_WITH_LAST_VALID"></a>

Replaces each invalid value in a column with the last valid value.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type of the column.
+ `advancedDataType` – Special data types that are detected by DataBrew in a column that has the data type `string`. The types that DataBrew can detect within a `string` column include SSN, Email, Phone Number, Gender, Credit Card, URL, IP Address, DateTime, Currency, ZipCode, Country, Region, State, and City.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "REPLACE_WITH_LAST_VALID",
        "Parameters": {
            "columnDataType": "number",
            "sourceColumn": "rating"
        }
    }
}
```