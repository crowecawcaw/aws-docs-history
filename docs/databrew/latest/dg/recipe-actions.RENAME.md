

# RENAME
<a name="recipe-actions.RENAME"></a>

Creates a new column with the different name, but with all of the same data. The old column is then removed from the dataset.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – A new name for the column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "RENAME",
        "Parameters": {
            "sourceColumn": "date_of_birth",
            "targetColumn": "birth_date"
        }
    }
}
```