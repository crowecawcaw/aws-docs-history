

# REMOVE\_INVALID
<a name="recipe-actions.REMOVE_INVALID"></a>

Deletes an entire row if an invalid value is encountered in a column of that row.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type of the column.
+ `advancedDataType` – Special data types that are detected by DataBrew in a column that has the data type `string`. The types that DataBrew can detect within a `string` column include SSN, Email, Phone Number, Gender, Credit Card, URL, IP Address, DateTime, Currency, ZipCode, Country, Region, State, and City.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "REMOVE_INVALID",
        "Parameters": {
            "columnDataType": "string",
            "sourceColumn": "help_url"
        }
    }
}
```