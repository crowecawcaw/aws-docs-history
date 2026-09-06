

# RANDOM\_BETWEEN
<a name="recipe-actions.functions.RANDOM_BETWEEN"></a>

In a new column, returns a random number between a specified lower bound (inclusive) and a specified upper bound (inclusive).

**Parameters**
+ `lowerBound` – The lower bound of the random number range.
+ `upperBound` – The upper bound of the random number range.
+ `targetColumn` – The name of the new column to be created.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "RANDOM_BETWEEN",
        "Parameters": {
            "lowerBound": "1",
            "targetColumn": "RANDOM_BETWEEN Column 1",
            "upperBound": "100"
        }
    }
}
```