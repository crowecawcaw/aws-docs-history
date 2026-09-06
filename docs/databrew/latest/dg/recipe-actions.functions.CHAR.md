

# CHAR
<a name="recipe-actions.functions.CHAR"></a>

Returns in a new column the Unicode character for each integer in the source column, or for a custom integer value.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value` – An integer that represents a Unicode value.
+ `targetColumn` – The name of the new column to be created.

**Note**  
You can specify either `sourceColumn` or `value`, but not both.

**Examples**  
  

```
{
    "RecipeAction": {
        "Operation": "CHAR",
        "Parameters": {
            "sourceColumn": "age",
            "targetColumn": "age_char"
        }
    }
}
```
  

```
{
    "RecipeAction": {
        "Operation": "CHAR",
        "Parameters": {
            "value": 42,
            "targetColumn": "asterisk"
        }
    }
}
```