

# SKEWNESS
<a name="recipe-actions.SKEWNESS"></a>

Applies transformations on your data values to change the distribution shape and its skew.

**Parameters**
+ `sourceColumn` – The name of an existing column. 

  `targetColumn` – The name of the new column to be created.

  `skewFunction`
  + `ROOT` – extract value-root. The root can be provided in the `value` parameter.

    `LOG` – log base value. The log base can be provided in the `value` parameter.

    `SQUARE` – square function

  `value` – Argument of the skewFunction.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "SKEWNESS",
        "Parameters": {
            "sourceColumn": "level",
            "targetColumn": "bin",
            "skewFunction": "LOG",
            "value": "2.718281828"
        }
    }
}
```