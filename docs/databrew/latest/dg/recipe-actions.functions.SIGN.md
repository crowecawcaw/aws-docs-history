

# SIGN
<a name="recipe-actions.functions.SIGN"></a>

Returns a new column with -1 if the value is less than 0, 0 if the value is 0, and \+1 if the value is greater than 0.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "SIGN",
        "Parameters": {
            "sourceColumn": "age",
            "targetColumn": "age_SIGN"
        }
    }
}
```