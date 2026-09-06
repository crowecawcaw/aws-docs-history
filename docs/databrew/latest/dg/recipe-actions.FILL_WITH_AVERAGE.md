

# FILL\_WITH\_AVERAGE
<a name="recipe-actions.FILL_WITH_AVERAGE"></a>

Returns a column with missing data replaced by the average of all values.

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "FILL_WITH_AVERAGE",
        "Parameters": {
            "sourceColumn": "age"
        }
    }
}
```