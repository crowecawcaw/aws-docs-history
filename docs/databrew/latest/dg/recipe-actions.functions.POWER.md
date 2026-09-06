

# POWER
<a name="recipe-actions.functions.POWER"></a>

Returns the value of a number to the power of the exponent in a new column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value` – A number whose value is to be raised.
+ `targetColumn` – The name of the new column to be created.
+ `exponent` – The power to which the value will be raised.

**Note**  
You can specify either `sourceColumn` or `value`, but not both.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "POWER",
        "Parameters": {
            "exponent": "3",
            "sourceColumn": "age",
            "targetColumn": "age_cubed"
        }
    }
}
```