

# IS\_EVEN
<a name="recipe-actions.functions.ISEVEN"></a>

Returns a Boolean value in a new column that indicates whether the source column or value is even. If the source column or value is a decimal, the result is false.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.
+ `trueString` – A string that indicates whether the value is even.
+ `falseString` – A string that indicates whether the value is *not* even.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "IS_EVEN",
        "Parameters": {
            "falseString": "Value is odd",
            "sourceColumn": "height_cm",
            "targetColumn": "height_cm_IS_EVEN",
            "trueString": "Value is even"
        }
    }
}
```