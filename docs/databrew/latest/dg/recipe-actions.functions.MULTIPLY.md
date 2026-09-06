

# MULTIPLY
<a name="recipe-actions.functions.MULTIPLY"></a>

Multiplies two numbers and returns the result in a new column.

**Parameters**
+ `sourceColumn1` – The name of an existing column.
+ `value1` – A numeric value.
+ `sourceColumn2` – The name of an existing column.
+ `value2` – A numeric value.
+ `targetColumn` – The name of the new column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "MULTIPLY",
        "Parameters": {
            "sourceColumn1": "hourly_rate",
            "sourceColumn2": "hours",
            "targetColumn": "total_pay"
        }
    }
}
```