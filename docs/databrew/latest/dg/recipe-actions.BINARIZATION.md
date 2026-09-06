

# BINARIZATION
<a name="recipe-actions.BINARIZATION"></a>

Takes all the values in a selected numeric source column, compares them to a threshold value, and outputs a new column with a 1 or 0 for each row. 

**Parameters**
+ `sourceColumn` – The name of an existing column. 

  `targetColumn` – The name of the new column to be created.

  `threshold` – Number indicating the threshold for assigning the value of 0 or 1.

  `flip` – Option to flip binary assignment so that lower values are assigned 1 and higher values are assigned 0. When the flip parameter is true, values lower than or equal to the threshold value result in 1, and values greater than the threshold value result in 0.

**Example**  
  

```
{
    "Action": {
        "Operation": "BINARIZATION",
        "Parameters": {
            "sourceColumn": "level",
            "targetColumn": "bin",
            "threshold": "100.0",
            "flip": "false"
        }
    }
}
```