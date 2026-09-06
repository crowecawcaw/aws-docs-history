

# UNNEST\_MAP
<a name="recipe-actions.UNNEST_MAP"></a>

Unnests a column of type `map` and generates a column for the key and value. If there is more than one key-value pair, a row corresponding to each key value would be generated. This function only unnests one level of a map column.

**Parameters**
+ `sourceColumn` — The name of an existing column. This column must be of `struct` type.
+ `removeSourceColumn` — If `true`, the source column is deleted after the function is complete.
+ `targetColumn` — If provided, each of the generated column will start with this as the prefix.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "UNNEST_MAP",
        "Parameters": {
            "sourceColumn": "address",
            "removeSourceColumn": "false",
            "targetColumn": "address"
        }
    }
}
```