

# FILL\_WITH\_SUM
<a name="recipe-actions.FILL_WITH_SUM"></a>

Returns a column with missing data replaced by the sum of all values.

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "FILL_WITH_SUM",
        "Parameters": {
            "sourceColumn": "age"
        }
    }
}
```