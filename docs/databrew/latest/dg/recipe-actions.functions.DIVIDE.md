

# DIVIDE
<a name="recipe-actions.functions.DIVIDE"></a>

Divides one input number by another and returns the result in a new column.

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
        "Operation": "DIVIDE",
        "Parameters": {
            "sourceColumn1": "height_cm",
            "targetColumn": "divide_by_2",
            "value2": "2"
        }
    }
}
```