

# LOG
<a name="recipe-actions.functions.LOG"></a>

Returns the logarithm of a value in a new column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.
+ `base` – The base of the logarithm. The default is 10.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "LOG",
        "Parameters": {
            "base": "10",
            "sourceColumn": "age",
            "targetColumn": "age_LOG"
        }
    }
}
```