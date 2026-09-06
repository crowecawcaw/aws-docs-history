

# TO\_STRING\_COLUMN
<a name="recipe-actions.TO_STRING_COLUMN"></a>

Changes the data type of an existing column to STRING.

**Note**  
We recommend using CHANGE\_DATA\_TYPE recipe action rather than TO\_STRING\_COLUMN.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – A value that must be `string`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "TO_STRING_COLUMN",
        "Parameters": {
            "columnDataType": "string",
            "sourceColumn": "age"
        }
    }
}
```