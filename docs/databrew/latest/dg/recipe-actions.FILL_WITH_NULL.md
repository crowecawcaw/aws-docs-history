

# FILL\_WITH\_NULL
<a name="recipe-actions.FILL_WITH_NULL"></a>

Returns a column with data values replaced by null.

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "FILL_WITH_NULL",
        "Parameters": {
            "sourceColumn": "rating"
        }
    }
}
```