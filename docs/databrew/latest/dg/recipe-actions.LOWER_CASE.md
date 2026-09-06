

# LOWER\_CASE
<a name="recipe-actions.LOWER_CASE"></a>

Changes each string in a column to lowercase, for example: the quick brown fox jumped over the fence

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "LOWER_CASE",
        "Parameters": {
            "sourceColumn": "nationality"
        }
    }
}
```