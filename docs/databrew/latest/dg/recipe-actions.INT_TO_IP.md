

# INT\_TO\_IP
<a name="recipe-actions.INT_TO_IP"></a>

Converts the integer value of source column or other value to the corresponding IPv4 value in then target column, and returns the result in a new column. This function works for IPv4 only.

For example, consider the following integer.

```
167772410
```

If you use this value as an input to `INT_TO_IP`, the output value is as follows.

```
10.0.0.250
```

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value` – A character string to evaluate.
+ `targetColumn` – The name of the new column to be created.

You can specify either `sourceColumn` or `value`, but not both.

**Example**  
  

```
[  {
    "RecipeAction": {
      "Operation": "INT_TO_IP",
      "Parameters": {
        "sourceColumn": "my_integer",
        "targetColumn": "INT_TO_IP Column 1"
      }
    }
  }
]
```