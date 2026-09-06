

# KTH\_LARGEST
<a name="recipe-actions.functions.KTH_LARGEST"></a>

 Returns the *k*th largest number from the selected source columns in a new column. 

**Parameters**
+ `sourceColumns` – A JSON-encoded string representing a list of existing columns.
+ `targetColumn` – A name for the newly created column.
+ `value` – A number representing *k*.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "KTH_LARGEST",
        "Parameters": {
            "sourceColumns": "[\"height_cm\",\"weight_kg\",\"age\"]",
            "targetColumn": "KTH_LARGEST Column 1",
            "value": "2"
        }
    }
}
```