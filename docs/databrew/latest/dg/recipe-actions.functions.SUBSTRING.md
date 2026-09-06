

# SUBSTRING
<a name="recipe-actions.functions.SUBSTRING"></a>

Returns in a new column some or all of the specified strings in the source column, based on the user-defined starting and ending index values.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `startPosition` – The character position to begin with, from the left end of the string.
+ `endPosition` – The character position to end with, from the left end of the string.
+ `targetColumn` – The name of the new column to be created.

**Note**  
You can specify either `sourceColumn` or `value`, but not both.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "SUBSTRING",
        "Parameters": {
            "sourceColumn": "last_name",
            "startPosition": "5",
            "endPosition": "8",
            "targetColumn": "chars_5_through_8"
        }
    }
}
```