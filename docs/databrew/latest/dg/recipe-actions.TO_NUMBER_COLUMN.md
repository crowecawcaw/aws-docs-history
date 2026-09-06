

# TO\_NUMBER\_COLUMN
<a name="recipe-actions.TO_NUMBER_COLUMN"></a>

Changes the data type of an existing column to NUMBER.

**Note**  
We recommend using CHANGE\_DATA\_TYPE recipe action rather than TO\_NUMBER\_COLUMN.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – A value that must be `number`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "TO_NUMBER_COLUMN",
        "Parameters": {
            "columnDataType": "number",
            "sourceColumn": "hours_worked"
        }
    }
}
```