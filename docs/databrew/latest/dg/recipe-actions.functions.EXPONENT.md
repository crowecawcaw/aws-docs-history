

# EXPONENT
<a name="recipe-actions.functions.EXPONENT"></a>

Returns Euler’s number raised to the *n*th degree in a new column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "EXPONENT",
        "Parameters": {
            "sourceColumn": "age",
            "targetColumn": "age_EXPONENT"
        }
    }
}
```