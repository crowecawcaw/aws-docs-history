

# PI
<a name="recipe-actions.functions.PI"></a>

Returns the value of pi (3.141592653589793) in a new column.

**Parameters**
+ `targetColumn` – The name of the new column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "PI",
        "Parameters": {
            "targetColumn": "PI Column 1"
        }
    }
}
```