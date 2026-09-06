

# FLOOR
<a name="recipe-actions.functions.FLOOR"></a>

Returns the largest integral number greater than or equal to the input number in a new column.

**Parameters**
+ `sourceColumn1` – The name of an existing column.
+ `value` – A numeric value.
+ `targetColumn` – The name of the new column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "FLOOR",
        "Parameters": {
            "targetColumn": "FLOOR Column 1",
            "value": "42"
        }
    }
}
```