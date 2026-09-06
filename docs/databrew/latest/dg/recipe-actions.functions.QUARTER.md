

# QUARTER
<a name="recipe-actions.functions.QUARTER"></a>

Creates a new column containing the date-based quarter from a string that represents a date.

**Note**  
Quarters are designated in the new column as 1, 2, 3, or 4.  
1 is January, February, and March.
2 is April, May, and June.
3 is July, August, and September.
4 is October, November, and December.

**Parameters**
+ `sourceColumn` – The name of an existing column. The source column can be of type `string`, `date`, or `timestamp`.
+ `value` – A character string to evaluate.
+ `targetColumn` – A name for the newly-created column.

**Note**  
You can specify either `sourceColumn` or `value`, but not both.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "QUARTER",
        "Parameters": {
            "sourceColumn": "DATETIME Column 1",
            "targetColumn": "DATETIME Column 1_QUARTER"
        }
    }
}
```