

# GET\_ADVANCED\_DATATYPE
<a name="recipe-actions.GET_ADVANCED_DATATYPE"></a>

Given a string column, identifies the advanced data type of the column, if any.

**Parameters**
+ `columnName` – The name of the string column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "GET_ADVANCED_DATATYPE",
        "Parameters": {
            "sourceColumn": "columnName"
        }
    }
}
```