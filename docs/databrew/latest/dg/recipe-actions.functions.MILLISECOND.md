

# MILLISECOND
<a name="recipe-actions.functions.MILLISECOND"></a>

Creates a new column containing the millisecond value from a source column or input value.

**Parameters**
+ `sourceColumn` – The name of an existing column. The source column can be of type `string`, `date`, or `timestamp`.
+ `value` – A character string to evaluate.
+ `targetColumn` – A name for the newly-created column.

**Note**  
You can specify either `sourceColumn` or `value`, but not both.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "MILLISECOND",
        "Parameters": {
            "sourceColumn": "DATETIME Column 1",
            "targetColumn": "DATETIME Column 1_MILLISECOND"
        }
    }
}
```