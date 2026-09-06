

# REPLACE\_WITH\_CUSTOM
<a name="recipe-actions.REPLACE_WITH_CUSTOM"></a>

Replace detected entities with a custom value.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `sourceColumns` – A list of existing column names.
+ `columnDataType` – The data type of the column.
+ `value` – The custom value to be used to replace invalid values.
+ `advancedDataType` – Special data types that are detected by DataBrew in a column that has the data type `string`. The types that DataBrew can detect within a `string` column include SSN, Email, Phone Number, Gender, Credit Card, URL, IP Address, DateTime, Currency, ZipCode, Country, Region, State, and City.

**Note**  
Use either `sourceColumn` or `sourceColumns`, but not both.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "REPLACE_WITH_CUSTOM",
        "Parameters": {
            "columnDataType": "number",
            "sourceColumn": "",
            "sourceColumns": ["column1", "column2"],
            "value": 0
        }
    }
}
```