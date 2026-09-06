

# EXTRACT\_PATTERN
<a name="recipe-actions.EXTRACT_PATTERN"></a>

Creates a new column, based on a regular expression, from the values in an existing column. 

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.
+ `pattern` – A regular expression that indicates which character or characters to extract and create the new column from.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "EXTRACT_PATTERN",
        "Parameters": {
            "pattern": "^....*...$",
            "sourceColumn": "last_name",
            "targetColumn": "first_and_last_few_characters"
        }
    }
}
```