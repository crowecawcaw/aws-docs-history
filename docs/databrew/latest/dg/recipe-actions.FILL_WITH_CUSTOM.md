

# FILL\_WITH\_CUSTOM
<a name="recipe-actions.FILL_WITH_CUSTOM"></a>

Returns a column with missing data replaced by a specific value.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type for the column. This type must be `date`, `number`, `boolean`, `unsupported`, `string`, or `timestamp`.
+ `value` – The custom value to fill in. The data type must match the value that you choose for `columnDataType`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "FILL_WITH_CUSTOM",
        "Parameters": {
            "columnDataType": "string",
            "sourceColumn": "last_name",
            "value": "No last name provided"
        }
    }
}
```