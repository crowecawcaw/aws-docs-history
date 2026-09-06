

# UNNEST\_ARRAY
<a name="recipe-actions.UNNEST_ARRAY"></a>

Unnests a column of type `array` into a new column. If the array contains more than one value, then a row corresponding to each element is generated. This function only unnests one level of an array column.

**Parameters**
+ `sourceColumn` — The name of an existing column. This column must be of `struct` type.
+ `targetColumn` — Name of the target column that is generated.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "UNNEST_ARRAY",
        "Parameters": {
            "sourceColumn": "address",
            "targetColumn": "address"
        }
    }
}
```