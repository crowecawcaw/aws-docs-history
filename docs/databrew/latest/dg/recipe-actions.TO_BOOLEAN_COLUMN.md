

# TO\_BOOLEAN\_COLUMN
<a name="recipe-actions.TO_BOOLEAN_COLUMN"></a>

Changes the data type of an existing column to BOOLEAN.

**Note**  
We recommend using CHANGE\_DATA\_TYPE recipe action rather than TO\_BOOLEAN\_COLUMN.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – A value that must be `boolean`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "TO_BOOLEAN_COLUMN",
        "Parameters": {
            "columnDataType": "boolean",
            "sourceColumn": "is_present"
        }
    }
}
```