

# EXTRACT\_BETWEEN\_POSITIONS
<a name="recipe-actions.EXTRACT_BETWEEN_POSITIONS"></a>

Creates a new column, based on character positions, from the values in an existing column. 

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.
+ `startPosition` – The character position at which to perform the extract.
+ `endPosition` – The character position at which to end the extract.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "EXTRACT_BETWEEN_POSITIONS",
        "Parameters": {
            "endPosition": "9",
            "sourceColumn": "last_name",
            "startPosition": "3",
            "targetColumn": "characters_3_to_9"
        }
    }
}
```