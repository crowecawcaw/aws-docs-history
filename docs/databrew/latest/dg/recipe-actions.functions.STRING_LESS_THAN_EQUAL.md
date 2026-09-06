

# STRING\_LESS\_THAN\_EQUAL
<a name="recipe-actions.functions.STRING_LESS_THAN_EQUAL"></a>

Creates a new column populated with one of the following:
+ `True` if one string in a column (or value) is less than or equal to another string in a different column (or value).
+ `False` if there is no match.

**Parameters**
+ `sourceColumn1` – The name of an existing column.
+ `sourceColumn2` – The name of an existing column.
+ `value1` – A character string to evaluate.
+ `value2` – A character string to evaluate.
+ `targetColumn` – The name of the new column to be created.

**Note**  
You can specify only one of the following combinations:  
Both of `sourceColumn{{N}}`.
One of `sourceColumn{{N}}` and one of `value{{N}}`.
Both of `value{{N}}`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "STRING_LESS_THAN_EQUAL",
        "Parameters": {
            "sourceColumn1": "first_name",
            "targetColumn": "string_less_than_equal",
            "value2": "s"
        }
    }
}
```