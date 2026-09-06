

# FILL\_WITH\_LAST\_VALID
<a name="recipe-actions.FILL_WITH_LAST_VALID"></a>

Returns a column with missing data replaced by the most recent valid value for that column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type for the column. This type must be `date`, `number`, `boolean`, `unsupported`, `string`, or `timestamp`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "FILL_WITH_LAST_VALID",
        "Parameters": {
            "columnDataType": "string",
            "sourceColumn": "birth_date"
        }
    }
}
```