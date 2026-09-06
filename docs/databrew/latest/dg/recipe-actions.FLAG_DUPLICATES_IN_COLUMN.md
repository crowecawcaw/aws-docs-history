

# FLAG\_DUPLICATES\_IN\_COLUMN
<a name="recipe-actions.FLAG_DUPLICATES_IN_COLUMN"></a>

Returns a new column with a specified value in each row that indicates whether the value in the row's source column matches a value in an earlier row of the source column. When matches are found, they are flagged as duplicates. The initial occurrence is not flagged, because it doesn't match an earlier row. 

**Parameters**
+ `sourceColumn` – Name of the source column.
+ `targetColumn` – Name of the target column.
+ `trueString` – String to be inserted in the target column when a source column value duplicates an earlier value in that column.
+ `falseString` – String to be inserted in the target column when a source column value is distinct from earlier values in that column.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "FLAG_DUPLICATES_IN_COLUMN",
        "Parameters": {
            "sourceColumn": "Name",
            "targetColumn": "Duplicate",
            "trueString": "TRUE",
            "falseString": "FALSE"          
        }
    }
}
```