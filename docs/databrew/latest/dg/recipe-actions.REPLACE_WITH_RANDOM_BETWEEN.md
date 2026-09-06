

# REPLACE\_WITH\_RANDOM\_BETWEEN
<a name="recipe-actions.REPLACE_WITH_RANDOM_BETWEEN"></a>

Replaces values with a random number.

**Parameters**
+ `lowerBound` – The lower bound of the random number range.
+ `sourceColumns` – A list of existing column names.
+ `upperBound` – The upper bound of the random number range.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "REPLACE_WITH_RANDOM_BETWEEN",
        "Parameters": {
            "lowerBound": "1",
            "sourceColumns": ["column1", "column2"],
            "upperBound": "100"
        }
    }
}
```