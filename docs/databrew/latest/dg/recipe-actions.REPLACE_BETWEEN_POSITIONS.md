

# REPLACE\_BETWEEN\_POSITIONS
<a name="recipe-actions.REPLACE_BETWEEN_POSITIONS"></a>

Replaces the characters between two positions with user-specified text.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `startPosition` – A number indicting at what character position in the string the substitution is to begin.
+ `endPosition` – A number indicting at what character position in the string the substitution is to end.
+ `value` – The replacement character or characters to be substituted.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "REPLACE_BETWEEN_POSITIONS",
        "Parameters": {
            "endPosition": "20",
            "sourceColumn": "nationality",
            "startPosition": "10",
            "value": "E"
        }
    }
}
```