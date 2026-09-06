

# REPLACE\_WITH\_NULL
<a name="recipe-actions.REPLACE_WITH_NULL"></a>

Replaces each invalid value in a column with a null value.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type of the column.
+ `advancedDataType` – Special data types that are detected by DataBrew in a column that has the data type `string`. The types that DataBrew can detect within a `string` column include SSN, Email, Phone Number, Gender, Credit Card, URL, IP Address, DateTime, Currency, ZipCode, Country, Region, State, and City.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "REPLACE_WITH_NULL",
        "Parameters": {
            "columnDataType": "number",
            "sourceColumn": "weight_kg"
        }
    }
}
```