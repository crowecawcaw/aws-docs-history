

# DUPLICATE
<a name="recipe-actions.DUPLICATE"></a>

Creates a new column with the different name, but with all of the same data. Both the old and new columns are retained in the dataset.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – A name for the duplicate column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "DUPLICATE",
        "Parameters": {
            "sourceColumn": "last_name",
            "targetColumn": "copy_of_last_name"
        }
    }
}
```