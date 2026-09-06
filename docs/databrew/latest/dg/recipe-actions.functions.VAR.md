

# VARIANCE
<a name="recipe-actions.functions.VAR"></a>

 Returns the variance from the selected source columns in a new column. Variance is defined as `Var(X) = [Sum ((X – mean(X))^2)]/Count(X)`.

**Parameters**
+ `sourceColumns` – A JSON-encoded string representing a list of existing columns.
+ `targetColumn` – A name for the newly created column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "VARIANCE",
        "Parameters": {
            "sourceColumns": "[\"age\",\"years_in_service\"]",
            "targetColumn": "VARIANCE Column 1"
        }
    }
}
```