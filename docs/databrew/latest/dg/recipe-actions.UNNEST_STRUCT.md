

# UNNEST\_STRUCT
<a name="recipe-actions.UNNEST_STRUCT"></a>

Unnest a column of type `struct` and generates a column for each of the keys present in the struct. This function only unnests struct level one.

**Parameters**
+ `sourceColumn` — The name of an existing column. This column must be of struct type.
+ `removeSourceColumn` — If `true`, the source column is deleted after the function is complete.
+ `targetColumn` — If provided, each of the generated column will start with this as the prefix.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "UNNEST_STRUCT",
        "Parameters": {
            "sourceColumn": "address",
            "removeSourceColumn": "false"
            "targetColumn": "add"
        }
    }
}
```