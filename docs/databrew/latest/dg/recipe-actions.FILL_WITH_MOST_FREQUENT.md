

# FILL\_WITH\_MOST\_FREQUENT
<a name="recipe-actions.FILL_WITH_MOST_FREQUENT"></a>

Returns a column with missing data replaced by the most frequent value.

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "FILL_WITH_MOST_FREQUENT",
        "Parameters": {
            "sourceColumn": "position"
        }
    }
}
```