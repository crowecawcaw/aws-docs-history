

# FILL\_WITH\_MEDIAN
<a name="recipe-actions.FILL_WITH_MEDIAN"></a>

Returns a column with missing data replaced by the median of all values.

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "FILL_WITH_MEDIAN",
        "Parameters": {
            "sourceColumn": "age"
        }
    }
}
```